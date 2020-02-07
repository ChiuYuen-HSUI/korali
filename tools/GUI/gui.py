import tkinter as tk
from tkinter import *
from tkinter import ttk # if python.7 Tkinter. ttk is like the CSS.
from tkinter import PhotoImage

from PIL import ImageTk, Image

import sys, os
import matplotlib
matplotlib.use('TkAgg') # Backend of matplotlib.
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
#from matplotlib.figure import Figure
import matplotlib.animation as animation # Replot every x seconds.
from matplotlib import style 
#from mpl_finance import candlestick_ohlc
import urllib
import json
import pandas as pd
import numpy as np
import matplotlib.dates as mdates # Modify dates and ticker
import matplotlib.ticker as mticker
from matplotlib import pyplot as plt

import json


# ************ DESCRIPTION ****************
# Panel = Componente que dentro puede tener otros objetos graficos. Agrupador.
# Los tiene que ordenar de alguna manera.
# Layouts =  Como orde
# Label = ETiqueta, texto.
# Pack = ejecuta el layout ( manera de ordenar los componentes en panel padre )

# Frame = marco. Ventana de root. Tab.
# Labelframe = marco con texto.
# Entry = input para escribir
# ----------- END DESCRIPTION -------------



# ************ VARIABLES ******************
HUGE_FONT = ("Verdana",14)
LARGE_FONT = ("Verdana",12) #Font and size.
NORM_FONT = ("Verdana",10) #Font and size.
SMALL_FONT = ("Verdana",8) #Font and size.

RES_FONT = ('Courier',12)


darkColor ='lightseagreen'
lightColor = '#00A3E0'
extraColor = '#183A54'

visualization = 'ggplot'
newVisualization = 'ggplot'

style.use(visualization) # also: dark_background or ...

f = plt.figure() # figsize=(4,4), dpi=100

# Defaults that the client can change later:
exchange = 'Bitstamp' # Initial exchange.
DatCounter = 9000 # Update.
programName = 'btce'
resampleSize = '15Min'
DataPace = 'live' # DEFAULT GRAPH SETTINGS
candleWidth = 0.8
refreshRate = ''
paneCount = 1
UpdateInterval = 6
EMAs = []   # In case you want to add different estimates. When clicked none, clear.
SMAs = []

chartLoad = True

# ----- MAIN PAGE:
itemVariable=StringVar()
experimentname = StringVar()
rateDict={}
itemVariable=StringVar()
quantityVar = StringVar()
#quantityVar.trace('w',quantityFieldListener)
itemRate=2

nameVar = 'None yet'
typeVar = 'None yet'
defaultVar = '0'
descriptionVar = 'None description yet in here, but you should add one.'
rateVar = StringVar()
rateVar2 = StringVar()
rateVariable = 'None yet'
rateVar.set("%.2f"%itemRate)
costVar=StringVar()
#costVar.trace('w', costFieldListener)
storeOptions=['Frozen','Fresh']
addItemNameVar=StringVar()
addItemRateVar=StringVar()
addItemTypeVar=StringVar()
addstoredVar=StringVar()
addstoredVar.set(storeOptions[0])

optionsExperiment=['a','b','c','d','e']

varmenubutton = 'Experiments'

## TAB1 LEFT FRAME BUTTONS VARIABLES:
counter = 0

#==========update tree View
updateTV = ttk.Treeview(height=15, columns=('Name','Rate','type','Store_Type'))


itemLists= list()
totalCost=0.0
totalCostVar=StringVar()
totalCostVar.set("Total Cost = {}".format(totalCost))

updateItemId=""

# +++++++++
element_header = ['First Name','Last Name']
element_list = ['First','Second']
movie_index = 2
movie_count = 1

# Example of data:
Actors_list = [("Rowan","Atkinson"),("John","Candy"),("Morgan","Freeman"),("James","Garner"),("Cary","Grant"),("Kate","Hudson"),
("Jack","Nicholson"),("William","Powell"),("Arnold","Schwarzenegger"),("Tom","Selleck"),("John","Wayne")]
Movies_list = [[("Bean","1997"),("Mr. Bean's Holiday","2007"),("The Lion King","1994"),("Johnny English","2003"),("Johnny English Reborn","2011"),("Keeping Mum","2005"),("The Black Adder","1982-1983")],
[("Dr. Zonk and the Zunkins","1974"),("Tunnel Vision","1976"),("SCTV","1976-1979"),("1941","1979")],
[("The Pawnbroker","1964"),("Blade","1973"),("The Electric Company","1971-1977"),("Attica","1980"),
("Brubaker","1980"),("Street Smart","1980"),("Driving Miss Daisy","1989"),("Glory","1989"),("Unforgiven","1992"),
("Outbreak","1995"),("Se7en","1995"),("Amistad","1997"),("The Bucket List","2007")],
[("Cash McCall","1960"),("Sugarfoot","1957"),("Cheyenne","1955-1957"),("Maverick","1957-1962"),("The Great Escape","1963")],
[("Singapore Sue","1932"),("She Done Him Wrong","1933"),("I'm No Angel","1933"),("Born to be Bad","1934")],
[("200 Cigarettes","1999"),("Almost Famous","2000"),("How to Lose a Guy in 10 Days","2003")],
[("The Cry Baby Killer","1958"),("Seahunt","1961"),("Easy Rider","1969"),("One Flew Over the Cuckoo's Nest","1975")],
[("Mr. Roberts","1955"),("Ziegfeld Follies","1945"),("Manhattan Melodrama","1934"),("The Thin Man","1934")],
[("Hercules in New York","1969"),("Conan the Barbarian","1982"),("The Terminator","1984")],
[("The Rockford Files","1978-1979"),("The Sacketts","1979"),("Magnum, P.I.","1980-1988"),("Blue Bloods","2010-")],
[("The Shootist","1976"),("McQ","1974"),("The Cowboys","1972"),("Brown of Harvard","1926")]]



