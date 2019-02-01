#ifndef _KORALI_H_
#define _KORALI_H_

#include "dimension.h"

namespace Korali
{

class KoraliBase
{
  public:

  // Public Methods
  KoraliBase(size_t dim, double (*fun) (double*, int), size_t seed);

  double getTotalDensityLog(double* x);
  double getTotalDensity(double* x);

  Dimension* getDimension(int dim);
  Dimension* operator[] (int x);
  void setMaxFitnessEvaluations(size_t maxFitnessEvaluations);
  void setMaxGenerations(size_t maxGenerations);

  void setLambda(size_t lambda);
  void setMu(size_t mu, std::string type = "Logarithmic");
  void setMuCovariance(double muCovariance);
  void setSigmaCumulationFactor(double sigmaCumulationFactor);
  void setDampingFactor(double dampFactor);
  void setCumulativeCovariance(double cumulativeCovariance);
  void setCovarianceMatrixLearningRate(double covarianceMatrixLearningRate);
  void setDiagonalCovarianceMatrixEvalFrequency(size_t diagonalCovarianceMatrixEvalFrequency);
  void setCovarianceEigensystemEvaluationFrequency(size_t covarianceEigensystemEvaluationFrequency);

  void setStopFitnessEvalThreshold(double stopFitnessEvalThreshold);
  void setStopFitnessDiffThreshold(double stopFitnessDiffThreshold);
  void setStopFitnessDiffHistoryThreshold(double stopFitnessDiffHistoryThreshold);
  void setStopMinDeltaX(double stopMinDeltaX);
  void setStopMaxStdDevXFactor(double stopMaxStdDevXFactor);
  void setStopMaxTimePerEigenDecomposition(double stopMaxTimePerEigendecomposition);
  void setStopMinFitness(double _stopMinFitness);

  void run();

  private:

  // Dimesion, Fitness, and Distribution Variables
	size_t _seed;
	size_t _dimCount;
  Dimension* _dims;
  Distribution* _gaussianGenerator;

  double (*_fitnessFunction) (double*, int);
  double* _fitnessVector;
  double** _samplePopulation;

  // Configuration Variables

  double* _muWeights;
  double _muEffective;
  double _muCovariance;
  double _sigmaCumulationFactor;
  double _dampFactor;
  double _cumulativeCovariance;
  double _covarianceMatrixLearningRate;

  size_t _maxFitnessEvaluations;   // Defines maximum number of fitness evaluations
  size_t _maxGenerations; // Defines maximum number of generations
  size_t _lambda; // Number of offspring per sample cycle
  size_t _mu;
  size_t _diagonalCovarianceMatrixEvalFrequency;
  size_t _covarianceEigensystemEvaluationFrequency;

  // Stop conditions
  double _stopFitnessEvalThreshold; // Defines minimum function value below which it stops
  double _stopFitnessDiffThreshold; // Defines minimum function value differences before stopping
  double _stopFitnessDiffHistoryThreshold; // Defines minimum function value differences among best values before stopping
  double _stopMinDeltaX; // Defines minimum delta of input parameters among generations before it stops.
  double _stopMaxStdDevXFactor; // Defines maximum standard deviation before it stops.
  double _stopMaxTimePerEigendecomposition; // Defines maximum time to be spent on eigensystem decomposition
  double _stopMinFitness; // Defines the minimum fitness allowed, otherwise it stops

  // Private CMAES-Specific Variables
  double sigma;  /* step size */

  double *rgxmean;  /* mean x vector, "parent" */
  double *rgxbestever;
  double **rgrgx;   /* range of x-vectors, lambda offspring */
  int *index;       /* sorting index of sample pop. */
  double *arFuncValueHist;

  double chiN;
  double **C;  /* lower triangular matrix: i>=j for C[i][j] */
  double **B;  /* matrix with normalize eigenvectors in columns */
  double *rgD; /* axis lengths */

  double *rgpc;
  double *rgps;
  double *rgxold;
  double *rgout;
  double *rgBDz;   /* for B*D*z */
  double *rgdTmp;  /* temporary (random) vector used in different places */
  double *rgFuncValue;

  double gen; /* Generation number */
  double countevals;
  double state; /* 1 == sampled, 2 == not in use anymore, 3 == updated */

  double maxdiagC; /* repeatedly used for output */
  double mindiagC;
  double maxEW;
  double minEW;

  short flgEigensysIsUptodate;
  double genOfEigensysUpdate;
  double dMaxSignifKond;


  // Private CMAES-Specific Methods

  double** cmaes_SamplePopulation();
  double** cmaes_ReSampleSingle(int iindex);
  double* cmaes_SampleSingleInto(double *rgx);
  double* cmaes_UpdateDistribution(int save_hist, const double *rgFunVal);
  void Adapt_C2(int hsig);
  void TestMinStdDevs();
  void cmaes_PrintResults();
  double function_value_difference();
  bool cmaes_TestForTermination();
  void cmaes_UpdateEigensystem(int flgforce);
  void Eigen( int N,  double **C, double *diag, double **Q);
  int MaxIdx(const double *rgd, int len);
  int MinIdx(const double *rgd, int len);
  void Sorted_index(const double *rgFunVal, int *iindex, int n);

  double doubleRangeMax(const double *rgd, int len);
  double doubleRangeMin(const double *rgd, int len);
  void initializeInternalVariables();

  int is_feasible(double *pop);
  double evaluate_population();
};

} // namespace Korali

#endif // _KORALI_H_
