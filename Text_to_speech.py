#03/02/2021
#wednesday

#Following 3 modules you have to import in your system.
from tkinter import *
from gtts import gTTS
from playsound import playsound


window = Tk()
#above line initiate the window.
#window is the name of the window created in this project.
#further all the happpening goingto occur in the window can only be accessed by it only.
window.geometry("500x500")
#above line set the dimensions of the window.
window .configure(bg='ghost white')
#above line make the window configurable and allow us to set the background color. 
window.title('project - Text to speech')
#above line set the title of the window.


Label(window, text = "TEXT_TO_SPEECH", font = "arial 20 bold", bg='white smoke').pack()
#Label() widget is used to display one or more than one line of text that users can’t able to modify
#window is the name which we refer to our window
#text = which we display on the label.
#font = in which the text is written.
#pack = organize widget in block.

Label(text ="project - Text to speech", font = 'arial 15 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')

Msg = StringVar()
#Msg is a string type variable

Label(window,text ="Enter Text", font = 'arial 15 bold', bg ='white smoke').place(x=20,y=60)

entry_field = Entry(window, textvariable = Msg ,width ='50')
#Entry() = it used to create an input text field.
#textvariable =  it is used to retrieve the current text to entry widget
entry_field.place(x=20,y=100)
#above line set's the dimension of the entry field.

def Text_to_speech():
    Message = entry_field.get()
    #above line will take the message from the entry field.
    speech = gTTS(text = Message)
    #text is the sentences or text to be read.
    speech.save('text.mp3')
    #speech.save(‘DataFlair.mp3’) will saves the converted file as DataFlair as mp3 file
    playsound('text.mp3')
    #playsound() used to play the sound

def Exit():
    window.destroy()

#root.destroy() will quit the program by stopping the mainloop().
def Reset():
    Msg.set("")
#Reset function set Msg variable to empty strings.

Button(window, text = "PLAY", font = 'arial 15 bold' , command = Text_to_speech ,width = '4').place(x=25,y=140)

Button(window, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = Exit, bg = 'OrangeRed1').place(x=100 , y = 140)

Button(window, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset).place(x=175 , y = 140)

#Button() widget used to display button on the window

window.mainloop()
#window.mainloop() is a method that executes when we want to run our program.