# -----

questions = ["Optimization","Sampling","Bayesian Inference","Hierarchical Bayesian Modeling"]
questions_seconds = ['5 Seconds','10 Seconds','30 Seconds','1 Min','10 Min','30 Min','1 Hour']
# --------- END VARIABLES ----------------


## ********* DATABASE *********
def populate_list():
    pass


def add_item():
    pass


def select_item(event):
    pass


def remove_item():
    pass


def update_item():
    pass


def clear_text():
    pass

############# BILLS RESTAURANT ###############
def itemAddWindow(self):

    global nameVar
    global typeVar
    global defaultVar
    global descriptionVar
    global counter

    backButton = Button(self, text="Back" , command=lambda:readAllData())
    backButton.grid(row=0, column=1)

    nameVar = 2
    print(nameVar)


    counter = 1



    AddItemButton = Button(self, text="Add Experiment", width=20, height=2, command=lambda:addItem())
    AddItemButton.grid(row=3, column=3,pady=(10,0))
    
def addItemListener(self):
    remove_all_widgets(self)
    itemAddWindow(self)

def movetoBills():
    remove_all_widgets()
    viewAllBills()

def moveToUpdate():
    remove_all_widgets()
    updateItemWindow()

def remove_all_widgets(self):
    global app
    for widget in KORALI_Page.winfo_children(self):
        widget.grid_remove()

def LogOut():
    pass

def optionMenuListener():
    pass

def printExperiment():
    global varmenubutton
    print('This is :',varmenubutton)


######## TREE VIEW
def OnClick(self, event):
    global return_index
    item = self.tree.identify('item',event.x,event.y)
    return_index = (int((item[1:4]),16) - 1)
    reload_tree(return_index,self)

def isnumeric(s):
    """test if a string is numeric"""
    for c in s:
        if c in "1234567890-.":
            numeric = True
        else:
            return False
    return numeric

def change_numeric(data):
    """if the data to be sorted is numeric change to float"""
    new_data = []
    if isnumeric(data[0][0]):
        # change child to a float
        for child, col in data:
            new_data.append((float(child), col))
        return new_data
    return data

def sortby(tree, col, descending):
    """sort tree contents when a column header is clicked on"""
    # grab values to sort
    data = [(tree.set(child, col), child) for child in tree.get_children('')]
    # if the data to be sorted is numeric change to float
    data = change_numeric(data)
    # now sort the data in place
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)
    # switch the heading so that it will sort in the opposite direction
    tree.heading(col,
        command=lambda col=col: sortby(tree, col, int(not descending)))

def reload_tree(tree_index,source_tree):
    global movie_index,movie_count
    if source_tree == actor_listbox:
        i = movie_count
        for movies in Movies_list[movie_index]:
            movie_listbox.tree.delete('I' + '%03X' % i)
            i = i + 1
            movie_count = i
        i = 1
        for item in Movies_list[tree_index]:
            movie_listbox.tree.insert('',(i), values=item)
        movie_index = tree_index
        i = i + 1
    elif source_tree == movie_listbox:
        pass

############ TREE VIEW END ##################


 

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

## ********************** BASIC FUNCTIONS ***********************
# Miniture isntance:
def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title('!')
    label = ttk.Label(popup, text = msg, font = NORM_FONT)
    label.pack(side = 'top',fill='x', pady = 10)
    B1 = ttk.Button(popup, text='Okay', command = popup.destroy)
    B1.pack()
    popup.mainloop()

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

def doNothing():
    print("KORALI ROCKS")

def changeColor(newVisualization):

    if newVisualization == 'dark_background':
        visualization = newVisualization
        style.use(visualization)
        plt.rc_context({'legend.facecolor':'black','axes.edgecolor':'gray', 'xtick.color':'red','ytick.color':'black','grid.color':'darkslategray'}) #'ytick.labelsize':8,
       
    elif newVisualization == 'classic':
        visualization = newVisualization
        style.use(visualization)
    elif newVisualization == 'ggplot':
        visualization = newVisualization
        style.use(visualization)
        plt.rc_context({'legend.facecolor':'darkgray'}) #'ytick.labelsize':8,
    elif newVisualization == 'bmh':
        visualization = newVisualization
        style.use(visualization)
    else:
        style.use('ggplot')




