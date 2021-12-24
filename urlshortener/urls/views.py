from operator import itemgetter

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response

from .models import URL
from .serializers import URLSerializer
from .services import from_base_10_to_64
from .constants import ALPHABET


class URLCreateAPI(GenericViewSet, CreateModelMixin):
    serializer_class = URLSerializer
    queryset = URL.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        url_obj = URL.objects.create(url=serializer.data["url"])
        digits = from_base_10_to_64(url_obj.pk)
        digits.reverse()
        return Response(
            f"http://{request.get_host()}"
            f"/{itemgetter(*digits)(ALPHABET)}"
        )







