Usage
=====
Preparing the input file
------------------------

The program requires a white-space or tab-delimited file containing two columns (SMILES, moleculeID) without headers. The program also supports the Enamine file format by the added `-e` or `--enamine` flag.

```
COCCC(=O)Nc1ncc(s1)Br  CP000000418470
C1CC(C(=O)NC1)SCCC=CBr  CP000000432409
CC(C)(C)CNC(=O)c1ccsc1Br  CP000001634597
c1c(coc1Br)C(=O)NC2CCSC2  CP000001645677
c1c(c([nH]n1)C(=O)NCC2(CC2)N)Br  CP000001647414
```

Running in batch mode
---------------------

MolSanitizer now supports the batch mode ``msani_batch``, which allows handling bigger SMILES databases on the SLURM-based cluster. Nearly all the flags supported by the standalone MolSanitizer are supported by the batch mode. In principle, ``msani_batch`` will split the input file into chunks of smaller input files, which is defined by the ``-l`` or ``--lines_per_job`` flag (default: 1000). The split files will then be submitted to the SLURM cluster using an array of jobs. By default, a maximum of 100 jobs will be submitted simultaneously to avoid interfering with other users within the same project, but you can change this limit with the ``--max_jobs`` flag.

The additional flags supported by ``msani_batch`` so far:

.. code-block:: console

    -n, --projectName           The account that will be charged by the SLURM cluster for running tasks (default: naiss2023-3-39)
    -l, --lines_per_job         Number of lines to process per job (default: 50)
    -t, --time                  Time limit in hours for each SLURM job (default: 2)
    --max_jobs                  Maximum number of jobs to run simultaneously (default: 100)

The default values of these additional flags can be modified in the `MolSanitizer/batch_configurations.yaml <https://github.com/your-repo/MolSanitizer/blob/main/batch_configurations.yaml>`_ file.

**Usage**:

.. code-block:: console

    msani_batch -i example.smi -l 50 --db2
    msani_batch -i example.smi -l 50 --stereosiomers --protonation --db2 --nocleanup
    msani_batch -i example.smi -l 50 -n snic2021-3-32 -t 2 --db2

**Expected Output**:

.. code-block:: console

    Starting MolSanitizer in batch mode

    Using project name (-p): snic2021-3-32
    Time limit for each job (-t): 2 hours
    Maximum number of jobs running parallel (--max_jobs): 100
    Number of compounds per job (-l): 50 lines

    Submitting 9 jobs

