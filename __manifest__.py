{
    "name":"Shipments Shop",
    "author":"Salim Alaoui",
    "category":"Inventory",
    "version":"1.0",
    "description": "Shopify store management integration with Odoo and ARAMEX",
    "website":"https://www.linkedin.com/in/salimelomarialaoui/",
    "depends":[
        "base",
        # "stock",
        # "purchase"
    ],
    "data": [ 
        "views/base_menu.xml",
        "views/produit_view.xml",
        "security/ir.model.access.csv",
        "views/entree_view.xml",
        "views/commande_view.xml",
        # "views/ligne_view.xml",
        # "views/synchroniser_view.xml",
    ],
    "application":True
}