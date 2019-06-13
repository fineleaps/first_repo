from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login


app_name = "results"

urlpatterns = [

    url(r'^result/add/(?P<campaign_slug>[-\w]+)/(?P<prospect_id>[0-9]+)/$',
        views.result_add, name='result_add'),

    # url(r'^campaign/list/$', views.CampaignListView.as_view(), name='campaign_list'),
    # path('campaign/detail/<int:pk>/', views.CampaignDetailView.as_view(), name='campaign_detail'),

]