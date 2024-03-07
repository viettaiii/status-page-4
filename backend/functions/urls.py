from django.urls import path
from . import views


# path: /functions/
urlpatterns = [

    path('management/', views.function_list, name='function_list'),
    path('create/', views.function_create, name='function_create'),
    path('update/<int:pk>/', views.function_update, name='function_update'),
    path('delete/<int:pk>/', views.function_delete, name='function_delete'),
]
