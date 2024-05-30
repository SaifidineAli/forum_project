"""
URL configuration for forum_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static

import authentication.views
import forum.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # urls pour authentification
    path('connexion/', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True
    ), name='login'),
    path('deconnexion/', authentication.views.logout_user, name='logout'),
    path('inscription/', authentication.views.signup_page, name='signup'),
     path('users/', authentication.views.user_list, name='user_list'),
    # inclusion des urls liés à l'app forum
    path('forum/', include('forum.urls')),
    path('', forum.views.category_list, name='home'),
]


# Uniquement si on est en mode développement (pour le téversement des photos)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)