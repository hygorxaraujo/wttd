from django.shortcuts import resolve_url as r
from django.test import TestCase

from eventex.subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):

    def setUp(self):
        self.sub = Subscription.objects.create(
            name='Hygor Xavier Araújo',
            cpf='12345678901',
            email='contact@hygorxaraujo.com',
            phone='(32) 91111-2222',
        )
        self.resp = self.client.get(r('subscriptions:detail', self.sub.uid))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    def test_context(self):
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = (self.sub.name, self.sub.cpf, self.sub.email, self.sub.phone)
        with self.subTest():
            for expected in contents:
                self.assertContains(self.resp, expected)


class SubscriptionDetailNotFound(TestCase):

    def test_not_found(self):
        resp = self.client.get(r('subscriptions:detail',
                                 '702beb91-3ac5-4993-9928-2a1dfe12fd32'))
        self.assertEqual(404, resp.status_code)
