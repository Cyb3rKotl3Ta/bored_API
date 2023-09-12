import argparse
import os
import sys
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'boredapi_project.settings')
django.setup()

from boredapi_app.api_wrapper import BoredAPIWrapper
from boredapi_app.database_manager import ActivityDatabaseManager

def main():
    parser = argparse.ArgumentParser(description="Fetch and save random activities with filtering options.")
    parser.add_argument(
        "command",
        choices=["new", "list"],
        help="Command to execute: 'new' to fetch and save a new activity, 'list' to list saved activities."
    )

    # Filtering options
    parser.add_argument("--type", help="Filter by activity type")
    parser.add_argument("--participants", type=int, help="Filter by number of participants")
    parser.add_argument("--price_min", type=float, help="Minimum price filter")
    parser.add_argument("--price_max", type=float, help="Maximum price filter")
    parser.add_argument("--accessibility_min", type=float, help="Minimum accessibility filter")
    parser.add_argument("--accessibility_max", type=float, help="Maximum accessibility filter")

    args = parser.parse_args()

    if args.command == "new":
        # Fetch and save a new activity with filters
        activity_wrapper = BoredAPIWrapper()
        activity_data = activity_wrapper.fetch_activity(
            activity_type=args.type,
            participants=args.participants,
            price_min=args.price_min,
            price_max=args.price_max,
            accessibility_min=args.accessibility_min,
            accessibility_max=args.accessibility_max
        )

        if not activity_data:
            print("No matching activity found.")
            sys.exit(1)

        db_manager = ActivityDatabaseManager()
        db_manager.save_activity(activity_data)
        print("Activity saved successfully.")

    elif args.command == "list":
        # List saved activities
        num_activities = 3  # Default to listing the latest 3 activities

        db_manager = ActivityDatabaseManager()
        latest_activities = db_manager.get_latest_activities(num_activities)
        
        if not latest_activities:
            print("No saved activities found.")
            sys.exit(1)

        print("Latest Activities:")
        for activity in latest_activities:
            print(f"- {activity.activity}")

if __name__ == "__main__":
    main()