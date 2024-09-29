# importing modules
import tkinter
import pygame
import random
import os

# importing sub-modules
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# initialization of mixer
pygame.mixer.init()

# clearing console from messages
os.system("cls")

# playing theme audio
pygame.mixer.music.load("assets/audio/theme.mp3")
pygame.mixer.music.play()

# variable section
is_music_playing = True

# specific/thunder variable (metadata)
__version__ = "v1.0.0"
__updated__ = "29.09.2024"
__tag__ = "@dusanrsc"
__by__ = "Dusan Rosic"

# CONSTANTS section
TITLE = "Access Key Generator"

ROOT_WIDTH =  "500"
ROOT_HEIGHT = "300"
ROOT_SIZE = f"{ROOT_WIDTH}x{ROOT_HEIGHT}"

KEY_INPUT_X = 85
KEY_INPUT_Y = 200
KEY_INPUT_WIDTH = 6
KEY_INPUT_FONT_SIZE = 13
GAP = 70

# hexadecimal color tuple CONSTANTS section
RED = "#FF0000"
GREEN = "#00FF00"
BLUE = "#0000FF"

BLACK = "#000000"
WHITE = "#FFFFFF"

ALPHA = GREEN

KEY_INPUT_BACKGROUND_COLOR = RED
KEY_INPUT_TEXT_COLOR = WHITE
BUTTON_BACKGROUND_COLOR = KEY_INPUT_BACKGROUND_COLOR
BUTTON_TEXT_COLOR = KEY_INPUT_TEXT_COLOR

# lists section
keys = [
	"PTMGF-28VKB-2W934-482QH-98623", 
	"DXR32-X44M7-CYTCX-P6H6P-97CPG",
	"KJG93-HDPGB-PXBPP-TFB49-9DBVB",
	"QRR4P-F4FDP-H986R-RF6P3-7QK3R"
]

# functions section
# generate key section
def generate_key():

	# clearing entry input fields from previous keys
	key_input_1.delete(0, END)
	key_input_2.delete(0, END)
	key_input_3.delete(0, END)
	key_input_4.delete(0, END)
	key_input_5.delete(0, END)

	# generating new index number to assign it with key list content
	random_keys = random.randint(0, len(keys)-1)

	# displaying new key in entry input fiels
	key_input_1.insert(1, keys[random_keys][:5].upper())
	key_input_2.insert(1, keys[random_keys][6:11].upper())
	key_input_3.insert(1, keys[random_keys][12:17].upper())
	key_input_4.insert(1, keys[random_keys][18:23].upper())
	key_input_5.insert(1, keys[random_keys][24:29].upper())

# copy key function
def copy_key():

	# clearing previous clipboard
	root.clipboard_clear()

	# adding keys segment-by-segment to clipboard
	root.clipboard_append(f"{key_input_1.get()}-{key_input_2.get()}-{key_input_3.get()}-{key_input_4.get()}-{key_input_5.get()}")

# play or pause music function
def play_or_pause_music():

	# setting up global variable
	global is_music_playing

	# condition for music play/pause controlling
	if is_music_playing:
		is_music_playing = False
		play_or_pause_music_button.config(text=" ■ ")
		pygame.mixer.music.stop()

	else:
		is_music_playing = True
		play_or_pause_music_button.config(text=" ♫ ")
		pygame.mixer.music.play()

# root window settings section
root = Tk()
root.title(f"{TITLE} | {__version__} | by: {__tag__}")
root.config(bg=WHITE)
root.geometry(ROOT_SIZE)
root.resizable(False, False)

# initialization of background image
img = Image.open("assets/image/background.png")
photo = ImageTk.PhotoImage(img)

# creating and placing background image as label
background = Label(root, image=photo)
background.place(x=0, y=0, relwidth=1, relheight=1)

# entry input field section
# entry input field for key 0-5
key_input_1 = Entry(root, width=KEY_INPUT_WIDTH, font=("Arial", KEY_INPUT_FONT_SIZE), bg=KEY_INPUT_BACKGROUND_COLOR, fg=KEY_INPUT_TEXT_COLOR)
key_input_1.place(x=KEY_INPUT_X, y=KEY_INPUT_Y)

# entry input field for key 5-10
key_input_2 = Entry(root, width=KEY_INPUT_WIDTH, font=("Arial", KEY_INPUT_FONT_SIZE), bg=KEY_INPUT_BACKGROUND_COLOR, fg=KEY_INPUT_TEXT_COLOR)
key_input_2.place(x=KEY_INPUT_X+(GAP), y=KEY_INPUT_Y)

# entry input field for key 10-15
key_input_3 = Entry(root, width=KEY_INPUT_WIDTH, font=("Arial", KEY_INPUT_FONT_SIZE), bg=KEY_INPUT_BACKGROUND_COLOR, fg=KEY_INPUT_TEXT_COLOR)
key_input_3.place(x=KEY_INPUT_X+(GAP*2), y=KEY_INPUT_Y)

# entry input field for key 15-20
key_input_4 = Entry(root, width=KEY_INPUT_WIDTH, font=("Arial", KEY_INPUT_FONT_SIZE), bg=KEY_INPUT_BACKGROUND_COLOR, fg=KEY_INPUT_TEXT_COLOR)
key_input_4.place(x=KEY_INPUT_X+(GAP*3), y=KEY_INPUT_Y)

# entry input field for key 20-25
key_input_5 = Entry(root, width=KEY_INPUT_WIDTH, font=("Arial", KEY_INPUT_FONT_SIZE), bg=KEY_INPUT_BACKGROUND_COLOR, fg=KEY_INPUT_TEXT_COLOR)
key_input_5.place(x=KEY_INPUT_X+(GAP*4), y=KEY_INPUT_Y)

# buttons section
# copy key to clipboard button
key_copy_button = Button(root, text="          COPY          ", font=("Arial Bold", 8), bg=BUTTON_BACKGROUND_COLOR, relief=RIDGE, fg=BUTTON_TEXT_COLOR, command=copy_key)
key_copy_button.place(x=KEY_INPUT_X+(GAP*3)-170, y=KEY_INPUT_Y+40)

# generate key button 
key_generate_button = Button(root, text="          GENERATE          ", font=("Arial Bold", 8), bg=BUTTON_BACKGROUND_COLOR, relief=RIDGE, fg=BUTTON_TEXT_COLOR, command=generate_key)
key_generate_button.place(x=KEY_INPUT_X+(GAP*3)-35, y=KEY_INPUT_Y+40)

# play/pause music button
play_or_pause_music_button = Button(root, text=" ♫ ", font=("Arial", 8), bg=BUTTON_BACKGROUND_COLOR, relief=RIDGE, fg=BUTTON_TEXT_COLOR, command=play_or_pause_music)
play_or_pause_music_button.place(x=int(ROOT_WIDTH)-25, y=int(ROOT_HEIGHT)-27)

# starting program (mainloop)
root.mainloop()
