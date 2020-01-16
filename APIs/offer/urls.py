from django.urls import path
from offer import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('offer/', views.OfferList.as_view()),
    path('offer/<first_name>/', views.OfferManage.as_view()),
    path('generateoffer/', views.GenerateOffer.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)