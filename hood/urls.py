from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^new_profile/$', views.profile_setup, name='new_profile'),
    url(r'^new_hood/$', views.new_hood, name='new_hood'),
    url(r'^new_biz/$', views.new_biz, name='new_biz'),
    url(r'^new_message/$', views.new_message, name='new_message'),
    url(r'^biz/(\d+)', views.business, name=biz)
]
