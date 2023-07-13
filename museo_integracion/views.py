from django.views.generic import TemplateView

class IndexPage(TemplateView):
    template_name = "index.html"

class Visita(TemplateView):
    template_name = "./html/visita.html"

class Tickets(TemplateView):
    template_name = "./html/Tickets.html"

class AboutUs(TemplateView):
    template_name = "./html/aboutus.html"

class Exhibiciones(TemplateView):
    template_name = "./html/exhibiciones.html"

class Mujeres(TemplateView):
    template_name = "./html/mujeres.html"

class NoticiaGrid1(TemplateView):
    template_name = "./html/noticia_grid1.html"

class NoticiaGrid2(TemplateView):
    template_name = "./html/noticia_grid2.html"

class NoticiaGrid3(TemplateView):
    template_name = "./html/noticia_grid3.html"

class NoticiaGrid4(TemplateView):
    template_name = "./html/noticia_grid4.html"

class NuevaSala(TemplateView):
    template_name = "./html/nueva_sala.html"
