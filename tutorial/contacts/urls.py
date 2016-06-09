from django.conf.urls import url

from . import views

app_name = "contacts"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contacts/', views.create, name='create'),
    url(r'^(?P<contact_id>[0-9]+)/$', views.read, name='read'),
    url(r'^(?P<contact_id>[0-9]+)/update$', views.update, name='update'),
    url(r'^(?P<contact_id>[0-9]+)/delete$', views.delete, name='delete'),
]