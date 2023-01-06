from django.conf.urls import url, include
from django.contrib import admin
from . import views
# gotta import one more views... of the articles one.. but cant just import it as views... same name woyld throw an error
from articles import views as articles_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^articles/', include('articles.urls')),
    # url(r'^about/$', views.about),
    url(r'^$', articles_views.article_list, name="home_page"),
    # kisi aur k view ka url i see...
    url(r'^accounts/', include('accounts.url'))
]

# += ysv is like... appending into list... we do this bcz we want our static files 2 b servable.. to be able to view on web
urlpatterns += staticfiles_urlpatterns()
# so ... must they have their urls.. so thats why urlpatterns mwi daal dia
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# ok ysv .. above thing is for like.. our media to be servable... so we need 2 things..., under which url to serve them(1st parameter)
# and what are the MEDIA files/ where they are...(final rightmost part of url k liye(e.g. main.css ))
