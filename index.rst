.. Reproducible Computational Science documentation master file, created by
   sphinx-quickstart on Wed Apr  8 08:57:24 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Reproducible Computational Science - a Guideline
================================================


   More than 70% of researchers have tried and failed to reproduce another scientist's experiments, and more than half have failed to reproduce their own experiments. [\ `1 <https://www.nature.com/news/1-500-scientists-lift-the-lid-on-reproducibility-1.19970>`_\ ]


In the field of modeling and simulation, we can *and should* ensure reproducibility with a fully automated workflow [\ `2 <https://www.practicereproducibleresearch.org/core-chapters/2-assessment.html>`_\ ] from the input scripts to a finished document. This allows for external verification, greater trust in your results and comparative ease in reconstructing details of your own work in the future.

We would like to establish a working group within BAM that develops a wiki/handbook of possible approaches to tackle these challenges. 
Everyone should be able to access these documents and will be able to use these as a basis for future projects.
The competence center modeling and simulation will coordinate the efforts towards 
this goal, provide guidance and the infrastructure (e.g. a wiki, repositories). 
For completing the tasks itself, however, we mainly rely on the work of the interested participants.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   reproducibility.md
   example.md
   CONTRIBUTING.md
   docker.md
   pydoit.md
   snakemake.md
   conda.md
   scripts/modify_files.rst

From `BAM/jupyter-integration <https://github.com/BAMResearch/jupyter-integration>`_:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* `JupyterLab with version control <https://bamresearch.github.io/jupyter-integration/en_jupyterlab_with_version_control.html>`_
* `Using Git and TortoiseGit <https://bamresearch.github.io/jupyter-integration/en_version_control_with_git.html>`_
