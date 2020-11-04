Conda
====

What is it?
-----------

[Conda](https://docs.conda.io/en/latest/) is a package/dependency management system that allows users to create reproducible computing environments for their analysis. It was originally developed for Python libraries, but has since been extended to also handle other software. It works with `environments` in which software is installed and that are (mostly) separated from the operating system. 

Why should I use it?
--------------------

Conda allows you to separate the execution environment for different projects and explicitly control the version of each software in the environment independently of the operating system software management. This means you can have 
- different versions of the same software for each project (it its own environment) without causing conflicts  
- explicitly control the version of each software in your analysis to ensure reproducibility and prevent changes in results caused by version changes  
- install software that might not be available from the package management of your operating system  

Installation
------------

Conda can be installed as part of the [Miniconda](https://docs.conda.io/en/latest/miniconda.html) package. It works on Windows, MacOSX and Linux. See the website for further installation instructions.  

Channels
--------
Software packages for conda (also called `recipes`) are provided in repositories called `channels`. Channels can be created by anyone and many organizations or even individual researchers maintain their own channels. By default conda will install packages from the main channel at [anaconda.com](https://repo.anaconda.com/pkgs/), but you specify other channels, when installing packages (see below). Useful channels include [`conda-forge`](https://anaconda.org/conda-forge) for community maintained packages, [`r`](https://anaconda.org/r) for R packages, and [`bioconda`](https://anaconda.org/bioconda) for bioinformatics packages. You can use the search on the [Anaconda main page](https://anaconda.org/) to search for channels, that provide a certain package. Just remember, that anyone can provide a channel and make sure that the channel is reliable.

Managing your environments
--------------------------
This is only a short introduction on managing you environments. For full details see the conda documentation on this topic [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

### Creating an empty environment
~~~sh
conda create -n exampleEnv
~~~
The easiest way to create an environment is to just specify its name (with `-n`). This will create an empty environment in that you can install packages late (see below).  

### Activating (entering) an environment
To work with your environment, you have to activate it. While an environment is activated all packages that were installed into it are available as if the were installed system wide.  
To activate your newly created environment you use:
~~~sh
conda activate exampleEnv
~~~
Depending on your conda installation, this might not work. In this case on Linux you can try:
~~~sh
source activate exampleEnv
~~~
After the environment is activated the command prompt of your terminal should change to include the name of the environment for example it might look like this:
~~~sh
(exampleEnv) heeger@lagoa:~$
~~~

### Deactivating (leaving) an environment
You can deactivate an environment with the command:
~~~sh
conda deactivate
~~~

### Installing packages in an environment
Once you activated an environment you can install additional packages withe `install` command. For example to install `doit` use:
~~~sh
conda install doit
~~~
You can specify the version of the package you want to install like this:
~~~sh
conda install doit=0.33.1
~~~
And you can install multiple packages at once (with partially explicit version requirements) like this:
~~~sh
conda install doit=0.33.1 numpy
~~~

### Creating an environment with packages
You can also create an environment and install packages into it in one command:
~~~sh
conda create -n exampleEnv doit=0.33.1 numpy
~~~

### Using different channels
If you want to install packages from other `channels` you can use the `-c` option in your command:
~~~sh
#from within a environment
conda install -c conda-forge biopython=1.78
#or when creating the environemnt
conda create -n exampleEnv -c conda-forge biopython=1.78
~~~

### Creating environments from a file
To share environments it can be useful to define them in a yaml file, which can be easily shared and create the environment from the file. For example create a file called `exampleEnv.yaml` with the following content:
~~~yaml
name: exampleEnv
channels:
    - conda-forge
    - bioconda
dependencies:
    - biopython=1.78
    - bioconductor-mgsa=1.38.0
~~~

The environment can be create form this file with the command:
~~~sh
conda env create --file exampleEnv.yaml
~~~