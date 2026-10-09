# Módulo Odoo 18: Customer Loyalty Extension (`customer_loyalty`)

[![Odoo Version](https://img.shields.io/badge/Odoo-18.0-714B67.svg)](https://www.odoo.com)
[![License](https://img.shields.io/badge/License-LGPL--3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0.html)
[![Role](https://img.shields.io/badge/Architecture-Tech%20Lead-orange.svg)]()

## 🎯 Visão Geral do Projeto

O módulo **`customer_loyalty`** estende as capacidades nativas de fidelização do Odoo 18 (`loyalty` e `sale_loyalty`), adicionando uma camada de inteligência de negócio focada na progressão automática de níveis de clientes (**Bronze**, **Silver**, **Gold**), visualização de saldo consolidado em tempo real no backend, automações agendadas e relatórios analíticos em PDF.

Em alinhamento com as melhores práticas de engenharia de software e arquitetura Odoo, este módulo **não reinventa o motor de recompensas ou e-commerce**. Em vez disso, alavanca a infraestrutura nativa do ERP, reduzindo a dívida técnica e garantindo total compatibilidade com futuras atualizações.

---

## 🚀 Funcionalidades Principais

* **Relação Multi-Carteira (1:N):** Conexão nativa com `loyalty.card`, permitindo que um cliente acumule pontos em múltiplos programas em paralelo (compras, campanhas sazonais, filiais)[cite: 1].
* **Gestão Automática de Níveis (`res.partner`):**
  * 🥉 **Bronze:** $0$ a $999$ pontos
  * 🥈 **Silver:** $1.000$ a $4.999$ pontos
  * 🥇 **Gold:** $5.000+$ pontos
* **Pontuação Automática na Venda:** Atribuição de $1\text{ ponto}$ a cada $10\text{ unidades monetárias}$ consumidas na confirmação do pedido de venda (`sale.order`).
* **UI/UX em Tempo Real (OWL Widget):** Exibição badge do saldo consolidado e nível diretamente na Form View do cliente no backend.
* **Segurança & Controlo de Acesso:** Edição manual de pontos restrita ao grupo de segurança `customer_loyalty.group_loyalty_card`.
* **Automação Semanal (Cron Job):** Processo agendado (domingos às 23:00) que identifica clientes Gold e dispara notificações/cupons promocionais por e-mail.
* **Relatório Analítico QWeb (PDF):** Extrato consolidado de saldo e carteiras ativas do parceiro.
* **Integração Nativa no Portal/Checkout:** Resgate direto de recompensas e consulta de histórico via e-commerce/portal nativo do Odoo.

---

## 🏗️ Estrutura do Módulo

```text
customer_loyalty/
├── __init__.py
├── __manifest__.py
├── README.md
├── DOCUMENTATION.md
├── data/
│   ├── cron_data.xml
│   └── loyalty_data.xml
├── models/
│   ├── __init__.py
│   ├── loyalty_card.py
│   ├── res_partner.py
│   └── sale_order.py
├── report/
│   ├── loyalty_report.xml
│   └── loyalty_report_template.xml
├── security/
│   ├── ir.model.access.csv
│   └── loyalty_security.xml
├── static/
│   └── src/
│       └── components/
│           └── loyalty_badge/
└── views/
    ├── partner_views.xml