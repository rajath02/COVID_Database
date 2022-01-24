from django.urls import URLPattern, path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("home/", views.home, name="home"),
    path("home/new_cases.html", views.new_cases, name="new_cases"),
    path("home/recovered.html", views.recovered, name="recovered"),
    path("home/deaths.html", views.death, name="deaths"),
    path("home/vaccine.html", views.vaccines, name="vaccine")
]

urlpatterns += staticfiles_urlpatterns()