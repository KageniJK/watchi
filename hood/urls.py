from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^new_profile/$', views.profile_setup, name='new_profile'),
]
