# Customer Loyalty — Odoo 18

Módulo de personalização do programa de fidelização de clientes para o **Odoo 18**, desenvolvido para complementar as funcionalidades nativas do Odoo Loyalty com recursos adicionais de acompanhamento, visualização e gestão de pontos.

## Funcionalidades

### 1. Integração com o sistema nativo de fidelização

O módulo aproveita os mecanismos nativos do Odoo para gerir os cartões de fidelização e a atribuição de pontos, evitando a duplicação de funcionalidades já disponibilizadas pela plataforma.

Esta abordagem permite manter a compatibilidade com o funcionamento padrão do Odoo e reduzir a complexidade da implementação.

### 2. Resumo de fidelização do cliente

Disponibiliza informações relacionadas com a fidelização do cliente, permitindo acompanhar os seus pontos e o respectivo nível de fidelização.

O objectivo é facilitar a consulta das informações relevantes para a equipa de vendas e para os utilizadores responsáveis pela gestão dos clientes.

### 3. Widget interactivo com OWL

Inclui um widget desenvolvido com **OWL (Odoo Web Library)** para apresentar informações de fidelização numa interface interactiva integrada no Odoo.

O componente permite consultar os dados relevantes de forma organizada, melhorando a experiência de utilização.

### 4. Ajustes manuais de pontos

Disponibiliza um assistente para efectuar ajustes manuais de pontos de fidelização, de acordo com as permissões configuradas.

Esta funcionalidade permite tratar situações excepcionais sem alterar directamente os dados na base de dados.

### 5. Envio automático de e-mails para clientes Gold

Inclui uma acção automatizada para o envio de e-mails aos clientes que se enquadram no nível Gold, utilizando o mecanismo de tarefas agendadas do Odoo.

A automatização reduz a necessidade de intervenções manuais e facilita a comunicação com os clientes elegíveis.

### 6. Relatório em PDF

Disponibiliza um relatório em PDF com informações relacionadas com a fidelização, permitindo consultar e partilhar os dados apresentados pelo módulo.

O relatório utiliza os mecanismos de geração de documentos do Odoo.

## Arquitectura técnica

O módulo foi desenvolvido seguindo os padrões de extensão do Odoo, privilegiando a reutilização das funcionalidades nativas e a separação das responsabilidades.

| Componente                 | Responsabilidade                                            |
| -------------------------- | ----------------------------------------------------------- |
| Modelos existentes do Odoo | Gestão nativa dos cartões e dos mecanismos de fidelização   |
| Modelos personalizados     | Informação complementar de fidelização e níveis de clientes |
| OWL                        | Apresentação interactiva das informações de fidelização     |
| Assistente (Wizard)        | Ajustes manuais de pontos                                   |
| Segurança                  | Controlo de acesso às operações disponibilizadas            |
| Acções agendadas (Cron)    | Automatização do envio de e-mails                           |
| QWeb / PDF                 | Geração de relatórios                                       |

## Requisitos

* Odoo 18.0
* Aplicação de Vendas, conforme a configuração utilizada
* Funcionalidades nativas de fidelização do Odoo
* Dependências adicionais declaradas no ficheiro `__manifest__.py`

## Instalação

1. Copiar o módulo para um directório de addons do Odoo.
2. Confirmar que as dependências declaradas no `__manifest__.py` estão instaladas.
3. Reiniciar o serviço do Odoo.
4. Actualizar a lista de aplicações.
5. Instalar o módulo **Customer Loyalty**.

Para instalar através da linha de comandos, ajustar o caminho da configuração, o nome da base de dados e o caminho dos addons à respectiva instalação:

```bash
./odoo-bin \
    -c /caminho/para/odoo.conf \
    -d nome_da_base_de_dados \
    -i customer_loyalty \
    --stop-after-init
```

## Configuração e utilização

Após a instalação:

1. Configurar os programas de fidelização através das funcionalidades nativas do Odoo.
2. Confirmar as permissões dos utilizadores que irão utilizar os ajustes manuais.
3. Verificar a configuração das tarefas agendadas e dos modelos de e-mail.
4. Aceder às funcionalidades personalizadas disponibilizadas pelo módulo.
5. Gerar o relatório em PDF para validar a apresentação das informações.

Os menus e as opções disponíveis dependem da configuração e das permissões definidas no sistema.

## Testes recomendados

Para validar o comportamento do módulo, recomenda-se testar os seguintes cenários:

* Instalação do módulo e carregamento das dependências.
* Integração com os mecanismos nativos de fidelização.
* Apresentação correcta das informações de fidelização.
* Funcionamento do widget OWL.
* Aplicação de ajustes manuais de pontos por utilizadores autorizados.
* Restrição das operações para utilizadores sem as permissões necessárias.
* Execução da tarefa agendada de envio de e-mails.
* Geração e visualização do relatório em PDF.

## Princípios de implementação

O desenvolvimento segue os seguintes princípios:

* **Reutilização:** aproveitar as funcionalidades nativas do Odoo sempre que possível.
* **Modularidade:** manter as funcionalidades personalizadas organizadas e independentes.
* **Segurança:** controlar o acesso às operações através dos mecanismos de permissões do Odoo.
* **Manutenibilidade:** seguir os padrões de desenvolvimento da plataforma.
* **Integração:** utilizar os mecanismos nativos de modelos, vistas, assistentes, tarefas agendadas e relatórios.

## Compatibilidade

* **ERP:** Odoo
* **Versão:** 18.0
* **Tipo:** Módulo personalizado

## Autor

**Jardel Elias Bernardo**

Odoo Developer

GitHub: [JardelLion](https://github.com/JardelLion)
