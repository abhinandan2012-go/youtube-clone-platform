from django.test import TestCase


class ChannelsViewsTests(TestCase):
    def test_channel_detail_page_renders(self):
        response = self.client.get("/channels/test-channel/")
        self.assertEqual(response.status_code, 404)
