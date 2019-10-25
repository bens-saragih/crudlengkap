from django.conf.urls import url 
from .views import SosmedListView,SosmedFormView,SosmedDeleteView


urlpatterns=[
	url(r'^$',SosmedListView.as_view(),name='list'),
	url(r'^create/$',SosmedFormView.as_view(),name='create'),
	url(r'^update/(?P<update_id>[0-9]+)$',SosmedFormView.as_view(),name='update'),
	url(r'^delete/(?P<delete_id>[0-9]+)$',SosmedDeleteView.as_view(),name='delete')


]