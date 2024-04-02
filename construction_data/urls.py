from django.urls import path
from .views import SurfaceView, UsageView, BatimentImpactCarboneView

urlpatterns = [
    path("surface/<int:batiment_id>/", SurfaceView.as_view(), name="surface"),
    path("usage/<int:batiment_id>/", UsageView.as_view(), name="usage"),
    path(
        "impact-carbone/<int:batiment_id>/",
        BatimentImpactCarboneView.as_view(),
        name="batiment-impact-carbone",
    ),
]
