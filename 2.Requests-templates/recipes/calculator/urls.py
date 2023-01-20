from django.urls import path

from .views import omlet_view, pasta_view, buter_view

urlpatterns = [
    path('omlet/', omlet_view),
    path('pasta/', pasta_view),
    path('buter/', buter_view),
]
