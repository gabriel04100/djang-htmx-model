from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_view, name='predict_view'),
    
]

htmx_urls = [
    path('validate/', views.validate_input_view, name='validate_input')
]
urlpatterns += htmx_urls