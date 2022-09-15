#!/usr/bin/python
# IMPORTS
from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox
# from PIL import ImageTk,Image


# DEFINING WINDOW
root = Tk()
# root.iconbitmap(bitmap = "is7.ico")
img = PhotoImage(file='is7.gif')
root.tk.call('wm', 'iconphoto', root._w, img)
root.title('IS-7-Translator')
root.geometry("1090x560")

def call_translate():
    translated.delete(1.0, END)
    try:
        for key, value in languages.items():
            if (value == original_combo.get()):
                from_key = key
        
        for key, value in languages.items():
            if (value == final_combo.get()):
                to_key = key
        
        words = textblob.TextBlob(original.get(1.0, END))
        words = words.translate(from_lang=from_key, to=to_key)

        translated.insert(1.0, words)

    except Exception as e:
        messagebox.showerror("IS-7-Translator", e)

def clear():
    original.delete(1.0, END)
    translated.delete(1.0, END)

# TEXT BOXES
original = Text(root, height=20, width=50, font=("Monospace", 12))
original.grid(row=0, column=0, pady=20, padx=10)

# is7img = ImageTk.PhotoImage(Image.open("is7.png"))

call_button = Button(root, text="TRANSLATE", font=("Monospace", 16), command=call_translate)
call_button.grid(row=0, column=1)

# is7 = Label(call_button, image=is7img)
# is7.grid(row=1, column=0)

translated = Text(root, height=20, width=50, font=("Monospace", 12))
translated.grid(row=0, column=2, pady=20, padx=10)

# GRABBING LANGUAGE LIST FROOM GOOGLETRANS

languages = googletrans.LANGUAGES
language_list = list(languages.values())

# COMBO BOXES

original_combo = ttk.Combobox(root, width=50, value=language_list, font=("Monospace", 12))
original_combo.current(21)
original_combo.grid(row=1, column=0)

final_combo = ttk.Combobox(root, width=50, value=language_list, font=("Monospace", 12))
final_combo.current(21)
final_combo.grid(row=1, column=2)

# CLEAR BUTTON

clear_button = Button(root, text="Clear", command=clear, font=("Monospace", 12))
clear_button.grid(row=2, column=1)

root.mainloop()
