#ifndef _TMCMC_H_
#define _TMCMC_H_

#include "base.h"
#include "distribution.h"

namespace Korali
{

struct optim_options {
    size_t MaxIter;             /* Max number of search iterations */
    double Tol;                 /* Tolerance for root finding */
    bool    Display;             /* Print output */
    double Step;                /* Search stepsize */
    double LowerBound;          /* Lower bound for root finding (fmincon & fzerosearch)*/
    double UpperBound;          /* Upper bound for root finding (fmincon & fzerosearch)*/
};

typedef struct data_t {
    int MaxStages;                  /* Max number of tmcmc generations */
    int nChains;

    double *compositeprior_distr;   /*[PROBDIM]*/

    double *prior_mu;
    double *prior_sigma;

    int    auxil_size;
    double *auxil_data;

    int MinChainLength;         /* MinChainLength > 0: setting MinChainLength */
    int MaxChainLength;         /* MaxChainLength > 0: splitting long chains */

    double lb, ub;              /* generic lower and upper bound*/

    double TolCOV;              /* Target coefficient of variation of weights */
    double MinStep;             /* Min update of rho */
    double bbeta;               /* Covariance scaling parameter */
    int    burn_in;             /* Number of burn in iterations */

    optim_options options;      /* Optimization options (see above) */

    int prior_type;             /* 0: uniform, 1: gaussian, 3: composite */

    int *Num;               /*[MAXGENS];*/
    int    use_proposal_cma;
    double **init_mean;     /* [DATANUM][PROBDIM] */
    double **local_cov;     /* [DATANUM][PROBDIM*PROBDIM] */
    bool use_local_cov;
    double local_scale;
} data_t;


typedef struct runinfo_t {
    int    Gen;
    double *CoefVar;        /*[MAXGENS];*/
    double *p;              /*[MAXGENS];*/
    int    *currentuniques; /*[MAXGENS];*/
    double *logselections;  /*[MAXGENS];*/
    double *acceptance;     /*[MAXGENS];*/
    double **SS;            /*[PROBDIM][PROBDIM];*/
    double **meantheta;     /*[MAXGENS][PROBDIM]*/
} runinfo_t;


typedef struct cgdbp_s {
    double *point;      /*[PROBDIM];*/
    double F;
    double prior;

    int counter;        /* not used (?)*/
    int nsel;           /* for selection of leaders only*/
    int queue;          /* for submission of leaders only*/
    int surrogate;      //TODO: used? (DW)
    double error;       //TODO: used? (DW)

    int error_flg;
    int posdef;         //TODO: can we combine this with error_flg? (DW)
    double *gradient;   /*[PROBDIM]*/
    double *cov;        /*[PROBDIM]*/
    double *evec;       /*[PROBDIM][PROBDIM]*/
    double *eval;       /*[PROBDIM]*/
} cgdbp_t;


typedef struct cgdb_s {
    int     entries;
    cgdbp_t *entry;     /*[MAX_DB_ENTRIES];*/
    pthread_mutex_t m;
} cgdb_t;


typedef struct dbp_s {
    double *point; /*[PROBDIM];*/
    double F;
    int    nG;
    double G[64];    /* maxG*/
    int    surrogate;
} dbp_t;


typedef struct db_s {
    int   entries;
    dbp_t *entry; /*[MAX_DB_ENTRIES];*/        /* */
    pthread_mutex_t m;
} db_t;


typedef struct resdbp_s {
    double *point;    /*[EXPERIMENTAL_RESULTS+1]; // +1 for the result (F)*/
    double F;
    int counter;    /* not used (?)*/
    int nsel;    /* for selection of leaders only*/
} resdbp_t;


typedef struct resdb_s {
    int      entries;
    resdbp_t *entry; /*[MAX_DB_ENTRIES];*/
    pthread_mutex_t m;
} resdb_t;


typedef struct fparam_s {
    const double *fj;
    int           fn;
    double        pj;
    double        tol;
} fparam_t;


typedef struct sort_s {
    int idx;
    int nsel;
    double F;
} sort_t;

class KoraliTMCMC : public KoraliBase
{
  public:

	// TMCMC Fields
  data_t    data;
  runinfo_t runinfo;
  cgdbp_t *leaders;

  db_t    full_db;
  cgdb_t  curgen_db;
  resdb_t curres_db;

  // Public Methods
	KoraliTMCMC(Problem* problem, MPI_Comm comm);

	// TMCMC Configuration Methods
	void setMaxStages(int MaxStages) { data.MaxStages = MaxStages; }
	void setToleranceCOV(double TolCOV) { data.TolCOV = TolCOV; }
	void setUseLocalCOV(double use_local_cov) { data.use_local_cov = use_local_cov; }
	void setCovarianceScaling(double bbeta) { data.bbeta = bbeta; }
	void setBurnInIterations(int burn_in) { data.burn_in = burn_in; }
	void setChainLength(size_t min, size_t max) { data.MinChainLength = min; data.MaxChainLength = max; }

	// Optimization Contiguration Methods
	void setMaxIterations(size_t MaxIter) { data.options.MaxIter = MaxIter; }
	void setTolerance(double Tol) { data.options.Tol = Tol; }
	void setDisplay(bool Display) { data.options.Display = Display; }
	void setStepSize(double Step) { data.options.Step = Step; }
	void setBounds(double lower, double upper) { data.options.LowerBound = lower; data.options.UpperBound = upper; }

  // Overriding Base Korali Class virtual methods
  void Korali_InitializeInternalVariables();
  void Korali_GetSamplePopulation();
  bool Korali_CheckTermination();
  void Korali_PrintResults();
  void Korali_UpdateDistribution(const double *fitnessVector);

};

} // namespace Korali

#endif // _TMCMC_H_