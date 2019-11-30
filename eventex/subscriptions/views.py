from django.conf import settings
from django.core import mail
from django.http import HttpResponseRedirect, Http404
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

    sub = Subscription.objects.create(**form.cleaned_data)

    _send_email('Confirmação de inscrição',
                settings.DEFAULT_FROM_EMAIL,
                sub.email,
                'subscriptions/subscription_email.txt',
                {'subscription': sub})

    return HttpResponseRedirect(f'/inscricao/{sub.uid}/')


def _new(request):
    return render(request, 'subscriptions/subscription_form.html', {'form': SubscriptionForm()})


def _send_email(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])


def detail(request, uid):
    try:
        subscription = Subscription.objects.get(uid=uid)
    except Subscription.DoesNotExist:
        raise Http404

    return render(request, 'subscriptions/subscription_detail.html',
                  context={'subscription': subscription})
