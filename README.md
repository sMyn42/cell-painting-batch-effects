# Examining Batch Effects on Cell Painting Data

This project examines the presence of batch effects in (high-throughput) single-cell morphology data of different strains of cells subjected to various perturbations.
In addition to evaluating the benefits of the kBET detection algorithm, Harmony is used to correct for the observed batch effect. Ultimately, the goal is to benchmark these two processes and evaluate their effectiveness on the LINCS cell morphology data.

@TODO update README

## Computational Environment

We use [conda](https://docs.conda.io/en/latest/) to manage the computational environment.

After installing conda, execute the following to install and navigate to the environment:

```bash
# First, install the conda environment
conda env create -f environment.yml

# Then, activate the environment and you're all set!
conda activate myenv
```

In addition, the kBET package for R needs to be installed, and here are the instructions from https://github.com/theislab/kBET, to be run the the R console:

```bash
library(devtools)
install_github('theislab/kBET')
```
