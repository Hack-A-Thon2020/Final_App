from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.index, name="index"),
                  path('about', views.about, name="about"),
                  path('<int:book_id>', views.book, name="book"),
                  path('donate', views.donate, name="donate"),
                  path('dept_ce', views.dept_ce, name="dept_ce"),
                  path('dept_civil', views.dept_civil, name="dept_civil"),
                  path('dept_mba', views.dept_mba, name="dept_mba"),
                  path('dept_maths', views.dept_maths, name="dept_maths"),
                  path('dept_ec', views.dept_ec, name="dept_ec"),
                  path('dept_mechanical', views.dept_mechanical, name="dept_mechanical"),
                  path('cart', views.cart, name="cart"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
