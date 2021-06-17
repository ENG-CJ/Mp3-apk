import pygame
from pygame import mixer
from tkinter import *
import os
from PIL import ImageTk,Image
# function
def play_song():
    global current_song
    current_song=play_list.get(ACTIVE)
    display_song.config(text=f'Song:   {current_song}')
    songs_status.set('Playing.')
    mixer.music.load(current_song)
    mixer.music.play()

def Pause():
    display_song.config(text='Song: Paused')
    mixer.music.pause()

def Stop():
    display_song.config(text='Song: Stopped')
    mixer.music.stop()

def resume():
    display_song.config(text='{current_song}')
    mixer.music.unpause()


root=Tk()
root.state('zoomed')
root.config(bg='#463e3f')
root.resizable(0,0)
root.title('MP3 APP | Developed By ENG-CJ')
root.iconbitmap('HEADPHONE.ico')
# frame
frame=Frame(root,bd=12,relief='flat',bg='#34282c',width=1540,height=560)
frame.place(x=0,y=205)

# mixing songs
mixer.init()
songs_status=StringVar()
songs_status.set('Choosing..')

play_list=Listbox(frame,selectmode=SINGLE,width=500,height=30,bd=0,bg='#34282c',fg='white')
play_list.place(x=0,y=1)

os.chdir(r"C:\Users\PC\Music\All Musics")
songs=os.listdir()
for s in songs:
    play_list.insert(END,s)


# Buttons
play_button=Button(root,text='Play',bg='blue',fg='white',font=('Verdana',11,'bold'),
                   bd=5,relief='flat',command=play_song)
play_button.place(x=10,y=770)
Pause=Button(root,text='Pause',bg='#000080',fg='white',font=('Verdana',11,'bold'),
                   bd=5,relief='flat',command=Pause)
Pause.place(x=80,y=770)
Stop=Button(root,text='Stop',bg='#9f000f',fg='white',font=('Verdana',11,'bold'),
                   bd=5,relief='flat',command=Stop)
Stop.place(x=165,y=770)
Resume=Button(root,text='Resume',bg='green',fg='white',font=('Verdana',11,'bold'),
                   bd=5,relief='flat',command=resume)
Resume.place(x=235,y=770)

display_song=Label(root,bg='#34282c',fg='white',font=('Kanit',12,'bold'))
display_song.place(x=490,y=775)



Label(root,bg='#8b0000',
    height=14).pack(fill=X)
Label(root,text='Music Player App [Mp3]',bg='#8b0000',fg='white',
      font=('Mate SC',25,'bold'),height=5).place(x=500,y=0)
Label(root,text='Play Your Song ',bg='#8b0000',fg='white',
      font=('Mate SC',12)).place(x=620,y=120)
# images
img=Image.open(r'Portal_Grey_1.png')
resize=img.resize((200,200),Image.ANTIALIAS)
new=ImageTk.PhotoImage(resize)
Label(root,image=new,bg='#8b0000').place(x=280,y=10)

img2=Image.open('girl.png')
resize2=img2.resize((200,200),Image.ANTIALIAS)
new2=ImageTk.PhotoImage(resize2)
Label(root,image=new2,bg='#8b0000').place(x=1335,y=12)



mainloop()