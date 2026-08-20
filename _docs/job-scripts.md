---
title: 'Writing Slurm job scripts'
summary: 'Allocate resources, record logs, submit batch jobs, and run reproducible compute tasks safely.'
step: '03'
next_label: 'Next step'
next_title: 'Use Conda on the cluster'
next_url: '/docs/conda/'
---
## <span class="header-section-number"></span> A basic script

All options actually have short versions (for example, *--job-name* could be replaced by *-J*). I used the long names here for clarity. Not all options of this script are mandatory, but I feel this is the minimum that should be given in order to make the intent clear.

I use a generic *program* in all scripts. Replace it with whatever executable you want. If it’s for testing purposes, you can simply replace it by *hostname* or *ls*.

I give *ibrain* as the argument for *--partition* and you may not have access to it. Replace it with one of the partition you see appearing in the output of *sinfo*.

    #!/bin/sh
        #SBATCH --job-name example_script

        #SBATCH --ntasks 1
        #SBATCH --cpus-per-task 1
        #SBATCH --mem 2G

        #SBATCH --partition ibrain
        #SBATCH --output %x-%j.out
        #SBATCH --error %x-%j.out
        #SBATCH --hint=nomultithread

        ## This is a comment.

        module purge
        module load gcc/7.3.1

        srun program

A few notes on the options.

