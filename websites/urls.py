from django.urls import path
from . import views

urlpatterns = [
    path('', views.WebsiteListView.as_view(), name='website-list'),
    path('detail/<int:pk>', views.WebsiteDetailView.as_view(), name='website-detail'),

]