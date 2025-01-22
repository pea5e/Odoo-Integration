from requests import post 



url = "https://ws.dev.aramex.net/shippingapi.v2/shipping/service_1_0.svc/json/CreateShipments"
url = "https://ws.aramex.net/shippingapi.v2/shipping/service_1_0.svc/json/CreateShipments"

# https://www.aramex.com/docs/default-source/resourses/resourcesdata/shipping-services-api-manual.pdf
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
                "Line1":"",
                "Line2":"",
                "Line3":"",
                "City":"",
                "StateOrProvinceCode":"",
                "PostCode":"",
                "CountryCode":""
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
