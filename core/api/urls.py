from django.conf.urls import url, include

urlpatterns = [
    url(r'^page/', include('core.api.page.urls')),
]
