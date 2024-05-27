#tkinter brings all the GUI to work as one
from tkinter import * #This module is inbuilt and it is used for the GUI
from tkinter.ttk import Progressbar 
from pygame import mixer #This module is used for the music/sound in video game
import pyttsx3 #This module is for converrting text to speech  


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

mixer.init()

mixer.music.load('image/kbc.mp3')
mixer.music.play(-1)

correct_answers = ["Russia", "Ab Lincoln", "Heron", "Dollar", "Python", "36",
                   "Linux", "Brazil", "11:23PM", "MI", "Jupiter", "7", "1000 years", "Apple",
                   "Bill Gates"]

def select(event):
    callButton.place_forget()
    progressbarA.place_forget()
    progressbarB.place_forget()
    progressbarC.place_forget()
    progressbarD.place_forget()

    progressbarLabelA.place_forget()
    progressbarLabelB.place_forget()
    progressbarLabelC.place_forget()
    progressbarLabelD.place_forget()
    b = event.widget
    value = b['text']
    
    for i in range(15):
        if value == correct_answers[i]:
            questionArea.config(state=NORMAL)
            questionArea.delete(1.0, END)
            if i == 14:  # If the last question is answered correctly
                display_congratulatory_message()
            else:
                 questionArea.insert(END, question[i+1])
            questionArea.config(state=DISABLED)

            #It is used for updating the text in the option button 
            optionButton1.config(text=first_option[i+1])
            optionButton2.config(text=second_option[i+1])
            optionButton3.config(text=third_option[i+1])
            optionButton4.config(text=fourth_option[i+1])

            amountLabel.config(image=amountimages[i])
            return

    else:
        # Play the "mld.wav" sound for wrong answer
        mixer.music.load('image/mld.wav')
        mixer.music.play()

    # Display losing message
    display_losing_message()
    
    
def display_losing_message():
    def close():
        root1.destroy()
        root.destroy()
    
    def tryagain():
        mixer.music.stop()
        mixer.music.load('image/kbc.mp3')
        mixer.music.play(-1)
        LifeLine50Button.config(state=NORMAL, image=image50)
        audiencePoleButton.config(state=NORMAL, image=audiencePole)
        phoneLifeLineButton.config(state=NORMAL, image=phoneImage)
        root1.destroy()
        reset_question()
    
    root1=Toplevel()
    root1.overrideredirect(True)
    root1.config(bg='black')
    root1.geometry("500x400+140+30")    
    imgLabel=Label(root1, image=centreImage, bd=0)
    imgLabel.pack( pady=30)

    loseLabel=Label(root1, text='You Lose', font=('arial', 40, 'bold'), bg='red', fg='white')
    loseLabel.pack()

    tryagainButton=Button(root1, text='Try Again', font=('arial',20, 'bold'), bg='black', fg='white'
                             ,activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                             command=tryagain)
    tryagainButton.pack()

    closeButton=Button(root1, text='Close', font=('arial',20, 'bold'), bg='black', fg='white'
                             ,activebackground='black', activeforeground='white', bd=0, cursor='hand2'
                             ,command=close)
    closeButton.pack()
    

def display_congratulatory_message():
    def close():
        root2.destroy()
        root.destroy()

    def playagain():
        LifeLine50Button.config(state=NORMAL, image=image50)
        audiencePoleButton.config(state=NORMAL, image=audiencePole)
        phoneLifeLineButton.config(state=NORMAL, image=phoneImage)
        root2.destroy()
        reset_question()
    mixer.music.stop()
    mixer.music.load('image/Kbcwon.mp3')
    mixer.music.play()
    root2 = Toplevel()
    root2.overrideredirect(True)
    root2.config(bg='black')
    root2.geometry("500x400+140+30")
    root2.title('Congratulations! You Won!')
    imgLabel=Label(root2, image=centreImage, bd=0)
    imgLabel.pack( pady=30)

    congrats_label = Label(root2, text='Congratulations! You Won!', font=('arial', 20, 'bold'), bg='black', fg='white')
    congrats_label.pack()

    playagainButton=Button(root2, text='Play Again', font=('arial',20, 'bold'), bg='black', fg='white'
                             ,activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                             command=playagain)
    playagainButton.pack()

    closeButton=Button(root2, text='Close', font=('arial',20, 'bold'), bg='black', fg='white'
                             ,activebackground='black', activeforeground='white', bd=0, cursor='hand2'
                             ,command=close)
    closeButton.pack()

   
    #When you click the play again button it will reset the questions
