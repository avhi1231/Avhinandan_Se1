import paytmchecksum
from django.shortcuts import render, redirect
from django.http import JsonResponse
def initiate_payment(request):
    order_id = "ORDER" + str(int(time.time()))
    paytm_params = {
        "MID": "YourMerchantID",
        "WEBSITE": "WEBSTAGING",
        "INDUSTRY_TYPE_ID": "Retail",
        "CHANNEL_ID": "WEB",
        "ORDER_ID": order_id,
        "CUST_ID": "customer@example.com",
        "TXN_AMOUNT": "100.00",
        "CALLBACK_URL": "http://127.0.0.1:8000/payments/response/",
    }
    checksum = paytmchecksum.generateSignature(paytm_params, "YourMerchantKey")
    paytm_params["CHECKSUMHASH"] = checksum
    return render(request, "payments/paytm_redirect.html", {"paytm_params": paytm_params})

def payment_response(request):
    response_dict = {}
    for key, value in request.POST.items():
        response_dict[key] = value
    checksum_verified = paytmchecksum.verifySignature(
        response_dict, "YourMerchantKey", response_dict["CHECKSUMHASH"]
    )
    if checksum_verified and response_dict["STATUS"] == "TXN_SUCCESS":
        # Update your database and transaction status
        return JsonResponse({"status": "Payment Successful"})
    else:
        return JsonResponse({"status": "Payment Failed"})