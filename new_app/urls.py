from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('hello/', views.hello_veiw, name="hello"),
    path('about/', views.about_view, name="about"),
    path('item_detail/<int:item_id>/', views.item_detail_view, name="item_detail")
    
]
