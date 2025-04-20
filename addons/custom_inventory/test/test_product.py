from odoo.tests import TransactionCase
from odoo.exceptions import ValidationError


class ProductTest(TransactionCase):

    #setup the test environment
    def SetUp(self):
        super(ProductTest, self).setUp()

        self.product_full_stock = self.env['product'].create({
            'name': 't-shirt',
            'category': 'clothing',
            'price': 100,
            'stock': 10
        })

        self.product_low_stock = self.env['product'].create({
            'name': 't-shirt',
            'category': 'clothing',
            'price': 100,
            'stock': 4
        })

        #check if discount is applied
        def test_discount_price_based_on_stock():
            
            self.assertEqual(self.product_full_stock.discounted_price, 100,
                             'Products with stock >= 5 should not have discount applied')
            
            self.assertEqual(self.product_low_stock.discounted_price, 90,
                             'Products with stock >= 5 should have 10% discount applied')
            
            self.product_full_stock.stock = 4

            self.assertEqual(self.product_full_stock.discounted_price, 90,
                             'Discounted price should update when stock falls below 5')
            
            self.product_low_stock = 10 

            self.assertEqual(self.product_low_stock.discounted_price, 100,
                             'Discounted price should update when stock goes up then 5')
            
        #prevent adding products with stock = 0
        def test_product_with_no_stock_cannot_be_created():

             with self.assertRaises(ValidationError) as assert_error:
                self.env['product'].create({
                'name': 'shoes',
                'category': 'clothing',
                'price': 100,
                'stock': 0
                })



        
            

