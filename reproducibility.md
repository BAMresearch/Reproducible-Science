What makes scientific results reproducible?
===========================================

The idea of reproducible science is to provide not only the final results of
your research (often in the form of a paper), but also enable others to redo
your experiments and analysis. This allows for external verification, greater
trust in your results and comparative ease in reconstructing details of your
own work in the future.

So what is necessary for your computational results to be reproducible? The 
following is based loosly on
[this article](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003285),
which I would encourage you to read.


Automate everything
-------------------

You should have no manual steps in your result creation, that means codifying
everything you do. This often also replaces a lot of documentation of the sort
"click here, copy this from here to there, and rename that to xyz". There are
several ways of achieving that.

You could write a straightforward shell script in
[bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) if you're under Linux
or MacOSX, or [batch files](https://en.wikipedia.org/wiki/Batch_file) or
[Powershell](https://en.wikipedia.org/wiki/PowerShell) if you're under Windows.
This has, however, a serious drawback: all steps in your pipeline are run
again, even if that is not necessary. For example, if you only change your
postprocessing part, there is no need to run the simulation again. (You
probably could implement checks like this in your favorite shell language, but
then you're just reimplementing some of the solutions below. Don't.)

Better solutions to this are build systems, of which there are
[many](https://en.wikipedia.org/wiki/List_of_build_automation_software). The
most widely known and almost universally available (at least on Linux systems),
is [make](https://en.wikipedia.org/wiki/Make_(software)). If you're already
familiar with make and it suits your work, go with it. However, I find the
syntax dismal, and the timestamp-based decisions sometimes result in
unnecessary reruns. Python-based alternatives which we're going to use here are
[doit](pydoit.md) or [Snakemake](snakemake.md) . If you know Python, you'll 
feel right at home.


Keep everything under version control
-------------------------------------

Version control is a way of keeping track of the changes you made to your code
and why. While there are also
[many](https://en.wikipedia.org/wiki/List_of_version-control_software) version
control systems, one has emerged as the clear winner and is widely known and
supported.

Learn [Git](https://git-scm.com/) and use it habitually everywhere, all the time.


Archive your environment
------------------------

This part is quite difficult. Software changes its behaviour as newer versions
are released. To make your results reproducible, the code needs to be run with
the same version again. The least you should do is write down the version
numbers of the software that is important. But this is prone to error, likely
to become out-of-date and makes reproducing your results much more difficult
than it should be.

A better solution would be to provide a virtual machine with all the software
that you've used preinstalled. This satisfies the reproducibility requirements,
but is also cumbersome to use and archive, and not very transparent in terms of
how you've set up your environment.

A new approach is to use containers, which will allow you to easily distribute
your environmental setup along with the rest of the code, while also being
faster than virtual machines. This is discussed in detail in the
[docker](docker) section.


For Analyses That Include Randomness, Note Underlying Random Seeds
------------------------------------------------------------------

To make results that stem from computations that include randomness
reproducible, set the seed of the RNG to a fixed value.


Record intermediate results
---------------------------

This is where it gets tricky. If you're intermediate files are just a couple of
MBs, than sure, check them into Git and be done with it (use Git LFS).

For large simulations, possible approaches could be

1. Put them into \<insert-favorite-cloud-storage-provider-here\>, and make it
    clear where to find this data.
2. Take a look at [Git-Annex](https://git-annex.branchable.com/), where you can
    combine git with storing data anywhere you want (other servers, your phone,
    Dropbox, Amazon S3, USB stick, Git LFS, Bittorrent, Google Drive, IPFS, ...).
3. Just give up. At a certain scale, in situ visualization is the only feasible
    thing anyway


Provide Public Access to Scripts, Runs, and Results
---------------------------------------------------

None of the above matters in terms of me being able to reproduce your results if I'm not able to find your code/data. For code, a good approach would be to upload your repository to [Github](https://github.com/) and include the link in your paper. Use a [tag](https://git-scm.com/book/en/v2/Git-Basics-Tagging) to mark the version that created the final paper.

Additionally, you can upload your code and data to [Zenodo](https://zenodo.org/), where you'll get a DOI for it that will allow you to reference it in the future.