def loadChart(run): # run can be start or stop
    global chartLoad

    if run == 'start':
        chartLoad = True
    elif run == 'stop':
        chartLoad = False


def changeTimeFrame(tf):
    global DataPace
    global DatCounter

    if tf == '7d' and resampleSize == '1Min': # Too much data... so popup!! 
        popupmsg('Too much data chosen, choose a smaller time frame or higher Iteration Interval')
    else:
        DataPace = tf
        DatCounter = 9000 

def changeSampleSize(size,width): 
    global resampleSize
    global DatCounter
    global candleWidth

    if DataPace == '7d' and resampleSize == '1Min': # Too much data... so popup!! 
        popupmsg('Too much data chosen, choose a smaller time frame or higher Iteration Interval')
    elif DataPace == 'live':
        popupmsg('You are currently viewing tick data, not OHLC')
    else:
        resampleSize = size
        DatCounter = 9000
        candleWidth = width


def changeExchange(toWhat,pn):#To what we exchange, pn = programmer name.
    global exchange
    global DatCounter
    global programName # We global so we can modify them.

    exchange = toWhat
    programName = pn
    DatCounter = 9000

## ------------------- END BASIC FUNCTIONS --------------------------

def WindowSize():
    pass






## ************** ANIMATE FUNCTION *******************
def animate(i):
    
    global refreshRate      
    global DatCounter

    # We need to PAUSE OR RESUME THE PLOT:

    if chartLoad:
        if paneCount == 1:
            if DataPace == 'live':   #
                try:
                        # Define 2 subplots:
                    if exchange == 'Bitstamp':

                        a = plt.subplot2grid((6,4), (0,0), rowspan = 5, colspan = 4) # 0,0 = starting point, rowspan, colspan 
                        a2 = plt.subplot2grid((6,4), (5,0), rowspan = 1, colspan = 4, sharex = a) # Share x axis with a. If you zoom in, they are aligned.
                        
                        #if newVisualization == 'dark_background':
                        #    plt.rcParams["axes.grid"] = False


                        dataLink = 'https://www.bitstamp.net/api/transactions/'# to add parameters use ?limit=2000&moreparameters=203.
                        data = urllib.request.urlopen(dataLink) # THIS IS IN BYTES, WE NEED TO DECODE IT.
                        data = data.read().decode("utf-8")
                        data = json.loads(data)

                        #data = data["btc_usd"] # btc_usd is the first 'key'.
                        data = pd.DataFrame(data) # Transform data into a dataframe.

                        # From subplots *********************:
                        data["datestamp"] = np.array(data['date'].apply(int)).astype('datetime64[s]')
                        dateStamps = data['datestamp'].tolist()
                        #allDates = data['datestamp'].tolist()

                        volume = data['amount'].apply(float).tolist() # ******

                        a.clear()

                        # plot dates:
                        a.plot_date(dateStamps, data["price"],lightColor,label="buys") # Colors: #00A3E0
                        #candlestick_ohlc(a,data[['date','tid','price','type','amount']].values, width=candleWidth,colorup=lightColor,colordown=darkColor)              

                        a2.fill_between(dateStamps, 0, volume, facecolor = darkColor) # SPecify the minimum point of the fill... 0.

                        a.xaxis.set_major_locator(mticker.MaxNLocator(5)) # Max amount of actual marks.
                        a.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S')) # How the data looks!
                      
                        #plt.tight_layout()
                        #Fix the OVERLAP OF AXIS:
                        plt.setp(a.get_xticklabels(), visible = False) #we wanna remove the labels of the top graph.

                        a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc = 3, ncol= 2, borderaxespad = 0)

                        title = "KORALI output\nLast Result: "+str(data["price"][0])#Last value.
                        a.set_title(title, color = 'black')
                        print('UPDATED')

                    if exchange == 'Bitfinex':
                        a = plt.subplot2grid((6,4), (0,0), rowspan=5, colspan=4)
                        a2 = plt.subplot2grid((6,4), (5,0), rowspan=1, colspan=4, sharex = a)

                        plt.setp(a.get_xticklabels(), visible = False)
                        
                        dataLink = 'https://api.bitfinex.com/v1/trades/btcusd?limit=2000'

                        data = urllib.request.urlopen(dataLink)
                        data = data.read().decode('utf-8')
                        data = json.loads(data)
                        data = pd.DataFrame(data)
                        
                        volume = data["amount"].apply(float).tolist()

                        #print(data)

                        data["datestamp"] = np.array(data['timestamp']).astype('datetime64[s]')
                        allDates = data["datestamp"].tolist()

                        buys = data[(data['type']=='buy')]
                        #buys["datestamp"] = np.array(buys['timestamp']).astype('datetime64[s]')
                        buyDates = (buys["datestamp"]).tolist()

                        sells = data[(data['type']=='sell')]
                        #sells["datestamp"] = np.array(sells['timestamp']).astype('datetime64[s]')
                        sellDates = (sells["datestamp"]).tolist()

                        a.clear()
                        
                        
                        a.plot_date(buyDates,buys["price"], lightColor, label ="buys")
                        a.plot_date(sellDates,sells["price"], darkColor, label = "sells")
                        
                        a2.fill_between(allDates,0, volume, facecolor=darkColor)

                        a.xaxis.set_major_locator(mticker.MaxNLocator(5))
                        a.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
                        plt.setp(a.get_xticklabels(), visible=False)
                        
                        #plt.tight_layout()
                        a.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
                           ncol=2, borderaxespad=0)
                        
                        title = exchange+' Coin Data\nLast Value: '+str(data["price"][0])
                        a.set_title(title, color ='black')
                        
                        priceData = data["price"].apply(float).tolist()

                    if exchange == 'IXIC_2019':
                        a = plt.subplot2grid((6,4), (0,0), rowspan=5, colspan=4)
                        a2 = plt.subplot2grid((6,4), (5,0), rowspan=1, colspan=4, sharex = a)
                        
                        df = pd.read_csv('/home/mark/Escritorio/PYTHON/korali_no_env/res_data.csv',parse_dates=['Date'], index_col='Date')

                        opens = df['Open']
                        closes = df['Close']
                        
                        #opensDates = (opens['datestamp']).tolist()

                        volume = df["Adj"]
                        a.clear()
                        
                        
                        a.plot_date(df.index,df["Open"], lightColor, label ="Opens")
                        a.plot_date(df.index,df["Close"], darkColor, label = "Closes")
                        a.plot_date(df.index,df['Low'], 'y', label = 'Low')
                        a.plot_date(df.index,df['High'], 'r', label = 'High')
                        
                        #csticks = candlestick_ohlc(a, df[['Open', 'High', 'Low', 'Close','Adj']].values, width=candleWidth, colorup=lightColor, colordown=darkColor)
                        
                        a2.fill_between(df.index,0, volume, facecolor=darkColor)

                        a.xaxis.set_major_locator(mticker.MaxNLocator(5))
                        a.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
                        plt.setp(a.get_xticklabels(), visible=False)
                        
                        #plt.tight_layout()
                        a.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
                           ncol=2, borderaxespad=0.)
                        
                        title = exchange+' Stock Price\nLast Value: '+str(df["Close"][-1])
                        a.set_title(title, color ='black')
                        print('UPDATED')
                        
                        #priceData = data["price"].apply(float).tolist()
                   # https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offsetaliases

                    
                except Exception as e:
                    print('Failed because of:',e)
                    
            elif DataPace != 'live':
                #if DatCounter > 12: 
                try:
                    if exchange == 'IXIC_2019':
                        a = plt.subplot2grid((6,4), (0,0), rowspan=5, colspan=4)
                        a2 = plt.subplot2grid((6,4), (5,0), sharex=a, rowspan=1, colspan=4)

                        df = pd.read_csv('/home/mark/Escritorio/PYTHON/korali_no_env/res_data.csv',parse_dates=['Date'],index_col='Date')
                
                        a.set_ylabel("Stock")

                        volume = df['Adj']
                        x = (len(df['Close']))-1 #Most recent DATAPOINT

                        #dfresampled = pd.DataFrame({'Datetime':dateStamp})
                        dfresampled = pd.DataFrame()
                        #dfresampled = dfresampled.set_index('Datetime')

                        
                        if DataPace == 'D':
                            title = exchange+' 1 Day Data\nLast Price: '+str(df['Close'][x])   
                        elif DataPace == 'W':
                            title = exchange+' 1 Week Data\nLast Price: '+str(df['Close'][x])
                        elif DataPace == 'B':
                            title = exchange+' Weekdays Data\nLast Price: '+str(df['Close'][x])
                        else:
                            title = 'okay'

                        dfresampled = df.resample(DataPace).mean()
                    
                        a.clear()
                        dfresampled = df.resample(DataPace).mean()
                       
                        a.plot_date(dfresampled.index,dfresampled['Open'], lightColor, label ="Opens")
                        a.plot_date(dfresampled.index,dfresampled['Close'], darkColor, label = "Closes")
                        a.plot_date(dfresampled.index,dfresampled['Low'], 'y', label = 'Low')
                        a.plot_date(dfresampled.index,dfresampled['High'], 'r', label = 'High')
                        plt.setp(a.get_xticklabels(), visible = False)

                        a2.fill_between(df.index,0, volume, facecolor=darkColor)

                        a.xaxis.set_major_locator(mticker.MaxNLocator(5))
                        a.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))

                        #plt.tight_layout()
                        a.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
                            ncol=2, borderaxespad=0.)
                        a.set_title(title, color ='black')

                except Exception as e:
                    print(str(e),"main animate non tick")
                    DatCounter = 9000
            else:
                print('NOT IMPLEMENTED YET')
                        
                #else:
                 #   DatCounter += 1
                

