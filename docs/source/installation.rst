Installation
=====

.. _installation:

CONDA environment (recommended)
------------

We will set up the environment using `Anaconda <https://docs.anaconda.com/anaconda/install/index.html>`_.


.. code-block:: console

   $ git clone https://github.com/Isra3l/MolSanitizer.git
    

Example of how to set up a working conda environment to run the code:

.. code-block:: console
   
   $ conda env create -f MolSanitizer/environment.yml
   $ conda activate msani
   $ pip install -e MolSanitizer


Dependencies
------------

MolSanitizer is built upon the following packages:
- RDKit 2024.09.1 (`Reference <https://www.rdkit.org/docs/Install.html>`_)
- OpenBabel 3.1.1 (`Reference <https://openbabel.org/docs/dev/Installation/install.html>`_)
- Mol2DB2 (`Reference <https://github.com/ryancoleman/mol2db2>`_)
- AMSOL 7.1 (`Reference <https://comp.chem.umn.edu/sds/>`_)

By default, pip will install all the dependencies, except for AMSOL, which is licensed under the Apache License, Version 2.0. The user is asked to download and compille the source code from the `official website <https://comp.chem.umn.edu/sds/>`_.
