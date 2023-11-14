import requests


def search_gifs(search_query):
    api_key = 'LEgEpvtuR54mQBAgcVIBLeV3NJ5lGGQN'
    endpoint = f"https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={search_query}&limit=5"

    response = requests.get(endpoint)

    if response.status_code == 200:
        data = response.json()
        gifs = data['data']

        for gif in gifs:
            print(gif['url'])
    else:
        print("Failed to retrieve GIFs. Check your API key and try again.")


if __name__ == "__main__":
    search_word = input("Enter a search word: ")
    search_gifs(search_word)
