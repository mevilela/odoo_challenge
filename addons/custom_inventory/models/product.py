from odoo import models, fields, api
from odoo.exceptions import ValidationError

#Task 2 
class Product(models.Model):
    _name = 'product'
    _description = 'products'

    name = fields.Char(string='Product Name', required=True)
    category = fields.Selection([('eletronics','Eletronics'), ('clothing','Clothing'),
                                 ('furniture', 'Furniture')])
    price = fields.Float(string='Price')
    stock = fields.Integer(string='Stock')
    is_available = fields.Boolean(string='Is available', compute='compute_if_stock_is_available', store=True)
    
    #task 3: add discounted_price 
    discounted_price = fields.Float(string='Discounted price', compute='compute_discount', store=True) 

    # #bonus: add action button - custom discount 
    custom_discount = fields.Float(string='Custom Discount (%)')


    #constraints
    #check if price is a positive value
    @api.constrains('price')
    def check_positive_float(self):
            for record in self:
                if record.price <= 0:
                    raise ValidationError("Price must be a positive value.")
                
    #check if the stock is available - use depends to link the variables
    @api.depends('stock')
    def compute_if_stock_is_available(self):
        for record in self:
            if record.stock > 0:
                record.is_available = True
    
    #task 3: compute_discount 
    #bonus task: if custom discount then applies custom discount otherwise, low stock business rule
    @api.depends('stock', 'price')
    def compute_discount(self):
        for record in self:
            if record.custom_discount > 0:
                 record.discounted_price = record.price - (record.price * record.custom_discount / 100)
            elif record.stock < 5:
                record.discounted_price = record.price - (record.price * 0.1)
            else:
                 record.discounted_price = record.price

    #check if stock is a positive value
    @api.constrains('stock')
    def check_positive_stock(self):
            for record in self:
                if record.stock <= 0:
                    raise ValidationError("Stock must be a positive value.")
    
    #bonus: add action button - custom discount 
    def action_custom_discount(self):
         for record in self:
              if 0 < record.custom_discount < 100:
                   record.discounted_price = record.price - (record.price * record.custom_discount / 100)
              else: 
                   raise ValidationError("Discount percentage must be a number between 0 and 100")

