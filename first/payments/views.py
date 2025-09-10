from django.shortcuts import render


# Create your views here.
def bk(request):
    payments_method = "bkash"
    discount = "10%"
    condition = 'Only for first time users'
    payments_info = {'pm': payments_method, 'dis': discount, 'con': condition}
    return render(request, "payments/payments1.html", payments_info)

def rk(request):
    payments_method = "rocket"
    discount = "15%"
    condition = 'Only for first time users'
    payments_info = {'pm': payments_method, 'dis': discount, 'con': condition}
    return render(request, "payments/payments2.html", payments_info)
