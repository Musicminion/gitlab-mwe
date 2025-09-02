from flask import Flask, request
app = Flask(__name__)

# @app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
# @app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
# def catch_all(path):
#     print(f"--- {request.method} {request.url} ---")
#     print("Headers:", dict(request.headers))
#     print("Args:", request.args)
#     print("Form:", request.form)
#     print("JSON:", request.get_json(silent=True))
#     print("Data:", request.data)
#     print("-----------------------------")
#     return {"method": request.method, "url": request.url, "headers": dict(request.headers), "args": request.args, "form": request.form, "json": request.get_json(silent=True), "data": request.data.decode()}, 200


# 针对 POST http://customers.ayaka.space/graphql
# {
#   "data": {
#     "cloudActivationActivate": {
#       "licenseKey": "-----BEGIN GITLAB LICENSE-----\n...\n-----END GITLAB LICENSE-----",
#       "futureSubscriptions": [
#         {
#           "cloudLicenseEnabled": true,
#           "offlineCloudLicenseEnabled": false,
#           "plan": "ultimate",
#           "company": "Example Inc",
#           "email": "user@example.com", 
#           "name": "User Example",
#           "startsAt": "2024-01-01",
#           "expiresAt": "2025-01-01",
#           "usersInLicenseCount": 100
#           "addOnPurchases": [
#             {
#               "addOn": "duo_amazon_q",
#               "quantity": 75,
#               "startedOn": "2024-01-01",
#               "expiresOn": "2025-01-01",
#               "purchaseXid": "C-00345678",
#               "trial": false,
#               "amazonQIntegration": {
#                 "enabled": true,
#                 "iamRoleArn": "arn:aws:iam::123456789012:role/GitLabDuoAmazonQRole"
#               }
#             }
#           ]
#         }
#       ],
#       "newSubscription": true,
#       "errors": []
#     }
#   }
# }
@app.route('/graphql', methods=['POST'])
def graphql():
    print("JSON Data:", request.get_json(silent=True), flush=True)
    return {
        "data": {
            "cloudActivationActivate": {
                "licenseKey": "-----BEGIN GITLAB LICENSE-----\neyJkYXRhIjogImRxWDR5QmVjUTdGNTM2bHo5MUFZZVQ2RnRnbEtWdzNDb3E4emJtOUhwTUhYM1RSOVRod3M2MnJQZFk0RytidWcyOHM2RmZzNnZudEpPdEZjVU1VekxIcE1IQUpMVlZzNWRpM1hHN2VReURqVHhMTHE5bHdNdml2c3FDQ3FCYTVSbXlnUHdGejFTbVhWZ3NCU2JiYVdMbGthT0phTElqbnhnMU5nOFJQaThmSVUxM2ppT1NvV0VUaFBZZ3dyOXlKOXYwMXpLMmdtWW1HVUFYQmwyRmhHdW5BaldkZi9XcmxiR0IyNEFlUzh3OFNkQ2M4RTlDSktzbk5aOGg1N3JOVUJ4RytjQ0k1WVNORG1IMytzT1BOdXpiZEszZmpCWE9RaU1iZWFNS0lObWpHQzMvVmhBRjNhU1JZZThoRDNlRjdvYUI4cklmMzZPaDFnbXZFSzd2Y1hZOXZLSm83VWp4VnNmZVA0dXM0QnM1ZUJ6Sy9ORGtYVzN5UHQ2ckxlTys2T092dnJ1a3VGMmpMLzdtdERCZCs0Q0dTWG4ySHZrbEltUEVJZW01MG1ubUtsNFlXK2hyYXZIOTdwTE1TZlpUU3NFcUFPREcrV1krd1dmYjJTbnlaZHp0S1NsVzNuWmM3RWo1YlBvSVRwVzhVemp4WnBEZmQ0V2MzUEh6U0E0bTBSaldMU3F2RjZuRjhreUdPaGRTYjV5VUp2ZmswYmFINndtNVdjQ1FCUEhlbVQrRXZOOU1obUJJeDhSclZmR3AzbXV3Qy9TVWtKZkZuQ2V1bkJvZm01RW5kQThwU0pxUU4rR3lJT3gwQ2pTWnJYd01Ob0Z4anMwS0VlUTFjZzFwVXJSNnhZVXlsNFNtcDdTQ1I3ZzNaQi9IQ3FpY1hiWWdCTU5UOHpCMjhPZjVsMzRURWx5T3NuNDRhSjc4NFcyWGEyelgyenU1d2JsYnJqc3NYdmVmZHNuQT09IiwgImtleSI6ICJmSnVUemxHSVdLbzlPaWlSQ1N1SFY2YWRiSmFEQ0xSL2pVeWpoZ1FXZSt3Y09BNENmS3cyajBWVTJ1Z1l1dGRHa3lnV0kzYmJKSGlLRVFtdlZUUmZ5QkdIQ0J3RzlRdVgvZWs0TTdHVkhqNlk2TktHMEUwd3BPK29aVmNXUk1sampJdVExaWlsdFZaRU54TlFVZTY0TDkvcE9MYUFFaHRwd0J4K0RJZGpPemsyUUQ3UWFRK3VIWEE5RHdTd3Y0TzkrZGd2NnhIR0hTVHBvTGYvNWtHdXNBVzZQaS9YcHBWY0F2NHIxT1FoVlFobjRscUt6ZTVMbjE1UVNPTlJ3a0xOTGNhVGpIK0dtUDk2Tit1djR2YzZLdEdKUDFKK0xwUnpiMU1Wbk9KRld2dys1RjdnSm12VktndnNzb29hVHpkSytKMnE4QVc5WGczSkR5bER5Q2UwRWc9PSIsICJpdiI6ICJhT2NCcEN1RmU4YVFVN0NtSVhsbmxRPT0ifQ==\n-----END GITLAB LICENSE-----",
                "futureSubscriptions": [
                    {
                        "cloudLicenseEnabled": True,
                        "offlineCloudLicenseEnabled": False,
                        "plan": "ultimate",
                        "company": "Example Inc",
                        "email": "user@example.com",
                        "name": "User Example",
                        "startsAt": "2025-01-01",
                        "expiresAt": "2099-01-01",
                        "usersInLicenseCount": 10000,
                        "addOnPurchases": [
                            {
                                "addOn": "duo_amazon_q",
                                "quantity": 750,
                                "startedOn": "2025-01-01",
                                "expiresOn": "2099-01-01",
                                "purchaseXid": "C-00345678",
                                "trial": False,
                                "amazonQIntegration": {
                                    "enabled": True,
                                    "iamRoleArn": "arn:aws:iam::123456789012:role/GitLabDuoAmazonQRole"
                                }
                            }
                        ]
                    }
                ],
                "newSubscription": True,
                "errors": []
            }
        }
    }

# 开启debug
if __name__ == '__main__':
    print("Starting debug server on port 80...")
    app.run(host='0.0.0.0', port=80, debug=True)