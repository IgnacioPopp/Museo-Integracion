"""
URL configuration for museo_integracion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from .views import IndexPage, AboutUs, Visita, Tickets, Exhibiciones, Mujeres, NoticiaGrid1, NoticiaGrid2, NoticiaGrid3, NoticiaGrid4, NuevaSala

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", IndexPage.as_view(), name="landing_page"),
    path('aboutus/', AboutUs.as_view(), name="aboutus_page"),
    path('visita/', Visita.as_view(), name="visita_page"),
    path('tickets/', Tickets.as_view(), name='tickets_page'),
    path('exhibiciones/', Exhibiciones.as_view(), name='exhibiciones_page'),
    path('mujeres/', Mujeres.as_view(), name='mujeres_page'),
    path('noticia_grid1/', NoticiaGrid1.as_view(), name='noticiagrid1_page'),
    path('noticia_grid2/', NoticiaGrid2.as_view(), name='noticiagrid2_page'),
    path('noticia_grid3/', NoticiaGrid3.as_view(), name='noticiagrid3_page'),
    path('noticia_grid4/', NoticiaGrid4.as_view(), name='noticiagrid4_page'),
    path('nueva_sala/', NuevaSala.as_view(), name='nuevasala_page')
]


