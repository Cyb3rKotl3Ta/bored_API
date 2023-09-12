from django.test import TestCase
from boredapi_app.api_wrapper import BoredAPIWrapper
from boredapi_app.database_manager import ActivityDatabaseManager
from rest_framework.test import APIRequestFactory
from .models import Activity
from .views import ActivityViewSet

# class ActivityViewSetTestCase(TestCase):
#     def test_create_activity(self):
#         factory = APIRequestFactory()
#         view = ActivityViewSet.as_view({'post': 'create'})

#         # Simulate a POST request to create an activity
#         response = view(factory.post('/api/activity/'))

#         # Check if the response has a successful status code
#         self.assertEqual(response.status_code, 201)

#         # Check if an activity was created in the database
#         self.assertEqual(Activity.objects.count(), 1)

#     def test_create_activity_with_invalid_data(self):
#         factory = APIRequestFactory()
#         view = ActivityViewSet.as_view({'post': 'create'})

#         # Simulate a POST request with invalid data
#         response = view(factory.post('/api/activity/', {'invalid_key': 'invalid_value'}))

#         # Check if the response has a status code indicating a bad request
#         self.assertEqual(response.status_code, 400)

#         # Check that no activity was created in the database
#         self.assertEqual(Activity.objects.count(), 0)

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

class BoredAPIWrapperTestCase(TestCase):
    def test_fetch_activity(self):
        wrapper = BoredAPIWrapper()
        activity = wrapper.fetch_activity()

        self.assertIsNotNone(activity)
        self.assertIsInstance(activity, dict)
        self.assertIn('activity', activity)


















# import unittest
# from boredapi_app.api_wrapper import BoredAPIWrapper
# from boredapi_app.database_manager import ActivityDatabaseManager
# from boredapi_app.models import Activity

# class ActivityDatabaseManagerTestCase(unittest.TestCase):
#     def setUp(self):
#         # Set up a test database and create some sample data
#         self.db_manager = ActivityDatabaseManager()

#     def tearDown(self):
#         # Clean up the test database
#         Activity.objects.all().delete()

#     def test_save_activity(self):
#         # Create a sample activity data dictionary
#         activity_data = {
#             'activity': 'Test Activity',
#             'type': 'test',
#             'participants': 1,
#             'price': 0.0,
#             'key': 'test_key',
#         }

#         # Save the activity to the database using the manager
#         self.db_manager.save_activity(activity_data)

#         # Retrieve the saved activity from the database
#         saved_activity = Activity.objects.first()

#         # Assert that the saved activity matches the expected data
#         self.assertIsNotNone(saved_activity)
#         self.assertEqual(saved_activity.activity, 'Test Activity')
#         self.assertEqual(saved_activity.type, 'test')
#         self.assertEqual(saved_activity.participants, 1)
#         self.assertEqual(saved_activity.price, 0.0)
#         self.assertEqual(saved_activity.key, 'test_key')

#     def test_get_latest_activities(self):
#         # Create and save multiple sample activities
#         for i in range(1, 6):
#             activity_data = {
#                 'activity': f'Test Activity {i}',
#                 'type': 'test',
#                 'participants': 1,
#                 'price': 0.0,
#                 'key': f'test_key_{i}',
#             }
#             self.db_manager.save_activity(activity_data)

#         # Retrieve the latest 3 activities from the database
#         latest_activities = self.db_manager.get_latest_activities(num_activities=3)

#         # Assert that the number of retrieved activities is as expected
#         self.assertEqual(len(latest_activities), 3)

#         # Assert the order of retrieved activities (latest first)
#         self.assertEqual(latest_activities[0].activity, 'Test Activity 5')
#         self.assertEqual(latest_activities[1].activity, 'Test Activity 4')
#         self.assertEqual(latest_activities[2].activity, 'Test Activity 3')

# class TestBoredAPIWrapper(unittest.TestCase):
#     def test_fetch_activity(self):
#         wrapper = BoredAPIWrapper()
#         activity = wrapper.fetch_activity()

#         self.assertIsNotNone(activity)
#         self.assertIsInstance(activity, dict)
#         self.assertIn('activity', activity)