## ---------------- END OF ANIMATE FUNCTION --------------

#############################################################
## ******************* CLASSES ******************************
 
class KORALI(tk.Tk): #Inherited tk.tk

    # Initializing:
    def __init__(self,*args,**kwargs): # Self is implied, you don't need to pass self, but is a must.
        tk.Tk.__init__(self,*args,**kwargs)
 
        tk.Tk.wm_title(self,'KORALI')

        container = tk.Frame(self) # Edge of the window. Tkinter offers 2 options: Pack. Grid.
        container.pack(side = "top", fill = "both", expand = True) # Fill the entire space. Expand = If there is white space, you can expand it.
        container.grid_rowconfigure(0, weight=1) # The minimum is 0. weight is the priority... who goes first...
        container.grid_columnconfigure(0, weight=1)

        # Barra de arriba:
        menubar = tk.Menu(container) #Menu in the container.
        homemenu = tk.Menu(menubar, tearoff=0) # Tearoff = if clicking in the dashedline, we can make it its own window.
        homemenu.add_command(label='New Project...',command = lambda: popupmsg('Not supported just yet!'))
        homemenu.add_command(label='Save',command = lambda: popupmsg('Not supported just yet!'))
        homemenu.add_command(label='Save as...',command = lambda: popupmsg('Not supported just yet!'))
        homemenu.add_separator() # Separator baselr.
        homemenu.add_command(label='Open Project...',command = lambda: popupmsg('Not supported just yet!'))
        homemenu.add_command(label='Export as...',command = lambda: popupmsg('Not supported just yet!'))
        homemenu.add_separator() # Separator bar.
        homemenu.add_command(label='Exit',command = quit)
        menubar.add_cascade(label='Home',menu = homemenu)

        # CLIENT CHOICES:
        exchangeChoice = tk.Menu(menubar, tearoff = 1)
        exchangeChoice.add_command(label='IXIC_2019',
                                     command = lambda: changeExchange("IXIC_2019","ixic_2019")) # ChangeExchange, display BTCE-e , read as btce.
        exchangeChoice.add_command(label='Bitfinex',
                                     command = lambda: changeExchange("Bitfinex","bitfinex")) # ChangeExchange, display BTCE-e , read as btce.
        exchangeChoice.add_command(label='Bitstamp',
                                     command = lambda: changeExchange("Bitstamp","bitstamp")) # ChangeExchange, display BTCE-e , read as btce.
        menubar.add_cascade(label='Edit',menu = exchangeChoice)

        # TIME FRAME OF DATA:
        dataTF = tk.Menu(menubar, tearoff = 1)
        dataTF.add_command(label = 'Real Time', 
                        command = lambda: changeTimeFrame('live'))

        dataTF.add_command(label = '1 Day', 
                        command = lambda: changeTimeFrame('D'))
        dataTF.add_command(label = '3 Week', 
                        command = lambda: changeTimeFrame('W'))
        dataTF.add_command(label = 'Weekdays', 
                        command = lambda: changeTimeFrame('B'))

        menubar.add_cascade(label = 'Data Time Frame' , menu = dataTF)

        # Which kind of data are we looking at ? 
        OHLCI = tk.Menu(menubar, tearoff = 1)
        OHLCI.add_command(label = 'Live', 
                        command = lambda: changeTimeFrame('live'))
        OHLCI.add_command(label = '1 Iteration', 
                        command = lambda: changeSampleSize('1Mimatplotlib graph optionsn',0.0005)) # Min and width of the candles.
        OHLCI.add_command(label = '10 Iterations', 
                        command = lambda: changeSampleSize('5Min',0.003)) # Min and width of the candles
        OHLCI.add_command(label = '100 Iterations', 
                        command = lambda: changeSampleSize('15Min',0.008)) # Min and width of the candles
        OHLCI.add_command(label = '500 Iterations', 
                        command = lambda: changeSampleSize('30Min',0.016)) # Min and width of the candles
        OHLCI.add_command(label = '1000 Iterations', 
                        command = lambda: changeSampleSize('1H',0.032)) # Min and width of the candles
        OHLCI.add_command(label = '+1000 Iterations', 
                        command = lambda: changeSampleSize('3H',0.096)) # Min and width of the candles
        
        menubar.add_cascade(label = 'Iteration Interval', menu = OHLCI)



        tradeButton = tk.Menu(menubar, tearoff = 1)
        tradeButton.add_command(label = 'Manual F.P.M',
                                command = lambda: popupmsg('This is not live yet'))

        tradeButton.add_command(label = 'Automated F.P.M',
                                command = lambda: popupmsg('This is not live yet'))
        tradeButton.add_separator()


        tradeButton.add_command(label = 'Lambda',
                                command = lambda: popupmsg('This is not live yet'))
        tradeButton.add_command(label = 'Theta',
                                command = lambda: popupmsg('This is not live yet'))
        tradeButton.add_separator()

        tradeButton.add_command(label = 'Set-Up Quick Lambda/Theta changes',
                                command = lambda: popupmsg('This is not live yet'))

        menubar.add_cascade(label='F.P.M', menu = tradeButton)

        ##### BEING ABLE TO FREEZE THE UPDATE WHEN ZOOMING!
        startStop = tk.Menu(menubar, tearoff = 1)
        startStop.add_command(label = 'Resume',
                                command = lambda: loadChart('start'))
        startStop.add_command(label = 'Pause',
                                command = lambda: loadChart('stop'))
        menubar.add_cascade(label='Resume/Pause Client', menu = startStop) 

        colorMenu = tk.Menu(menubar, tearoff = 0)
        colorMenu.add_command(label='Classic',
                                command = lambda: changeColor('classic'))
        colorMenu.add_command(label = 'Night Mode',
                                command = lambda: changeColor('dark_background'))
        colorMenu.add_command(label = 'Day mode',
                                command = lambda: changeColor('ggplot'))
        colorMenu.add_command(label = 'Bmh',
                                command = lambda: changeColor('bmh'))

        menubar.add_cascade(label = 'Graph Visualization', menu = colorMenu)
                                

        ##### HELP MENU:
        helpmenu = tk.Menu(menubar, tearoff = 0)
        helpmenu.add_command(label='Tutorial', command = tutorial)
        menubar.add_cascade(label='Help', menu = helpmenu)

        tk.Tk.config(self, menu = menubar)

        # **** The Toolbar ****
        toolbar = tk.Frame(self, background='darkcyan')
        insertButt = tk.Button(toolbar, text='Close KORALI', command=quit)
        insertButt.config(bd = 2)
        insertButt.pack(side='right',padx=2,pady=2) # Padding options.

        #printButt = ttk.Button(toolbar, text='Function2', command=doNothing)
        #printButt.pack(side='left',padx=2,pady=2) # Padding options.
        
        toolbar.pack(side='bottom', fill='x')



        # Which frame shall I show?
        self.frames = {} # Dictionary.


        frame = KORALI_Page(container,self) #Pass through container, and self.
        self.frames[KORALI_Page] = frame 
        frame.grid(row=0, column=0, sticky='nsew') # Sticky = Strech everything to north,south,e,w..

        self.show_frame(KORALI_Page)

        # Done with initializing.

        #icon = PhotoImage(file='/home/mark/Escritorio/PYTHON/korali_no_env/logo.ico')   
        #self.call('wm', 'iconphoto', root._w, icon)

    def show_frame(self,cont): # Cont = controler.
        frame = self.frames[cont]
        frame.tkraise() # Raise it to the front!
        
        ####3 *************** SEPARATOR

        ######### INDIVIDUAL TABS #############


        #tk.Tk.iconbitmap(self, default="clienticon.png")
        self.minsize(600,400)
        


