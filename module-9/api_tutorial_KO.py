import requests
import json

def test_api(url):
    response = requests.get(url)
    print("Status Code:", response.status_code)
    return response

def pretty_print_json(data):
    print("\nFormatted JSON:")
    print(json.dumps(data, sort_keys=True, indent=4))

def get_astronauts():
    url = "http://api.open-notify.org/astros"
    response = test_api(url)

    if response.status_code == 200:
        print("\nRaw JSON:")
        print(response.text)

        data = response.json()
        pretty_print_json(data)

        print("\nAstronaut List:")
        for person in data["people"]:
            print(f"{person['name']} on {person['craft']}")
    else:
        print("Check the API URL!")


def main():
    get_astronauts()

if __name__ == "__main__":
    main()