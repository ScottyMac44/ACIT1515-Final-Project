from tkinter import *
import os

def createWindow():
    root = Tk()
    root.title('Todo List')
    root.mainloop()

    return root

def loginWindow():
    root = createWindow()
    root.geometry('300x200')
    frame = Frame(root)
    frame.pack()

    usernameEntry = Entry(frame, width=40)
    passwordEntry = Entry(frame, width=40)

    usernameLabel = Label(frame, text="Username:")
    passwordLabel = Label(frame, text="Password:")

    usernameLabel.pack()
    usernameEntry.pack(padx=5, pady=5)

    passwordLabel.pack()
    passwordEntry.pack(padx=5, pady=5)

    submitButton = Button(frame, text="Submit")
    newUserButton = Button(frame, text="New User")
    newUserButton.pack()



def newUserWindow():
    root = Toplevel()
    root.geometry('300x200')
    frame = Frame(root)
    frame.pack()

    usernameEntry = Entry(frame, width=40)
    passwordEntry = Entry(frame, width=40)
    confirmEntry = Entry(frame, width=40)

    usernameLabel = Label(frame, text="Username:")
    passwordLabel = Label(frame, text="Password:")
    confirmLabel = Label(frame, text="Confirm password:")

    usernameLabel.pack()
    usernameEntry.pack(padx=5, pady=5)

    passwordLabel.pack()
    passwordEntry.pack(padx=5, pady=5)

    confirmLabel.pack()
    confirmEntry.pack(padx=5, pady=5)

    registerButton = Button(frame, text="Register")
