day 14
import requests

def fetch_github_user_data(username):
    """
    Fetch user data from GitHub API for the given username.

    Args:
        username (str): GitHub username.

    Returns:
        dict: User profile information if found, otherwise None.
    """
    base_url = f"https://api.github.com/users/{triddles-1}"
    
    try:
        response = requests.get(base_url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        user_data = response.json()
        return user_data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    return None

def display_user_data(user_data):
    """
    Display user data in a readable format.

    Args:
        user_data (dict): User profile information from GitHub API.
    """
    if user_data:
        print(f"Name: {user_data.get('name', 'Not Available')}")
        print(f"Username: {user_data.get('login')}")
        print(f"Bio: {user_data.get('bio', 'Not Available')}")
        print(f"Location: {user_data.get('location', 'Not Available')}")
        print(f"Public Repositories: {user_data.get('public_repos')}")
        print(f"Followers: {user_data.get('followers')}")
        print(f"Following: {user_data.get('following')}")
        print(f"GitHub URL: {user_data.get('html_url')}")
    else:
        print("User data could not be retrieved.")

if __name__ == "__main__":
    username = input("Enter the GitHub username: ").strip()
    user_data = fetch_github_user_data(username)
    display_user_data(user_data)