class KORALI_Page(tk.Frame): # Page with Graphs.
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        # ************** TABS **********************
        totalTabs = ttk.Notebook(self)

        tab1 = tk.Frame(totalTabs)
        totalTabs.add(tab1, text = "Korali")
        leftFrame = ttk.Frame(tab1)
        leftFrame.grid(column = 0, row = 0, sticky = 'nsew',)
        sep = tk.Frame(tab1, width=4, bd=2, relief='sunken')
        sep.grid(column = 1,row = 0, sticky = 'ns')
        rightFrame = ttk.Frame(tab1)
        rightFrame.grid(column = 2, row = 0, sticky = 'nsew')

        # Make frames same width:
        tab1.grid_columnconfigure(0, weight=1, uniform="group1")
        tab1.grid_columnconfigure(2, weight=1, uniform="group1")
        #parent.grid_rowconfigure(0, weight=1)

        
        # LEFT SIDE OF TAB1:
        '''
        labels = ['Name: ','Type: ','Default: ','Description: ']

        for it in range(len(labels)):
            cur_label = tk.Label(labelframe, text = labels[it])
            cur_label.grid(row=it+1,column=0, sticky='NE')
        '''
        variablesname=tk.Label(leftFrame, text="VARIABLES", font="Arial 20")
        variablesname.grid(row=0, column=2,pady = 30)
        variablesname.config(fg=extraColor)

        '''
        logoutBtn = Button(leftFrame, text = "Logout",width=15, height=2,command=lambda:LogOut())
        logoutBtn.grid(row=1, column=4,pady=(10,0))
        '''
        # LABELS:
        itemLabel = Label(leftFrame, text="Experiment Name:")
        itemLabel.grid(row=1, column=0, padx=(5,0),pady=(10,0), sticky ='E')
        itemLabel.config(font= HUGE_FONT)

        rateLabel= Label(leftFrame, text="Type:")
        rateLabel.grid(row=1, column=2, padx=(10,0), pady=(10,0), sticky = 'E')
        rateLabel.config(font=HUGE_FONT)

        quantityLabel = Label(leftFrame, text="Default:")
        quantityLabel.grid(row=2, column=0,padx=(5,0),pady=(10,0), sticky = 'E')
        quantityLabel.config(font=HUGE_FONT)

        costLabel= Label(leftFrame, text="Description:")
        costLabel.grid(row=2, column=2, padx=(10,0), pady=(10,0), sticky = 'E')
        costLabel.config(font = HUGE_FONT)

        #itemValue = Label(leftFrame, text = experimentname)
        #itemValue.grid(row=1, column = 1, padx = 10, pady =10)
        #itemValue.config(font= RES_FONT)
        #rateValue = Label(leftFrame, text =rateVar)
        #rateValue.grid(row=1, column=3, padx=(10,0), pady=(10,0))
        #rateValue.config(font = RES_FONT)
        #rateValue = Label(leftFrame, textvariable=rateVar)
        #rateValue.grid(row=1, column=3, padx=(10,0), pady=(10,0))
        #quantityEntry=Entry(leftFrame, textvariable=quantityVar)
        #quantityEntry.grid(row=2, column=1,padx=(5,0),pady=(10,0))
        #costEntry=Entry(leftFrame, textvariable=costVar)
        #costEntry.grid(row=2, column=3, padx=(10,0), pady=(10,0))

        # ENTRIES:
        
        itemEntry = Entry(leftFrame)
        itemEntry.grid(row = 1, column = 1, padx=10, pady = 10)
        
        rateEntry = Entry(leftFrame, textvariable = typeVar)
        rateEntry.grid(row=1, column = 3, pady=10, padx=10, sticky = 'W')

        quantityEntry=Entry(leftFrame, textvariable =defaultVar)
        quantityEntry.grid(row=2, column=1,padx=(5,0),pady=(10,0))

        costEntry=Entry(leftFrame, textvariable =descriptionVar, width = 38)
        costEntry.grid(row=2, column=3, padx=(10,0), pady=(10,0), columnspan=2)

        itemEntry.insert(END,nameVar)
        rateEntry.insert(END,typeVar)
        quantityEntry.insert(END,defaultVar)
        costEntry.insert(END,descriptionVar)

        ############ JSON MANIPULATION + CASCADE-TREE ###################

        # Import json file into variable data:
        with open('../../source/experiment/experiment.config') as jsonfile:
            data = json.load(jsonfile)

        #Experiments = []
        Names = []
        Types = []
        Defaults =[]
        Descriptions = []
        default_counter = 0

        for key in data.keys():
            if key == 'Configuration Settings':
                for it in range(0,len(data[key])):
                    Experiment = data[key][it]           
                    for option in Experiment.keys():
                        var = Experiment[option]
                        if option == 'Options':
                            continue
                        if option == 'Name':
                            Names.append(var)
                        elif option == 'Type':
                            Types.append(var)
                        elif option == 'Default':
                            Defaults.append(var)
                            default_counter = 1
                        elif option == 'Description':
                            if default_counter == 0:
                                Defaults.append('0')
                                Descriptions.append(var)
                            else:
                                Descriptions.append(var)
                                default_counter = 0
                        #Experiments.append(var)
            else:
                pass #print('Not yet')
        
        '''
        # create a treeview with scrollbar
        tree = ttk.Treeview(leftFrame,columns=element_header, show="headings")
        vsb = ttk.Scrollbar(leftFrame,orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        tree.grid(column=1, row=8, sticky='nsew')
        vsb.grid(column=2, row=8, sticky='ns')
        tree.grid_columnconfigure(0, weight=1)
        vsb.grid_rowconfigure(0, weight=1)
        tree.bind( "<Double-Button-1>", OnClick)
       
        
        for col in element_header:
            tree.heading(col, text=col.title(),
                command=lambda c=col: sortby(tree, c, 0))
            # adjust the column's width to the header string
            tree.column(col, width=60)
        for item in element_list:
            tree.insert('', 'end', values=item)
        '''


                
        menubutton = tk.Menubutton(leftFrame, text = varmenubutton,indicatoron=True,borderwidth=1, relief="raised", width=20, border=3)
        main_menu = tk.Menu(menubutton, tearoff=False)
        menubutton.configure(menu=main_menu)

        n = len(Names)

        for num in range(0,n):
            menu = tk.Menu(main_menu, tearoff=False)
            main_menu.add_cascade(label=Names[num], menu=menu)
            menu.add_radiobutton(value=Types[num], label=[Types[num]+', '+Defaults[num]+', '+Descriptions[num]], variable=Types[num],
                                                    command = lambda: printExperiment(),indicatoron = 0)
                

        menubutton.grid(row=8, column = 0, pady=10, padx=10)
        



        '''
        tv = ttk.Treeview(leftFrame)
        tv.grid(row=8,column=0, pady=10, padx=10)

        # Create first names:
        for it in range(0,len(Names)):
            tv.insert('',str(it),'item '+str(it),text = Names[it])

        for it in range(0,len(Names)):
            tv.insert('item '+str(it),str(it),str(it),text = Types[it])

        for it in range(0,len(Names)):
            tv.insert('item '+str(it),str(it),str(it),text = Defaults[it])
        '''
        
        # BUTTONS:

        buttonBill = Button(leftFrame, text=" + ", width =5,border = 3,command=lambda:generate_bill())
        buttonBill.grid(row=5, column=0,padx=(5,0),pady=(10,0))

        addNewItem = Button(leftFrame, text="Add Experiment", width=15, height=2,relief = 'raised', border = 3, command=lambda: itemAddWindow(leftFrame))
        addNewItem.grid(row=7, column=3, padx=(10,0),pady=(10,0), sticky='W', columnspan = 2)
        updateItem = Button(leftFrame, text="Update Experiment", width=15, height=2, border = 3 ,relief ='raised', command=lambda: moveToUpdate())
        updateItem.grid(row=8, column=3, padx=(10,0), pady=(10,0), sticky='W', columnspan = 2)

        showallEntry= Button(leftFrame, text="Show Selected", width=15, height=2, border = 3 , relief = 'raised',command=lambda:movetoBills())
        showallEntry.grid(row=9, column=3, padx=(10,0), pady=(10,0), sticky = 'W', columnspan=2)

    
        ## RIGHT FRAME:

        billLabel=Label(rightFrame, text="Experiments Chosen", font="Arial 20")
        billLabel.grid(row=0, column=2,pady = 30)

        billsTV = ttk.Treeview(rightFrame,height=15, columns=('Rate','Quantity','Cost'))

        billsTV.grid(row=1, column=0, columnspan=5, padx = 20)

        scrollBar = Scrollbar(rightFrame, orient="vertical",command=billsTV.yview)
        scrollBar.grid(row=2, column=4, sticky="NSE")
        
        billsTV.configure(yscrollcommand=scrollBar.set)

        billsTV.heading('#0',text="Name")
        billsTV.column('#0', width= 200)
        billsTV.heading('#1',text="Type")
        billsTV.column('#1', width = 200)
        billsTV.heading('#2',text="Default")
        billsTV.column('#2', width = 100)
        billsTV.heading('#3',text="Description")
        billsTV.column('#3', width = 340)
        
        totalCostLabel = Label(rightFrame, textvariable=totalCostVar)
        totalCostLabel.grid(row=3,column=1)
        generateBill = Button(rightFrame, text="Generate Graph",width=15, border = 3,relief = 'raised', command = lambda:print_bill())
        generateBill.grid(row=3,column=4)


