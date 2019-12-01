from django.core import mail
from django.shortcuts import resolve_url as r
from django.test import TestCase


class SubscribePostValid(TestCase):

    def setUp(self):
        data = dict(name='Hygor', cpf='12345678901', email='contact@hygorxaraujo.com',
                    phone='11-92222-3333')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'contact@hygorxaraujo.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = (
            'Hygor',
            '12345678901',
            'contact@hygorxaraujo.com',
            '11-92222-3333',
        )
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
