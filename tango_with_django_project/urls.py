from django.conf.urls import url
from django.contrib import admin
from rango import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from registration.backends.simple.views import RegistrationView


# Create a new class that redirects the user to the index page,
#if successful at logging


class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/rango/'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rango/', include('rango.urls')),
    url(r'^admin/', admin.site.urls),
    #following url HAS to be above the accounts/ one for some reason
    url(r'^accounts/register/$',
        MyRegistrationView.as_view(),
            name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

