import requests

class MLXIntegration:
    def __init__(self, api_url, api_key):
        """
        Initialize the MLX Integration.

        Args:
            api_url (str): The base URL for the MLX API.
            api_key (str): API key for authenticating with the MLX API.
        """
        self.api_url = api_url
        self.api_key = api_key

    def _api_request(self, endpoint, method='GET', data=None):
        """
        Make a request to the MLX API.

        Args:
            endpoint (str): API endpoint to call.
            method (str): HTTP method (e.g., 'GET', 'POST').
            data (dict, optional): Data to send in the request.

        Returns:
            dict: Response from the MLX API.
        """
        url = f"{self.api_url}/{endpoint}"
        headers = {'Authorization': f'Bearer {self.api_key}'}

        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, json=data, headers=headers)
        else:
            raise ValueError("Unsupported HTTP method")

        return response.json()

    def create_profile(self, profile_name, profile_settings):
        """
        Create a new MLX profile.

        Args:
            profile_name (str): Name of the MLX profile.
            profile_settings (dict): Settings for the MLX profile.

        Returns:
            bool: True if the profile was created successfully, False otherwise.
        """
        data = {
            'name': profile_name,
            'settings': profile_settings
        }
        result = self._api_request('create_profile', 'POST', data)
        return result.get('success', False)

    def switch_profile(self, profile_name):
        """
        Switch to an existing MLX profile.

        Args:
            profile_name (str): Name of the MLX profile to switch to.

        Returns:
            bool: True if the switch was successful, False otherwise.
        """
        data = {'name': profile_name}
        result = self._api_request('switch_profile', 'POST', data)
        return result.get('success', False)

    def delete_profile(self, profile_name):
        """
        Delete an MLX profile.

        Args:
            profile_name (str): Name of the MLX profile to delete.

        Returns:
            bool: True if the profile was deleted successfully, False otherwise.
        """
        data = {'name': profile_name}
        result = self._api_request('delete_profile', 'POST', data)
        return result.get('success', False)

# Example Usage
if __name__ == "__main__":
    api_url = 'https://api.multiloginapp.com'
    api_key = 'your_api_key'

    mlx_integration = MLXIntegration(api_url, api_key)
    if mlx_integration.create_profile('Profile1', {'setting1': 'value1'}):
        print("Profile created successfully.")
    if mlx_integration.switch_profile('Profile1'):
        print("Switched to Profile1 successfully.")
    if mlx_integration.delete_profile('Profile1'):
        print("Profile deleted successfully.")
