"""exam_task_wad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

import main_app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('layout/', main_app.views.layout_example),

    # good CRUD
    path('good/', main_app.views.list_goods),
    path('good/add/', main_app.views.layout_example),
    path('good/edit/<int:id>', main_app.views.layout_example),
    path('good/delete/<int:id>', main_app.views.layout_example),

    # checkout CRUD

    path('checkouts/', main_app.views.list_checkouts),
    path('checkouts/add/', main_app.views.layout_example),
    path('checkouts/edit/<int:id>', main_app.views.layout_example),
    path('checkouts/delete/<int:id>', main_app.views.layout_example),

    # User manipulation

    path('users/', main_app.views.layout_example),
    path('register/', main_app.views.register_user),
    path('login/', main_app.views.auth_user),
    path('logout/', main_app.views.layout_example),
    path('profile/', main_app.views.profile),

]
