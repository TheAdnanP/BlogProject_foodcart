from django.contrib import admin
from django.urls import path, include

from foodcart import views
from django.conf import Settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('contact.html/', views.contact),
    path('index.html/', views.home),
    path('about.html/', views.about),
    path('cookies.html/', views.cookies),
    path('testimonial.html/',views.testimonial)
]

