from django.urls import path
from offer import views

urlpatterns = [
    path('offer/', views.offer_list),
    path('offer/<first_name>/', views.offer_manage),
]