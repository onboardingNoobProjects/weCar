from django.conf.urls import url
from . import views

urlpatterns = [
    # /wecar/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /wecar/deal/add
    url(r'^deal/add/$', views.DealCreate.as_view(), name='deal-add'),

    # # /wecar/register
    # url(r'^register/$', views.UserForm.as_view(), name='register'),

    # /wecar/<deal_id>
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
