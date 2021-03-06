from django.shortcuts import resolve_url as r
from django.test import TestCase


class HomeTest(TestCase):
    fixtures = ['keynotes.json']

    def setUp(self) -> None:
        self.response = self.client.get(r('home'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_link(self):
        self.assertContains(self.response, f'href="{r("subscriptions:new")}"')

    def test_speakers(self):
        """Must show keynote speakers"""
        contents = [
            f'href=\"{r("speaker_detail", slug="grace-hopper")}\"',
            'Grace Hopper',
            'http://hbn.link/hopper-pic',
            f'href=\"{r("speaker_detail", slug="alan-turing")}\"',
            'Alan Turing',
            'http://hbn.link/turing-pic',
        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_speakers_link(self):
        self.assertContains(self.response, f"href=\"{r('home')}#speakers\"")

    def test_talks_link(self):
        self.assertContains(self.response, f"href=\"{r('talk_list')}\"")
