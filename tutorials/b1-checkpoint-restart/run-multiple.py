#!/usr/bin/env python3

# In this example, we demonstrate how a Korali experiment can
# be resumed from any point (generation). This is a useful feature
# for continuing jobs after an error, or to fragment big jobs into
# smaller ones that can better fit a supercomputer queue.

# First, we run a simple Korali experiment.

import sys
sys.path.append('model')
from model import *

import korali
k = korali.initialize()

k["Problem"]["Type"] = "Evaluation/Direct/Basic"
k["Problem"]["Objective"] = "Maximize"
k["Problem"]["Objective Function"] = model

k["Solver"]["Type"] = "Optimizer/CMAES"
k["Solver"]["Population Size"] = 5
k["Solver"]["Termination Criteria"]["Max Generations"] = 50
k["Solver"]["Termination Criteria"]["Generations Per Run"] = 25
k["Solver"]["Console Frequency"] = 10

k["Variables"][0]["Name"] = "X"
k["Variables"][0]["Lower Bound"] = -10.0
k["Variables"][0]["Upper Bound"] = +10.0

k["Result Path"] = '_result_run-multiple'
k["Solver Count"] = 8

print('------------------------------------------------------')
print('Now running first 25 generations...')
print('------------------------------------------------------')

k.run()

print('------------------------------------------------------')
print('Now running last 25 generations...')
print('------------------------------------------------------')

k.run()
