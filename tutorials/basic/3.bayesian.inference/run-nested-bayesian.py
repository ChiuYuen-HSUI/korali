#!/usr/bin/env python3

# In this example, we demonstrate how Korali samples the posterior distribution
# in a bayesian problem where the likelihood is calculated by providing
# reference data points and their objective values.

# Importing the computational model
import sys
sys.path.append('./model')
from model import *

# Creating new experiment
import korali
e = korali.Experiment()

# Setting up the reference likelihood for the Bayesian Problem
e["Problem"]["Type"] = "Bayesian/Reference"
e["Problem"]["Likelihood Model"] = "Additive Normal"
e["Problem"]["Reference Data"] = getReferenceData()
e["Problem"]["Computational Model"] = lambda sampleData: model(sampleData, getReferencePoints())

# Configuring Nested Sampling parameters
e["Solver"]["Type"] = "Nested"
e["Solver"]["Number Live Points"] = 1500
e["Solver"]["Batch Size"] = 1
e["Solver"]["Covariance Scaling"] = 1.0
e["Solver"]["Add Live Points"] = True
e["Solver"]["Resampling Method"] = "Ellipse"


# Configuring the problem's random distributions
e["Distributions"][0]["Name"] = "Uniform 0"
e["Distributions"][0]["Type"] = "Univariate/Uniform"
e["Distributions"][0]["Minimum"] = -5.0
e["Distributions"][0]["Maximum"] = +5.0

e["Distributions"][1]["Name"] = "Uniform 1"
e["Distributions"][1]["Type"] = "Univariate/Uniform"
e["Distributions"][1]["Minimum"] = -5.0
e["Distributions"][1]["Maximum"] = +5.0

e["Distributions"][2]["Name"] = "Uniform 2"
e["Distributions"][2]["Type"] = "Univariate/Uniform"
e["Distributions"][2]["Minimum"] = 0.0
e["Distributions"][2]["Maximum"] = +5.0

# Configuring the problem's variables and their prior distributions
e["Variables"][0]["Name"] = "a"
e["Variables"][0]["Prior Distribution"] = "Uniform 0"

e["Variables"][1]["Name"] = "b"
e["Variables"][1]["Prior Distribution"] = "Uniform 1"

e["Variables"][2]["Name"] = "[Sigma]"
e["Variables"][2]["Prior Distribution"] = "Uniform 2"


e["File Output"]["Frequency"] = 0
e["Console Output"]["Frequency"] = 500
e["Solver"]["Termination Criteria"]["Max Generations"] = 100000
e["Solver"]["Termination Criteria"]["Max Effective Sample Size"] = 10000
e["Solver"]["Termination Criteria"]["Max Gain Factor"] = 1e-9

# Starting Korali's Engine and running experiment
k = korali.Engine()
k.run(e)
