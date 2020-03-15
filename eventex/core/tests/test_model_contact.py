from django.core.exceptions import ValidationError
from django.test import TestCase

from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self) -> None:
        self.speaker = Speaker.objects.create(
            name='John Doe',
            slug='john-doe',
            photo='',
        )

    def test_email(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='john@example.com',
        )
        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.PHONE,
            value='32-999999999',
        )
        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kind should be limited to E or P"""
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker, kind=Contact.EMAIL, value='john@example.com')
        self.assertEqual('john@example.com', str(contact))


class ContactManagerTest(TestCase):
    def setUp(self) -> None:
        s = Speaker.objects.create(
            name='John Doe',
            slug='john-doe',
            photo='',
        )
        s.contact_set.create(kind=Contact.EMAIL, value='john@doe.com')
        s.contact_set.create(kind=Contact.PHONE, value='32-988887777')

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['john@doe.com']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['32-988887777']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)
