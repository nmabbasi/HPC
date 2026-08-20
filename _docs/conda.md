---
title: 'Conda environments on the cluster'
summary: 'Create, activate, export, and use isolated software environments in HPC workflows.'
step: '04'
next_label: 'Next step'
next_title: 'Manage custom software'
next_url: '/docs/custom-modules/'
---

## What Conda solves

Conda creates isolated software environments. Each environment records the packages and versions needed for one analysis, preventing conflicts between projects and making a workflow easier to reproduce on another machine or cluster.

> **Use the cluster policy first:** if your HPC service provides a supported Conda or Miniforge module, use that installation. Install a personal copy only when the service documentation permits it.

## Start with an available Conda installation

Check whether your cluster already provides Conda, Miniconda, or Miniforge through environment modules.

```bash
module avail conda miniforge miniconda
module load miniforge
conda --version
```

The module name differs by institution. If no supported module is available, follow your service documentation to install Miniforge or Miniconda in your home or project space, then initialise it only for your interactive shell.

## Configure reliable package channels

For bioinformatics software, use `conda-forge` and `bioconda` with strict channel priority. Run this once for your user account.

```bash
conda config --add channels conda-forge
conda config --add channels bioconda
conda config --set channel_priority strict
conda config --show channels
```

Strict priority reduces incompatible package combinations and makes solving environments more predictable.

## Create a project environment

Create one environment per project or analysis stage. Choose a clear name and install only the tools you need.

```bash
conda create --name rnaseq-qc fastqc multiqc samtools
conda activate rnaseq-qc
fastqc --version
```

Keep the `base` environment for Conda itself. Do not install project tools into `base`.

## Add and remove packages safely

Activate the environment before changing it. Check the installed packages after every meaningful change.

```bash
conda activate rnaseq-qc
conda install cutadapt
conda list
conda remove cutadapt
```

When a package cannot be resolved, first confirm the channel order and strict priority. Avoid mixing `pip install` with Conda unless the package is unavailable through Conda and you record that decision in the project documentation.

## Export the environment for reproducibility

Export a shareable YAML file when the environment is working. Store it alongside your analysis code and job scripts.

```bash
conda env export --from-history > environment.yml
```

Use `--from-history` to capture the packages you explicitly requested, rather than every platform-specific dependency. Recreate the environment on another system with:

```bash
conda env create --file environment.yml
conda activate rnaseq-qc
```

## Use Conda in a Slurm job

Load the same Conda source and activate the environment inside the batch script. Do not rely on an interactive terminal session being inherited by a compute node.

```bash
#!/usr/bin/env bash
#SBATCH --job-name=rnaseq-qc
#SBATCH --cpus-per-task=4
#SBATCH --time=01:00:00

module load miniforge
conda activate rnaseq-qc

fastqc --threads "$SLURM_CPUS_PER_TASK" reads.fastq.gz
```

If `conda activate` is unavailable in batch jobs, source the Conda shell hook supplied by your module or personal installation before activation. Your HPC service documentation will show the exact path.

## Quick troubleshooting

- Run `conda info` and `conda config --show channels` before reporting an environment problem.
- Run `which tool-name` and `tool-name --version` after activation to confirm the intended executable.
- Keep `environment.yml`, the batch script, and package versions in the same project repository.
- Deactivate when you finish the interactive session with `conda deactivate`.
