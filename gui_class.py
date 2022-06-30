'''
Author: Carson Pribble
File: gui_class.py
Purpose: This is the GUI version of the Paragon Seat Scraper. It
    has multiple dependencies and when run, will open a small gui
    window with options for displaying current data (held in text file),
    updating that data with the seat scraper running headlessly,
    and displaying the current text file data in a scrolltext box.
    This version is object oriented (a class)
'''
# IMPORTS FOR TKINTER, OS AND PILLOW
from tkinter import *
import tkinter.scrolledtext as st
from os import startfile
from PIL import ImageTk, Image

# IMPORTS FOR SEAT_SCRAPER TOOLS AND SCRAPER
from scrape_tools import *

import time

class ParagonGui(object):

    def __init__(self):
        self.window = Tk()
        self.window.title("Paragon  Volume Checker GUI")
        self.window.geometry("600x300")
        self.window.configure(bg="lightgrey")

        # Main Label
        self.lbl_title = Label(self.window, text="Paragon Seat Scraper", bg="lightgrey", fg="black", font=("Helvetica", 16))
        self.lbl_title.place(x=10,y=10)

        # Buttons
        self.btn_display_data = Button(self.window, text="Display Data",bg="black", fg="grey", command=self.displayData)
        self.btn_display_data.place(x=10,y=50)

        self.btn_update_file = Button(self.window, text="Update File", bg="black", fg="grey", command=self.runScraper)
        self.btn_update_file.place(x=10,y=90)

        self.btn_open_file = Button(self.window, text="Open Current Data File", bg="black", fg="grey", command=self.openFile)
        self.btn_open_file.place(x=10,y=130)

        # Image
        self.paragon_image = Image.open(".\paragon_img.jpg")
        self.paragon_image = self.paragon_image.resize((110,110), Image.Resampling.LANCZOS)
        paragon_image_tk = ImageTk.PhotoImage(self.paragon_image)
        self.lbl_image = Label(self.window, image=paragon_image_tk)
        self.lbl_image.place(x=10,y=170)

        # Text area
        self.text_area = st.ScrolledText(self.window, width=35, height=15, font=("Helvetica", 12))
        self.text_area.place(x=250,y=10)       

        # Mainloop
        self.window.mainloop()

    # Methods
    def displayData(self):
        self.text_area.delete('1.0', END)
        # Calls function to get data from txt file. scrape_tools.getDataGui
        seat_data = getDataGui()
        self.text_area.insert(INSERT,seat_data)

    def runScraper(self):
        # Add feedback message to text_area for feedback
        self.text_area.delete('1.0', END)
        self.text_area.insert(INSERT, "PROCESSING DATA, PLEASE \nWAIT UNTIL A COMPLETION \nMESSAGE IS SHOWN!")
        # Add a temporary label next to the Update File button for feedback
        processing_lbl = Label(self.window, text="Processing", bg="lightgrey", fg="black", font=("Helvetica", 10))
        processing_lbl.place(x=90,y=90)
        self.window.update()
        movies = getMovies()
        writeToFileFormatted(movies)
        self.text_area.delete('1.0', END)
        self.text_area.insert(INSERT, "COMPLETED!")
        # Remove temporary label
        processing_lbl.after(1000, processing_lbl.destroy)

    def openFile(self):
        try:
            startfile(".\lux_box_seats.txt")
        except:
            print("No File Exists")
            self.text_area.delete('1.0', END)
            self.text_area.insert(INSERT, "File Was Not Found")




instance = ParagonGui()