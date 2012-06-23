from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(
        r'^$',
        'form.views.contact_form',
        name="contact_form",
    ),
)