![build](https://github.com/BAMresearch/Reproducible-Science/workflows/Python%20package/badge.svg)

Reproducible Science Template
=============================

> More than 70% of researchers have tried and failed to reproduce another scientist's experiments, and more than half have failed to reproduce their own experiments. [[1]]

In the field of modeling and simulation, we can *and should* ensure reproducibility with a fully automated workflow [[2]] from the input scripts to a finished document. This allows for external verification, greater trust in your results and comparative ease in reconstructing details of your own work in the future.

We would like to establish a working group within BAM that develops a wiki/handbook of possible approaches to tackle these challenges. 
Everyone should be able to access these documents and will be able to use these as a basis for future projects.
The competence center modeling and simulation will coordinate the efforts towards 
this goal, provide guidance and the infrastructure (e.g. a wiki, repositories). 
For completing the tasks itself, however, we mainly rely on the work of the interested participants.

[1]: https://www.nature.com/news/1-500-scientists-lift-the-lid-on-reproducibility-1.19970
[2]: https://www.practicereproducibleresearch.org/core-chapters/2-assessment.html


# Website with further information

Visit https://BAMresearch.github.io/Reproducible-Science/ for further content or build the sphinx-based website locally by running `doit` (see [requirements](requirements.txt)).

# Run the example

To run the example, you can first start our docker container

~~~sh
<host> cd <root of this git repository>
<host> sudo docker run -ti -v $(pwd):/repro fb77/reproducible
~~~

in an interactive terminal (`-ti`) and with the current directory (`$(pwd)` - use `${PWD}` (curly brackets!) on windows powershell) available at `/repro` within the container. You are now in the `fb77/reprodicble` docker container. To start the pydoit script, run

~~~sh
<docker> cd repro/example
<docker> doit
~~~


---

Alternatively, you can combine all the steps above into one command
~~~sh
<host> sudo docker run -v "$(pwd)":/repro fb77/reproducible /bin/bash -c "cd repro/example && doit"
~~~

