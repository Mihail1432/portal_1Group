from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portal.urls')),
    path('forum/', include('forum.urls')),
    path('diary/', include("diary.urls")),
    path('events/', include("events.urls")),
    path('surveys/', include("surveys.urls")),
    path('votes/', include("votes.urls")),
    path('announcements/', include("announcements.urls")),
    path('materials/', include("materials.urls")),
    path('protfolio/', include("portfolio.urls")),
    path('gallery/', include("gallery.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
