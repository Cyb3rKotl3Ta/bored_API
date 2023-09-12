from .models import Activity

class ActivityDatabaseManager:
    def save_activity(self, activity_data):
        """
        Save an activity to the database.
        :param activity_data: A dictionary containing activity details.
        """
        activity = Activity(
            activity=activity_data['activity'],
            type=activity_data['type'],
            participants=activity_data['participants'],
            price=activity_data['price'],
            key=activity_data['key']
        )
        activity.save()

    def get_latest_activities(self, num_activities=5):
        """
        Get the latest activities saved in the database.
        :param num_activities: Number of latest activities to retrieve (default is 5).
        :return: Queryset containing the latest activities.
        """
        return Activity.objects.all().order_by('-id')[:num_activities]