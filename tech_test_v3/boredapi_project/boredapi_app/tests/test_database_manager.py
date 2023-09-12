from django.test import TestCase
from boredapi_app.database_manager import ActivityDatabaseManager
from boredapi_app.models import Activity

class ActivityDatabaseManagerTestCase(TestCase):
    def test_save_and_retrieve_activity(self):
        db_manager = ActivityDatabaseManager()

        # Create a sample activity data dictionary
        activity_data = {
            'activity': 'Test Activity',
            'type': 'test',
            'participants': 1,
            'price': 0.0,
            'key': 'test_key',
        }

        # Save the activity to the database
        db_manager.save_activity(activity_data)

        # Retrieve the saved activity from the database
        saved_activity = Activity.objects.first()

        self.assertIsNotNone(saved_activity)
        self.assertEqual(saved_activity.activity, 'Test Activity')
        self.assertEqual(saved_activity.type, 'test')
        self.assertEqual(saved_activity.participants, 1)
        self.assertEqual(saved_activity.price, 0.0)
        self.assertEqual(saved_activity.key, 'test_key')