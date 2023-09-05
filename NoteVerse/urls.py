"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from Notes import views
from allauth.account.views import EmailView
from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2LoginView,
    OAuth2CallbackView,
)
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Notes.urls')),
    path('verification/' , include('verify_email.urls')),
    #path('accounts/' , include('allauth.urls')),
    path('accounts/email/', EmailView.as_view() , name='account_email'),
    path('accounts/google/login/', OAuth2LoginView.adapter_view(adapter=GoogleOAuth2Adapter), name='google_login'),
    path('accounts/google/login/callback/', OAuth2CallbackView.adapter_view(adapter=GoogleOAuth2Adapter), name='google_callback'),
    path('accounts/facebook/login/', OAuth2LoginView.adapter_view(adapter=FacebookOAuth2Adapter), name='facebook_login'),
    path('accounts/facebook/callback/', OAuth2CallbackView.adapter_view(adapter=FacebookOAuth2Adapter), name='facebook_callback'),
]
