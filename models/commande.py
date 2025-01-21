from odoo import models , fields 
import shopify
class Commande(models.Model):
    _name = "commande"

    cid = fields.Char(required=True)
    client = fields.Text(required=True)
    montant = fields.Float(required=True)
    name = fields.Text(required=True)
    time = fields.Datetime(required=True)
    city = fields.Text(required=True)
    adresse = fields.Text()


    lignes = fields.One2many('ligne', 'commande')

    _sql_constraints = [
        ('unique_cid','unique("cid")',"Cet ID est déjà utilisé")
    ]

    def unlink(self):
        shopify.ShopifyResource.activate_session( shopify.Session(  ) )
        for commande in self:
            shopify.Order.find(commande.cid).destroy()
        return super().unlink()



    
