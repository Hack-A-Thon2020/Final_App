from . import views
from django.urls import path

urlpatterns = [

    path('<int:user_id>', views.user_reward, name="user_reward"),

    ]