def reset_question():
    questionArea.config(state=NORMAL)
    questionArea.delete(1.0, END)
    questionArea.insert(END, question[0])
    questionArea.config(state=DISABLED)

    optionButton1.config(text=first_option[0])
    optionButton2.config(text=second_option[0])
    optionButton3.config(text=third_option[0])
    optionButton4.config(text=fourth_option[0])

    amountLabel.config(image=amountimage)

def LifeLine50():
    LifeLine50Button.config(image=image50x, state=DISABLED)
    if questionArea.get(1.0, 'end-1c')==question[0]:
       optionButton1.config(text='')
       optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c')==question[1]:
       optionButton1.config(text='')
       optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c')==question[2]:
       optionButton2.config(text='')
       optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c')==question[3]:
       optionButton1.config(text='')
       optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c')==question[4]:
       optionButton1.config(text='')
       optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c')==question[5]:
       optionButton2.config(text='')
       optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c')==question[6]:
       optionButton4.config(text='')
       optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c')==question[7]:
       optionButton1.config(text='')
       optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c')==question[8]:
       optionButton2.config(text='')
       optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c')==question[9]:
       optionButton1.config(text='')
       optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c')==question[10]:
       optionButton1.config(text='')
       optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c')==question[11]:
       optionButton1.config(text='')
       optionButton2.config(text='')

    if questionArea.get(1.0, 'end-1c')==question[12]:
       optionButton2.config(text='')
       optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c')==question[13]:
       optionButton1.config(text='')
       optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c')==question[14]:
       optionButton2.config(text='')
       optionButton4.config(text='')


def audiencePoleLifeline():
    audiencePoleButton.config(image=audiencePolex, state=DISABLED)
    progressbarA.place(x=580, y=190)
    progressbarB.place(x=620, y=190)  
    progressbarC.place(x=660, y=190)  
    progressbarD.place(x=700, y=190)  

    progressbarLabelA.place(x=580, y=320)
    progressbarLabelB.place(x=620, y=320)
    progressbarLabelC.place(x=660, y=320)
    progressbarLabelD.place(x=700, y=320)

    if questionArea.get(1.0, 'end-1c')==question[0]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=70)
        progressbarD.config(value=90)

    if questionArea.get(1.0, 'end-1c')==question[1]:
        progressbarA.config(value=20)
        progressbarB.config(value=80)
        progressbarC.config(value=40)
        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c')==question[2]:
        progressbarA.config(value=80)
        progressbarB.config(value=20)
        progressbarC.config(value=10)
        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c')==question[3]:
        progressbarA.config(value=50)
        progressbarB.config(value=30)
        progressbarC.config(value=70)
        progressbarD.config(value=40)

    if questionArea.get(1.0, 'end-1c')==question[4]:
        progressbarA.config(value=30)
        progressbarB.config(value=60)
        progressbarC.config(value=30)
        progressbarD.config(value=50)

    if questionArea.get(1.0, 'end-1c')==question[5]:
        progressbarA.config(value=90)
        progressbarB.config(value=10)
        progressbarC.config(value=0)
        progressbarD.config(value=50)

    if questionArea.get(1.0, 'end-1c')==question[6]:
        progressbarA.config(value=10)
        progressbarB.config(value=80)
        progressbarC.config(value=80)
        progressbarD.config(value=10)

    if questionArea.get(1.0, 'end-1c')==question[7]:
        progressbarA.config(value=30)
        progressbarB.config(value=80)
        progressbarC.config(value=40)
        progressbarD.config(value=50)

    if questionArea.get(1.0, 'end-1c')==question[8]:
        progressbarA.config(value=70)
        progressbarB.config(value=50)
        progressbarC.config(value=20)
        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c')==question[9]:
        progressbarA.config(value=30)
        progressbarB.config(value=40)
        progressbarC.config(value=80)
        progressbarD.config(value=50)

    if questionArea.get(1.0, 'end-1c')==question[10]:
        progressbarA.config(value=20)
        progressbarB.config(value=50)
        progressbarC.config(value=20)
        progressbarD.config(value=50)

    if questionArea.get(1.0, 'end-1c')==question[11]:
        progressbarA.config(value=30)
        progressbarB.config(value=70)
        progressbarC.config(value=80)
        progressbarD.config(value=20)

    if questionArea.get(1.0, 'end-1c')==question[12]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c')==question[13]:
        progressbarA.config(value=30)
        progressbarB.config(value=10)
        progressbarC.config(value=70)
        progressbarD.config(value=70)

    if questionArea.get(1.0, 'end-1c')==question[14]:
        progressbarA.config(value=30)
        progressbarB.config(value=60)
        progressbarC.config(value=80)
        progressbarD.config(value=50)

   
