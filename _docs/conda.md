---
title: 'Conda environments on the cluster'
summary: 'Create, activate, export, and use isolated software environments in HPC workflows.'
step: '04'
next_label: 'Next step'
next_title: 'Manage custom software'
next_url: '/docs/custom-modules/'
---
## Goals

- Understand what Conda is and how it can simplify analysis pipelines.
- Learn how to install and configure Conda on any system.
- Be able to create reproducible computing environments for (almost) any task.



## Conda in Theory

### What is Conda?

<a href="https://docs.conda.io/projects/conda/en/latest/index.html" rel="nofollow"><strong>Conda</strong></a> is a Python-based environment and package manager. It helps produce reproducible analysis pipelines using crowd-sourced and version-controlled packages.



If you are new to this type of approach, you may not know what that means. Here is some quick vocabulary so we're all on the same page:

- **Environment**: A computing environment is the collection of programs, language libraries, etc. in which a computer operates. Environments can be defined at many different levels similar to the ecological sense where an environment may refer to a 1 cm x 1 cm square of grass or an entire continent.
- **Package**: A package is a collection of software that may contain things such as programs (e.g. Python), programming libraries (e.g. Perl), or other useful tools. Conda combines packages to construct environments for doing complex tasks.



In short, what that means is Conda creates self-contained modules that contain all of the necessary programs, etc. for completing a particular computing task.



### Why is Conda useful?

Using Conda as part of analysis workflows has a lot of advantages:

- It works on all major operating systems (Mac, Windows, and Linux).

  > **NOTE:** While Conda works on all operating systems, not all packages are available for every operating system. Windows tends to be the most affected by this.

- It helps keep your computing environment organized so you're less likely to end up in <a href="https://en.wikipedia.org/wiki/Dependency_hell" rel="nofollow"><strong>"dependency hell"</strong></a>.

- Packages are version-controlled so you can easily switch versions if one isn't working.

- Environments can be reproducible and shareable leading to increased analytical veracity.

