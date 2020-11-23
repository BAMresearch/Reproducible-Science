A complete, executable example
==============================

In the `example/` folder, you'll find a complete example of how a reproducible
pipeline might look like. To execute the code, just run `doit` in the `example/`
directory and `doit show` to display the finished document.

Specifically, its a finite element simulation using
[FEniCS](https://fenicsproject.org/), a postprocessing step using
[Paraview](https://www.paraview.org/) and the final mock paper is created with
[LaTeX](https://www.latex-project.org/). The details of how this is put
together can be found in the subdirectories:

`example/`

- the main `dodo.py` file that wires/automates all actions required to display 
  the publication-ready document

`example/computation/`

- scripts needed to run the simulations, e.g. via [`docker`](docker.md)
- raw result files

`example/plots/`

- scripts needed for postprocessing that usually take data from `computation/` 
- publication-ready images (pdfs/pngs/...)

`example/tex/`

- tex code that usually takes the images from `plots/`
