from django.views.generic.base import TemplateView
from django.views import View

# Create your views here.

class Index(TemplateView):
    template_name = 'home/index.html'