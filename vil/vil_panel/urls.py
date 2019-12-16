from django.urls import path
from . import views
from vil_panel.views import (
StoreDetailListView,
StoreDetailView,
StoreDetailCreateView,
StoreDetailUpdateView,
StoreDetailDeleteView
)

urlpatterns = [
    path('', views.home, name='vilpanel-home'),
    #path('store/', views.store, name='vilpanel-store'),
	path('storemanager/', views.storemanager, name='vilpanel-storemanager'),
	path('zonal/', views.zonalmanager, name='vilpanel-zonal'),
	
	path('storedetail/list/', StoreDetailListView.as_view(), name='vilpanel-storedetaillist'),
	path('storedetail/list/<int:pk>/', StoreDetailView.as_view(), name='vilpanel-storedetail'),
	path('storedetail/new/', StoreDetailCreateView.as_view(), name='vilpanel-storedetailcreate'),
	path('storedetail/<int:pk>/update/', StoreDetailUpdateView.as_view(), name='vilpanel-storedetailupdate'),
	path('storedetail/<int:pk>/delete/', StoreDetailDeleteView.as_view(), name='vilpanel-storedetaildelete'),
]