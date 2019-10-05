# DMCASkipper

Made to skip songs in spotify that risks DMCA strikes


## How to use it
You interact with the program in the system tray. 

When you start the program it will automatically skip songs from artist signed by Atlantic Records.
The program can also skip Warner Records' artists' songs, but you have to enable it yourself.
You can also disable the auto skip. 


## For developing
If you clone project, you need to install some dependencies with pip: 
```
pip install pystray
pip install SwSpotify
```

To build the program yourself, go into the DMCASkipper folder use pyinstaller:
```
pyinstaller --noconsole --onefile src/main.py  
```
If it is not installed, install it by using pip. 
