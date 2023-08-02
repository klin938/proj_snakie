# WHAT
DEMO the implementation of snakemake workflows that are platform independent, and how to run them on the HPC with different resource schedulers and on the cloud (via kubernetes). It is the collective works based on:
* [Snakemake-Profiles](https://github.com/Snakemake-Profiles)
* [Snakemake Cluster Execution](https://snakemake.readthedocs.io/en/stable/executing/cluster.html)
* [Snakemake Cloud Execution](https://snakemake.readthedocs.io/en/stable/executing/cloud.html#executing-a-snakemake-workflow-via-kubernetes)
# Preparation
The snakemake environment is supported by [mamba](https://github.com/mamba-org/mamba)
```
cd smk-novice-multiQC
mamba env create -p envs/smake --file envs/environment.yaml
mamba activate envs/smake/
```
To cleanup an env (if needed)
```
mamba env remove -p envs/smake
```
# RUN
Checkout README inside each workflow directory
