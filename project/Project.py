# you have to install the Requests Module : pip install requests
import requests
import json

class APIFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.github.com'

    def fetch_repositories(self, username):
        endpoint = f'/users/{username}/repos'
        # requests.get() >>> https://www.w3schools.com/python/ref_requests_get.asp
        # The Authorization field is used in HTTP headers to authenticate a user-agent with the server.
        response = requests.get(self.base_url + endpoint, headers={'Authorization': f'token {self.api_key}'})

# Code 200 means that the HTTP request was a success
# Here we will convert the Data into a JSON format

        if response.status_code == 200:
            return response.json()
        else:

# Here if we have an issue with retrieving the request it will provide the code

            print(f"Failed to fetch repositories for {username}. Status code: {response.status_code}")
            return None

class Repository:
    def __init__(self, name, description, stars):
        self.name = name
        self.description = description
        self.stars = stars

    def display_info(self):
        print(f"Repository: {self.name}")
        print(f"Description: {self.description}")
        print(f"Stars: {self.stars}")

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def write_to_file(self, data):
        with open(self.filename, 'w') as file:
            # Converts the Python objects into JSON
            json.dump(data, file, indent=4)

    def read_from_file(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return []

def Project():

    api_key = input("Kindly enter the API_key of your Github: ")
    username = input("Kinly enter the Username of your Github account: ") 

    api_fetcher = APIFetcher(api_key)
    repositories_data = api_fetcher.fetch_repositories(username)

    if repositories_data:
        repositories = []
        for data in repositories_data:
            #https://gist.github.com/jasonrudolph/6057563
            repository = Repository(data['name'], data['description'], data['stargazers_count'])
            repositories.append(repository)

        
        for repo in repositories:
            repo.display_info()

        
        file = FileManager('repositories.json')
        # when the class is created the Data will be stored in the __dict__ , which is fetch_repositories (predefined Function )
        file.write_to_file([repo.__dict__ for repo in repositories])
        print("Repository data saved to 'repositories.json'.")

    
        saved_data = file.read_from_file()
        print("Data read from file:")
        print(saved_data)

if __name__ == "__Project__":
         Project()