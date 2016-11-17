from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^form_info$', views.process),
    url(r'^result$', views.result)
]
