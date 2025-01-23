from odoo import models , fields  

class Ligne(models.Model):
    _name = "ligne"

    lid = fields.Char()
    
    quantity = fields.Integer()

    produit = fields.Many2one('produit')

    commande = fields.Many2one('commande',ondelete='cascade')


    _sql_constraints = [
        ('unique_lid','unique("lid")',"Cet ID est déjà utilisé")
    ]
    
