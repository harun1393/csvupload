from django.conf.urls import url
from . import views 

urlpatterns = [
	url(r'^client/',views.client_home, name='client-home'),
	url(r'^finance/',views.finance_home, name='finance-home'),
	url(r'^marketing/',views.marketing_home, name='marketing-home'),
	url(r'^logout/$', views.user_logout, name='logout'),
]
