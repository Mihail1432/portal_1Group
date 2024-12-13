from django.views.generic import ArchiveIndexView, DetailView
from gallery.models import Image

class GalleryHomeView(ArchiveIndexView):
    model = Image
    allow_empty = True
    date_field = "uploaded_at"
    context_object_name = "images"
    template_name = "gallery/home.html"


class ImageDetailView(DetailView):
    model = Image
    context_object_name = "image"
    template_name = "gallery/image_detail.html"