import glob

files = ["scripts/modify_files", "scripts/excel", "scripts/word"]

sources = [f + ".py" for f in files]
targets = [f + ".rst" for f in files]


def task_website():
    pages = glob.glob("*.md")
    return {
        "file_dep": pages + targets + ["conf.py", "index.rst"],
        "actions": ["sphinx-build . .build"],
        "verbosity": 2,
    }


def task_to_rst():
    """
    In an attempt of "literate programming", we directly use a documented,
    runnable(!) python file that we convert to *.rst for the website.
    """
    for source, target in zip(sources, targets):
        s = source.split("/")[1]
        yield {
            "basename": "convert via to_rst.py",
            "name": source,
            "targets": [target],
            "file_dep": [source, "scripts/to_rst.py"],
            "actions": [
                f"cd scripts && python3 {s}", # run
                f"python3 scripts/to_rst.py {source} > {target}", # convert
            ],
        }
