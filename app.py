import requests

API_URL = "https://v2.jokeapi.dev/joke/Programming?type=single"

def get_joke():
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get("joke", "Aucune blague trouvée.")
    except requests.RequestException as e:
        return f"Erreur lors de l'appel à l'API : {e}"

if __name__ == "__main__":
    joke = get_joke()
    print("Blague (en anglais) :", joke)
