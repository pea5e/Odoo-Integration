from requests import post 



url = "https://ws.dev.aramex.net/shippingapi.v2/shipping/service_1_0.svc/json/CreateShipments"
url = "https://ws.aramex.net/shippingapi.v2/shipping/service_1_0.svc/json/CreateShipments"

# https://www.aramex.com/docs/default-source/resourses/resourcesdata/shipping-services-api-manual.pdf
json = """
{
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
        "Reference1":null,
        "Reference2":null,
        "Reference3":null,
        "Reference4":null,
        "Reference5":null
    },
    "Shipments" : {
        "Reference1":null,
        "Reference2":null,
        "Reference3":null,
        "Shipper":{
            "Reference1":null,
            "Reference2":null,
            "AccountNumber":"102331",
            "PartyAddress":null,
            "Contact":null
        },
        "Consignee":{
            "Reference1":null,
            "Reference2":null,
            "AccountNumber":null,
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
        "ThirdParty":null,
        "ShippingDateTime":"",
        "DueDate":null,
        "Comments":null,
        "PickupLocation":null,
        "OperationsInstructions":null,
        "AccountingInstructions":null,
        "Details":{

        },
        "Attachments":null,
        "ForeignHAWB":null,
        "TransportType":null,
        "Number":null,
        "PickupGUID":null
    },
    "LabelInfo" : {
        "ReportID":9201,
        "ReportType":"URL"
    }
}

"""
