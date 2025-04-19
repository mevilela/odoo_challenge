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


    #constraints
    #check if price is a positive value
    @api.constrains('price')
    def check_positive_float(self):
            for record in self:
                if record.price <= 0:
                    raise ValidationError("Price must be a positive value.")
                
    #check if the stock is available - use depends to link the variables
    @api.depends('stock', 'is_available')
    def compute_if_stock_is_available(self):
        for record in self:
            if record.stock > 0:
                record.is_available = True
        