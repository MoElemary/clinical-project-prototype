from django.urls import path

from . import views

urlpatterns = [path("", views.homepage, name="homepage_user"),
               path("about-us/", views.about_us, name="information"),
               # path("Admin_page/", views.Admin_view, name="admin_view"),
               ]
