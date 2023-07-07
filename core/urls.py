from django.contrib import admin
from django.urls import path, include
from .views import Sub


urlpatterns = [
    path("admin/", admin.site.urls),
    path("main", Sub.as_view()),
    path("", Sub.as_view()),
    path("user/", include("user.urls")),
]
