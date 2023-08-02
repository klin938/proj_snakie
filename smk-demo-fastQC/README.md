# WHAT
The simplest example of a fastQC workflow.
# INPUT
Input files will be downloaded on-the-fly.
# SGE/Brenner
snakemake --use-conda -j8 --profile brenner
# PBS/Gadi
snakemake --use-conda -j8 --profile gadi
# Kubernetes/GKE
snakemake --k8s-cpu-scalar 0.5 --kubernetes --use-conda -j8 --default-remote-provider GS --default-remote-prefix YOU_BUCKET_NAME
