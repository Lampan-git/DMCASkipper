# DMCASkipper

Program to skip songs in Spotify that risks DMCA strikes


## How to use it
You interact with the program in the system tray. 

When you start the program it will automatically skip songs from artist signed by Atlantic Records.
The program can also skip Warner Records' artists' songs, but you have to enable it yourself.
You can also disable the auto skip. 

## Downloading it and running it
### Windows
#### Easiest
Download the `DMCASkipper.exe` in releases

#### Run it via python
Clone/download the project and install the dependencies:
```
pip install pystray
pip install SwSpotify
```
Run the program by just executing the `main.py` file with python: `python src/main.py`

#### Build it yourself
Clone/download the project and install the dependencies. Go into the DMCASkipper folder and use pyinstaller:
```
pyinstaller --noconsole --onefile --icon=icon.ico src/main.py  
```
If pyinstaller is not installed, install it by using pip. 

After you have the `.exe` file, just run it and it should work out of the box. 


### Linux or OSX:
I have not tried it on Linux or OSX. But should work with some minor changes, since all the libraries supports it. 
