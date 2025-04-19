{
    'name': 'Custom Inventory',
    'summary': 'First Odoo 17 module',
    'description': '''
        One AiQ: Odoo Challenge.
    ''',
    'version': '1.0',
    'category': 'custom',
    'license': 'LGPL-3', 
    'author': 'Maria Eduarda Vilela',
    'depends': [
        'base',
    ],
    'data': [
        
        'security/ir.model.access.csv',
        'views/product_view.xml',
        'views/menus.xml',
        
    ],
    
    'installable': True,
    'application': True,

}

