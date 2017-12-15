"""for learning_logs def url model"""

from django.conf.urls import url

from . import views

urlpatterns = [
	#zhu ye
	url(r'^$', views.index, name='index'),
	#show all topics
	url(r'^topics/$', views.topics, name='topics'),
	#show detail page
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
	#for new topic page
	url(r'^new_topic/$', views.new_topic, name='new_topic'),
	#for the items of new topic page
	url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
	#for edit items
	url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]





