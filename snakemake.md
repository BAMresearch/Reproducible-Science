Snakemake
=========


What is it?
-----------
`Snakemake` is a python based workflow management system that allows for whole analysis pipelines to be automatized.
It lets you define workflows as a set of rules that state how to produce one or more output files from one or more input files.
Dependencies between rules will be automatically inferred on execution and independent rules will be evaluated in parallel.
If the output files for a rule are newer than the input files it will not be executed again.
Snakemake can directly use conda or docker for reproducible software environments.  


Why should I use it?
--------------------
Snakemake allows to automatize data analysis.
On the one hand this means that analysis can be quickly repeated if necessary (e.g. when new data is available).
On the other hand automation drastically reduces the potential for human error.
The rule-based structure of Snakemake enforces a modular design, that improves organization of the code and helps with reusability of analysis steps.
Additionally the integration with conda allows for automatic installation of required software as well as the explicit selection and documentation of software versions, which is necessary for reproducibility.


Installation
------------
Snakemake can be installed via `conda`:
~~~sh
conda install -c conda-forge snakemake
~~~
or via `pip`
~~~sh
pip install snakemake
~~~
Note that some of the more advances features (like report generation) might not be available when you install via `pip`.

Basic use
---------
Snakemake has many features and options. This is only a very small introduction. You can find the full documentation [here](https://snakemake.readthedocs.io).  
   
A Snakemake workflow consist of a set of rules that are implicitly linked by their input and output files.
A rule normally has at least one input file, at least one output file and defines how to produce one from the other.
A minimal toy example (that just copies a file) might look like this:
~~~python
rule exampleCp1:
    input: "inFile.txt"
    output: "outFile.txt"
    shell:
        "cp {input} {output}"
~~~
Here the actual process of the rule is defined with the `shell` keyword. This means the following string will directly be interpreted as a command to the shell.  
The curly brackets in `{input}` and `{output}` mark them as wildcards.
They will be replaced with all the input and all the output files.
In cases with more the one input/output file they can be referenced by position or by a given name like this:
~~~python
rule mergeExample:
    input: "input1.fastq", "input2.fastq"
    output: merged="mergedOut.fasta", notMerged1="unmerged1.fastq", notMerged2="unmerged2.fastq"
    shell:
        "vsearch --fastq_mergepairs {input[0]} --reverse {input[1]} --fastqout_notmerged_fwd {ouput.notMerged1}  --fastqout_notmerged_rev {output.notMerged2} {output.merged}"
~~~
Instead of giving a shell command you can also add python code directly or call python or R scripts. To add python code in the Snakemake file you can use the `run` keyword:
~~~sh
rule exampleCp2:
    input: "inFile.txt"
    output: "outFile.txt"
    run:
        with open(ouput[0], "w") as out:
            for line in input[0]:
                 out.write(line)
~~~
This should only ever be used for very short snippets of code. It is good practice to put your python code into its own script file. For the above example the python script (`exampleCp3.py`) would look like this:
~~~python
with open(snakemake.ouput[0], "w") as out:
    for line in snakemake.input[0]:
         out.write(line)
~~~
And the rule (using the `script` keyword) calling it would be:
~~~sh
rule exampleCp2:
    input: "inFile.txt"
    output: "outFile.txt"
    script:
        "exampleCp3.py"
~~~

To find out in which order your rules have to be executed Snakemake will compare input and output file names of rules and link them accordingly. 
As a starting point it will use the first rule in the file.
Therefore it is common practice to define a `all` rule as the first in the file, that has as inputs the files that should be produced in the end.

For example here is a workflow with three simple rules and an `all` rule:
~~~sh
rule all:
    input: "fileE.txt"

rule firstRule:
    input: "fileA.txt"
    output: "fileB.txt"
    shell:
        "cp {input} {output}"

rule secondRule:
    input: "fileB.txt", "fileC.txt"
    output: "fileD.txt"
    shell:
        "paste {input[0]} {input[1]} > {ouput}"

rule thirdRule:
    input: "fileD.txt"
    output: "fileE.txt"
    shell:
        "cp {input} {output}"
~~~

This would define a workflow looking like this:

~~~
  fileA.txt ──> fileB.txt ─┐
                           │
                           ├──> fileD.txt ──> fileE.txt
                           │
  fileC.txt ───────────────┘
~~~

If you write your rules into a file called `Snakefile` you can then execute them by just calling
~~~sh
snakemake
~~~
in the folder where the file is. If you give your file a different name (e.g. `main.snakemake.py`), you have to use the `-s` option to execute your worklflow:
~~~sh
sankemake -s main.snakemake.py
~~~

Wildcards
---------
In many cases you want a rule executed for multiple files (e.g. different samples).
You can use wildcards in input and output file names to achieve this.
For example:
~~~python
rule exampleWildcards:
    input: "sample{sNr}.txt"
    output: "sample{sNr}_filtered.txt"
    shell:
        "grep \"YES\" {input} > {output}"
~~~

If you want to run this for sample 1-4 you can write your `all` rule like this:
~~~python
rule all:
    input: expand("sample{sNr}_filtered.txt", sNr=[1,2,3,4])
~~~
You can also use multiple wildcards in one file name and use wildcards as values in your command, for example to try out different values for parameters for the filtering in the example above:

~~~python
rule all:
    input: expand("sample{sNr}_filtered_{value}.txt", sNr=[1,2,3,4], value=["YES", "TRUE", "OK"])

rule exampleWildcards2:
    input: "sample{sNr}.txt"
    output: "sample{sNr}_filtered_{value}.txt"
    shell:
        "grep \"{wildcards.value}\" {input} > {output}"
~~~
The `expand` command will create all combinations of the entries of both lists.

Parallelization
---------------
Snakemake will by default only use one thread, but you can use the `-j` option to give it access to multiple cores. In this case independent rules will be executed in parallel automatically. In addition you can use multiple threads in one rule if the software you are using supports it using the `threads` keyword. Here is a hypothetical example:
~~~python
rule exampleParallel:
    input: "inFile.txt"
    output: "outFile.txt"
    threads: 8
    shell:
        "parallelProgram -o {output} -t {threads} {input}"
~~~
If you run this example with `-j 8`, eight cores will be used to run `parallelProgram`. If you use `-j 4`, the rule will automatically only use four threads. If you use `-j 16`, two instances of the rule will be evaluated in parallel, if they are independent.

Parametrization
---------------
You can obviously hard code command line parameters into the command you give to the `shell` command, but it is better to use the `params` keyword to have them all in one place:
~~~python
rule clusterExample:
    input: "data.tsv"
    output: "clusters.txt"
    params: k=4, dist="euclidean"
    shell:
        "kMeansCluster -k {params.k} -d {params.dist} -o {output} {input}"
~~~
You can also store all parameters in a separate configuration file (yaml or json). For the example above you could have a config file `config.json`:
~~~json
{
 "k": 4,
 "dist": "euclidean"
}
~~~
The snakefile could than look like this:
~~~python
configfile: "config.json"

rule clusterExample2:
    input: "data.tsv"
    output: "clusters.txt"
    shell:
        "kMeansCluster -k {config[k]} -d {config[dist]} -o {output} {input}"
~~~

Conda integration
-----------------
Snakemake offers direct integration with [conda](https://docs.conda.io), which allows to fix software versions as well as  automation of installation.
For this you have to create a conda environment file that defines the software, the version you want and the conda `channel` it can be found in (if not the default).
For example for [Blast](https://blast.ncbi.nlm.nih.gov/Blast.cgi) this environment file (`blast.yaml`) would look like this:
~~~yaml
channels:
 - bioconda
dependencies:
 - blast=2.9.0
~~~
To use this environment in your Snakemake workflow, use the `conda` keyword:
~~~python
rule clusterExample:
    input: query="sequences.fasta", db="nt"
    output: "balast_hits.txt"
    conda:
        "blast.yaml"
    shell:
        "blastn -query {input.query} -db {input.sb} -out {output}
~~~
To run this using conda you have to use the `--use-conda` option when you execute sankemake:
~~~sh
snakemake --use-conda
~~~
Snakemake will then use conda (which has to be installed) to automatically install Blast and run it.

Other features
--------------
Snakemake is a powerful tool, that offers many additional features. You can find more details in the [documentation](https://snakemake.readthedocs.io). Interesting features include:
 * [Cluster](https://snakemake.readthedocs.io/en/stable/executing/cluster.html) and [cloud](https://snakemake.readthedocs.io/en/stable/executing/cloud.html) execution
 * Automated [report generation](https://snakemake.readthedocs.io/en/stable/snakefiles/reporting.html)
 * [Modularization](https://snakemake.readthedocs.io/en/stable/snakefiles/modularization.html) with wrappers and sub-workflows
 * Automated config file [validation](https://snakemake.readthedocs.io/en/stable/snakefiles/configuration.html#validation)
