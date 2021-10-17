from pynput import keyboard
import globals as g

def setkb(key):
	g.kbhit = key

def on_press(key):
	setkb(str(key))
	#print(kbhit)

def on_release(key):
	setkb('none')
	# Stop listener
	if key == keyboard.Key.esc:
		return False


# non-blocking fashion
listener = keyboard.Listener(on_press = on_press, on_release = on_release)
