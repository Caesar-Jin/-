from django.conf.urls import url,  include

from . import view
from like import views

urlpatterns = [
    url(r'^love/$', view.dog),
    url(r'^make/$', view.mouse)
    #总路由包含子路由，（写上哪个个应用的子路由）
]