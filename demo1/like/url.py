
from django.conf.urls import url, include

from . import view
from . import views

urlpatterns = [

    url(r'^child/$',views.index),
    url(r'^people/$',view.index),
    url(r'^love/$',view.cat)
    #总路由包含子路由，（写上哪个个应用的子路由）
]
