"""
factory/urls.py
--------------------------------------------------
URL Configuration file for the factory application.
"""
from django.urls import path
from factory import views


app_name='factory'
#------------------ INDEX PAGE ------------------------------
urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
]

#------------------- WIDGET URL MAPPING ----------------------
urlpatterns += [
  path('widgets/', views.ListWidgets.as_view(), name='widget-list'),
  path('widget/', views.CreateWidget.as_view(), name='make-widget'),
  path('widget/<int: pk>/', views.EditWidget.as_view(), name='change-widget'),
  path('widget/<int:pk>/delete/', views.DeleteWidget.as_view(), name='delete-widget'),
]
