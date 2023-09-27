import json
from collections import Counter
from pathlib import Path
from pprint import pprint

import requests
from bs4 import BeautifulSoup
from requests.exceptions import SSLError, ConnectionError


def is_valid(word: str) -> bool:
    return "[" not in word and "]" not in word


def get_all_urls(artist_code: int) -> list:
    page = 1
    links = []
    while True:
        print(f"Fetching page: {page}")
        r = requests.get(f"https://genius.com/api/artists/{artist_code}/songs?page={page}&sort=popularity")

        if r.status_code == 200:
            response = r.json().get("response", {})
            next_page = response.get("next_page")

            songs = response.get("songs")
            links.extend([song.get('url') for song in songs])

            if not next_page:
                print("No more page to break !")
                break

            page += 1
        else:
            print("Couldn't get page.")
            continue

    return links


def extract_lyrics(url: str) -> list:
    print(f"Fetching lyrics:: {url}")
    r = requests.get(url)
    if r.status_code != 200:
        return []

    soup = BeautifulSoup(r.content, 'html.parser')
    lyrics = soup.find("div", class_="Lyrics__Container-sc-1ynbvzw-1")
    if not lyrics:
        print(f"Second fetch lyrics:: {url}")
        return extract_lyrics(url)

    all_words = []
    for sentence in lyrics.stripped_strings:
        sentence_words = [word.strip(".").strip(',').lower() for word in sentence.split() if is_valid(word)]
        all_words.extend(sentence_words)

    return all_words


def get_all_words(word_len: int = 5, artist_code: int = 29743):
    file = Path.cwd() / f"song_words_{artist_code}.json"

    if file.exists():
        with open(file, 'r') as f:
            words = json.load(f)
    else:
        try:
            urls = get_all_urls(artist_code=artist_code)
        except SSLError:
            return print("Internet error !!")
        except ConnectionError:
            return print("Internet error !!")

        words = []
        for url in urls:
            lyrics = extract_lyrics(url=url)
            words.extend(lyrics)

        with open(file, 'w') as f:
            json.dump(words, f, indent=4)

    counter = Counter([w for w in words if len(w) > word_len])
    most_common = counter.most_common(15)
    pprint(most_common)


artiste_code = input("Entrer le code l'artiste dans genius.com: ")
word_length = input("Entrer la longueur du mot à filtrer: ")
get_all_words(word_len=int(word_length), artist_code=int(artiste_code))
