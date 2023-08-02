# WHAT
An example workflow from [The Carpentries Incubator](https://carpentries-incubator.github.io/snakemake-novice-bioinformatics/index.html).
# INPUT
Input data requires preparation.
```
wget --content-disposition https://ndownloader.figshare.com/files/35058796
```
untar the downloaded archive file, and copy the required directories to the snakemake workdir:
```
mv data/yeast/transcriptome ./transcriptome
mv data/yeast/reads ./raw
```
Note there is file naming discrepancy in the dataset, but you are smart, should be able to fix it :). The `./raw` directory should looks like:
```
$ ls ./raw
etoh60_1_1.fq  etoh60_2_1.fq  etoh60_3_1.fq  ref_1_1.fq  ref_2_1.fq  ref_3_1.fq  temp33_1_1.fq  temp33_2_1.fq  temp33_3_1.fq
etoh60_1_2.fq  etoh60_2_2.fq  etoh60_3_2.fq  ref_1_2.fq  ref_2_2.fq  ref_3_2.fq  temp33_1_2.fq  temp33_2_2.fq  temp33_3_2.fq
```
# SGE/Brenner
```
snakemake --use-conda -j20 --profile brenner -p summ_counts
snakemake --use-conda -j20 --profile brenner -p multiqc
```
# PBS/Gadi
```
snakemake --use-conda -j20 --profile gadi -p summ_counts
snakemake --use-conda -j20 --profile gadi -p multiqc
```
# Kubernetes/GKE
It is required to upload the input dataset (`./raw` and `./transcriptome` to the GCS bucket first.
```
snakemake --k8s-cpu-scalar 0.5 --kubernetes --use-conda -j20 --default-remote-provider GS --default-remote-prefix YOU_BUCKET_NAME -p summ_counts
snakemake --k8s-cpu-scalar 0.5 --kubernetes --use-conda -j20 --default-remote-provider GS --default-remote-prefix YOU_BUCKET_NAME -p multiqc
```
Note: when running on Kubernetes/GKE, the rule `salmon_quant` fails due to [this BUG](https://github.com/snakemake/snakemake/issues/2381) in snakemake. 
