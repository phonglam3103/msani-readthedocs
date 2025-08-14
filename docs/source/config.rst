.. _config:
Config file
============

The config file is designed to be reused across different projects. It is a YAML file that contains the configuration for the MolSanitizer tool. The file can be customized to suit specific needs, such as defining the chemical space of interest, setting up the protonation, tautomerization, 3D generation options, and specifying the output format.


Nearly all the options are available, except ones that are designed to be triggered once only like `--version`, `--help`, or `--smiles`.


The keywords in the config file need to match that with the long_name of the command line options. For example, if you want to set the `--protonation` option, you would use `protonation: true` in the config file. 

To create a template for the config file, you can run the following command:

.. code-block:: console

    $ msani --create_config

The file will be created in the current working directory with the name `config.yaml`. You can then edit this file to customize the settings for your project. Here is the template of the config file:

```
    # Input-output options
    input_files: [file1.smi, file2.smi]
    extended: false

    # Filtering options (other options include hba, hbd, mw, chiral)
    removesalts: false
    unwanted: [regular, optional]
    pains: false
    # ha: 17-25
    # logp: 350

    # SMILES processing options
    tautomers: true
    protonation: true
    pH: 7
    pH_range: 0
    # prot_lib: None #In case of modified protonation library
    # tau_lib: None  # In case of modified tautomer library

    # Conformer generation options
    # gen3d: false
    # format: [db2.tgz]
    # method: rdkit
    # numconfs: 2000
    # energywindow: 25
    # rigid: None
    # torsion: None # In case of modified torsion definitions
```
