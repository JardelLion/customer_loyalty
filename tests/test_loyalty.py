# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase
from odoo.exceptions import AccessError, UserError


class TestCustomerLoyalty(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # 1. Modelos
        cls.Partner = cls.env['res.partner']
        cls.SaleOrder = cls.env['sale.order']

        # 2. Cliente de Teste (Sem carteiras iniciais)
        cls.partner = cls.Partner.create({
            'name': 'Cliente Teste Fluxo Real',
            'email': 'real_flow@example.com',
        })

        # 3. Produto para Compra
        cls.product = cls.env['product.product'].create({
            'name': 'Produto Teste Fidelidade',
            'list_price': 100.0,
        })

        # 4. Utilizador Restrito (Sem o grupo 'Loyalty Card')
        cls.user_restricted = cls.env['res.users'].create({
            'name': 'Operador Sem Permissao',
            'login': 'user_no_loyalty',
            'groups_id': [(6, 0, [cls.env.ref('base.group_user').id])],
        })

    def _create_and_confirm_sale(self, amount_units):
        """ Método auxiliar para gerar vendas e acionar a criação automática de cartões """
        order = self.SaleOrder.create({
            'partner_id': self.partner.id,
            'order_line': [(0, 0, {
                'product_id': self.product.id,
                'product_uom_qty': amount_units,
                'price_unit': 100.0, # Ex: 10 unidades * 100 = $1,000 (Gera 100 pontos)
            })]
        })
        order.action_confirm()
        return order

    def test_01_automatic_card_creation_and_level_upgrade(self):
        """ Validar que o cartão é criado automaticamente na confirmação da venda """
        # Garantir que o cliente não tem cartões associados inicialmente
        self.assertEqual(len(self.partner.loyalty_card_ids), 0)
        self.assertEqual(self.partner.loyalty_level, 'bronze')

        # Confirmar venda de 10.000 USD (Deve gerar a carteira automática com 1.000 pts -> Nível Silver)
        self._create_and_confirm_sale(100)

        # Invalidar cache para carregar a nova carteira criada em background pelo Odoo
        self.partner.invalidate_recordset()

        # Validações
        self.assertGreaterEqual(len(self.partner.loyalty_card_ids), 1, "O cartão deveria ter sido criado automaticamente na venda!")
        self.assertGreaterEqual(self.partner.total_loyalty_points, 1000.0)
        self.assertEqual(self.partner.loyalty_level, 'silver')

    def test_02_multiple_sales_card_consolidation(self):
        """ Validar que múltiplas vendas acumulam no mesmo cliente e evoluem o nível para Gold """
        # Primeira Venda: $20.000 -> 2.000 pontos
        self._create_and_confirm_sale(200)
        
        # Segunda Venda: $30.000 -> 3.000 pontos
        self._create_and_confirm_sale(300)

        self.partner.invalidate_recordset()

        # Total acumulado: 5.000 pontos -> Nível Gold (>= 5000)
        self.assertGreaterEqual(self.partner.total_loyalty_points, 5000.0)
        self.assertEqual(self.partner.loyalty_level, 'gold')

   