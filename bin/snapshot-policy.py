#!/usr/bin/env python3
"""Congela a versão vigente de um documento legal como snapshot imutável.

Uso: bin/snapshot-policy.py <privacidade|termos>

Lê docs-publicos/<slug>.md, descobre a `version` do frontmatter e cria
docs-publicos/legal/<slug>-<version>.md com o mesmo corpo, porém com
permalink versionado (/<slug>/<version>/) e marcado como arquivado. Nunca
sobrescreve um snapshot existente — versões publicadas são imutáveis.

Rode este comando ANTES de bumpar a `version` do documento vigente, para
preservar o texto exato da versão que está saindo de circulação.
"""

import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# No repo do manual o conteúdo (privacidade.md, termos.md, legal/) fica na RAIZ.
DOCS = REPO
SLUGS = ("privacidade", "termos")


def split_frontmatter(text):
    if not text.startswith("---"):
        raise SystemExit("documento sem frontmatter")
    end = text.find("\n---", 3)
    if end == -1:
        raise SystemExit("frontmatter não fechado")
    block = text[3:end]
    body = text[end + 4:]  # tudo após o '\n---' de fechamento
    fm = {}
    for line in block.splitlines():
        s = line.strip()
        if not s or s.startswith("#") or ":" not in s:
            continue
        key, _, value = s.partition(":")
        value = value.strip()
        if len(value) >= 2 and value[0] in "\"'" and value[-1] == value[0]:
            value = value[1:-1]
        fm[key.strip()] = value
    return fm, body


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in SLUGS:
        raise SystemExit("uso: bin/snapshot-policy.py <privacidade|termos>")
    slug = sys.argv[1]
    src = os.path.join(DOCS, f"{slug}.md")
    with open(src, "r", encoding="utf-8") as fh:
        text = fh.read()

    fm, body = split_frontmatter(text)
    version = fm.get("version")
    if not version:
        raise SystemExit(f"{src}: frontmatter sem 'version'")

    dest_dir = os.path.join(DOCS, "legal")
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, f"{slug}-{version}.md")
    if os.path.exists(dest):
        raise SystemExit(
            f"Snapshot já existe (imutável): {os.path.relpath(dest, REPO)}"
        )

    new_fm = [
        "---",
        "layout: section",
        f'title: "{fm.get("title", slug)} — versão {version} (arquivada)"',
        "nav_exclude: true",
        f"permalink: /{slug}/{version}/",
        f'version: "{version}"',
        f'change_summary: "{fm.get("change_summary", "")}"',
        f"requires_reconsent: {fm.get('requires_reconsent', 'true')}",
        "archived: true",
        "sitemap: false",
        "---",
    ]
    out = "\n".join(new_fm) + body
    if not out.endswith("\n"):
        out += "\n"
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write(out)
    print(f"Snapshot criado: {os.path.relpath(dest, REPO)}")


if __name__ == "__main__":
    main()
