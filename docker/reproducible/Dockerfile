# Thanks to Christoph Pohl for setting this up!

FROM debian:10-slim

# Pydoit and Fenics
RUN apt-get update && apt-get install -y --no-install-recommends wget perl-modules libperl5.28 ca-certificates python3-gdbm python3-doit fenics libfontconfig1 python3-matplotlib g++
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Paraview
RUN wget -nv "https://www.paraview.org/paraview-downloads/download.php?submit=Download&version=v5.8&type=binary&os=Linux&downloadFile=ParaView-5.8.0-osmesa-MPI-Linux-Python2.7-64bit.tar.gz" -O paraview.tar.gz
RUN mkdir /opt/paraview
RUN tar xf paraview.tar.gz -C /opt/paraview --strip-components=1
ENV PATH=/opt/paraview/bin:$PATH

# Latex
RUN wget -nv http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz -O install-tl-unx.tar.gz
RUN mkdir install-tl
RUN tar xf install-tl-unx.tar.gz -C install-tl --strip-components=1
COPY texlive.profile texlive.profile
RUN install-tl/install-tl --profile texlive.profile --location ftp://ftp.fu-berlin.de/tex/CTAN/systems/texlive/tlnet/
ENV PATH=/usr/local/texlive/2018/bin/x86_64-linux:$PATH
RUN tlmgr update --all
RUN tlmgr install latexmk koma-script lipsum graphics latex-bin xetex fontspec pgf xcolor epstopdf-pkg geometry
