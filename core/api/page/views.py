from rest_framework.viewsets import ModelViewSet

from core.api.page.serializers import PageSerializer
from core.models import Page


class PageViewSet(ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    model = Page
