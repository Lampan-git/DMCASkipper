from threading import Thread
from time import sleep

import pystray
from SwSpotify import spotify
from SysTrayIcon import *
from spotify_local import SpotifyLocal

import requests
from bs4 import BeautifulSoup

stop = False
currentSong = ("", "")
autoskip = True
ar_skip = True
wr_skip = False

skipListAR = []
skipListWR = []
s = SpotifyLocal()


def main():
    global stop
    global s
    stop = False
    icon_color = "#33ed00"
    if (currentSong[1] in skipListAR or currentSong[1] in skipListWR) and currentSong[1] != "":
        icon_color = "#b0000c"

    ic = pystray.Icon('test', create_image(bgcolor=icon_color), menu=Menu(
        Item(
            current_to_string(),
            "",
            enabled=False),
        Item('Stop DMCASkipper',
             lambda: set_stop(True)),
        Item(
            'Autoskip',
            on_clicked_autoskip,
            checked=get_autoskip,
            radio=True),
        Item(
            'Skip Atlantic Records\' songs',
            on_clicked_ar,
            checked=get_ar_skip,
            radio=True),
        Item(
            'Skip Warner Records\' songs',
            on_clicked_wr,
            checked=get_wr_skip,
            radio=True)))

    process = Thread(target=run, args=(ic,))
    ic.run(process.start())
    process.join()


def run(ic):
    global stop
    global currentSong
    restart = False
    try:
        currentSong = spotify.current()
    except:
        currentSong = ("", "")

    print(currentSong)

    try:
        while not stop:
            try:
                if spotify.current() != currentSong:
                    currentSong = spotify.current()
                    ic.stop()
                    ic.update_menu()
                    restart = True
                    break
            except:
                if currentSong != ("", ""):
                    currentSong = ("", "")
                    ic.stop()
                    ic.update_menu()
                    restart = True
                    break

            if currentSong[1] in skipListAR and ar_skip and autoskip:
                print("SKIP")
                s.skip()

            if currentSong[1] in skipListWR and wr_skip and autoskip:
                print("SKIP")
                s.skip()

            sleep(0.5)
    finally:
        ic.stop()
        if restart:
            sleep(0.1)
            Thread(target=main).start()


def set_stop(b):
    global stop
    stop = b


def on_clicked_autoskip(icon, item):
    global autoskip
    autoskip = not item.checked


def on_clicked_ar(icon, item):
    global ar_skip
    ar_skip = not item.checked


def on_clicked_wr(icon, item):
    global wr_skip
    wr_skip = not item.checked


def get_autoskip(icon):
    global autoskip
    return autoskip


def get_ar_skip(icon):
    global ar_skip
    return ar_skip


def get_wr_skip(icon):
    global wr_skip
    return wr_skip


def current_to_string():
    val = ""
    if currentSong != ("", ""):
        val = currentSong[0] + " - " + currentSong[1]
    else:
        val = "No song playing"
    return val


atlantic_records = "https://www.atlanticrecords.com/artists"
response = requests.get(atlantic_records)
soup = BeautifulSoup(response.text, "html.parser")
for div in soup.findAll("div", {"class": "artist-name"}):
    skipListAR.append(div.find('a').text)

warner_records = "https://en.wikipedia.org/wiki/List_of_current_Warner_Records_artists"
response = requests.get(warner_records)
soup = BeautifulSoup(response.text, "html.parser")
wrList = soup.findAll("li")

i = 0
for li in wrList:
    if i < 28:
        i = i + 1
        continue
    if li.text == "List of former Warner Records artists":
        break

    art = ""
    art = li.text
    if " (" in art:
        art = art.split(" (")[0]
    if " as " in art:
        art = art.split(" as ")[1]
    skipListWR.append(art)

print(skipListWR)

print(skipListAR)

try:
    currentSong = spotify.current()
except:
    currentSong = ("", "")
main()
