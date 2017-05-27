from django.conf.urls import url, include

urlpatterns = [
    url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
]
