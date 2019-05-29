#!/usr/bin/env python3
import sys
sys.path.append('./model')
from directModel import *
import korali

k = korali.Engine()

k["Seed"] = 0xC0FFEE;
k["Verbosity"] = "Detailed"

k["Problem"]["Type"] = "Direct"
k["Problem"]["Variables"][0]["Name"] = "X"
k["Problem"]["Variables"][0]["Distribution"] = "Uniform"
k["Problem"]["Variables"][0]["Minimum"] = -10.0
k["Problem"]["Variables"][0]["Maximum"] = +10.0

k["Solver"]["Method"] = "TMCMC"
k["Solver"]["Covariance Scaling"] = 0.02
k["Solver"]["Population Size"] = 50000
k["Solver"]["Coefficient of Variation"] = 0.5;
k["Solver"]["Burn In"] = 5

k.run(evaluateModel)