from . import views
from django.urls import path

urlpatterns = [
    path('checkout', views.checkout, name="checkout"),
    path('message', views.message, name="message"),
    ]