from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('items', views.index, name="items"),
                  path('donate', views.donate, name="donate"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
