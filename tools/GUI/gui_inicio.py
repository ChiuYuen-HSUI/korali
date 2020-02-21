import tkinter as tk
from tkinter import *
from tkinter import ttk # if python.7 Tkinter. ttk is like the CSS.
from tkinter.messagebox import showerror, showwarning, showinfo
import os, sys
import json



# ************ VARIABLES ******************
HUGE_FONT = ("Verdana",14)
LARGE_FONT = ("Verdana",12) #Font and size.
NORM_FONT = ("Verdana",10) #Font and size.
SMALL_FONT = ("Verdana",8) #Font and size.
RES_FONT = ('Courier',12)

darkColor ='lightseagreen'
lightColor = '#00A3E0'
extraColor = '#183A54'

contador = 1

menus = []

mainPath = '../../source/problem'

#############################################################
## ******************* FUNCTIONS ****************************

def openFile(fileName):
	print("Open File "+fileName+"!")

def printConfig(configPath, rightFrame):
    
    for widget in rightFrame.winfo_children():
        widget.destroy()
    archivo = configPath
    with open(archivo, 'r') as myfile:
        data=myfile.read()

    # parse file
    obj = json.loads(data)
    print(obj)
    conf = obj['Variables Configuration']
    
    d = conf  
    label=tk.Label(rightFrame, text="Set your own variables:  ", font="Arial 16")
    label.grid(row=0, column=0,pady = 20,padx=20, columnspan = 6, sticky='W')

    r = 1   
    for exp in d:
        for key in exp.keys():
            if key=='Description':
                label=tk.Label(rightFrame, text=key, font="Arial 12")
                label.grid(row=r, column=0, sticky='W',pady=20)
            else:
                label=tk.Label(rightFrame, text=exp[key], font="Arial 12")
                label.grid(row=r, column=0, sticky='W',columnspan=1)
                entry = tk.Entry(rightFrame)
                entry.grid(row=r, column = 1,sticky='W')
            r += 1
    #rightFrame.grid_columnconfigure(0, weight=1)
    myfile.close()

def splitPath(s):
    dirs = []
    dirName = ''
    for i in s:
        if i == os.path.sep:
            dirs += [dirName]
            dirName = ''
        else:
            dirName += i
    if len(dirName) > 0:
        dirs += [dirName]
    return dirs

def readDirs(filePath,configTreeDB):
    dirs = splitPath(filePath)
    levels=len(dirs)
    sublevel = levels + 1
    dirInfoDic={}
    childrenList=[]
    for (dirPath,dirNames,fileNames) in os.walk(filePath):
        if dirPath == filePath:
            for fileName in fileNames:
                if fileName.endswith('.config'):
                    dirName = dirs[levels-1]
                    configTreeDB[dirName] = dirInfoDic
                    dirInfoDic['config'] = filePath + os.path.sep + fileName
                    dirInfoDic['children'] = childrenList
            continue
        dirs=splitPath(dirPath)
        levels=len(dirs)
        if levels > sublevel:
            del dirNames[:]
            continue
        readDirs(dirPath, configTreeDB)
        dirName = dirs[levels - 1]
        childrenList += [dirName]


# ******************* TUTORIAL ******************
def tutorial():
    
    def page2():
        tut.destroy()
        tut2 = tk.Tk()

        def page3():
            tut2.destroy() # Destroys page 2 and opens page 3:
            tut3 = tk.Tk()

            tut3.wm_title('Part 3!')

            label = ttk.Label(tut3, text = 'Part 3', font = NORM_FONT)
            label.pack(side='top', fill='x', pady=10)
            B1 = ttk.Button(tut3, text='Done!', command=tut3.destroy)
            B1.pack()
            tut3.mainloop()

        tut2.wm_title('Part 2!')
        label = ttk.Label(tut2, text = 'Part 2', font = NORM_FONT)
        label.pack(side='top', fill='x', pady=10)
        B1 = ttk.Button(tut2, text='Done!', command= page3)
        B1.pack()
        tut2.mainloop()

    tut = tk.Tk()
    tut.wm_title('Tutorial')
    label = ttk.Label(tut, text='What do you need help with?', font = NORM_FONT)
    label.pack(side='top', fill='x', pady=10)

    B1 = ttk.Button(tut, text = 'Overview of the application', command = page2)
    B1.pack()
    B2 = ttk.Button(tut, text = 'How do I get Days-timed data?', command = lambda:popupmsg('Not yet complited')) # How do I trade???
    B2.pack()
    B3 = ttk.Button(tut, text = 'Graph Question/Help', command = lambda: popupmsg('Not yet complited'))
    B3.pack()

    tut.mainloop()
## -------------------------END OF TUTORIAL FUNCTION ----------------


def popupmsgwarning(text):
    Tk().withdraw()
    showwarning(title = 'Error',message=text)

