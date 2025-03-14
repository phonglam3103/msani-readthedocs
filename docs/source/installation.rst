Installation
=====

.. _installation:

Dependencies
------------

EirVS is built upon the following packages:

- RDKit 2024.09.1 (`Reference <https://www.rdkit.org/docs/Install.html>`_)

- OpenBabel 3.1.1 (`Reference <https://openbabel.org/docs/dev/Installation/install.html>`_)

- Mol2DB2 (`Reference <https://github.com/ryancoleman/mol2db2>`_)

- AMSOL 7.1 (`Reference <https://comp.chem.umn.edu/sds/>`_)

By default, conda will install all the dependencies, except for AMSOL, which is required for the generation of DB2 files. The user is asked to download and compille the source code from the `official website <https://comp.chem.umn.edu/sds/>`_. Instruction on how to compile on modern systems is provided in the EirVS/amsol directory.

For the early evaluation, the compiled version of AMSOL is provided in the EirVS directory.

Installation
------------

We will set up the environment using `Anaconda <https://docs.anaconda.com/anaconda/install/index.html>`_.


.. code-block:: console

   $ git clone https://github.com/phonglam3103/EirVS.git
    

Example of how to set up a working conda environment to run the code:

.. code-block:: console
   
   $ conda env create -f EirVS/environment.yml
   $ conda activate eirvs
   $ pip install -e EirVS


Testing
-------

EirVS uses `unittest <https://docs.python.org/3/library/unittest.html>`_ for testing. To run the tests, use the following command:

In the same folder as previous steps, use:

.. code-block:: console

   $ python -m unittest EirVS/test/test_eirvs.py

The test takes around 1-2 minutes to complete.