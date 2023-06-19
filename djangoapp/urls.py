from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.urls import path
from djangoapp.views import static_page_view
from django.views.generic import TemplateView


app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
    path('', static_page_view, name='index'),
    # path for about view
 path('about/', TemplateView.as_view(template_name='djangoapp/about.html'), name='about'),
    # path for contact us view
 path('contact/', TemplateView.as_view(template_name='djangoapp/contact.html'), name='contact'),
    # path for registration

    # path for login

    # path for logout

    path(route='', view=views.get_dealerships, name='index'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)