- The value given to *--job-name* is used to identify the job when calling *squeue*.
- A standard linux console output is composed of the output stream and the error stream. When you use *sbatch*, none of these will appear on the console. Instead, they will be redirected to the file, or files specified by the *--output* and *--error* options.
- Scripts have internal variables. Here *%x* will be replaced by the job name, and *%j* will be replaced by the job id. The job id is given automatically to the job upon calling *sbatch* and appears when calling *squeue*.
- The *--hint=nomultithread* option is discussed further in section [Hyperthreading](#hyperthreading). If you don’t care about / understand hyperthreading, just leave it there.

Also, most long versions of options have an associated variable obtained by

- capitalizing every letter,
- replacing the leading *--* by *SLURM\_*.
- replacing the dashes by underscores,

So, in the example above, the variable *\$SLURM_JOB_NAME*, *\$SLURM_NTASKS*, *\$SLURM_CPUS_PER_TASK* (and more) will be defined right after their corresponding option line.

## <span class="header-section-number"></span> Decomposing the script

A submission script is composed of the following parts:

- a shebang,
- options,
- comments,
- shell commands,
- run commands.

### <span class="header-section-number"></span> Shebang

The shebang is always the first line of the script. It specifies which shell interpreter to use for shell commands. Replace *sh* with whatever shell you want in the following line.

    #!/bin/sh

### <span class="header-section-number"></span> Options

Options are lines that start with

    #SBATCH

They have two purposes.

- The first is to specify resource allocation. In the example script, the duo of *--ntasks* and *--cpus-per-task* asks to allocate a single CPU, and the *--mem* option asks to allocate 2G.

**Note:** allocating a lot of resources does not mean that all of them will be used. If you call a single program that does not run in parallel, a single CPU will be used whether you allocate 1 or more CPUs. Be mindful that if you allocate more resources than necessary, those unused resources will not be available to the other users. Estimating the number of CPUs is usually not a problem as programs that run in parallel usually have an option specifying the number we want to use. It’s a bit harder to estimate memory. The best I got for that is to do some testing: either start with low memory and increase it until it runs, or start with high memory and monitor your program by sshing to the node being used (*squeue* will tell you that) and executing *top*.

**Other note:** in the current configuration, asking for 1 CPU will actually allocate 2, because slurm allocates by the core, and cores are hyperthreaded. More details in section [Hyperthreading](#hyperthreading).

- The second purpose is to be passed to the *srun* command. Unless overwritten when calling *srun*, all options given with *\#SBATCH* are assumed.

There are many more options:

    man sbatch

### <span class="header-section-number"></span> Comments

Any line starting with *\#* but not followed by *SBATCH* is a comment. If you want to comment an option, use more than one *\#*:

    ##SBATCH

In order to avoid confusion between comment and option while using a single *\#*, the comment in my example script uses two *\#*, even though only one is required.

### <span class="header-section-number"></span> Shell commands

Shell commands are used to setup the linux environment variables. They should **not** be preceeded by *srun*.

### <span class="header-section-number"></span> Run commands

Run commands are your actual computations. They should be preceeded by *srun*. The reason is that, as mentioned above, the options given with *\#SBATCH* apply to *srun*. In truth, when only one task is given with the *--ntasks* option, omitting *srun* will not change anything. Put it there anyway, for consistency.

## <span class="header-section-number"></span> Hyperthreading

Hyperthreading is activated on the nodes, meaning each core has two CPUs. But this does not double computational power, as using two CPUs of the same core is less efficient than using two CPUs of different cores. With that in mind, here is how slurm acts (with the number of CPUs you ask for being the product of *--ntasks* and *--cpus-per-task*):

- without the *--hint=nomultithread* option, asking for an odd number *N* of CPUs or asking for *N+1* CPUs is the same: slurm allocates the *N+1* CPUs of *(N+1)/2* cores,
- with the *--hint=nomultithread* option, asking for *N* CPUs will allocate the *2N* CPUs of *N* cores.

Note that if you like to use the *–mem-per-cpu* option instead of the *–mem* option, the total allocated memory will be based on the number of CPUs actually allocated, not the number of CPUs you asked for. Examples:

- without the *--hint=nomultithread* option, the combination of *--ntasks 1 --cpus-per-task 1 --mem-per-cpu 1G* will allocate 2G,
- the combination of *--ntasks 1 --cpus-per-task 2 --mem-per-cpu 1G --hint=nomultithread* will allocate 4G,

There really is only a single valid use of hyperthreading: when you want to ask for **all** the CPUs of a single node. In that case, remove the *--hint=nomultithread* option and allocate everything.

The rest of this documentation assumes we don’t use hyperthreading.

## <span class="header-section-number"></span> Running things in parallel

### <span class="header-section-number"></span> Calling the same program multiple times in parallel

    #!/bin/sh
        #SBATCH --job-name example_script

        #SBATCH --ntasks 3
        #SBATCH --cpus-per-task 1
        #SBATCH --mem 6G

        #SBATCH --partition ibrain
        #SBATCH --output %x-%j.out
        #SBATCH --error %x-%j.out
        #SBATCH --hint=nomultithread

        ## This is a comment.

        module purge
        module load gcc/7.3.1

        srun program

Recall that the options given with *\#SBATCH* are passed to *srun*. In this case, a single call to *srun program* would be equivalent to *srun --ntasks 3 program*, which would call *program* three times.

### <span class="header-section-number"></span> Several steps in parallel

Here is the full script.

    #!/bin/sh
        #SBATCH --job-name example_script

        #SBATCH --ntasks 3
        #SBATCH --cpus-per-task 1
        #SBATCH --mem 6G

        #SBATCH --partition ibrain
        #SBATCH --output %x-%j.out
        #SBATCH --error %x-%j.out
        #SBATCH --hint=nomultithread

        ## This is a comment.

        module purge
        module load gcc/7.3.1

        srun --ntasks=1 program0 &
        srun --ntasks=1 program1 &
        srun --ntasks=1 program2

Do not forget the *--ntasks 1* on the *srun* lines. If you do, *program0* will be called three times, and because three tasks are being run and you only allocated three, *program1* and *program2* will not be executed at the same time, and will have to wait for the previous tasks to end.

### <span class="header-section-number"></span> Arrays

This is useful when you want to use the same programs multiple times with various arguments. The requirements is that the arguments differ only by an integer number. Here is the script.

    #!/bin/sh
        #SBATCH --job-name example_script

        #SBATCH --ntasks 1
        #SBATCH --cpus-per-task 1
        #SBATCH --mem 2G

        #SBATCH --partition ibrain
        #SBATCH --output %x-%j.out
        #SBATCH --error %x-%j.out

        #SBATCH --array=1,5-20%4
        #SBATCH --hint=nomultithread

        ## This is a comment.

        module purge
        module load gcc/7.3.1

        srun program $SLURM_ARRAY_TASK_ID

The *--array* option takes a comma separated list of integer, where ranges are specified with a dash. The list can optionally be followed by *%N* for an integer *N* to limit the number of parallel calls.

The above example will effectively run *program* 17 times, and the arguments given to *program* will take the values 1 and all integers between 5 and 20 (both included). Because of the *%4*, it will start by executing with arguments 1, 5, 6, 7 (if enough resources are available) while keeping the other execution in queue (without executing them). Argument 8 will execute as soon as one of the first four is done, argument 9 will execute as soon as two of the first five is done, and so on. Without the *%4*, slurm would have executed all 17 arguments (if enough resources were available) at once.

It should be noted that the allocation you give (*--ntasks*, *--cpus-per-task* and *--mem 2G*) only concerns a single execution of *program*.

Finally, the arguments don’t need to be exactly integers. You can put something like *prefix-\${SLURM_ARRAY_TASK_ID}.extension* there.

### <span class="header-section-number"></span> OpenMP / fork

If you know a single execution of your program uses multiple threads/cores, give that number to *--cpus-per-task* and keep *--ntasks* at 1. If your program takes the number of threads/cores as argument, or if it checks an environment variable to decide how many threads/cores are used, recall that whatever you give to *--cpus-per-task* is accessible through the *\$SLURM_CPUS_PER_TASK* variable. Example script for an OpenMP program.

    #!/bin/sh
        #SBATCH --job-name example_script

        #SBATCH --ntasks 1
        #SBATCH --cpus-per-task 12
        #SBATCH --mem 24G

        #SBATCH --partition ibrain
        #SBATCH --output %x-%j.out
        #SBATCH --error %x-%j.out
        #SBATCH --hint=nomultithread

        ## This is a comment.

        module purge
        module load gcc/7.3.1

        OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK srun program

### <span class="header-section-number"></span> MPI programs

For pure MPI programs, keep *--cpus-per-task* at 1, set *--ntasks* to the number of processes you want, and replace *srun* by *mpirun*.

Here is a sample script for MPI/OpenMP hybrids.

    #!/bin/sh
        #SBATCH --job-name example_script

        #SBATCH --ntasks 8
        #SBATCH --cpus-per-task 8
        #SBATCH --mem 128G

        #SBATCH --partition ibrain
        #SBATCH --output %x-%j.out
        #SBATCH --error %x-%j.out
        #SBATCH --hint=nomultithread

        ## This is a comment.

        module purge
        module load gcc/7.3.1

        OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK mpirun program

### <span class="header-section-number"></span> Other options

You can request specific nodes with the *--nodelist* option, which takes a comma separated list of nodes with possible integer ranges between brackets:

    #SBATCH --nodelist ibrain-node[01-07],ibrain-node12

Be mindful that while slurm will use the requested node, other nodes may also be used if the resources you ask for exceed the requested nodes resources. If you want to **only** use the requested node, combine *--nodelist* with *--exclude*:

    #SBATCH --nodelist ibrain-gpu01
        #SBATCH --exclude ibrain-node[01-12]
