Docker
======

What is it?
-----------

Docker is a software to run what are called "containers". They are bundles of
software that are isolated from the main operating system. You can think of
them as fast and lightweight virtual machines.

Why should I use it?
--------------------

To be able to reproduce the computations, statistical evaluations, etc. of your
project, you need to specify all the software (including version numbers) that
was used in producing your results. Furthermore, you would like to provide
others with an easy way to set up their own environment with this set of
software ready to be used. Docker is an ideal tool to achieve this.

The containers are specified by a human-readable and version-controllable
text file (the `Dockerfile`) and can be uploaded to a central repository
(Dockerhub) that allows you and others to easily access the images you create.

How to install it
-----------------

If you're under Debian or Ubuntu, you can install Docker via apt:

    sudo apt install docker.io

If you want to run Docker as a user, you need to add yourself to the `docker` group:

    sudo gpasswd -a $USER docker

You may need to log out or reboot for this to take effect.

For other operating systems, take a look at the [official documentation](https://docs.docker.com/install/).

How to run stuff under Docker
-----------------------------

If you want to run programs under Docker, you simply say

    docker run <image-name> <command>

So for example, if I want to run my code under Ubuntu 18.04, I can do that no
matter what my actual OS is:

    docker run ubuntu:18.04 cat /etc/lsb-release

will print

    DISTRIB_ID=Ubuntu
    DISTRIB_RELEASE=18.04
    DISTRIB_CODENAME=bionic
    DISTRIB_DESCRIPTION="Ubuntu 18.04.4 LTS"

even if your computer is running Windows or Mac OSX.

This can also be useful if you want to try your code for different versions of say Python:

    docker run python:3.6 python3 -c "import sys; print(sys.version)"
    docker run python:3.7 python3 -c "import sys; print(sys.version)"
    docker run python:3.8 python3 -c "import sys; print(sys.version)"

If you want to work interactively on your container, you need to pass the
`--tty` and `--interactive` options, commonly shortened to `-ti`:

    docker run -ti ubuntu bash

So far, you could only access the files inside the container, but more often
than not you want to run the code you're currently working on that is not
bundled into a Docker image (yet). To do this, you can bind local folders to
folder names inside the container using the `--volume` option:

    docker run -v <local-dir>:<name-inside-the-container> <image-name> <command>

So if I want to run scripts from `~/code/project` inside the container, I would do this:

    docker run -v ~/code/project:/home/user/project python:3.7 python3 /home/user/project/myscript.py

All the options of `run` are documented [here](https://docs.docker.com/engine/reference/commandline/run/).

Creating your own images
------------------------

Sooner rather than later you probably want to install additional software to a
Docker image. You can build your own images based on others by writing a
`Dockerfile`. For example, say you want to use
[pandas](https://pandas.pydata.org/), which is not part of the basic python
image. Create a file called `Dockerfile` with the following content:

    FROM python:3.7
    RUN pip3 install pandas

You can probably already guess what this does. The first line says "base the
new image on the `python:3.7` image", and the second line installs pandas using
pip. To create the image, use `docker build` and the `--tag` option to give it
a name, and run this in the directory the `Dockerfile` is in:

    docker build --tag my_pandas_image .

With this new image, you can now use pandas from Docker:

    docker run my_pandas_image python3 -c "import pandas; print(pandas.__version__)"

The example `Dockerfile` is also in this repository.

Uploading your images to Dockerhub
----------------------------------

For now, you can only use `my_pandas_image` on your machine. To be able to
download it from different computers and for others to use it in reproducing
your results, you need to upload it somewhere. You can use Dockerhub for this.
We have been implicitly pulling images from Dockerhub throughout, e.g. the
`python:3.7` image.

First, you need an account for Dockerhub. Go to
[their website](https://hub.docker.com/signup) and register there. Then, login on your computer by running

    docker login

which will ask you for your username and password, and store these so that you
can push images to your account.

To push an image, it needs to be tagged correctly with your account name, so
for us this would be

    docker build --tag fb77/my_pandas_image .

where `fb77` is the username of our Dockerhub account. Substitute your
own login. Now you can upload the new image to Dockerhub using the `push` command:

    docker push

Once that is finished, you can run

    docker run fb77/my_pandas_image python3 -c "import pandas; print(pandas.__version__)"

on any computer that has an internet connection (and Docker installed).
