#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.mail import send_mail

from form.forms import FormContact

def contact_form(request):
    """
    Vista que hace que el formulario de contacto se procese
    """
    if request.method == 'POST':
        form = FormContact(request.POST)
        if form.is_valid():
            form.save()
            try:
                send_mail(
                    'User message',
                    form.cleaned_data['message'],
                    form.cleaned_data['name'],
                    [settings.CONTACT_EMAIL],
                    fail_silently=True,
                )
                messages.success(
                    request, 'Mensaje enviado exitosamente.')

            except:
                messages.warning(request, 'Por favor intente de nuevo.')

            return HttpResponseRedirect(reverse('contact_form'))
    else:
        form = FormContact()

    return render(request, 'contact/contact_form.html', {
        'form': form,
    })
