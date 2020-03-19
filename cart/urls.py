from . import views
from django.urls import path

urlpatterns = [

    path('<int:Book_id>', views.borrow, name="borrow"),
    ]