import datetime, pyglet
import pyglet
stop = False
while stop == False:
    time = str(datetime.datetime.now().time())
    print(time)
    if time >= "15:04:00.000000":
        music = pyglet.resource.media('sample.mp3')
        music.play()
        pyglet.app.run()
        break