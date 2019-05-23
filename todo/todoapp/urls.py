from django.conf.urls import url
from django.contrib import admin
from . import views


app_name = 'todoapp'
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
