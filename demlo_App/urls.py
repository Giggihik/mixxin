from django.urls import path, include, reverse_lazy
from django.contrib.auth import urls as auth_urls
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('account/', include(auth_urls)),
    path('', views.ServicesView.as_view(), name='home'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('req', views.RequestFormView.as_view(), name='request-form'),
    path('request/', views.RequestsView.as_view(), name='requests'), 
    path('login/',
         LoginView.as_view(success_url=reverse_lazy('form')),
         name='login'
    ) 
]
