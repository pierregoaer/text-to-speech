from tkinter import *
from tkinter.filedialog import askopenfile
import pyttsx3
from pdfminer.high_level import extract_text

window = Tk()
window.title("Title")
window.config(padx=20, pady=20)

engine = pyttsx3.init()


def open_pdf():
    file = askopenfile(filetypes=[('pdf file', '*.pdf')]).name
    speak_pdf(file)


def speak_pdf(file):
    text = extract_text(file)
    engine.say(text)
    engine.runAndWait()


def speak_text():
    text = text_entry.get()
    engine.say(text)
    engine.runAndWait()


open_file = Button(text="Select PDF and speak", command=open_pdf)
open_file.pack()

text_entry = Entry()
text_entry.pack()

speak_button = Button(text="Speak this text", command=speak_text)
speak_button.pack()


window.mainloop()
