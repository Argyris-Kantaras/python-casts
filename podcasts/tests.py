from django.test import TestCase
from django.utils import timezone
from .models import Episode
from django.urls import reverse

from datetime import datetime

class PodcastsTests(TestCase):
    def setUp(self):
        self.episode = Episode.objects.create(
            title = "My Podcasts",
            description = 'I did it',
            pub_date = timezone.now(),
            link = 'https://myawesomeshow.com',
            image = "https://image.myawesomeshow.com",
            podcast_name = 'Python',
            guid = 'gourounni1991',
        )

    def test_episode_content(self):
        self.assertEqual(self.episode.description, "I did it")
        self.assertEqual(self.episode.link, 'https://myawesomeshow.com' )
        self.assertEqual(self.episode.guid, "gourounni1991")

    def test_episode_str_representations(self):
        self.assertEqual(str(self.episode),"Python: My Podcasts")

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_coreect_template(self):
        response = self.client.get(reverse("homepage"))
        self.assertTemplateUsed(response, 'homepage.html')

    def test_homepage_list_contents(self):
        response = self.client.get(reverse('homepage'))
        self.assertContains(response, 'My Podcasts')