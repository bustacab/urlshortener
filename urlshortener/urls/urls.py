from rest_framework.routers import DefaultRouter
from .views import URLCreateAPI


default_router = DefaultRouter(trailing_slash=False)
default_router.register('urls', URLCreateAPI, basename="urls-create")


urlpatterns = default_router.urls
