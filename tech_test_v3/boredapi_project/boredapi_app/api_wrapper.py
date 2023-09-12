import requests

class BoredAPIWrapper:
    API_URL = 'https://www.boredapi.com/api/activity'

    def fetch_activity(self, activity_type=None, participants=None, price_min=None, price_max=None, accessibility_min=None, accessibility_max=None):
        # Build the request URL with query parameters based on filters
        params = {
            'type': activity_type,
            'participants': participants,
            'minprice': price_min,
            'maxprice': price_max,
            'minaccessibility': accessibility_min,
            'maxaccessibility': accessibility_max,
        }

        response = requests.get(self.API_URL, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None