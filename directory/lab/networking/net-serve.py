from tkinter import *
import webbrowser

class main(Frame):
   def __init__(self, master):
      self.master = master
      frame=Frame(master)

   #########################################################
     
      def donothing():
         x = 0 

      menubar = Menu(root)
      root.config(menu=menubar)
      filemenu = Menu(menubar, tearoff=0)
      filemenu.add_command(label="New", command=donothing)
      filemenu.add_command(label="Open", command=donothing)
      filemenu.add_command(label="Save", command=donothing)
      filemenu.add_separator()
      filemenu.add_command(label="Exit", command=root.quit)
      menubar.add_cascade(label="File", menu=filemenu)

      helpmenu = Menu(menubar, tearoff=0)
      helpmenu.add_command(label="Help Index", command=donothing)
      helpmenu.add_command(label="About...", command=self.showInfo)
      menubar.add_cascade(label="Help", menu=helpmenu)
     
   #########################################################
     
      #Create a label to display header
      self.headLbl=Label(frame, text="Network Services Python Toolkit Version 1.0",relief=RIDGE)
      self.headLbl.pack(side=TOP,fill=X)
     
      #Create a border using a dummy frame with a large border width
      spacerFrame=Frame(frame,borderwidth=10)
     
      #Create another frame to hold the center part of the format
      centerFrame=Frame(spacerFrame)
      leftColumn=Frame(centerFrame,relief=GROOVE,borderwidth=2)
      rightColumn=Frame(centerFrame,relief=GROOVE,borderwidth=2)
     
      #Create some colorful widgets
      self.colorLabel=Label(rightColumn, text="Select a Script:")
      self.colorLabel.pack(fill=X)
      self.colorLabel=Label(rightColumn, text="Enter an IP Address:")
      self.colorLabel.pack(fill=X)

     
      def ipaddress(o1,o2,o3,o4):
         input = []
     
      entryText=StringVar(master)
      entryText.set("")
      self.ipAddress=Entry(rightColumn,textvariable=entryText,width = 5)
      self.ipAddress.pack(side="top")
      self.ipAddress=Entry(rightColumn,textvariable=entryText,width = 5)
      self.ipAddress.pack(side="top")
      self.ipAddress=Entry(rightColumn,textvariable=entryText,width = 5)
      self.ipAddress.pack(side="top")
      self.ipAddress=Entry(rightColumn,textvariable=entryText,width = 5)
      self.ipAddress.pack(side="top")
     
      self.colorLabel=Label(rightColumn, text="Select a Script:")
      self.colorLabel.pack(fill=X)
     
      entryText=StringVar(master)
      entryText.set("Enter a subnet mask")
      self.ipAddress=Entry(rightColumn,textvariable=entryText)
      self.ipAddress.pack(fill=X)
     
      # Make the frames visible
      leftColumn.pack(side=LEFT, expand=YES, fill=Y)
      rightColumn.pack(side=LEFT, expand=YES, fill=BOTH)
      centerFrame.pack(side=TOP, expand=YES, fill=BOTH)
  
      #Create the Info button
      Button(spacerFrame, text="About", command=self.showInfo).pack(side=TOP, fill=X)
     
      #Create the Quit button
      Button(spacerFrame, text="Quit", command=self.quit).pack(side=TOP, fill=X)
     
      spacerFrame.pack(side=TOP, expand=YES, fill=BOTH)
      frame.pack(expand=YES, fill=BOTH)
     
   def quit(self):
      import sys; sys.exit()
  
   def showInfo(self):
      toplevel = Toplevel(self.master, bg="white")
      toplevel.transient(self.master)
      toplevel.iconbitmap(default='favicon.ico')
      toplevel.geometry("250x200") # widthxheight
      toplevel.title("About the Author")
      Label(toplevel, text="This script was created by Gilbert Salas\nLast Update: May 2019\n",
      fg="navy", bg="white").pack(pady=20)

      def callback(event):
         webbrowser.open_new(r"https://gil-ryan.github.io")
     
      link = Label(toplevel, text = "https://gil-ryan.github.io", fg="blue", bg="white", cursor="hand2")
      link.pack()
      link.bind("<Button-1>", callback)
     
      Button(toplevel, text="Close", command=toplevel.withdraw).pack(pady=30)      

   ######################################################### 
      
# Initialize Window
root = Tk()

init_main = main(root)
root.title('Network Services Python Toolkit')
# root.iconbitmap(default='favicon.ico')
root.geometry("750x750") # widthxheight

root.mainloop()