def phoneLifeLine():
    mixer.music.load('image/calling.mp3')
    mixer.music.play()
    callButton.place(x=70, y=260)
    phoneLifeLineButton.config(image=phoneImagex, state=DISABLED)

    

def phoneclick():
    for i in range(15):
        if questionArea.get(1.0, 'end-1c')==question[i]:
            engine.say(f'The answer is{correct_answers[i]}')
            engine.runAndWait()

    mixer.music.load('image/kbc.mp3')
    mixer.music.play(-1)
    
question = ["Which is the largest country in the world?",
             "Which ancient civilization built the Great Pyramid of Giza?",
             "Which one of these four birds has the longest beak and feet?",
             "The Industrial Revolution originated in which country??",
             "Guido van Rossum in 1991 designed which language?",
             "Find the sequence: 9, 18, 27, _?",
             "Which one is the first fully supported 64-bit operating system?",
             "Which country has won the most FIFA World Cup titles?",
             "what time corresponds to 23:23 hours ?",
             "Which team has won most number of IPL matches ?",
             "Which is the largest planet in our Solar system?",
             "How many continents are there in the world?",
             "How many years are there in one Millenium?",
             "ipad is manufactured by?",
             "Who founded Microsoft?"]

first_option = ["Nigeria", "John Adams",
                "Heron", "Germany",
                "Javascript", "36",
                "Windows 7", "Italy", "11:23PM", "KKR",
                "Earth", "8",
                "100 years", "Google", "Monty Ritz"]

second_option = ["USA", "Ab Lincoln",
                 "Parrot", "France",
                 "Python", "34",
                 "Linux", "Argentina", "11.11PM", "CSK",
                 "Uranus", "5",
                 "50 years",
                 "Microsoft", "Danis Lio"]

third_option = ["China", "Putin",
                "Crow", "England",
                "Java", "30",
                "Mac", "Germany", "7:23PM", "MI",
                "Mars", "7",
                "500 years",
                "Amazon", "Bill Gates"]

fourth_option = ["Russia", "Barack Obama",
                 "Pigeon", "United States",
                 "C++", "37",
                 "Windows XP", "Brazil", "9.11PM", "RCB",
                 "Jupiter",
                 "6",
                 "1000 years", "Apple",
                 "Jeff Bezos"]

#Main GUI setup
 
root = Tk()
root.geometry("1270x652+0+0")
#For editing the Title
root.title('Who Wants To Be A Millionaire Created by Group3')
#For editing background colour
root.config(bg='black')



#you are structuring the layout of your GUI into different
#sections (top, center, bottom) within the leftframe. 
#This helps in organizing and managing
#the placement of widgets within your GUI.

leftframe = Frame(root, bg='black', padx=90)
leftframe.grid(row=0, column=0)

topFrame = Frame(leftframe, bg='black', pady=15)
topFrame.grid()

centreFrame = Frame(leftframe, bg='black', pady=15)
centreFrame.grid(row=1, column=0)

bottomFrame = Frame(leftframe)
bottomFrame.grid(row=2, column=0)

rightframe = Frame(root, pady=25, padx=50, bg='black')
rightframe.grid(row=0, column=1)

image50 = PhotoImage(file='image/50-50.png')
image50x = PhotoImage(file='image/50-50-x.png')

LifeLine50Button = Button(topFrame, image=image50, bg='black', bd=0, activebackground='black'
                          , command=LifeLine50)
LifeLine50Button.grid(row=0, column=0)

audiencePole=PhotoImage(file='image/audiencePole.png')
audiencePolex=PhotoImage(file='image/audiencePolex.png')

audiencePoleButton=Button(topFrame, image=audiencePole, bg='black', bd=0, activebackground='black', width=180,
                           height=80, command=audiencePoleLifeline)
audiencePoleButton.grid(row=0, column=1)

phoneImage=PhotoImage(file='image/phoneAFriend.png')
phoneImagex=PhotoImage(file='image/phoneAFriendx.png')

phoneLifeLineButton=Button(topFrame, image=phoneImage, bg='black', bd=0, activebackground='black', width=180, height=80,
                           command=phoneLifeLine)
phoneLifeLineButton.grid(row=0, column=2)

callimage=PhotoImage(file='image/phone.png')

callButton=Button(root, image=callimage, bd=0, bg='black', activebackground='black', cursor='hand2',
                  command=phoneclick)

