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
    @api.depends('stock', 'price')
    def compute_discount(self):
        for record in self:
            if record.stock < 5:
                record.discounted_price = record.price - (record.price * 0.1)
            else:
                 record.discounted_price = record.price

    #check if stock is a positive value
    @api.constrains('stock')
    def check_positive_stock(self):
            for record in self:
                if record.stock <= 0:
                    raise ValidationError("Stock must be a positive value.")


