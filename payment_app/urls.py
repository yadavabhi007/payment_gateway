from django.urls import path
from . import views


urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("payment/", views.OrderPayment.as_view(), name="payment"),
    path("callback/", views.callback, name="callback"),
]