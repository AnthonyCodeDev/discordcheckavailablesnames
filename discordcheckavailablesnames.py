import requests
import json
import time

class UsernameTester:
    """
    A class to test usernames for availability using an HTTP POST request to a given API endpoint.
    """

    def __init__(self, headers, url, usernames):
        """
        Initializes the tester with headers, URL, and a list of usernames to test.

        :param headers: Dictionary containing HTTP headers for the request
        :param url: API endpoint URL
        :param usernames: List of usernames to test
        """
        self.headers = headers
        self.url = url
        self.usernames = usernames

    def test_username(self, username):
        """
        Sends an HTTP POST request to test a single username.

        :param username: The username to test
        :return: The HTTP response object
        """
        data = {"username": username}
        response = requests.post(self.url, headers=self.headers, data=json.dumps(data))
        return response

    def handle_response(self, response, username):
        """
        Handles the HTTP response, including rate limiting and user interaction.

        :param response: The HTTP response object
        :param username: The username being tested
        :return: 'stop' to terminate or 'continue' to proceed
        """
        if response.status_code == 429:
            retry_after = int(response.headers.get('retry-after', 0))
            print(f"Rate limit hit. Retrying after {retry_after + 5} seconds...")
            time.sleep(retry_after + 5)
            return None

        if response.status_code == 200:
            response_json = response.json()
            if response_json.get('taken'):
                print(f"Username: {username} is taken")
            else:
                print(f"Success! Username: {username}")
                user_choice = input("Smash or Pass (s/p): ").strip().lower()
                if user_choice == 's':
                    print("Stopping the process.")
                    return 'stop'
                elif user_choice == 'p':
                    print("Continuing with the next username.")
                else:
                    print("Invalid choice. Continuing by default.")
        return 'continue'

    def run(self):
        """
        Executes the username testing process for all usernames in the list.
        """
        for index, username in enumerate(self.usernames):
            print(f"Testing username {index + 1}/{len(self.usernames)}: {username}")
            response = self.test_username(username)

            if not response:
                continue

            result = self.handle_response(response, username)
            if result == 'stop':
                break

if __name__ == "__main__":
    # HTTP headers for the API request
    headers = {
        "accept": "*/*",
        "accept-language": "en-US",
        "authorization": "token",
        "content-type": "application/json",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Not?A_Brand\";v=\"99\", \"Chromium\";v=\"130\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Linux\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
    }

    # API endpoint
    url = "https://discord.com/api/v9/users/@me/pomelo-attempt"

    # List of usernames to test
    usernames = [
        "usernames", "to", "test"
    ]

    tester = UsernameTester(headers, url, usernames)
    tester.run()
