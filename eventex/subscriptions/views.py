from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


def subscribe(request):
    if request.method == 'POST':
        return _create(request)
    else:
        return _new(request)


def _create(request):
    form = SubscriptionForm(request.POST)
    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html', {'form': form})

    _send_email('Confirmação de inscrição',
                settings.DEFAULT_FROM_EMAIL,
                form.cleaned_data['email'],
                'subscriptions/subscription_email.txt',
                form.cleaned_data)

    Subscription.objects.create(**form.cleaned_data)

    messages.success(request, 'Inscrição realizada com sucesso!')
    return HttpResponseRedirect('/inscricao/')


def _new(request):
    return render(request, 'subscriptions/subscription_form.html', {'form': SubscriptionForm()})


def _send_email(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])
