from odoo import models , fields 
import shopify

class Synchroniser(models.TransientModel):
    _name = "synchroniser"

    name = fields.Text()

    def read(self, fields=None, load='_classic_read'):

        redirect = {
            'type': 'ir.actions.act_window',
            'name': 'Commandes',
            'view_mode': 'tree',  
            'res_model': 'commande', 
            'target': 'current', 
        }
        shopify.ShopifyResource.activate_session( shopify.Session(  ) )
        
        orders = shopify.Order.find()
        last_record = self.env['commande'].search([], order='id desc', limit=1)
        if(last_record.create_date):
            orders = shopify.Order.find(created_at_min=str(last_record.create_date).replace(' ','T'))
        else :
            orders = shopify.Order.find()
        


        while True:
            for order in list(orders):
                dic = order.to_dict()

                com = self.env['commande'].create({
                "cid":dic["id"],
                "client": dic["customer"]["email"],
                "montant":float(dic["current_subtotal_price"]),
                "name":dic["name"],
                "time":dic["processed_at"].replace("T"," ")[:-6],
                "city":dic["shipping_address"]["city"],
                "adresse":dic["shipping_address"]["address1"]
                })
                for line in dic["line_items"]:
                    li = self.env['ligne'].create({
                    "lid":line["id"],
                    "quantity": line["quantity"],
                    "produit":int(line["sku"].split('-')[1]),
                    "commande":com.id,
                    })
                    li.produit.write({"quantity":li.produit.quantity-line["quantity"]})

            if orders.has_next_page():
                orders = orders.next_page()
                continue
            return super().read(fields,load)