###################
###################


        ## **** TAB 2 ***********
        tab2 = ttk.Frame(totalTabs)
        totalTabs.add(tab2, text = "On-live PLOTS")
        label = ttk.Label(tab2, text ="GRAPH PAGE", font = LARGE_FONT) # Running the initialization.
        # Add it to our windows.
        label.pack(pady=10,padx=10) # Padding so it looks better, not full.

        seconds = StringVar(tab2,value="Updating Graph every...")
        question_menu = tk.OptionMenu(tab2,seconds, *questions_seconds)
        question_menu.pack(pady =10,padx = 100, side = 'top')
        question_menu.config(font = LARGE_FONT, width = 35, highlightcolor = 'darkcyan')
       

        # Background:


        #Bring it to the front: plt.show() in matplotlib
        canvas = FigureCanvasTkAgg(f, tab2)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand = True)

        #Navigation Bar:
        toolbar = NavigationToolbar2Tk(canvas,tab2)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand = True)

        status = tk.Label(tab2,text='                                                                                                  Korali is updating the plot every '+str(UpdateInterval)+' seconds...                                                :)',
                                borderwidth=1, relief='sunken',anchor='w') # Border
        status.pack(side='bottom',fill='x')


        ## **** TAB 3 and rest ********
        tab3 = ttk.Frame(totalTabs)
        totalTabs.add(tab3, text = "Tab3")
        tab4 = ttk.Frame(totalTabs)
        totalTabs.add(tab4, text = "Tab4")
        tab5 = ttk.Frame(totalTabs)
        totalTabs.add(tab5, text = "Tab5")
        tab6 = ttk.Frame(totalTabs)
        totalTabs.add(tab6, text = "TAaaaaaaaaaaaaaaaaaaaaab6")
        tab7 = ttk.Frame(totalTabs)
        totalTabs.add(tab7, text = "T_230i-")



        totalTabs.pack(expand = 1, fill = "both")

        # **** Status Bar ****
        # Background:

## --------------- END OF CLASSES ------------------------    
########################################################    





app = KORALI()
app.geometry("1780x820") # Size of our application.

# f = figure ( its at the beggining of the file)
# interval = how long until you want to run it again, its in miliseconds. 1000 = 1 sec.
ani = animation.FuncAnimation(f,animate, interval = UpdateInterval*1000 )
app.mainloop()



