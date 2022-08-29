from . import views
from django.urls import path

urlpatterns = [
    path('', views.demo, name='demo'),
#     # path('add/', views.addition, name='addition'),
#     # path('contact/', views.contact, name='contact'),
#     # path('home/', views.home, name='home'),
#     # path('details/', views.details, name='details'),
#     # path('Thanks/', views.Thanks, name='Thanks'),
]
