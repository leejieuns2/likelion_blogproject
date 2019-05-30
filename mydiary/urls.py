"""mydiary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import diary.views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', diary.views.index, name = 'index'),
    path('new', diary.views.new, name = 'new'),
    path('detail/<int:blog_id>', diary.views.detail, name = 'detail'),
    path('edit/<int:blog_id>', diary.views.edit, name = 'edit'),
    path('blog/delete/<int:blog_id>', diary.views.delete, name = 'delete'),
    path('signup/', diary.views.signup, name="signup"),
    path('login/', diary.views.login, name="login"),
    path('logout/', diary.views.logout, name="logout"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

