// In this example, we demonstrate how Korali finds values for the
// variables that maximize the objective function, given by a
// user-provided computational model.

#include "korali.h"
#include "model/evaluateModel.h"

int main(int argc, char* argv[])
{
  // Starting Korali's Engine
  auto k = Korali::Engine();

  // Setting computational model
  k.setModel([](Korali::Model& d) { evaluateModel(d.getVariables(), d.getResults()); });

  // Selecting problem and solver types.
  k["Problem"] = "Optimization";
  k["Solver"]  = "DEA";
  k["Seed"]    = 31415;

  // Defining the problem's variables and their CMA-ES bounds.
  k["Variables"][0]["Name"] = "X";
  k["Variables"][0]["DEA"]["Lower Bound"] = -10.0;
  k["Variables"][0]["DEA"]["Upper Bound"] = +10.0;

  // Configuring CMA-ES parameters
  k["DEA"]["Objective"] = "Maximize";
  k["DEA"]["Sample Count"] = 32;

  k["DEA"]["Termination Criteria"]["Max Generations"]["Value"] = 500;

  // Setting output directory
  k["Result Directory"] = "_a1_optimization_dea_result";

  // Running Korali
  k.run();

}
