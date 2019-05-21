from django.conf.urls import url
from django.contrib import admin
from todoapp import views


app_name = 'todoapp'
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<task_id>[0-9]+)/$', views.detail, name='detail'),
]
