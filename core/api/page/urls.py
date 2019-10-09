from django.conf.urls import url

from core.api.page.views import PageViewSet

urlpatterns = [
    url(r'(?P<pk>[0-9]+)/$',
        PageViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'})),
    url(r'$', PageViewSet.as_view({'get': 'list', 'post': 'create'})),
]
