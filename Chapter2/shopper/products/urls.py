from django.urls import path

from . import views
#from .views import ( ProductListView)


urlpatterns = [

   path("", views.products, name="products"),
  
  
]
