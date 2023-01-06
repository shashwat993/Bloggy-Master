from django.conf.urls import url
from . import views
app_name='accounts'

urlpatterns=[
    url(r'^signup/$',views.signup_view,name="signup"),   # i verified ... by default request is GET request ok!?
    url(r'^login/$',views.login_page,name="login"), # will send get request, !post 
    url(r'^logout/$',views.logout_page,name='logout'),   # url associate krna is important! y? bcz--> form action requires it. it links url and function   
]