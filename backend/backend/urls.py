from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('history/', TemplateView.as_view(template_name='history.html'), name='history'),
    path('detail/', TemplateView.as_view(template_name='detail.html'), name='detail'),
    path('detail/', TemplateView.as_view(template_name='detail.html'), name='detail'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
]
