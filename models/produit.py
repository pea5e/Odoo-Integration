from odoo import models , fields , api 
from odoo.exceptions import  ValidationError
import shopify

class Produit(models.Model):
    _name = "produit"
    _log_access = False

    name = fields.Text(required=True)
    price = fields.Float()
    quantity = fields.Integer()
    shopify_id = fields.Char()


    _sql_constraints = [
        ('unique_name','unique("name")',"Ce nom est déjà utilisé")
    ]

    @api.constrains("price")
    def _is_price_valid(self):
        for record in self:
            if record.price <= 0:
                raise ValidationError("Veuillez saisir un prix valid")
            
    @api.model
    def create(self, vals):
        res = super().create(vals)
        shopify.ShopifyResource.activate_session( shopify.Session(  ) )
        product = shopify.Product()
        product.handle = vals["name"]
        product.title = vals["name"]
        variant = shopify.Variant({'sku':"produit-"+str(res.id),'price': vals["price"],"inventory_management": "shopify","inventory_quantity":0})
        product.variants = [variant]
        product.save()
        res.shopify_id = product.id
        
        return res


    
    def write(self,args):
        res = super().write(args)
        shopify.ShopifyResource.activate_session( shopify.Session(  ) )
        product = shopify.Product.find(self.shopify_id)
        product.handle = self.name
        product.title = self.name
        variant = product.variants[0]
        # https://community.shopify.com/c/graphql-basics-and/remove-inventorylevel-from-variant/td-p/1577756
        # https://shopify.dev/docs/api/admin-rest/2025-01/resources/inventorylevel
        variant.price = self.price
        # variant.inventory_quantity = self.quantity
        product.variants = [variant]
        print(product.save())
        # print(product.to_json())
        # print(product.errors.full_messages())

        return res
        


    def unlink(self):
        shopify.ShopifyResource.activate_session( shopify.Session(  ) )
        for product in self:
            shopify.Product.find(product.shopify_id).destroy()
        return super().unlink()
            
        

