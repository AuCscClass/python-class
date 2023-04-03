import os
from tkinter import *
from tkinter import filedialog # importing the library
from pygame import mixer
from PIL import ImageTk, Image


root = Tk()
root.title("Music player")
root.geometry("485x650+500+50")  # position of the background the x-axis, y-axis, how far from x-axis and y-axis
root.configure(background="#333333")  # for the background color
root.resizable(False, False)  # we don't want users setting or resizing the window
mixer.init()

songs = [] # An array for the song
current = "" # for the current song
pause = False 

def AddMusic():

    global current, root
    root = filedialog.askdirectory() 
    for song in os.listdir(root):
        name, ext = os.path.splitext(song)
        if ext == ".mp3":
            songs.append(song)


    for song in songs:
        playlist.insert(END, song)

    playlist.selection_set(0)
    current = playlist.get(ACTIVE)# Function to  add song


def PlayMusic():
    global current,pause
    if not pause:
        mixer.music.load(os.path.join(root, playlist.get(ACTIVE)))
        mixer.music.play()
    else:
        mixer.music.unpause()
        pause = False

def Pause():
    global current,pause
    mixer.music.pause()
    pause = True
def NextMusic():
    global current
    try:
        playlist.selection_clear(0,END)
        playlist.selection_set(songs.index(current)+1)
        current = songs[playlist.curselection()[0]]
        mixer.music.load(os.path.join(root, current))
        mixer.music.play()
    except:
        pass
def PreviousMusic():
    global current
    try:
        playlist.selection_clear(0, END)
        playlist.selection_set(songs.index(current)-1)
        current = songs[playlist.curselection()[0]]
        mixer.music.load(os.path.join(root, current))
        mixer.music.play()
    except:
        pass


lower_frame = Frame(root, bg="#FFFFFF", width=485, height=180) # to place it inside our widget we use the place command
lower_frame.place(x=0, y=300) # this is where we want to position our buttons

bg = Image.open("bg.jpg")
back_ground = ImageTk.PhotoImage(bg)
Label(root, image=back_ground).place(x=0, y=0, width=485, height=400)

image = Image.open("forwardb.jpg") # to load in the image
image = image.resize((32, 32)) # to resize the image
icon = ImageTk.PhotoImage(image) # converting the image
root.iconphoto(True, icon)


Menu = PhotoImage(file= "menu.PNG") # creating a menu background
Label(root, image= Menu).place(x=0, y=580, width=485, height=100) # where to position it? and place items

Frame_Music = Frame(root, bd = 1, width=4, height=1)
Frame_Music.place(x=0, y=480)

button_play = Image.open("playb.jpg")
button_play = button_play.resize((50,50))
play_button = ImageTk.PhotoImage(button_play)

button_stop = Image.open("stopb.jpg")
button_stop = button_stop.resize((50,50))
stop_button = ImageTk.PhotoImage(button_stop)

button_pause = Image.open("pausep.jpg")
button_pause = button_pause.resize((50,50))
pause_button = ImageTk.PhotoImage(button_pause)

button_forward = Image.open("forwardb.jpg")
button_forward = button_forward.resize((50,50))
forward_button = ImageTk.PhotoImage(button_forward)

button_back = Image.open("backwardb.jpg")
button_back = button_back.resize((50, 50))
back_button = ImageTk.PhotoImage(button_back)

Button(root, text= "Browse file", width = 60, height = 1, font= ("calibri", 12, "bold"), fg = "Black", bg="#FFFFFF", command=AddMusic).place(x=0, y=450)

Button(root, image=play_button, bg= "#FFFFFF", bd =0, width=60, height =60, command=PlayMusic).place(x=215, y=395)

Button(root, image=stop_button, bg="#FFFFFF", bd=0, width=80, height=60, command=mixer.music.stop).place(x=120, y=395)

Button(root, image=pause_button, bg = "#FFFFFF", bd=0, width = 80, height=60, command=Pause).place(x=300, y=395)


Button(root, image=forward_button, bg="#FFFFFF", bd=0, width=60, height=60, command=NextMusic).place(x=400, y=395)

Button(root, image=back_button, bg="#FFFFFF", bd=0, width=60, height=60, command=PreviousMusic).place(x=30, y=395)

scroll = Scrollbar(Frame_Music)
playlist = Listbox(Frame_Music, width = 77, font = ("Tahoma", 8), bg ="#333333", fg ="grey", selectbackground= "black", cursor="hand2", bd =0, yscrollcommand= scroll.set)

scroll.config(command = playlist.yview)
scroll.pack(side = RIGHT, fill = BOTH)
playlist.pack(side=RIGHT, fill=BOTH)


root.mainloop()
