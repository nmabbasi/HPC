---
title: 'Cluster basics and commands'
summary: 'Load modules, inspect partitions, monitor jobs, and understand the HPC environment before submitting work.'
step: '02'
next_label: 'Next step'
next_title: 'Write a Slurm job script'
next_url: '/docs/job-scripts/'
---
## <span class="header-section-number"></span> Modules

Some programs are only available through modules: you need to load modules to use them. As an example, if you want to compile MPI programs with *mpic++*, you’ll have to load the correct module:

    module load mpi/openmpi-x86_64

As always,

    man module

will give you all possible options/commands. Here are the most important.

    module avail

lists all available modules.

<img src="{{ '/MA.png' | relative_url }}" width="1500" height="1500" alt="MobXterm" />

    module list

lists all loaded modules.

    module load X
        module unload X

loads and unloads modules.

    module purge

unloads all modules.

Don’t forget to load the appropriate modules inside submission scripts (see [Writing a submission script](#writing-a-submission-script)). These inside-script module loads are usually preceded by *module purge*.

## <span class="header-section-number"></span> Listing partitions and nodes

    sinfo

The *STATE* column gives the states of the nodes given in the *NODELIST* column and may take (among others) the following values:

- idle: no resource allocated,
- mix: some resources allocated, but no resource fully allocated,
- alloc: at least one resource (number of CPUs or memory) fully allocated,
- drain: will finish the jobs currently running but will not accept any more jobs,
- down: node is shutdown.

All the possible states and a thousand options can be listed with:

    man sinfo

Also, the following command will display the characteristics of each node:

    sinfo --long --Node

The option *-p* allows restricting to the nodes of a single partition. The important columns of the output are *CPUS*, which gives the maximum number of CPUs that can be allocated, and *Memory*, which gives the maximum available memory in Megabytes.

## <span class="header-section-number"></span> Listing submitted jobs

    squeue

If you want to see only yours:

    squeue -u `whoami`

The *ST* column is for the state of the job. You’ll usually see either *R* for running or *PD* for pending.

## <span class="header-section-number"></span> Partitions, nodes and jobs in a GUI

If X is activated (see section [Running a GUI](#running-a-gui)), one can also run:

    sview&

## <span class="header-section-number"></span> Running tasks

There are two ways to run tasks on nodes: submit a job (section [Submitting a job](#submitting-a-job)) or start an interactive session (section [Running an interactive session](#running-an-interactive-session)). Interactive sessions should only be used in two cases:

- you want to run a GUI,
- you want to debug your program.

In all other cases, it is better to submit a job script. The reason is that you need to allocate resources when starting an interactive session. By nature, there is usually downtime in interactive sessions (modifying scripts/programs, or not realising that the task has completed and letting it idle), and during this downtime, the resources you allocated and are currently not using are also unavailable to the other cluster users.

If you struggle with the script, send an email to *yann.jullian<span style="display:none">foo</span><span class="citation" cites="univ-tours.fr">@univ-tours.fr</span>* and use an interactive session in the meantime.

## <span class="header-section-number"></span> Running an interactive session

You can only *ssh* directly onto a node if you have one job active on it. However, a similar result can be obtained by running:

    srun --partition=ibrain --ntasks=1 --cpus-per-task=12 --mem=12G --pty /bin/bash -l

The options you can give there are mostly the same as the *sbatch* option (see [Writing a submission script](#writing-a-submission-script)), and they specify resource allocation. The *--pty /bin/bash -l* part tells slurm to open a console. From there, you can execute the programs you want.

As long as the console is open (type *exit* to leave), the resources will be allocated.

As this is a long command, you may want to use an alias. Open your *~/.bashrc* and add a line:

    alias interactive='srun --partition=ibrain --ntasks=1 --cpus-per-task=1 --mem=1G --pty /bin/bash -l'

After relogging or running

    source ~/.bashrc

you’ll be able to simply type *interactive* to start an interactive session.

## <span class="header-section-number"></span> Running a GUI

### <span class="header-section-number"></span> If you connect with NX

Nothing more to do.

### <span class="header-section-number"></span> If you connect with SSH

#### <span class="header-section-number"></span> Linux / mac

Either give the *-X* option to the *ssh* command:

    ssh -X esmeralda

or add *ForwardX11 yes* in your *~/.ssh/config* :

    Host esmeralda
            Hostname 10.195.17.215
            User LOGIN
            ForwardX11 yes
            IdentityFile ~/.ssh/esmeralda

#### <span class="header-section-number"></span> Mac

Install *Xquartz*.

#### <span class="header-section-number"></span> Windows

Nothing more to do.

### <span class="header-section-number"></span> In all cases

Give the *--x11* option to *srun*.

    srun --x11 --partition=biopatic --nodelist=biopatic-node01 --ntasks=1 --pty rstudio

Or in two steps:

    srun --x11 --partition=biopatic --nodelist=biopatic-node01 --ntasks=1 --pty /bin/bash -l

then

    rstudio

## <span class="header-section-number"></span> Submitting a job

Write a submission script *launch.job* (see [Writing a submission script](#writing-a-submission-script)), then run:

    sbatch launch.job

## <span class="header-section-number"></span> Stopping a job

Get the ID number *N* of the job with the *squeue* command (*JOBID* column), then run:

    scancel N
