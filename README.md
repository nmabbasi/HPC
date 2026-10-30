# HPC & Slurm Guide

A documentation-first guide for secure cluster access, essential Linux terminal operations, Slurm batch scripting, Conda environment isolation, and cluster storage management.

[![Website: Live](https://img.shields.io/badge/Guide-Live%20on%20GitHub%20Pages-blue.svg)](https://nmabbasi.github.io/HPC/)
[![Generator: Jekyll](https://img.shields.io/badge/Built%20With-Jekyll-red.svg)](https://jekyllrb.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Live Guide

Read the online documentation at: **[https://nmabbasi.github.io/HPC/](https://nmabbasi.github.io/HPC/)**

---

## Topics Covered

- **Cluster Access**: SSH key authentication, MobaXterm setup, and proxy jump configurations.
- **Environment Management**: Conda / Mamba environment isolation, managing Python/R dependencies, and environment export for reproducibility.
- **Slurm Batch Workflows**: Job submission templates (`sbatch`), interactive sessions (`srun`), memory/CPU allocation, and array jobs.
- **Storage Hygiene**: Scratch directory quotas, temporary file cleanup, and data transfer via `rsync` and `scp`.
- **Troubleshooting**: Diagnosing Out-Of-Memory (OOM) kills, node failures, and queue bottlenecks.

---

## Running Locally

The site is built with Jekyll. To preview it locally:

```bash
bundle install
bundle exec jekyll serve
```
Then navigate to `http://localhost:4000/HPC/`.

---

## Author

**Nasir Mahmood Abbasi, PhD**  
Computational Biologist | Université de Bordeaux / CNRS  
- Portfolio: [nmabbasi.github.io](https://nmabbasi.github.io/)  
- GitHub: [@nmabbasi](https://github.com/nmabbasi)  
- Email: [nmabbasi@gmail.com](mailto:nmabbasi@gmail.com)
