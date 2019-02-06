"""projectDAW URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from index import views as index_views
from accounts import views as accounts_views
from .api import router




urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('index.urls')),
    url(r'^about/', index_views.about),
    url(r'^cita/$',accounts_views.ListarCitas, name='citas'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^userprofile/$', accounts_views.userprofile, name='userprofile'),
    url(r'^add', accounts_views.Add, name='add-cita'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^contact/', index_views.contact),
    url(r'^galeria/', index_views.galeria),
    path('api/', include(router.urls)),
    path('', RedirectView.as_view(url='/index/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
