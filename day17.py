import http.client

def fetch_webpage(host, path="/"):
    """
    Fetches and displays the content of a webpage.

    Args:
        host (str): The domain name (e.g., example.com).
        path (str): The URL path (default is "/").

    Returns:
        str: The content of the webpage.
    """
    try:
        # Create a connection to the host
        connection = http.client.HTTPConnection(host)

        # Send a GET request to the specified path
        connection.request("GET", path)

        # Get the server's response
        response = connection.getresponse()

        # Check the status code
        if response.status == 200:
            print(f"Successfully fetched content from {host}{path}")
            return response.read().decode("utf-8")
        else:
            print(f"Failed to fetch content. HTTP Status: {response.status}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Specify the host and path
    host = input("Enter the website you want to view:  ")
    path = input("type the url pathway you want. you can use '/' for the root url ")

    # Fetch and display the content
    content = fetch_webpage(host, path)
    if content:
        print("Page Content:")
        print(content)
