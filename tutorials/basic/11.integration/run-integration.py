#!/usr/bin/env python3
import os
import sys
sys.path.append('./model/')
from integrand import *
import numpy as np

# Variables
x = np.linspace (0.0,5.0, 100, dtype=np.float64) #grid for quadrature

# Creating new experiment
import korali
e = korali.Experiment()

e["Problem"]["Type"] = "Integration"
e["Problem"]["Integrand"] = lambda modelData: integrand(modelData)
e["Variables"][0]["Name"] = "x"
e["Variables"][0]["Sample Points"] = x.tolist()
e["Variables"][0]["Integration Method"] = "Rectangle" #"Trapezoidal", "Simpson", "MonteCarlo", "Custom"
#e["Variables"][0]["Lower Bound"] = 0.0
#e["Variables"][0]["Upper Bound"] = 5.0
e["Solver"]["Type"] = "Integrator"
#e["Solver"]["Executions Per Generation"] = 0
e["Console Output"]["Verbosity"] = "Detailed"

# Starting Korali's Engine and running experiment
k = korali.Engine()
k.run(e)
