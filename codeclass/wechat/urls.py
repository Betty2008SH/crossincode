from django.conf.urls import patterns, url

from wechat import views


urlpatterns = patterns(
    '',
    url(r'^', views.index_view),
)
