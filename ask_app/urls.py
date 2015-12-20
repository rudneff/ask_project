from django.conf.urls import url

from ask_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^handle_wsgi/$', views.handle_wsgi_get_post, name='wsgi_test')
]
