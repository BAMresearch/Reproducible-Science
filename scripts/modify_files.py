"""
Modifying files in python
=========================

Simple text files like ``parameters.txt``

.. literalinclude:: parameters.txt
   :linenos:

can easily be read (``"r"``) via

"""
with open("parameters.txt", "r") as prm_file:
    for line in prm_file:
        name, value = line.split("=")
        if name == "P2":
            print("[parameters.txt]  value of P2 is", float(value))

"""

Other file formats like `YAML <https://pyyaml.org/wiki/PyYAMLDocumentation>`_ or
`JSON <https://docs.python.org/3/library/json.html>`_ offer a more convenient access. For example, modifying the ``parameters.yaml``

.. literalinclude:: parameters.yaml
   :linenos:

requires ``pip3 install pyyaml`` and is done by
"""
import yaml

with open("parameters.yaml", "r") as prm_file:
    prm = yaml.load(prm_file, Loader=yaml.FullLoader)
prm_E = prm["Material parameters"]["E"]
assert prm_E["unit"] == "MPa"
print("[parameters.yaml] value of E is", prm_E["value"])

"""

Writing YAML is done via 

"""
prm_E["value"] = 17840.2
with open("parameters_modified.yaml", "w") as prm_file:
    yaml.dump(prm, prm_file)

"""
.. literalinclude:: parameters_modified.yaml
   :linenos:
"""

# .. include:: excel.rst
# .. include:: word.rst
