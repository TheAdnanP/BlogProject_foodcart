from django.contrib import admin
from django.urls import path, include

from foodcart import views
from django.conf import Settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_product', views.add_product),
    path('post/', views.add_product_post)
]

