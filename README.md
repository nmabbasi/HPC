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

The site is built with Jekyll using the official `github-pages` gem. Because `baseurl: /HPC` is configured in `_config.yml`, pages and stylesheet assets are served under the `/HPC/` path.

### Option 1: Using Bundler (Standard)

Prerequisites: Ruby and Bundler installed.

```bash
# Install dependencies from Gemfile
bundle install

# Start the local development server
bundle exec jekyll serve
```
Open **`http://localhost:4000/HPC/`** in your browser (the `/HPC/` subpath matches the repository site configuration).

To preview the site directly at the root (`http://localhost:4000/`), override the base URL flag:
```bash
bundle exec jekyll serve --baseurl ""
```

### Option 2: Using Docker (No Ruby installation required)

```bash
docker run --rm -it -v "$PWD:/srv/jekyll" -p 4000:4000 jekyll/jekyll jekyll serve
```
Open **`http://localhost:4000/HPC/`** in your browser.

---

## Author

**Nasir Mahmood Abbasi, PhD**  
Computational Biologist | Open to New Opportunities  
- Portfolio: [nmabbasi.github.io](https://nmabbasi.github.io/)  
- GitHub: [@nmabbasi](https://github.com/nmabbasi)  
- Email: [nmabbasi@gmail.com](mailto:nmabbasi@gmail.com)
