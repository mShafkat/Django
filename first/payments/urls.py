from django.urls import path
from.import views


urlpatterns = [
    path('bkash/',views.bkash,name ='payment_1'),
    path('rocket/',views.rocket,name ='payment_2'),

]
    