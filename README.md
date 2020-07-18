# Examining Batch Effects on Cell Painting Data

This project examines the presence of batch effects in (high-throughput) single-cell morphology data.
We use [kBET](https://github.com/theislab/kBET) to first detect the extent of batch effects, and then [Harmony](https://github.com/immunogenomics/harmony) to adjust for them.
Ultimately, our goal is to benchmark these two processes and evaluate their effectiveness single cell Cell Painting data.

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
