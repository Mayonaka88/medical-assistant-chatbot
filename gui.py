#Tkinter is used to create the GUI
from tkinter import *
from tkinter.font import BOLD

#We imported functions from chat.py 
#The functions are used to get the bot's response to the user's import and the category of the response
from predict import getBotInput, getTag

#Random is used to generate a unique number for the bot everytime the code is executed
import random



class ChatBot:
    def __init__(self):
        #We initialize and declare the main tkinter window display
        self.root = Tk()
        #The login() function has the first window that the user interacts with
        self.login()

    def run(self):
        #mainloop() function is used by Tkinter to start running
        self.root.mainloop()

    def mainWindowSetUp(self):

        #new fixed dimentions and a new title are declared here
        self.root.title("The Doctor's Office")
        self.root.geometry("400x625")
        self.root.resizable(width=FALSE, height=FALSE)

        #Here is a textbox where the number of the assistant and thier status is presented 
        self.label8 = Text(self.root,  width="50", height="8", font=("Arial", 12), foreground="gray",state='disabled',borderwidth=0,background="#eeeeee",cursor="arrow")
        self.label8.place(x=60,y=10, height=40, width=385)
        self.label8.tag_configure("online", foreground="green",font=("Arial", 10))
        self.label8.tag_configure("offline", foreground="red",font=("Arial", 10))

        #the random() function is used to create a unique assistant number everytime it is executed
        self.label8.configure(state='normal')
        assistantNum = round(random.random() * 100000)
        self.label8.insert('end', "Assistant #" + str(assistantNum) +"\n")
        #The chat bot starts off as offline until the user interacts with it
        self.label8.insert('end', "Offline","offline")
        self.label8.configure(state='disabled')

        #Here is where we drew the profile picture of the chat bot using shapes and text and not an image
        self.canvas1 = Canvas(self.root)
        self.canvas1.place(x=10,y=5, height=45, width=50)
        self.canvas1.create_oval(2, 2, 40, 40,fill="#0e8bcd",width=2,outline="#80c1e3")
        self.canvas1.create_text(22, 22, font=("Arial", 20),text="ツ",fill="white")

        #Here is where the dialog between the user and the chat bot will be displayed
        self.chatWindow = Text(self.root, bd=1, bg="white",  width="50", height="8", font=("Arial", 12), foreground="gray", state='disabled',padx=10, pady=10,wrap=WORD, cursor="arrow")
        self.chatWindow.place(x=6,y=55, height=385, width=370)
        self.chatWindow.tag_configure("user", foreground="white", background="#0e8bcd", justify=LEFT)
        self.chatWindow.tag_configure("bot", foreground="black", background="#d0ebff", justify=LEFT)

        #this is a simple scrollbar for the chat window
        scrollbar = Scrollbar(self.root, command=self.chatWindow.yview)
        scrollbar.place(x=375,y=55, height=385)

        #here is where the user will type in thier message so it can be processed by the bot and displayed on the chat window
        self.messageWindow = Entry(self.root, bd=1, bg="white",width="30", font=("Arial", 12), foreground="black")
        self.messageWindow.place(x=128, y=530, height=88, width=260)
        self.messageWindow.focus()
        #when the enter key is pressed, the userTyping() function will be called upon
        self.messageWindow.bind("<Return>",self.userTyping)

        #here is where the button is created and when pressed it will call upon the userTyping() function
        button = Button(self.root, text="Send",  width="12", height=5,bd=0, bg="#0080ff", activebackground="#00bfff",foreground='#ffffff',font=("Arial", 12), command=lambda: self.userTyping(None))
        button.place(x=6, y=530, height=88)

        #here is a textbox that has the patient info
        self.userInfoTitle = Text(self.root,  width="50", height="8", font=("Arial", 10, BOLD), foreground="black",state='disabled',borderwidth=0,background="#eeeeee",cursor="arrow")
        self.userInfoTitle.place(x=6,y=445, height=20, width=385)
        self.userInfoTitle.tag_configure("center", justify='center')
        self.userInfoTitle.configure(state='normal')
        self.userInfoTitle.insert('end', "Patient Info","center")
        self.userInfoTitle.configure(state='disabled')

        self.userInfo = Text(self.root,  width="50", height="8", font=("Arial", 8), foreground="gray",state='disabled',borderwidth=0,background="#eeeeee",cursor="arrow")
        self.userInfo.place(x=6,y=460, height=60, width=385)
        self.userInfo.tag_configure("info", foreground="black")
        self.userInfo.configure(state='normal')
        self.userInfo.insert('end', "Name: " ,"info")
        self.userInfo.insert('end', name1)
        self.userInfo.insert('end', "Age: " ,"info")
        self.userInfo.insert('end', age1)
        self.userInfo.insert('end', "Gender: " ,"info")
        self.userInfo.insert('end',gender1)
        self.userInfo.insert('end', "Phone Number: " ,"info")
        self.userInfo.insert('end', phoneNum1)
        self.userInfo.configure(state='disabled')

    def login(self):

        #Fixed dimentions and the title of the window are declared here
        self.root.title("The Waiting Room")
        self.root.geometry("400x375")
        self.root.resizable(width=FALSE, height=FALSE)
        
        #The welcome message is created here using labels
        self.label1 = Label(self.root, text="Welcome!",  width="12", height=5,bd=0, activebackground="#00bfff",foreground='black',font=("Arial", 12))
        self.label1.place(x=25,y=5, height=35, width=345)

        self.label2 = Label(self.root, text="Please fill out this form and your",  width="12", height=5,bd=0, activebackground="#00bfff",foreground='black',font=("Arial", 10))
        self.label2.place(x=25,y=40, height=35, width=345)

        self.label8 = Label(self.root, text="medical assistant will see you shortly!",  width="12", height=5,bd=0,foreground='black',font=("Arial", 10))
        self.label8.place(x=25,y=65, height=35, width=345)

        #This label is empty until the user tries to proceed without filling out the form
        self.label3 = Label(self.root, text="",  width="12", height=5,bd=0,foreground='red',font=("Arial", 10))
        self.label3.place(x=25,y=95, height=25, width=345)

        #These labels are used to display the criteria of the form
        self.label4 = Label(self.root, text="Name:",  width="12", height=5,bd=0,foreground='black',font=("Arial", 10))
        self.label4.place(x=25,y=125, height=35, width=90)

        self.label5 = Label(self.root, text="Age:",  width="12", height=5,bd=0,foreground='black',font=("Arial", 10))
        self.label5.place(x=25,y=175, height=35, width=90)

        self.label6 = Label(self.root, text="Gender:",  width="12", height=5,bd=0,foreground='black',font=("Arial", 10))
        self.label6.place(x=25,y=225, height=35, width=90)

        self.label7 = Label(self.root, text="Phone number:",  width="12", height=5,bd=0,foreground='black',font=("Arial", 10))
        self.label7.place(x=25,y=275, height=35, width=90)
        
        #Here is where the textboxes the user writes in are created
        self.chatWindow1 = Text(self.root, bd=1, bg="white",  width="50", height="8", font=("Arial", 10), foreground="gray", padx=10, pady=10,wrap=WORD)
        self.chatWindow1.place(x=120,y=125, height=35, width=250)

        self.chatWindow2 = Text(self.root, bd=1, bg="white",  width="50", height="8", font=("Arial", 10), foreground="gray", padx=10, pady=10,wrap=WORD)
        self.chatWindow2.place(x=120,y=175, height=35, width=250)

        self.chatWindow3 = Text(self.root, bd=1, bg="white",  width="50", height="8", font=("Arial", 10), foreground="gray", padx=10, pady=10,wrap=WORD)
        self.chatWindow3.place(x=120,y=225, height=35, width=250)

        self.chatWindow4 = Text(self.root, bd=1, bg="white",  width="50", height="8", font=("Arial", 10), foreground="gray", padx=10, pady=10,wrap=WORD)
        self.chatWindow4.place(x=120,y=275, height=35, width=250)

        #Here is where the button is created. When the button is pressed, it will call the loginForm() function
        self.button1 = Button(self.root, text="Send",  width="12", height=5,bd=0, bg="#0080ff", activebackground="#00bfff",foreground='#ffffff',font=("Arial", 12), command=lambda: self.loginForm(None))
        self.button1.place(x=120,y=325, height=35, width=250)

    def loginForm( self, event):
        #this function is used to get data from the textboxes and save them 
        #then it calls on the mainWindowSetUp() function which is where the user can interact with the chatbot
        
        #here the user data are saved in global variables so it can be used later
        #the get() function extracts the data from the textboxes and saves them in thier respective variable
        global name1
        global age1
        global gender1
        global phoneNum1
        name1 = self.chatWindow1.get("1.0", END)
        age1 = self.chatWindow2.get("1.0", END)
        gender1 = self.chatWindow3.get("1.0", END)
        phoneNum1 = self.chatWindow4.get("1.0", END)

        #if the textboxes are left empty, the variables will save "\n"
        #by using this if statment, we force the user to fill out the form so they can proceed
        if name1 == "\n" or age1 == "\n" or gender1 == "\n" or phoneNum1 == "\n" :
            self.label3.config(text="Please enter valid information to proceed", foreground="red")
        else:
            #if the textboxes are filled out, then all the elements of the login page are deleted so we can have an empty window that the other function can use
            self.label1.destroy()
            self.label2.destroy()
            self.label3.destroy()
            self.label4.destroy()
            self.label5.destroy()
            self.label6.destroy()
            self.label7.destroy()
            self.label8.destroy()
            self.chatWindow1.destroy()
            self.chatWindow2.destroy()
            self.chatWindow3.destroy()
            self.chatWindow4.destroy()
            #after all the elements are removed, the function that houses the chat bot is called upon
            self.mainWindowSetUp()


    def userTyping(self, event):
        #We extract the user's message that they imputted and send it to addUserAndBotInputs() function
        userInput = self.messageWindow.get()
        self.addUserAndBotInputs(userInput)

    def addUserAndBotInputs(self, userInput):
        #This function is used to send the user's message to be processed by the bot using the getBotInput() function and 
        #display both the user's and the bot's messages on the chat window

        #If the user didnt write anything, the program would not display anything
        if not userInput:
            return
        
        #user's input is being printed on the chat window
        self.messageWindow.delete(0, END)
        self.chatWindow.configure(state='normal')
        self.chatWindow.insert('end', "User: " )
        self.chatWindow.insert('end', " "+userInput+" ", "user" )
        self.chatWindow.insert('end', "\n"+"\n" )
        self.chatWindow.see(END)
        self.chatWindow.configure(state='disabled')

        #the getTag() function returns "Offline" if the message that the user sent is a "goodbye" message
        #any other message will return "Online"
        tag =getTag(userInput)
        if tag == "Online":
            self.label8.configure(state='normal')
            self.label8.delete("1.16",END)
            self.label8.insert('end', "\n"+"Online","online")
            self.label8.configure(state='disabled')

        elif tag == "Offline":
            self.label8.configure(state='normal')
            self.label8.delete("1.16",END)
            self.label8.insert('end', "\n"+"Offline","offline")
            self.label8.configure(state='disabled')

        #here is where we send the user's input to be processed by the bot using the getBotInput()
        #the getBotInput() function will return a the bot's response as a string
        #then it will be displayed in the chat window 
        botInput = getBotInput(userInput)
        self.chatWindow.configure(state='normal')
        self.chatWindow.insert('end', "Bot: " )
        self.chatWindow.insert('end', " "+botInput+" ", "bot" )
        self.chatWindow.insert('end', "\n"+"\n" )
        self.chatWindow.see(END)
        self.chatWindow.configure(state='disabled')
    

#When the Python interpreter reads a file and the module is being executed, the __name__ variable is set as __main__
#this if statment is true when we run the file
#so when it is true, it creates an object of the ChatBot class, which is the class we coded above, and it excecutes the run() function of that object
if __name__ == "__main__":
    bot = ChatBot()
    bot.run()