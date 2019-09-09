#! /usr/bin/env python3

import json
import numpy as np
import matplotlib.pyplot as plt

from korali.auxiliars.fileIO import *
from korali.plotter.helpers import hlsColors, pauseLight, drawMulticoloredLine, checkFigure
from korali.plotter.helpers import verifyGeneration, initDefaults, getStateAndGeneration, appendStates, appendStateVectors


# Plot TMCMC results (read from .json files)
def plot(src, plotAll=False, live=False, generation=None, test=False, mean=''):
    plt.style.use('seaborn-dark')
        
    verifyGeneration(generation, 1)

    resultfiles = getResultFiles(src, 1, generation)
    if (resultfiles == []):
     print("[Korali] Error: Did not find Korali results in the folder...".format(src))
     exit(-1)
 
    if (plotAll == False):
        resultfiles = [resultfiles[-1]]

    samples = []
    solverName, names, numdim, gen = initDefaults(src, "initial.json", [samples])
 
    while True: 
        
        for filename in resultfiles:
            path   = '{0}/{1}'.format(src, filename)
         
            fig, ax = plt.subplots(numdim, numdim, figsize=(8,8))
            
            updateLegend = live or plotAll
            if (updateLegend):
                fig.show()
        
            with open(path) as f:
                data    = json.load(f)
                
                state, gen = getStateAndGeneration(data)
                anneal = float(data['Solver']['Internal']['Annealing Exponent'])
                populationSize = int(data['Solver']['Population Size'])
        
                if updateLegend:
                    checkFigure(fig.number)
         
                samples = np.reshape( data['Solver']['Internal']['Sample Database'], (populationSize,numdim) )
                plot_samples(ax, gen, populationSize, anneal, samples)
        
        if (live == False):
            break
        
        resultfiles = getResultFiles(src, gen, generation, False)
        if (resultfiles == []):
         print("[Korali] Error: Did not find Korali results in the folder...".format(src))
         exit(-1)

    checkFigure(fig.number)
    plt.show()
    print("[Korali] Figures closed - Bye!")


# General plotting function
def plot_samples(ax, gen, numentries, anneal, samples): 
    plt.suptitle( 'TMCMC\nGeneration {0}\n' \
            'Number of Samples {1}\n' \
            '(Annealing Exponent {2:.3e})'.format(str(gen), \
            str(numentries), anneal), fontweight='bold', fontsize  = 12 )

    plot_histogram(ax, samples)
    plot_upper_triangle(ax, samples, False)
    plot_lower_triangle(ax, samples)
    pauseLight(0.05) 


# Plot histogram of sampes in diagonal
def plot_histogram(ax, theta):
    dim = theta.shape[1]
    num_bins = 50
    for i in range(dim):

        if (dim == 1): 
            ax_loc = ax
        else: 
            ax_loc = ax[i,i]
 
        hist, bins, _ = ax_loc.hist(theta[:, i], num_bins, density=True,
                                    color='lightgreen', ec='black')
        
        if i == 0:
           
            # Rescale hist to scale of theta -> get correct axis titles
            widths = np.diff(bins)
            if (dim > 1) :  
                hist = hist / np.max(hist) * (ax_loc.get_xlim()[1] -
                                                ax_loc.get_xlim()[0])
                bottom = ax_loc.get_xlim()[0]
                ax_loc.cla()
                ax_loc.bar(bins[:-1], hist, widths,
                    color='lightgreen', ec='black', bottom=bottom)
                ax_loc.set_ylim(ax_loc.get_xlim())
                ax_loc.set_xticklabels([])
            else:
                ax_loc.cla()
                ax_loc.bar(bins[:-1], hist, widths,
                     color='lightgreen', ec='black')

        elif i == theta.shape[1] - 1:
            ax_loc.set_yticklabels([])
        
        else:
            ax_loc.set_xticklabels([])
            ax_loc.set_yticklabels([])
        ax_loc.tick_params(axis='both', which='both', length=0)


#Plot scatter plot in upper triangle of figure
def plot_upper_triangle(ax, theta, lik=False):
    dim = theta.shape[1]
    if (dim == 1): return
    
    for i in range(dim):
        for j in range(i + 1, dim):
            if lik:
                ax[i, j].scatter(theta[:, j], theta[:, i], marker='o', s=10,
                    c=theta, alpha=0.5)
            else:
                ax[i, j].plot(theta[:, j], theta[:, i], '.', markersize=1)
            ax[i, j].set_xticklabels([])
            ax[i, j].set_yticklabels([])
            ax[i, j].grid(b=True, which='both')


#Plot 2d histogram in lower triangle of figure
def plot_lower_triangle(ax, theta):
    dim = theta.shape[1]
    if (dim == 1): return

    for i in range(dim):
        for j in range(i):
            # returns bin values, bin edges and bin edges
            H, xe, ye = np.histogram2d(theta[:, j], theta[:, i], 10, density=True)
            # plot and interpolate data
            ax[i, j].imshow(H.T, aspect="auto", interpolation='spline16',
                            origin='lower', extent=np.hstack((
                                                ax[j, j].get_xlim(),
                                                ax[i, i].get_xlim())),
                                                cmap=plt.get_cmap('jet'))
            
            if i < theta.shape[1]-1:
                ax[i, j].set_xticklabels([])
            if j > 0:
                ax[i, j].set_yticklabels([])
