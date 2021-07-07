from django.shortcuts import render
from django.views.generic import TemplateView


class IndexOfInstallerView(TemplateView):
    template_name = 'index.html'
