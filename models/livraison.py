from odoo import models , fields , api
from requests import post 
from random import randint

class Livraison(models.Model):
    _name = "livraison"


    suivi = fields.Text()
    commande = fields.Many2one('commande',ondelete='cascade')


    _sql_constraints = [
        ('unique_commande','unique("commande")',"Cette commande est déjà en mode livraison")
    ]

    @api.model
    def create(self, vals):
        res = super().create(vals)
        # url = "https://ws.dev.aramex.net/shippingapi.v2/shipping/service_1_0.svc/json/CreateShipments"
        url = "https://ws.aramex.net/shippingapi.v2/shipping/service_1_0.svc/json/CreateShipments"
        json = {
            "ClientInfo" : {
                "UserName":"testingapi@aramex.com",
                "Password":"R123456789$r",
                "Version":"v1",
                "AccountNumber":"102331",
                "AccountPin":"321321",
                "AccountEntity":"LON",
                "AccountCountryCode":"GB",
                "Source":24
            },
            "Transaction" : {
                "Reference1":None,
                "Reference2":None,
                "Reference3":None,
                "Reference4":None,
                "Reference5":None
            },
            "Shipments" : {
                "Reference1":None,
                "Reference2":None,
                "Reference3":None,
                "Shipper":{
                    "Reference1":None,
                    "Reference2":None,
                    "AccountNumber":"102331",
                    "PartyAddress":None,
                    "Contact":None
                },
                "Consignee":{
                    "Reference1":None,
                    "Reference2":None,
                    "AccountNumber":None,
                    "PartyAddress":{
                        "Line1":res.commande.adresse,
                        "Line2":None,
                        "Line3":None,
                        "City":res.commande.city,
                        "StateOrProvinceCode":None,
                        "PostCode":None,
                        "CountryCode":"MA"
                    },
                    "Contact":{
                        "Department":"",
                        "PersonName":"",
                        "Title":"",
                        "CompanyName":"",
                        "PhoneNumber1":"",
                        "PhoneNumber1Ext":"",
                        "PhoneNumber2":"",
                        "PhoneNumber2Ext":"",
                        "FaxNumber":"",
                        "CellPhone":"",
                        "EmailAddress":"",
                        "Type":""
                    }
                },
                "ThirdParty":None,
                "ShippingDateTime":"",
                "DueDate":None,
                "Comments":None,
                "PickupLocation":None,
                "OperationsInstructions":None,
                "AccountingInstructions":None,
                "Details":{
                    "Dimensions":None,
                    "NumberOfPieces":1,
                    "ActualWeight":100,
                    "ProductGroup":"DOM",
                    "ProductType":"OND",
                    "PaymentType":"C",
                    "PaymentOptions":"ASCC",
                    "Services":None,
                    "DescriptionOfGoods":"Electronics",
                    "GoodsOriginCountry":"MA",
                    "CustomsValueAmount":None,
                    "CashOnDelivery":None,
                    "InsuranceAmount":None,
                    "CashAdditionalAmount":None,
                    "CashAdditionalDescription":None,
                    "CollectAmount":None,
                    "items":None
                },
                "Attachments":None,
                "ForeignHAWB":None,
                "TransportType":None,
                "Number":None,
                "PickupGUID":None
            },
            "LabelInfo" : {
                "ReportID":9201,
                "ReportType":"URL"
            }
        }


        req = post(url,json=json)

        print(req.content.decode())
        print(req.status_code)
        suivi = str(randint(100000,999999))
        print(res.write({"suivi":suivi}))

        mail_values = {
            'subject': 'Suivez votre commande',
            'body_html': f'<a href="https://www.aramex.com/ma/en/track/track-results-new?source=aramex&ShipmentNumber={suivi}">Suivez votre commande sur Aramex</a>',
            'email_to': res.commande.client,
            'email_from': 'alaouisalim30@gmail.com',
        }
        mail = self.env['mail.mail'].create(mail_values)

        mail.send()

        return res



    