def crearMenu(padre,directorio):
    global menus
    if directorio not in menus:
        subMenu = Menu(padre)
        padre.add_cascade(label=directorio, menu = subMenu)
        dirInfo=configTreeDB[directorio]
        configPath=dirInfo['config']
        if configPath != "NULL":
            dirs=splitPath(configPath)
            subMenu.add_command(label = dirs[len(dirs)-1], command = lambda : printConfig(configPath,rightFrame))
        children=dirInfo['children']
        for child in children:
            crearMenu(subMenu,child)

    menus.append(directorio)

## Crea los tabs de uno en uno
def crearTab(totalTabs,cont):
    global contador
    global menus
    
    if contador < 6:
        ## Create Tab and frames inside:
        tab = tk.Frame(totalTabs)
        totalTabs.add(tab, text = 'Experiment '+str(cont))
        leftFrame = ttk.Frame(tab)
        leftFrame.grid(column = 0, row = 0, sticky = 'nsew',)
        sep = tk.Frame(tab, width=4, bd=2, relief='sunken')
        sep.grid(column = 1,row = 0, sticky = 'ns')
        rightFrame = ttk.Frame(tab)
        rightFrame.grid(column = 2, row = 0, sticky = 'nsew')
        ##
        # Make frames same width:
        tab.grid_columnconfigure(0, weight=1, uniform="group1")
        tab.grid_columnconfigure(2, weight=1, uniform="group1")

        # LEFT SIDE OF TAB1:

        variablesname=tk.Label(leftFrame, text="Variables", font="Arial 20")
        variablesname.grid(row=0, column=2,pady = 30)
        variablesname.config(fg=extraColor)

        ## CASCADE:

        dirs = splitPath(mainPath)

        menuButton = tk.Menubutton(leftFrame, text =dirs[2] , indicatoron=True, borderwidth = 1, relief='raised', width=20, border=3)
        menuPadre = tk.Menu(menuButton, tearoff=False)
        menuButton.configure(menu=menuPadre)

        for directorio in configTreeDB.keys():
            crearMenu(menuPadre,directorio)

        menus.clear() # Avoid 

        
        menuButton.grid(row=8, column = 0, pady=10, padx=10)

        contador += 1
    else:
        popupmsgwarning('Number of experiments exceeded!')
    
## ****************** END OF FUNCTIONS **********************

        
#############################################################
## ******************* CLASSES ******************************

 
class KORALI(tk.Tk): #Inherited tk.tk

    # Initializing:
    def __init__(self,*args,**kwargs): # Self is implied, you don't need to pass self, but is a must.
        tk.Tk.__init__(self,*args,**kwargs)
 
        tk.Tk.wm_title(self,'KORALI')

        # Barra de arriba:
        self.menubar = tk.Menu(self) # Menu in the container.
        self.homemenu = tk.Menu(self.menubar, tearoff=0) # Tearoff = if clicking in the dashedline, we can make it its own window.
        self.homemenu.add_command(label='New Experiment...',command = lambda: crearTab(self.totalTabs,contador))                       
        self.homemenu.add_command(label='Save',command = lambda: popupmsg('Not supported just yet!'))
        self.homemenu.add_command(label='Save as...',command = lambda: popupmsg('Not supported just yet!'))
        self.homemenu.add_separator() # Separator baselr.
        self.homemenu.add_command(label='Open Project...',command = lambda: popupmsg('Not supported just yet!'))
        self.homemenu.add_command(label='Export as...',command = lambda: popupmsg('Not supported just yet!'))
        self.homemenu.add_separator() # Separator bar.
        self.homemenu.add_command(label='Exit',command = quit)
        self.menubar.add_cascade(label='Home',menu = self.homemenu)


        ##### HELP MENU:
        helpmenu = tk.Menu(self.menubar, tearoff = 0)
        helpmenu.add_command(label='Tutorial', command = tutorial)
        self.menubar.add_cascade(label='Help', menu = helpmenu)

        tk.Tk.config(self, menu = self.menubar)

        # ************** TABS **********************
        # Create the TABS BAR
        self.totalTabs = ttk.Notebook(self)
        self.totalTabs.pack(expand = 1, fill = "both")

        # Call the function crearTab to create as many tabs as the user wants:
        crearTab(self.totalTabs, contador)

        
        # DOWN-TOOLBAR
        toolbar = tk.Frame(self, background='darkcyan')
        insertButt = tk.Button(toolbar, text='Close KORALI', command=quit)
        insertButt.config(bd = 2)
        insertButt.pack(side='right',padx=2,pady=2) # Padding options.
        
        toolbar.pack(side='bottom', fill='x')


## --------------- END OF CLASSES ------------------------    
########################################################    



configTreeDB = {}
readDirs(mainPath, configTreeDB)
print(configTreeDB)

app = KORALI()
app.geometry("1680x720") # Size of our application.
app.minsize("1360","400")
app.mainloop()




