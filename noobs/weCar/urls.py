from django.conf.urls import url
from django.contrib.auth import logout
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    # /wecar/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /wecar/<deal_id>
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /wecar/deal/add
    url(r'^add/$', views.DealCreate.as_view(), name='deal-add'),

    # /wecar/deal/<pk>/update
    url(r'^deal/(?P<pk>[0-9]+)/update/$', views.DealUpdate.as_view(), name='deal-update'),

    # /wecar/deal/<pk>/delete
    url(r'^deal/(?P<pk>[0-9]+)/delete/$', views.DealDelete.as_view(), name='deal-delete'),

    # /wecar/register
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /wecar/logout
    # url(r'^logout/$', views.logout_view , name='logout')
    # url(r'^logout/$', views.Logout.as_view(), name='logout'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout', kwargs={ 'next_page' : 'index', }),

]
