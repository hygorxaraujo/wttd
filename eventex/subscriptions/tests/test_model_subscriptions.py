from datetime import datetime

from django.test import TestCase

from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self) -> None:
        self.sub = Subscription(
            name='Hygor Xavier Araújo',
            cpf='12345678901',
            email='contact@hygorxaraujo.com',
            phone='(32) 91111-2222',
        )
        self.sub.save()

    def test_create(self) -> None:
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self) -> None:
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.sub.created_at, datetime)

    def test_str(self):
        self.assertEqual('Hygor Araújo', str(self.sub))
