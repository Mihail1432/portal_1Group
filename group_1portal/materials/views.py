from django.shortcuts import render
from django.views.generic import ListView, DetailView
from materials.models import Material

# Create your views here.
class MaterialsHomeView(ListView):
    model = Material
    context_object_name = "materials"
    template_name = "materials/home.html"


class MaterialDetailView(DetailView):
    model = Material
    context_object_name = "material"
    template_name = "materials/material_detail.html"