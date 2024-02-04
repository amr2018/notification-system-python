## Python notification system based on Tkinter

This is a simple notification system that uses Tkinter as a GUI.
With this simple system, you can display notifications in an easy way.
You can add a custom alert sound and icon image.

[![ko-fi](https://ko-fi.com/freepythoncode)]

## Install requirements.txt
```
pip install -r requirements.txt

```

## How to use it 

```python

from notification import Notification

notify = Notification()
notify.icon_path = 'smile.png'
notify.audio_path = 'notification-sound.mp3'
notify.background = 'black'
notify.description = 'hi this is tkinter notification test\nhi this is tkinter notification test'
notify.show()

```
