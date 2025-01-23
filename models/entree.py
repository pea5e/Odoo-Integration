from odoo import models , fields , api 
from odoo.exceptions import  ValidationError
import shopify

class Entree(models.Model):
    _name = "entree"

    produit = fields.Many2one('produit', ondelete='cascade')
    quantity = fields.Integer()

    @api.constrains("quantity")
    def _is_quantity_valid(self):
        for record in self:
            if record.quantity <= 0:
                raise ValidationError("Veuillez saisir une quantity")
            
    @api.model
    def create(self, vals):
        res = super().create(vals)
        shopify.ShopifyResource.activate_session( shopify.Session(  ) )
        res.produit.write({"quantity":res.produit.quantity+res.quantity})
        # print(shopify.inventory_item.InventoryItem.find(shopify.Product.find()[0].to_dict()["variants"][0]['inventory_item_id']).to_dict())
        shopify.InventoryLevel.adjust(location_id=shopify.Location.find_first().id,
                                                  inventory_item_id=shopify.Product.find(res.produit.shopify_id).variants[0].inventory_item_id,
                                                    available_adjustment=res.quantity)
        return res

    
    def write(self,args):
        return False
