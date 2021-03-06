"""calender URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth import  views as auth_views
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('calender/', views.calender,name='calender'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.login, name='login'),
    path('logout/',auth_views.logout, {'next_page':'/'}, name='logout'),
    path('entry/<int:pk>', views.details ,name='details'),
    path ('entry/add', views.add, name='add'),
    path('entry/<int:pk>/delete', views.delete , name='delete'),
    path('entry/<int:id>/hapus', views.hapus, name='hapus'),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
