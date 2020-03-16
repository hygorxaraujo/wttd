from django.views.generic import DetailView

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.mixins import EmailCreateView
from eventex.subscriptions.models import Subscription

new = EmailCreateView.as_view(model=Subscription,
                              form_class=SubscriptionForm,
                              email_subject='Confirmação de inscrição', )


class Detail(DetailView):
    model = Subscription
    slug_field = 'uid'
    slug_url_kwarg = 'uid'


detail = Detail.as_view()
