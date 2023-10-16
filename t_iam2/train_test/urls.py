from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('check_data/', views.check_data, name='check_data'),
    path('login_submit/',views.login_submit, name='login_submit'),
    path('login_account_submit/',views.login_account_submit, name='login_account_submit')
]