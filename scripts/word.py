"""
Interacting with MS Word
------------------------

One use case in reproducible science that works great in the context of
LaTeX files is the separation of text and images, where the images are
generated automatically in separate workflows. For MS Word, the challenge
is to update images of a document automatically.

A MS Word document is basically a zip file containing a text layer and a 
picture layer. Those pictures are, if unzipped, stored in word/media and can 
be accessed via

"""
import zipfile

z = zipfile.ZipFile("report.docx")
all_files = z.namelist()
images = [f for f in all_files if f.startswith("word/media/")]
print(images)

"""
You can now modify the contents (actually creating a new zip file) to replace 
one of the images with another one. This is conveniently done by the provided
``class UpdatableZipFile`` (web search: *python replace file in zip* lead to 
https://stackoverflow.com/a/35435548 )

You can direcly overwrite the *report.docx*, but we chose to work on a copy of
it (*report_modified.docx*) here.

"""

from updateable_zip_file import *

shutil.copy("report.docx", "report_modified.docx")

new_images = [  # order matters!
    "dummy_images/red.png",
    "dummy_images/blue.png",
    "dummy_images/gray.png",
    "dummy_images/green.png",
]

with UpdateableZipFile("report_modified.docx", "a") as o:
    for new, old in zip(new_images, images):
        o.write(new, old)

"""
The big inconvenience is that you cannot recover the image names from 
the \*.docx file, so you have to rely on the ordering.

**Comment (TTitscher):** As the MS Excel/Word is not part of my daily work, I
have no experience how the methods above perform in practice. However, I 
believe that this topic is important and I suggest forming a working group
(lead by someone else) that investigates the methods further.
"""