- It works exceptionally well when combined the workflow managers. See the ["Additional Resources"](#additional-resources) section below for more information.



## Conda in Practice

### Installing Conda

The process for installing Conda is the same across most operating systems but we will use the University of Michigan Great Lakes HPC cluster as a uniform Linux environment for the purposes of this tutorial.

> **NOTE:** If you don't have access to the cluster, skip to Step 3. Then, make sure to choose the correct installer and adjust accordingly going forward.



**1.** Log into the Great Lakes cluster.

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="ssh UNIQNAME@greatlakes.arc-ts.umich.edu">

``` notranslate
ssh UNIQNAME@greatlakes.arc-ts.umich.edu

```

</div>



**2.** You should be in your home folder but let's check to make sure.

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="pwd">

``` notranslate
pwd

```

</div>



**3.** To install Conda, we first need to find the proper installer on the <a href="https://docs.conda.io/en/latest/mini{{ '/docs/conda/' | relative_url }}" rel="nofollow"><strong>website</strong></a>. We will be installing Miniconda instead of Anaconda since it only contains the essentials and tends to run faster. Right-click and copy the link address for the Miniconda Linux 64-bit installer that uses Python 3.7.

<a href="{{ '/miniconda_installer.png' | relative_url }}" rel="noopener noreferrer" target="_blank"><img src="{{ '/miniconda_installer.png' | relative_url }}" style="max-width: 100%;" alt="Image of Miniconda Linux installers" /></a>



**4.** Return to your terminal and use `wget` to download the installation script to your home folder on the cluster.

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh">

``` notranslate
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

```

</div>



**5.** Verify the installation script is now in your home folder.

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="ls">

``` notranslate
ls

```

</div>



**6.** It's good practice to make sure downloaded files weren't corrupted during the download process. One way to do that is using <a href="https://en.wikipedia.org/wiki/Checksum" rel="nofollow"><strong>checksum hashes</strong></a> which are unique signatures generated based on the file contents. Some (but not all) sites will make the hash available so you can verify the download was successful. If your hash doesn't match the host's hash, it means there was an error with your download and you should probably try it again. The larger the files (e.g. large DNA sequencing files), the more important it is to check. Let's check ours now.

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="shasum -a 256 Miniconda3-latest-Linux-x86_64.sh">

``` notranslate
shasum -a 256 Miniconda3-latest-Linux-x86_64.sh

```

</div>



**7.** Compare the hash to the hash listed next to the installer. If it doesn't match (ours does so no problems), try downloading again or check your internet settings.

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="8a324adcc9eaf1c09e22a992bb6234d91a94146840ee6b11c114ecadafc68121  Miniconda3-latest-Linux-x86_64.sh">

``` notranslate
8a324adcc9eaf1c09e22a992bb6234d91a94146840ee6b11c114ecadafc68121  Miniconda3-latest-Linux-x86_64.sh

```

</div>



**8.** To install Miniconda, we need to run the script we just downloaded.

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="bash Miniconda3-latest-Linux-x86_64.sh">

``` notranslate
bash Miniconda3-latest-Linux-x86_64.sh

```

</div>



**9.** Follow the prompts on the screen to install the program to your home folder. When it asks whether you want to initialize Miniconda3, say `yes`. The process should only take a few minutes.



**10.** When initializing, the installer will add a code chunk to the bottom of your `~/.bashrc` file. This file is used for customizing your terminal and environment. When the chunk is added to this file, it sets up your environment for using Conda though it does so based on which shell you are currently using. This is normally a good thing but can cause problems when submitting jobs to the cluster because the cluster's shell configuration is slightly different than the one we interact with. If we don't alter the code at the bottom of the `~/.bashrc`, our environment won't be passed to the cluster nodes properly and our jobs will fail. To fix this, we need to comment out most of the lines.

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="nano ~/.bashrc">

``` notranslate
nano ~/.bashrc

```

</div>

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="# # &gt;&gt;&gt; conda initialize &gt;&gt;&gt;
   # # !! Contents within this block are managed by 'conda init' !!
   # __conda_setup=&quot;$('/home/wlclose/miniconda3/bin/conda' 'shell.bash' 'hook' 2&gt; /dev/null)&quot;
   # if [ $? -eq 0 ]; then
   #     eval &quot;$__conda_setup&quot;
   # else
       if [ -f &quot;/home/wlclose/miniconda3/etc/profile.d/conda.sh&quot; ]; then
           . &quot;/home/wlclose/miniconda3/etc/profile.d/conda.sh&quot;
       else
           export PATH=&quot;/home/wlclose/miniconda3/bin:$PATH&quot;
       fi
   # fi
   # unset __conda_setup
   # # &lt;&lt;&lt; conda initialize &lt;&lt;&lt;">

``` notranslate
# # >>> conda initialize >>>
   # # !! Contents within this block are managed by 'conda init' !!
   # __conda_setup="$('/home/wlclose/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
   # if [ $? -eq 0 ]; then
   #     eval "$__conda_setup"
   # else
       if [ -f "/home/wlclose/miniconda3/etc/profile.d/conda.sh" ]; then
           . "/home/wlclose/miniconda3/etc/profile.d/conda.sh"
       else
           export PATH="/home/wlclose/miniconda3/bin:$PATH"
       fi
   # fi
   # unset __conda_setup
   # # <<< conda initialize <<<

```

</div>



**11.** Now that we've installed Conda and tweaked our `~/.bashrc`, we need to reload the shell session for our changes to take place. When we source `~/.bash_profile`, it should also source `~/.bashrc`. Alternatively, you can restart your terminal or terminal session.

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="source ~/.bash_profile">

``` notranslate
source ~/.bash_profile

```

</div>



**12.** Let's do a quick check to make sure we can now access the `conda` command.

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="conda --help">

``` notranslate
conda --help

```

</div>

Looks great!



**13.** For our last step, we can also create a `~/.condarc` file for <a href="https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/use-condarc.html" rel="nofollow">configuring Conda</a> similar to how we use our `~/.bashrc` to configure our shell, . We can use this to tell Conda where and how to search for packages that we want to download. With Conda, packages are retreived from version-controlled repositories called **channels** and different channels will have different themes. For example, the main bioinformatics channel is called <a href="https://bioconda.github.io/index.html" rel="nofollow"><strong>Bioconda</strong></a>.



Conda comes with a few default channels included but they aren't always that useful. To fix this, we can add new channels to our `~/.condarc` file. Today, we'll be adding the <a href="https://conda-forge.org/" rel="nofollow"><strong>Conda-Forge</strong></a> channel. Packages on Conda-Forge are typically more up-to-date than the default channels and adding it will help satisfy a lot of potential dependency issues.



To add Conda-Forge to your channels, type the following. If your `~/.condarc` doesn't already exist, this will also create it.

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="conda config --add channels conda-forge">

``` notranslate
conda config --add channels conda-forge

```

</div>



For the last configuration (and for more complex reasons) we should also change how priority is set when searching for packages. You can read more about it <a href="https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-channels.html#strict-channel-priority" rel="nofollow">here</a>.

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="conda config --set channel_priority strict">

``` notranslate
conda config --set channel_priority strict

```

</div>



With all that out of the way, Conda is now ready to use!



## Creating and Managing Environments

### Environments 101

Now that we've installed Conda, we're ready to start learning how to use it as an environment-based package manager. Environments are an integral part of Conda-based workflows. They are customizable, reproducible, and shareable modules that contain the resources for a specific task or set of tasks. Environments also help avoid "dependency hell" where required programs are incompatible with previously installed programs or program versions.



**1.** To start with, let's see what environments we currently have set up. This will list all of the environments available for us to use along with their locations.

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="conda env list">

``` notranslate
conda env list

```

</div>

By default, an environment called `base` is created when installing and intializing Conda. `base` contains a number of standard Python packages that may or may not be useful.



**2.** Because we altered the code in our `~/.bashrc`, the `base` environment isn't loaded automatically when we log into the shell. This can help speed up tasks if you don't need to use anything in the environment but, if we do need to use something in the environment, we'll need to activate the environment first. We'll start with the `base` environment.

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="conda activate base">

``` notranslate
conda activate base

```

</div>



**3.** You should now see that the word `base` is in your prompt showing that we've loaded the base environment. Another way to check which environment you have active is to look at the `$CONDA_PREFIX` shell variable. If you don't have any environment loaded, the output will be blank.

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="echo $CONDA_PREFIX">

``` notranslate
echo $CONDA_PREFIX

```

</div>



**4.** Now that we have the `base` environment loaded, let's see which programs it contains for us to use.

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="conda list">

``` notranslate
conda list

```

</div>

The output from this command lists all of the programs, their versions, the build number, and the channel they came from if outside of the `defaults` channels.



**5.** We can check to make sure we are using the programs from our environment by using `which` to print the executable path or by checking our shell `$PATH` variable. The `$PATH` variable lists the order of folders from first to last that the shell will look through to find executables. The shell will execute the first binary it finds and ignore the rest so it's important our `$PATH` is in the correct order.

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="which python
   echo $PATH">

``` notranslate
which python
   echo $PATH

```

</div>



### Creating Task-Specific Environments

In a typical workflow, it's good practice to create environments for each task or script being executed to keep the environment running as fast as possible, reduce the likelihood of conflicting programs/versions, and assist in debugging when things don't work out. Let's create a new environment for analyzing 16S bacterial sequencing data with <a href="https://mothur.org/wiki/Main_Page" rel="nofollow"><strong>mothur</strong></a>.

**1.** First, let's deactivate the current environment.

> **NOTE:** Deactivating the current environment is being done here for the sake of clarity. The process of creating and managing a new environment are exactly the same whether another environment is active or not.

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="conda deactivate">

``` notranslate
conda deactivate

```

</div>



**2.** Next, let's create an empty environment for our `mothur` analysis.

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="conda create -n mothur">

``` notranslate
conda create -n mothur

```

</div>



**3.** We should see it in our list of available environments now. Also note that the new environment is created in the `miniconda3/envs/` subdirectory in our home folder. This is where binaries, etc. will be downloaded to if you ever need to find them.

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="conda env list">

``` notranslate
conda env list

```

</div>



**4.** Let's activate the new environment.

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="conda activate mothur">

``` notranslate
conda activate mothur

```

</div>



**5.** If we look at which programs the environment contains, we'll see that it's empty.

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="conda list">

``` notranslate
conda list

```

</div>



**6.** To add new packages (in this case `mothur`), we can search for them on <a href="https://anaconda.org/" rel="nofollow"><strong>Anaconda Cloud</strong></a>. Using Anaconda Cloud, we can find which channels we can retrieve `mothur` from, which versions are available, and a lot of other useful information.



When we search for `mothur`, we can see that it's available from multiple channels but we'll use Bioconda specifically.

<a href="{{ '/anaconda_mothur_search_results.png' | relative_url }}" rel="noopener noreferrer" target="_blank"><img src="{{ '/anaconda_mothur_search_results.png' | relative_url }}" style="max-width: 100%;" alt="Image showing mothur available from multiple channels" /></a>



**7.** If we click on the Bioconda version, we'll be taken to the information page for `mothur` where we can see details about versions, metadata, and most importantly for us, installation instructions.

<a href="{{ '/anaconda_mothur_package_page.png' | relative_url }}" rel="noopener noreferrer" target="_blank"><img src="{{ '/anaconda_mothur_package_page.png' | relative_url }}" style="max-width: 100%;" alt="Image of bioconda/mothur package page" /></a>



**8.** Copy the installation code for `mothur`, paste it into your terminal, and run the installation. By specifying `-c` during the install, we can tell Conda which channel to use. This is particularly important when downloading packages that have multiple copies on multiple channels.

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="conda install -c bioconda mothur">

``` notranslate
conda install -c bioconda mothur

```

</div>

Even though we only told it to install `mothur`, notice that Conda automatically determines and installs the dependencies required for installing and running it. This is one of the major advantages of using a package manager like Conda as opposed to doing this manually.



**9.** When the installation finishes, see what other programs/dependencies were installed.

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="conda list">

``` notranslate
conda list

```

</div>



**10.** Next, let's try running `mothur` to see if it worked.

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="which mothur
   mothur">

``` notranslate
which mothur
   mothur

```

</div>

**Success!** We have now created a new, self-contained environment that contains everything we need to run `mothur` as part of our analysis.



To exit `mothur`, type:

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="quit()">

``` notranslate
quit()

```

</div>



### Using `.yaml` Files to Create and Share Reproducible Environments

The last important function we'll go over is the ability to <a href="https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file" rel="nofollow"><strong>create environments from a <code>.yaml</code> file</strong></a>. These files can also be shared with others so they can create similar environments. While you can programmatically export your entire environment (channels, packages, versions, etc.) to a `.yaml` file, **it's generally a bad idea** for a number of reasons, the main one being that they aren't typically cross-platform compatible (more information <a href="https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?highlight=environment#building-identical-conda-environments" rel="nofollow"><strong>here</strong></a>). We'll create one manually and then show how we use it to create a new environment.



**1.** To start, we'll create a `.yaml` file for our new environment. For the majority of environments, you only need to include the three essentials: **i) name**, **ii) channels**, and **iii) dependencies**. Setting specific <a href="https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/pkg-specs.html#package-match-specifications" rel="nofollow">versions</a> is optional but recommended in instances where reproducibility matters. In this case, we'll be creating an environment for using <a href="http://samtools.sourceforge.net/" rel="nofollow"><strong>SAMtools</strong></a> to manipulate sequencing alignment files.

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="nano testEnv.yaml">

``` notranslate
nano testEnv.yaml

```

</div>

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="name: samtools
   channels:
     - conda-forge
     - bioconda
   dependencies:
     - python=3.7.3
     - samtools=1.9">

``` notranslate
name: samtools
   channels:
     - conda-forge
     - bioconda
   dependencies:
     - python=3.7.3
     - samtools=1.9

```

</div>



**2.** Then, we use that file to create a new environment...

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="conda env create -f testEnv.yaml">

``` notranslate
conda env create -f testEnv.yaml

```

</div>



**3.** ...Which we can now use whenever we want!

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="conda env list">

``` notranslate
conda env list

```

</div>



**4.** When looking at our updated environment list, notice that the name of the new environment is set based on the `name` attribute in the `.yaml` file and not the name of the `.yaml` file itself. It's generally good practice to name your `.yaml` file based on the `name` attribute within the file so it's easier to keep track of things. Let's finish strong and fix that.

<div class="snippet-clipboard-content notranslate position-relative overflow-auto" snippet-clipboard-copy-content="mv testEnv.yaml samtools.yaml">

``` notranslate
mv testEnv.yaml samtools.yaml

```

</div>



## Conclusions

Congratulations on finishing the tutorial! Now that you know the fundamentals of how to set up Conda and use it to manage environments and packages, you should be able to reliably use it as part of your analysis workflows. That being said, it's important to note the material covered as part of this tutorial only scratches the surface of what can be done with Conda and there may be occasions when you want a little more control. In those situations, I highly recommend checking out the <a href="https://docs.conda.io/en/latest/" rel="nofollow"><strong>Conda documentation</strong></a> and checking out the various user communities. They're great resources for finding new tips, debugging errors, and getting general guidance. I've also included some additional items below that might help you get to where you want to be. Good luck!



### Best Practice DOs and DON'Ts of Conda

- DO verify the checksum hashes of downloaded files to make sure they downloaded properly.
- DO create separate environments for each task or script being ran.
- DON'T create Conda environments without using `.yaml` files (unless you're just testing something).
- DON'T export your entire environment as a `.yaml`.
- DO manually create `.yaml` files for each environment you plan on using.
- DO name your environment `.yaml` file using the same label as the `name` attribute within the file.



### Additional Resources

- There wasn't time to cover it as part of this tutorial but one of the most useful implementations of Conda is as part of a <a href="https://snakemake.readthedocs.io/en/stable/" rel="nofollow"><strong>Snakemake</strong></a> workflow. Where Conda is a package and environment manager, Snakemake is a workflow manager. By combining the two programs, you can create entirely reproducible analysis pipelines. As point of note, the <a href="https://snakemake.readthedocs.io/en/stable/tutorial/tutorial.html" rel="nofollow"><strong>Snakemake tutorial</strong></a> is also one of the best programming tutorials I've gone through.
- The majority of packages on Conda are maintained by users so if you think there's a package you would like to see or maybe one that needs to be fixed, it's a great opportunity to get involved with a great group of people. I personally help maintain Bioconda and have found it really rewarding. If you're interested in contributing, you can find more information on channel specific pages (e.g. <a href="https://bioconda.github.io/contributor/index.html" rel="nofollow"><strong>Bioconda</strong></a> or <a href="https://conda-forge.org/#contribute" rel="nofollow"><strong>Conda-Forge</strong></a>) and in the <a href="https://docs.conda.io/projects/conda-build/en/latest/" rel="nofollow"><strong>Conda documentation</strong></a>.
