from django.conf.urls import url
from django.contrib import admin
from fibermotor import views as zqxt_admin
from web import views as web
from log import views as log
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^host/$', zqxt_admin.host_listing),
    url(r'^host/(\d+)$', zqxt_admin.host_detail, name='host-detail'),
    url(r'^search/$', zqxt_admin.search, name='search'),
    url(r'^ip/$', zqxt_admin.ip_listing, name='ip-list'),
    url(r'^ip/(\d+)$', zqxt_admin.ip_detail, name='ip-detail'),
    url(r'^log/$', log.log_listing, name='log'),
    url(r'^', web.index),
]

urlpatterns += static('/static/', document_root='/static/')