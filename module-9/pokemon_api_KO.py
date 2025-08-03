import requests

def test_api(url):
    response = requests.get(url)
    print("Status Code:", response.status_code)
    return response

def show_raw_data(response):
    print("\nRaw JSON:")
    print(response.text)

def show_pokemon_info(response):
    data = response.json()
    print("\nFormatted Info:")
    print("Name:", data["name"])
    print("ID:", data["id"])
    print("Height:", data["height"])
    print("Weight:", data["weight"])

    print("Abilities:")
    for item in data["abilities"]:
        print("-", item["ability"]["name"])

def main():
    url = "https://pokeapi.co/api/v2/pokemon/ditto"
    response = test_api(url)
    show_raw_data(response)
    show_pokemon_info(response)

main()