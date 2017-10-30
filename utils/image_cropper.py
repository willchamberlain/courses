from Tkinter import *
from tkFileDialog import askopenfilename
import Image, ImageTk
from math import floor

if __name__ == "__main__":

    root = Tk()
    
    frame = Frame(root, bd=2, relief=SUNKEN)
    frame.grid_rowconfigure(0,weight=1)
    frame.grid_columnconfigure(0,weight=1)
    
    xscroll = Scrollbar(frame, orient=HORIZONTAL)
    xscroll.grid(row=1, column=0, sticky=E+W)
    
    yscroll = Scrollbar(frame, orient=VERTICAL)
    yscroll.grid(row=0, column=1, sticky=N+S)
    
    canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)    
    canvas.grid(row=0, column=0, sticky=N+S+E+W)
    
    xscroll.config(command=canvas.xview)
    yscroll.config(command=canvas.yview)
    
    frame.pack(fill=BOTH,expand=1)
    
    File = askopenfilename(parent=root, initialdir="/home/will/Desktop/pics/baby_team_ai/google_search/", title="choose an image")
    img = ImageTk.PhotoImage(Image.open(File)) 
    canvas.create_image(0,0,image=img, anchor="nw")
    canvas.config(scrollregion=canvas.bbox(ALL))
    
    def print_coords(event):
        
        x_scrolled = xscroll.get()
        x_scrolled_diff = x_scrolled[1]-x_scrolled[0]
        x_scrolled_max_travel = 1. - x_scrolled_diff
        x_scrolled_current_travel = x_scrolled[0]/x_scrolled_max_travel
        x_current_pixel_offset = x_scrolled_current_travel*img.width()
         
    
        print(event.x,event.y)
        bounding_box_centre       = [event.x, event.y]
        print(bounding_box_centre)
        bounding_box_centre[0]    = bounding_box_centre[0]+floor(x_current_pixel_offset)
        bounding_box_top_left     = [bounding_box_centre[0]-111, bounding_box_centre[1]-111]
        if bounding_box_top_left[0] < 0:
            offset = 0 - bounding_box_top_left[0]    
            bounding_box_top_left[0] = 0
            bounding_box_centre[0]   = bounding_box_centre[0] + offset
        if bounding_box_top_left[1] < 0:            
            offset = 0 - bounding_box_top_left[1]    
            bounding_box_top_left[1] = 0
            bounding_box_centre[1]   = bounding_box_centre[1] + offset
        bounding_box_bottom_right = [bounding_box_centre[0]+112, bounding_box_centre[1]+112]
        print(bounding_box_centre, bounding_box_top_left, bounding_box_bottom_right)
        print(x_scrolled)
        print(x_scrolled_diff, x_scrolled_diff/2.)
        print(x_scrolled_max_travel)        
        print(x_scrolled_current_travel)
        print(x_current_pixel_offset)
        
        
    canvas.bind("<Button 1>", print_coords)    
    
    
    root.mainloop()
