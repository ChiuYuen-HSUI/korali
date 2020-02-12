import tkinter as tk
from tkinter import *
from tkinter import ttk # if python.7 Tkinter. ttk is like the CSS.
from tkinter.messagebox import showerror, showwarning, showinfo
#import json
import os


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
varProblem = 'Problem'
varSolver = 'Solver'
varExperiment = 'Experiments'
Names = ['Hello','B','C','D','E','F']

Types = ['1','2','3','4','5','6']

hierarchy = []
configDB = [] # Lista de diccionarios.
paths = []
for (dirpath, dirnames,filenames) in os.walk('../../source'):
    for filename in filenames:
        if filename.endswith('.config'): 
            configDB.append(filename) # os.sep.join([dirpath, filename])
            path = os.getcwd()
            hierarchy.append(path+dirpath)
            #paths.append(dirpath)

print(hierarchy)
print('PATHS :')
print(paths)

tree = {} # Tree.

#############################################################
## ******************* FUNCTIONS ****************************

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
    #showerror(title = "Error", message = text)
    showwarning(title = 'Error',message=text)
    #showinfo(title='Error',message=text)


def printConfig(config):
    
    pass

    
            
## Crea los tabs de uno en uno
def crearTab(totalTabs,cont):
    global contador
    if contador < 6:
        # NEW TAB:
        tab1 = tk.Frame(totalTabs)
        totalTabs.add(tab1, text = "Experiment "+str(contador))
        leftFrame = ttk.Frame(tab1)
        leftFrame.grid(column = 0, row = 0, sticky = 'nsew',)
        sep = tk.Frame(tab1, width=4, bd=2, relief='sunken')
        sep.grid(column = 1,row = 0, sticky = 'ns')
        rightFrame = ttk.Frame(tab1)
        rightFrame.grid(column = 2, row = 0, sticky = 'nsew')

        # Make frames same width:
        tab1.grid_columnconfigure(0, weight=1, uniform="group1")
        tab1.grid_columnconfigure(2, weight=1, uniform="group1")
      
        # LEFT SIDE OF TAB1:

        variablesname=tk.Label(leftFrame, text="Variables", font="Arial 20")
        variablesname.grid(row=0, column=2,pady = 30)
        variablesname.config(fg=extraColor)

        ## CASCADE:

        Problem = tk.Menubutton(leftFrame, text = varProblem,indicatoron=True,borderwidth=1, relief="raised", width=20, border=3)
        Solver = tk.Menubutton(leftFrame, text = varSolver,indicatoron=True,borderwidth=1, relief="raised", width=20, border=3)
        Experiment = tk.Menubutton(leftFrame, text = varExperiment,indicatoron=True,borderwidth=1, relief="raised", width=20, border=3)
        mainProblemMenu = tk.Menu(Problem, tearoff=False)
        mainSolverMenu = tk.Menu(Solver, tearoff=False)
        mainExperimentMenu = tk.Menu(Experiment, tearoff=False)
        mainExperimentMenu.add_radiobutton(value=0, label='Experiment.config')

        #
        Problem.configure(menu=mainProblemMenu)
        Solver.configure(menu=mainSolverMenu)
        Experiment.configure(menu=mainExperimentMenu)
        ##
        evalMenu = tk.Menu(mainProblemMenu, tearoff=False)
        mainProblemMenu.add_cascade(label='Evaluation', menu=evalMenu)        
        ###
        directMenu = tk.Menu(evalMenu, tearoff=False)
        evalMenu.add_cascade(label='Direct', menu=directMenu)
        directMenu.add_radiobutton(value=0, label='Direct.config', command = lambda : printConfig('path'))
        ####
        basicMenu = tk.Menu(directMenu, tearoff=False)
        directMenu.add_cascade(label='Basic', menu=basicMenu)
        basicMenu.add_radiobutton(value=0, label='Basic.config')
        ####
        gradientMenu = tk.Menu(directMenu, tearoff=False)
        directMenu.add_cascade(label='Gradient', menu=gradientMenu)
        gradientMenu.add_radiobutton(value=1, label='Gradient.config')
        ###
        gaussProcessMenu = tk.Menu(evalMenu, tearoff=False)
        evalMenu.add_cascade(label='GaussianProcess', menu=gaussProcessMenu)
        gaussProcessMenu.add_radiobutton(value=0, label = 'GaussianProcess.config')
        ###
        bayesMenu = tk.Menu(evalMenu, tearoff=False)
        evalMenu.add_cascade(label='Bayessian', menu=bayesMenu)
        bayesMenu.add_radiobutton(value = 0, label ='Bayessian.config')
        ####
        hierMenu = tk.Menu(bayesMenu, tearoff=False)
        bayesMenu.add_cascade(label='Hierarchical', menu=hierMenu)
        hierMenu.add_radiobutton(value= 0, label='Theta.config')
        hierMenu.add_radiobutton(value= 1, label='ThetaNew.config')
        ##
        execMenu = tk.Menu(mainProblemMenu, tearoff=False)
        mainProblemMenu.add_cascade(label='Execution', menu=execMenu)
        ###
        gaussMenu = tk.Menu(execMenu, tearoff=False)
        execMenu.add_cascade(label='Gaussian', menu=gaussMenu)
        gaussMenu.add_radiobutton(value=0, label='Gaussian.config', command = lambda : printConfig('path'))
        ###
        modelMenu = tk.Menu(execMenu, tearoff=False)
        execMenu.add_cascade(label='Model', menu=modelMenu)
        modelMenu.add_radiobutton(value=1, label='Model.config')

        ### SOLVER CASCADE ###
        #
        executorMenu = tk.Menu(mainSolverMenu, tearoff=False)
        mainSolverMenu.add_cascade(label='Executor', menu=executorMenu)
        executorMenu.add_radiobutton(value=0,label = 'executor.config')
        #
        optimizerMenu = tk.Menu(mainSolverMenu, tearoff=False)
        mainSolverMenu.add_cascade(label='Optimizer', menu=optimizerMenu)
        ##
        cmaesMenu = tk.Menu(optimizerMenu, tearoff=False)
        optimizerMenu.add_cascade(label='CMAES', menu = cmaesMenu)
        cmaesMenu.add_radiobutton(value=0,label='CMAES.config')
        ##
        deaMenu = tk.Menu(optimizerMenu, tearoff=False)
        optimizerMenu.add_cascade(label='DEA', menu = deaMenu)
        deaMenu.add_radiobutton(value=0,label='DEA.config')
        ##
        LMCMAESMenu = tk.Menu(optimizerMenu, tearoff=False)
        optimizerMenu.add_cascade(label='LMCMAES', menu = LMCMAESMenu)
        LMCMAESMenu.add_radiobutton(value=0,label='LMCMAES.config')
        ##
        rpropMenu = tk.Menu(optimizerMenu, tearoff = False)
        optimizerMenu.add_cascade(label='Rprop', menu = rpropMenu)
        rpropMenu.add_radiobutton(value=0, label = 'Rprop.config')
        #
        samplerMenu = tk.Menu(mainSolverMenu, tearoff=False)
        mainSolverMenu.add_cascade(label='Sampler', menu=samplerMenu)
        ##
        mcmcMenu = tk.Menu(samplerMenu, tearoff = False)
        samplerMenu.add_cascade(label='MCMC', menu = mcmcMenu)
        mcmcMenu.add_radiobutton(value= 0, label = 'MCMC.config')
        ##
        tmcmcMenu = tk.Menu(samplerMenu, tearoff = False)
        samplerMenu.add_cascade(label='TMCMC', menu = tmcmcMenu)
        tmcmcMenu.add_radiobutton(value= 0, label = 'TMCMC.config')
        #
        sampleMenu = tk.Menu(mainExperimentMenu, tearoff = False)
        mainExperimentMenu.add_cascade(label='Sample', menu=sampleMenu)
        sampleMenu.add_radiobutton(value=0,label='Sample.config')
        #
        variableMenu = tk.Menu(mainExperimentMenu, tearoff = False)
        mainExperimentMenu.add_cascade(label='Variable', menu = variableMenu)
        variableMenu.add_radiobutton(value=0, label = 'variable.hpp')

    

        
        
       

        
        Problem.grid(row=8, column = 0, pady=10, padx=10)
        Solver.grid(row=8, column = 1, pady=10, padx=10)
        Experiment.grid(row=8, column = 2, pady=10, padx=10)

        contador += 1
    else:
        popupmsgwarning('Number of experiments exceeded!')
    

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





app = KORALI()
app.geometry("1680x720") # Size of our application.
app.minsize("1360","400")
app.mainloop()





