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
- AMSOL 7.1 (could be downloaded for free `here <https://comp.chem.umn.edu/sds/>`)