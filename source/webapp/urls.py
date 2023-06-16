from django.urls import path

from source.webapp.views import main, cat_stats

urlpatterns = [
    path('', main),
    path('cat_stats/', cat_stats)
]