centreImage=PhotoImage(file='image/center.png')

logoLabel=Label(centreFrame, image=centreImage, bg='black', width=300, height=200)
logoLabel.grid(row=0, column=0)

amountimage=PhotoImage(file='image/Picture0.png')
amountimage1=PhotoImage(file='image/Picture1.png')
amountimage2=PhotoImage(file='image/Picture2.png')
amountimage3=PhotoImage(file='image/Picture3.png')
amountimage4=PhotoImage(file='image/Picture4.png')
amountimage5=PhotoImage(file='image/Picture5.png')
amountimage6=PhotoImage(file='image/Picture6.png')
amountimage7=PhotoImage(file='image/Picture7.png')
amountimage8=PhotoImage(file='image/Picture8.png')
amountimage9=PhotoImage(file='image/Picture9.png')
amountimage10=PhotoImage(file='image/Picture10.png')
amountimage11=PhotoImage(file='image/Picture11.png')
amountimage12=PhotoImage(file='image/Picture12.png')
amountimage13=PhotoImage(file='image/Picture13.png')
amountimage14=PhotoImage(file='image/Picture14.png')
amountimage15=PhotoImage(file='image/Picture15.png')

amountimages=[amountimage1, amountimage2, amountimage3, amountimage4, amountimage5, amountimage6, 
              amountimage7, amountimage8, amountimage9, amountimage10, amountimage11, amountimage12,
                amountimage13, amountimage14, amountimage15

]


amountLabel=Label(rightframe, image=amountimage, bg='black')
amountLabel.grid(row=0, column=0)

layoutImage=PhotoImage(file='image/Lay.png')

layoutLabel=Label(bottomFrame, image=layoutImage, bg='black')
layoutLabel.grid(row=0, column=0)

questionArea=Text(bottomFrame, font=('arial', 18, 'bold'), width=34, height=2, wrap='word', bg='black', fg='white'
                   ,bd=0)
questionArea.place(x=70, y=10)

questionArea.insert(END, question[0])

labelA=Label(bottomFrame, text='A:', bg='black', fg='white', font=('arial', 16, 'bold'))
labelA.place(x=60, y=110)

optionButton1=Button(bottomFrame, text=first_option[0], font=('arial', 18, 'bold'), bg='black', fg='white'
                     ,bd=0, activebackground='black', activeforeground='white', cursor='hand2')
optionButton1.place(x=100, y=100)

labelB=Label(bottomFrame, text='B:', bg='black', fg='white', font=('arial', 16, 'bold'))
labelB.place(x=330, y=110)

optionButton2=Button(bottomFrame, text=second_option[0], font=('arial', 18, 'bold'), bg='black', fg='white'
                     ,bd=0, activebackground='black', activeforeground='white', cursor='hand2')
optionButton2.place(x=370, y=100)

labelC=Label(bottomFrame, text='C:', bg='black', fg='white', font=('arial', 16, 'bold'))
labelC.place(x=60, y=190)

optionButton3=Button(bottomFrame, text=third_option[0], font=('arial', 18, 'bold'), bg='black', fg='white'
                     ,bd=0, activebackground='black', activeforeground='white', cursor='hand2')
optionButton3.place(x=100, y=180)

labelD=Label(bottomFrame, text='D:', bg='black', fg='white', font=('arial', 16, 'bold'))
labelD.place(x=330, y=190)

optionButton4=Button(bottomFrame, text=fourth_option[0], font=('arial', 18, 'bold'), bg='black', fg='white'
                     ,bd=0, activebackground='black', activeforeground='white', cursor='hand2')
optionButton4.place(x=370, y=180)

progressbarA=Progressbar(root, orient=VERTICAL, length=120)
progressbarB=Progressbar(root, orient=VERTICAL, length=120)
progressbarC=Progressbar(root, orient=VERTICAL, length=120)
progressbarD=Progressbar(root, orient=VERTICAL, length=120)

progressbarLabelA=Label(root, text='A', font=('arial', 20, 'bold'), bg='black', fg='white')
progressbarLabelB=Label(root, text='B', font=('arial', 20, 'bold'), bg='black', fg='white')
progressbarLabelC=Label(root, text='C', font=('arial', 20, 'bold'), bg='black', fg='white')
progressbarLabelD=Label(root, text='D', font=('arial', 20, 'bold'), bg='black', fg='white')


#functionality

optionButton1.bind('<Button-1>', select)
optionButton2.bind('<Button-1>', select)
optionButton3.bind('<Button-1>', select)
optionButton4.bind('<Button-1>', select)






root.mainloop()