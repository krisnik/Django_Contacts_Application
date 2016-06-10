from django.conf.urls import url, include

from . import views

from rest_framework import routers
import restviews


app_name = "contacts"


router = routers.DefaultRouter()
router.register(r"contacts", restviews.ContactViewSet)


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contacts/', views.create, name='create'),
    url(r'^(?P<contact_id>[0-9]+)/$', views.read, name='read'),
    url(r'^(?P<contact_id>[0-9]+)/update$', views.update, name='update'),
    url(r'^(?P<contact_id>[0-9]+)/delete$', views.delete, name='delete'),

    #rest
    url(r'^rest/', include(router.urls)),
]