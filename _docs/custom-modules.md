---
title: 'Custom software modules'
summary: 'Create and use user-maintained module files for approved software on shared compute systems.'
step: '05'
next_label: 'Next step'
next_title: 'Get support'
next_url: '/docs/support/'
---

## When to create a custom module

Use a custom module when you have installed approved software in your project space and want a repeatable way to expose its commands. A module keeps paths and library settings out of job scripts, so the same software environment can be loaded interactively and in batch jobs.

> **Before you begin:** follow your institution’s storage and software policies. Do not install software in shared system locations unless your HPC service explicitly authorises it.

## Create a module-file directory

Choose a directory in your home or project area. In this example, `MODULE_ROOT` is a personal module-file directory.

```bash
export MODULE_ROOT="$HOME/modulefiles"
mkdir -p "$MODULE_ROOT/spades"
```

Module files are normally grouped by software name, then by version. This makes it straightforward to keep several versions side by side.

## Write a module file

Create a file named for the installed software version. Replace `/path/to/spades` with the actual directory containing the executable `bin` folder.

```bash
cat > "$MODULE_ROOT/spades/3.14.0" <<'EOF'
#%Module1.0
## SPAdes 3.14.0 installed in a user-managed project area
prepend-path PATH /path/to/spades/bin
EOF
```

The first line identifies the file as a module file. `prepend-path` places the software directory before the rest of your `PATH`, allowing the intended executable to be found consistently.

## Load the module

Tell the module system where to find your module files, then load the version you created.

```bash
module use --append "$MODULE_ROOT"
module load spades/3.14.0
which spades.py
```

Run `module avail` to review all available modules. If the software is not found, confirm the module-file path and the executable path in the `prepend-path` line.

## Make the module available in future sessions

Add the module-file location to your shell startup file only when your HPC service recommends this workflow. For Bash, the following line can be added to `~/.bashrc`:

```bash
module use --append "$HOME/modulefiles"
```

Open a new terminal session and verify that `module avail` shows your software. Keep project-specific module paths inside the project when they should not be used globally.

## Use custom modules in a Slurm job

Load the same module explicitly in the batch script. This keeps the compute-node environment reproducible instead of relying on an interactive shell session.

```bash
#!/usr/bin/env bash
#SBATCH --job-name=spades-test
#SBATCH --cpus-per-task=8
#SBATCH --time=01:00:00

module use --append "$HOME/modulefiles"
module load spades/3.14.0
spades.py --help
```

## Troubleshooting checklist

- Confirm that the module file is named with the exact version you load.
- Use `module show spades/3.14.0` to inspect the environment changes before a job runs.
- Use `which` and `--version` after loading a module to verify the executable and version.
- Keep the module file and installed software inside a backed-up project location.
- Include the `module use` and `module load` lines in every batch script that depends on the software.
