from django.shortcuts import render
from datetime import datetime


# Create your views here.
def bk(request):

    d = datetime.now()

    # payments_method = "bkash"
    # discount = "10%"
    # condition = 'Only for first time users'
    # payments_info = {'pm': payments_method, 'dis': discount, 'con': condition}
    # return render(request, "payments/payments1.html", payments_info)
    return render(request, "payments/payments1.html", {'date': d})

def rk(request):
    d = datetime.now()
    # payments_method = "rocket"
    # discount = "15%"
    # condition = 'Only for first time users'
    # payments_info = {'pm': payments_method, 'dis': discount, 'con': condition}
    # return render(request, "payments/payments1.html", payments_info)
    return render(request, "payments/payments2.html", {'date': d})
