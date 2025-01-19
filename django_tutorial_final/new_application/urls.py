from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("index", views.index, name = "index"),
    path("graph_generator", views.graph_generator, name = "graph_generator")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
