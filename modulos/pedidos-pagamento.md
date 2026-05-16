---
layout: docs
title: Pedidos de Pagamento
permalink: /modulos/pedidos-pagamento/
---

O módulo de **Pedidos de Pagamento** permite solicitar formalmente que a organização realize um pagamento a um fornecedor, prestador de serviços ou para cobrir uma despesa institucional.

> **Diferença em relação ao reembolso:** no reembolso, o membro já pagou do próprio bolso. No pedido de pagamento, o dinheiro vai diretamente da conta da organização para o destinatário.

> Acesse pelo menu **Pagamentos e Reembolsos → aba Pedidos de pagamento**.

## Lista de pedidos de pagamento

[![Lista de pedidos](../../assets/screenshots/manual-07-pedidos-lista.png)](../../assets/screenshots/manual-07-pedidos-lista.png)
*Lista de pedidos de pagamento — v0.10 (beta)*

A lista exibe todos os pedidos com: Descrição, Destinatário, Valor, Data da despesa, Solicitante e Status.

Os **cards de resumo** no topo mostram, de acordo com seu papel:
- **Aguardando minha aprovação** — *Presidente e Tesoureiro*
- **Aprovados aguardando pagamento** — *Tesoureiro*
- **Solicitado no período** — *todos os papéis*

**Status possíveis:**

| Status | Significado |
|---|---|
| ⬜ **Rascunho** | Salvo sem enviar |
| 🟡 **Aguardando aprovação** | Enviado para aprovação |
| 🟢 **Aprovado** | Aprovado, aguardando pagamento |
| 🔴 **Rejeitado** | Reprovado com motivo |
| 💙 **Pago** | Pagamento realizado e confirmado |

## Detalhe — Aguardando aprovação

[![Pedido aguardando aprovação](../../assets/screenshots/manual-08-pedido-aguardando.png)](../../assets/screenshots/manual-08-pedido-aguardando.png)
*Detalhe de pedido aguardando aprovação — v0.10 (beta)*

- **Valor**, **Destinatário**, **Solicitante** e **Data da despesa** no topo
- **Dados do pedido**: descrição, categoria, projeto, centro de custo
- **Documentos**: orçamento, nota fiscal ou contrato
- **Histórico de aprovações**
- **Ações**: Aprovar / Reprovar *(para aprovadores elegíveis)*

> Os dados de pagamento do destinatário (PIX/TED/Boleto) são visíveis apenas para aprovadores e tesoureiro.

## Detalhe — Rejeitado

[![Pedido rejeitado](../../assets/screenshots/manual-08b-pedido-rejeitado.png)](../../assets/screenshots/manual-08b-pedido-rejeitado.png)
*Detalhe de pedido rejeitado — v0.10 (beta)*

O motivo aparece em destaque no topo. O solicitante pode editar e reenviar o pedido corrigido.

## Detalhe — Aprovado

[![Pedido aprovado](../../assets/screenshots/manual-08c-pedido-aprovado.png)](../../assets/screenshots/manual-08c-pedido-aprovado.png)
*Detalhe de pedido aprovado — v0.10 (beta)*

O painel de Ações exibe: **"Aprovado — aguardando confirmação de pagamento pelo tesoureiro."**

O tesoureiro confirma o pagamento pelo lançamento gerado automaticamente em **Movimentações**.

## Novo pedido de pagamento

[![Novo pedido de pagamento](../../assets/screenshots/manual-08d-novo-pedido.png)](../../assets/screenshots/manual-08d-novo-pedido.png)
*Formulário de novo pedido — v0.10 (beta)*

Clique em **+ Nova solicitação** para abrir o formulário.

**Campos obrigatórios:**
- **Data da despesa** — data prevista ou da nota fiscal
- **Valor**
- **Destinatário** — nome do fornecedor ou prestador de serviços
- **Descrição** — o que está sendo pago e para qual finalidade
- **Dados de pagamento do destinatário**: PIX, TED ou Boleto

**Campos opcionais:** Categoria, Projeto, Centro de custo, Observações, Documentos (orçamento, nota, contrato).

> **Atenção:** aqui os dados de pagamento são do **destinatário** (fornecedor), não do solicitante. Não há pré-preenchimento automático.

**Botões de ação:**
- **Salvar rascunho** — salva sem enviar
- **Enviar para aprovação** — envia para aprovação
