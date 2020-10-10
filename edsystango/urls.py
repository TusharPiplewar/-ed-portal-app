"""edsystango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from edApp import views
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.SignUpPage),
    path('dashboard/',views.dashboard),
    path('Allclasses/',views.Allclasses),
    path('Newclasses/',views.Newclasses),
    path('Editdeleteclasses/',views.Editdeleteclasses),
    path('Subjecttoclasses/',views.Subjecttoclasses),
    path('Addsubject/',views.Addsubject),
    path('institute/',views.institute),
    path('Viewinstitute/',views.Viewinstitute),
    path('rules/',views.rules),
    path('fees/',views.fees),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
