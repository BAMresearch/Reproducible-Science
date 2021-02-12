Contributing
============

First, thank you for considering contributing!


Why?
- share your knowledge to others
- improve the quality of this project
- document your activities and collaboration in the project

... to the website
------------------

There are several ways you can contribute. If you are not (and do not want to get) familiar 
with github, you can simply open an issue with requested changes or send us an e-mail. However,
we encourage everyone to participate directly via [pull requests](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

### ... via the github.com web-interface:

- modify an existing 
[*.md](https://en.wikipedia.org/wiki/Markdown) file
via the github.com web interface
  - when saving (bottom of the page), create a new branch with your change
  - create a pull request

- create a new *.md file with your contribution
  - do not forget to add the new file to the [table of contents](https://github.com/BAMresearch/Reproducible-Science/blob/master/index.rst)

### ... via a git commit

The options above do not grant the option to visually check the changes you made on the website. 
For more complex changes like including hyperlinks, images, etc. however, you may want to check
a preview of the website. This can be done by building it locally. After installing the 
[dependencies](https://github.com/BAMresearch/Reproducible-Science/blob/master/requirements.txt),
the commandline tool `doit` (started in the root of the locally cloned repository) will build the
website and `xdg-open <repo_root>/.build/index.html` should display it. This "make website" workflow
is run via GitHub Actions on every push to the project, so it should work under Ubuntu/Linux. No guarantees
for Windows though.

> Note that `doit auto` conveniently rebuilds the website after every change you make and you only need
to refresh your browser to see your changes.

From here, edit your files locally, push them to a new branch and file a pull request. 
