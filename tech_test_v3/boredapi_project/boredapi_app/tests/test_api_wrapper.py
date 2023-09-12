from django.test import TestCase
from boredapi_app.api_wrapper import BoredAPIWrapper

class BoredAPIWrapperTestCase(TestCase):
    def test_fetch_activity(self):
        wrapper = BoredAPIWrapper()
        activity = wrapper.fetch_activity()

        self.assertIsNotNone(activity)
        self.assertIsInstance(activity, dict)
        self.assertIn('activity', activity)
