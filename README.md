# Customer Loyalty — Odoo 18

Módulo de personalização do programa de fidelização de clientes para o **Odoo 18**, desenvolvido para complementar a funcionalidade nativa de Loyalty, com foco no cálculo de pontos com base no valor total dos pedidos de venda e na reutilização dos mecanismos de gestão de carteiras disponibilizados pela plataforma.

## Funcionalidades

### 1. Integração com o sistema nativo de fidelização

O módulo utiliza os modelos e mecanismos nativos do Odoo para gerir os programas de fidelização, os cartões de fidelização e a atribuição de pontos.

Esta abordagem evita a duplicação de funcionalidades existentes e permite aproveitar o fluxo nativo de processamento dos pontos, mantendo a compatibilidade com a estrutura do Odoo.

### 2. Cálculo personalizado de pontos

O módulo permite calcular os pontos de fidelização com base no valor total do pedido de venda, utilizando a seguinte regra:

**1 ponto por cada 10 unidades monetárias do valor total do pedido.**

O cálculo utiliza divisão inteira, descartando a parte decimal do resultado. Assim, os valores inferiores à próxima unidade de dez não geram um ponto adicional.

Exemplos:

| Valor total do pedido | Pontos atribuídos |
| --------------------: | ----------------: |
|                   100 |                10 |
|                   105 |                10 |
|                   109 |                10 |
|                   110 |                11 |
|                   250 |                25 |

A regra personalizada é aplicada através da extensão do método `_program_check_compute_points()` do modelo `sale.order`, aproveitando o mecanismo nativo de cálculo de pontos dos programas de fidelização.

### 3. Configuração através do campo `use_order_total_for_points`

Foi adicionado ao modelo `loyalty.program` o campo booleano `use_order_total_for_points`, que permite determinar se um programa de fidelização deve utilizar a regra personalizada de cálculo de pontos.

O campo funciona da seguinte forma:

* **Ativado:** o programa calcula os pontos com base no valor total do pedido, atribuindo um ponto por cada dez unidades monetárias.
* **Desativado:** o programa mantém o comportamento de cálculo de pontos definido pelo Odoo.

Esta configuração permite aplicar a regra personalizada apenas aos programas pretendidos, sem alterar o comportamento dos restantes programas de fidelização.

### 4. Reutilização do mecanismo nativo de atribuição de pontos

A implementação preserva o fluxo nativo do Odoo para o processamento dos pontos, evitando criar um mecanismo paralelo de atualização das carteiras.

A extensão do cálculo permite adaptar a quantidade de pontos atribuídos, enquanto o Odoo continua responsável pelo processamento subsequente, de acordo com as regras de elegibilidade e configuração do programa.

Para que a atribuição ocorra, o programa deve cumprir os critérios de aplicabilidade exigidos pelo sistema nativo.

## Arquitectura técnica

| Componente        | Responsabilidade                                                                   |
| ----------------- | ---------------------------------------------------------------------------------- |
| `loyalty.program` | Configuração dos programas de fidelização e do campo `use_order_total_for_points`. |
| `sale.order`      | Extensão do cálculo de pontos com base no valor total do pedido de venda.          |
| `sale_loyalty`    | Integração com os mecanismos nativos de fidelização do Odoo.                       |

## Requisitos

* Odoo 18.0.
* Aplicação de Vendas (`sale`).
* Funcionalidades nativas de fidelização disponibilizadas pelo módulo `sale_loyalty`.

## Instalação

1. Copiar o módulo `customer_loyalty` para um directório de addons do Odoo.
2. Confirmar que as dependências declaradas no ficheiro `__manifest__.py` estão disponíveis.
3. Reiniciar o serviço do Odoo.
4. Actualizar a lista de aplicações.
5. Instalar o módulo **Customer Loyalty**.

Para instalar através da linha de comandos, ajustar os caminhos e o nome da base de dados à instalação utilizada:

```bash
./odoo-bin \
    -c /caminho/para/odoo.conf \
    -d nome_da_base_de_dados \
    -i customer_loyalty \
    --stop-after-init
```

Se o módulo já estiver instalado e for necessário aplicar alterações ao código, utilizar `-u customer_loyalty` em vez de `-i customer_loyalty`.

## Configuração e utilização

Após a instalação:

1. Aceder à aplicação de Vendas e às funcionalidades de fidelização.
2. Criar ou seleccionar um programa de fidelização.
3. Activar o campo `use_order_total_for_points` no programa que deverá utilizar o cálculo personalizado.
4. Confirmar que o programa está configurado para ser aplicado automaticamente aos pedidos elegíveis, de acordo com os critérios nativos do Odoo.
5. Criar e confirmar um pedido de venda elegível.
6. Verificar se a quantidade de pontos calculada corresponde ao valor total do pedido e à regra definida.

Os programas em que o campo `use_order_total_for_points` não estiver activado continuarão a utilizar o cálculo nativo de pontos.

## Testes recomendados

Para validar a implementação, recomenda-se testar os seguintes cenários:

* Instalação e actualização do módulo.
* Activação e desactivação do campo `use_order_total_for_points`.
* Cálculo correcto dos pontos para diferentes valores totais.
* Confirmação de que os valores inferiores à próxima unidade de dez não geram pontos adicionais.
* Verificação do comportamento de programas com a regra personalizada desactivada.
* Confirmação de que os programas cumprem os critérios nativos de elegibilidade.
* Verificação da integração com o mecanismo nativo de fidelização e das actualizações das carteiras.

## Princípios de implementação

* **Reutilização:** aproveitar os modelos e mecanismos nativos do Odoo.
* **Modularidade:** isolar a regra personalizada através da extensão dos modelos existentes.
* **Compatibilidade:** preservar o comportamento padrão dos programas que não utilizam a regra personalizada.
* **Manutenibilidade:** seguir os padrões de desenvolvimento e extensão do Odoo.
* **Configuração:** permitir activar a regra personalizada por programa através de um campo booleano.

## Compatibilidade

* **ERP:** Odoo
* **Versão:** 18.0
* **Tipo:** Módulo personalizado
* **Dependência principal:** `sale_loyalty`

## Autor

**Jardel Elias Bernardo**

Odoo Developer

GitHub: [JardelLion](https://github.com/JardelLion)
