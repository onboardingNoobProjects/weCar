from django.conf.urls import url
from . import views

urlpatterns = [
    # /wecar/
    url(r'^$', views.index, name='index'),

    # /wecar/<deal_id>
    url(r'^(?P<deal_id>[0-9]+)/$', views.detail, name='detail'),
]
