from django.contrib import admin
from django.urls import path
from ordertaker import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'ordertaker'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.order_view, name='home'),
    # path('summary/', summary),
]

urlpatterns += staticfiles_urlpatterns()
