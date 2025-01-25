import http.client

def fetch_webpage(host, path="/"):
    try:
        connection = http.client.HTTPConnection(host)
        connection.request("GET", path)
        response = connection.getresponse()
        if response.status == 200:
            return response.read().decode("utf-8")
        print(f"Failed: HTTP Status {response.status}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    host = input("Website (e.g., example.com): ")
    path = input("Path (e.g., /): ")
    content = fetch_webpage(host, path)
    if content:
        print("Content:")
        print(content)