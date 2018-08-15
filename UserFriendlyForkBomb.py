#  Copyright 2018 Nocturneon
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

# Nocturneon's User Friendly GUI Fork Bomb
# Now even your grandma can bring your system to a crawl!

# Import what we need to make our forks and GUI
import os
import tkinter
from tkinter import *
from tkinter import font

# A straightforward user experience
def userExperience():
    # Embrace the fork
    while 1:
        # Summon the forky boi
        os.fork()

# Begin Tkinter GUI for user friendliness
master = Tk()

# Big font for big helpfulness
bigBoi = font.Font(family='Comic Sans MS', size=72, weight='bold')

# Calculate coordinates and center window so that the button to fork your system up is right in your face; very user friendly!
w = 570
h = 280

ws = master.winfo_screenwidth()
hs = master.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

master.geometry('%dx%d+%d+%d' % (w, h, x, y))

# Clearly describe window, because it's more user friendly that way
master.wm_title("Nocturneon's User Friendly Fork Bomb")

# Big button so you know exactly where to click
b = Button(master, font=bigBoi, text="Fork My \n System Up", command=userExperience)
b.grid(row=1)

mainloop()

# Automatically focus on our creation
ip.focus_set()
