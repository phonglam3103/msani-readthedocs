Usage
#####

Preparing the input file
************************

The program requires a white-space or tab-delimited file containing two columns (SMILES, moleculeID) without headers. The program also supports the Enamine file format by the added `-e` or `--enamine` flag.

.. code-block:: console
   
   COCCC(=O)Nc1ncc(s1)Br  CP000000418470
   C1CC(C(=O)NC1)SCCC=CBr  CP000000432409
   CC(C)(C)CNC(=O)c1ccsc1Br  CP000001634597
   c1c(coc1Br)C(=O)NC2CCSC2  CP000001645677
   c1c(c([nH]n1)C(=O)NCC2(CC2)N)Br  CP000001647414


Overview
************************

The pipeline contains six preparation and/or filtering steps, which can be used simultaneously to prepare the database:

This is an example of a lazy pipeline that uses all the preparation and processing steps:

.. code-block:: console

    $ msani -i example.smi --enamine --lazy  # For enamine format
    $ msani -i example.smi --lazy

    # This is equivalent to:
    # msani -i example.smi --removesalts --tautomers --pains --unwanted all --stereoisomers --protonation


By default, the program produces a new file with a **_clean** suffix. If the PAINS or unwanted filters are applied, the rejected molecules with the reason for rejection will be output with a **_rejected** suffix.

The program by default will conduct the preparation and filtering in the order below:

.. image:: _static/Workflow.png
   :width: 800px


Help message
============

**Use the** ``--help (-h)`` **flag for more information.**

.. code-block:: console

    $ msani -h

    usage: msani [-i INPUT_FILES [INPUT_FILES ...]] [-s SMILES [SMILES ...]] [-e] [-pre PREFIX] [-enrich]
                 [--removesalts] [--create_custom] [--custom CUSTOM] [--unwanted [{all,regular,special,optional} ...]]
                 [--pains] [--tautomers] [--noneutralize] [--notaurdkit] [--stereoisomers] [--max_stereoisomers]
                 [--protonation] [--pH PH] [--pH_range PH_RANGE] [--db2] [--corina] [--långben] [--numconfs] 
                 [--randomSeed RANDOMSEED] [--numcores NUMCORES] [--timeout TIMEOUT] [--nocleanup] [--energywindow]
                 [--debug] [--lazy] [--help] [--timing]
                

    MolSanitizer - A package to prepare SMILES databases

    Input and output options:
    -i, --input_files     Input files containing chemical structures
    -s, --smiles          Input SMILES strings
    -e, --enamine         Enamine input format (default: False)
    -pre, --prefix        Prefix for the output files. If not provided, the input file name will be used.
    -enrich, --enrichment Enrichment mode (do not put in db2.tgz files)

    Filtering options:
    --removesalts         Remove salts from the structures (default: False)
    --create_custom       Generate a template for customized substructure filtering
    --custom              Filter out unwanted substructures using the customized list. To generate an example list,
                          use --create_custom
    --unwanted            Filter out unwanted substructures using the default list
    --pains               Remove PAINS violations from the structures (default: False)

    SMILES processing options:
    --tautomers           Tautomers enumeration (default: False)
    --noneutralize        Do not neutralize the molecule before tautomerization (default: False)
    --notaurdkit          Do not use RDkit to canonicalize the input SMILES
    --stereoisomers       Stereoisomers enumeration (only consider unspecified chiral centers) (default: False)
    --max_stereoisomers   Maximum number of stereoisomers to consider (default: 8 = 3 stereocenters)
    --protonation         Apply protonation to the structures (default: False)
    --pH, -p              pH for the protonation (default: 7)
    --pH_range, -r        pH range for the protonation (default: 0)

    DB2 related options:
    --db2, -db2           Generate conformers and stored in the DB2 format for DOCK 3.8 (default: False)
    --corina, -c          Use Corina for 3D structure generation (default: False)
    --långben, -igtor     Ignore the Torsion Library - generate every possible conformer
    --numconfs, -nconfs   Maximum number of conformers to generate (default: 2000)
    --randomSeed, -rs     Random seed for reproducibility (default: 42)
    --numcores, -j        Number of cores to use for parallel processing (default: 4)
    --timeout, -t         Timeout for the initial embedding for each SMILES entry before using OpenBabel in minutes (default: 2)
    --nocleanup           Do not clean up the temporary files (default: False)
    --energywindow, -w    Energy window for sampling the conformations (default: 25 (kcal/mol))

    Miscellaneous:
    --debug, -d           Enable debugging mode
    --lazy                Implement all the processing and preparation steps (default: False)
    --help, -h            Show this help message and exit
    --timing              Time the process


Setting configurations
======================

Many of the default values of MolSanitizer described below, both in the SINGLE MODE and BATCH MODE can be modified in `MolSanitizer/msani_configurations.yaml <https://github.com/Isra3l/MolSanitizer/blob/main/msani_configurations.yaml>`_ file. It is for the convenience of the  user so that he/she does not have to specify the values (such as numConfs, --max_stereoisomers, etc) every time the program is run. If the user specify the values in the command line, the values in the configuration file will be overwritten.

The users are asked to provide CORINA path if the he/she wants to use it for the generation of 3D coordinates. The path should be provided in the `CORINA` field.

Below is the default configuration file:

.. code-block:: yaml
    
    #===============SINGLE MODE================
    USE_CORINA: False
    CORINA: 'Path_to_CORINA/corina'
    ENERGY_WINDOW: 25
    NUMCONFS: 2000
    MAX_STEREOISOMERS: 8
    TIMEOUT: 2

    #================BATCH MODE=================
    SLURM_ACCOUNT: 'naiss2023-3-39'
    LINES_PER_JOB: 200
    TIME_LIMIT: 96
    MAX_JOBS: 500


Available filters and preparation steps
***************************************

Remove salts
============

To use the remove salts function, simply use the ``--removesalts`` flag. The program uses a predefined salt list in `MolSanitizer/Data/salt_stripping.txt <https://github.com/Isra3l/MolSanitizer/blob/main/MolSanitizer/Data/salt_stripping.txt>`_ to remove the salts, which contain both organic and inorganic salts commonly used in medicinal chemistry.

*Caution:* If the entry is an organic salt (e.g., sodium acetate CH\ :sub:`3` COO\ :sup:`-` Na\ :sup:`+`), the whole entry will be removed.

.. code-block:: console

    $ msani -i example.smi --removesalts

Tautomers standardization
============================


The tautomers could be generated using the ``--tautomers`` flag. MolSanitizer uses a two-step approach for the enumeration of tautomers. First, the canonical tautomer from the scoring function of ``rdMolStandardize.TautomerEnumerator`` is used. Then, the exceptions are corrected using the expert-curated SMARTS rules. The SMARTS rules are readily accessible at `MolSanitizer/Data/tautomers.txt <https://github.com/Isra3l/MolSanitizer/blob/main/MolSanitizer/Data/tautomers.txt>`_.

.. code-block:: console

    $ msani -i example.smi --tautomers

PAINS filtering
===============

Molecules that contain PAINS substructures can be efficiently eliminated using the ``--pains`` flag. The violated structures will be stored in the **_rejected** file.

.. code-block:: console

    $ msani -i example.smi --pains

Example of the **_rejected** output is as below:

.. code-block:: text

    CCOc1cccc(C=C2C(=O)N(Cc3ccccc3)C(C)=C2C(=O)OC)c1O Z57339064     "PAINS violation: Ene_five_het_c(85)"
    N#Cc1ccccc1COC(=O)c1cccc2c1C(=O)c1ccccc1C2=O      Z18301252     "PAINS violation: Quinone_a(370)"
    Nc1sc2c(c1C(=O)c1ccccc1)CCC2                      Z1259205366   "PAINS violation: Thiophene_amino_aa(45)"
    COCC1(CC(=O)NCc2cc(O)ccc2O)CC1                    Z2832180283   "PAINS violation: Mannich_a(296)"
    CCCCN(Cc1ccc(OS(=O)(=O)F)cc1)Cc1ccccc1O           Z4607533150   "PAINS violation: Mannich_a(296)"

Unwanted substructures filtering
============================


Molecules that contain unwanted substructures can be efficiently eliminated using the ``--unwanted`` flag. MolSanitizer uses an expert-curated list that contains undesirable substructures, accompanied by the reasons and references for filtering. The list can be obtained from `MolSanitizer/Data/filter_out.csv <https://github.com/Isra3l/MolSanitizer/blob/main/MolSanitizer/Data/filter_out.csv>`_.

There are four options accompanied by the ``--unwanted`` flag, which are *['all', 'regular', 'special', 'optional']*. If no option is specified, the *regular* filters will be applied. The choice of the options depends on the user and can vary between targets.

.. code-block:: console

    $ msani -i example.smi --unwanted
    $ msani -i example.smi --unwanted regular  # By default
    $ msani -i example.smi --unwanted regular special
    $ msani -i example.smi --unwanted all

It is also possible to filter out customized unwanted substructures, depending on the user's preference, using a customized SMARTS list. To generate a template for this list, use the ``--create_custom`` flag. This will result in the **templates.tsv** file.

.. code-block:: console

    $ msani --create_custom

The first two columns (SMARTS and LABEL) are required for the program to parse, while the remaining columns will be omitted by the program. To filter using the customized list, use the ``--custom`` flag with the path to the customized list file. It is also possible to apply both the available filters and the customized filters.

.. code-block:: console

    $ msani -i example.smi --custom templates.tsv
    $ msani -i example.smi --unwanted all --custom templates.tsv

Protonation
============================

MolSanitizer supports the assignment of protonation states at various pH values using the ``--protonation`` flag. By default, the pH is set to 7 (configurable via ``-p`` or ``--pH``), and the pH range is set to 0 (specified using ``-r`` or ``--range``). This configuration protonates molecules at a specific pH of 7. However, it is also possible to enumerate potential protonation states across a pH range. For instance, setting ``--range 2`` explores pH values within 7 ± 2. The program evaluates each pH value in the specified range and assigns the possible protonation states of the molecule at those pH levels. Only unique products are output to a file. Functional groups with multiple protonation possibilities (e.g., piperazine, amidine) are expanded, with an underscore (`_`) appended to their names to indicate variations.

The program employs SMARTS-based reactions to iteratively assign protonation states to atoms, considering the pKa of functional groups and the queried pH. Detailed SMARTS reaction definitions are available in the following resource: `MolSanitizer/Data/ionizations.txt <https://github.com/Isra3l/MolSanitizer/blob/main/MolSanitizer/Data/ionizations_v2.txt>`_.

.. code-block:: console
    $ msani -i example.smi --protonation # Default pH 7 +- 0
    $ msani -i example.smi --protonation --pH 7 --range 2 # Enumerate protonation states at pH 7 +- 2
    $ msani -i example.smi --protonation -p 7 -r 2 # Short version


.. code-block:: text

   Input:
   O=C(N1C(C2C(C1)C2O)C(O)=O)CN3CCNCC3 mol4_editted

   Output:
   O=C([O-])C1C2C(O)C2CN1C(=O)C[NH+]1CCNCC1 mol4_1
    O=C([O-])C1C2C(O)C2CN1C(=O)CN1CC[NH2+]CC1 mol4_2


Stereoisomers enumeration
============================


Stereoisomers enumeration will be considered for unspecified chiral centers using the ``--stereoisomers`` flag. For an entry that contains multiple stereoisomers, its ID will be expanded (e.g., mol8 -> mol8.1, mol8.2).

.. code-block:: console

    $ msani -i example.smi --stereoisomers

.. code-block:: text

   Input:
   C1C2CC3CC1CC(C2)(C3O)N                            mol8

   Output:
   N[C@@]12C[C@@H]3C[C@@H](C[C@@H](C3)[C@H]1O)C2     mol8_1
   N[C@@]12C[C@@H]3C[C@@H](C[C@@H](C3)[C@@H]1O)C2    mol8_2

It is possible to define the maximum number of stereoisomers generated for each molecule by adding the ``--max_stereoisomers`` flag.

.. code-block:: console

    $ msani -i example.smi --stereoisomers --max_stereoisomers 32

DB2 generation for DOCK 3.8
============================


The DB2 format ready for docking using DOCK 3.8 can be obtained using the ``--db2`` flag. MolSanitizer employs the `srETKDG-v3 <https://pubs.acs.org/doi/10.1021/acs.jcim.0c00025>`_ (small-ring ETKDGv3) method of RDKit to generate 10 or 100 initial conformations, which will be energy minimized using the `MMFF94s <https://doi.org/10.1186/s13321-014-0037-3>`_ forcefield. Some systematic error from the MMFF94s such as the non-planarity of the aromatic nitrogen atoms are fixed using a set of constraints. In cases when RDKit takes too long to embed the molecule (2 minutes), the new embedding method of `Open Babel <https://jcheminf.biomedcentral.com/articles/10.1186/s13321-019-0372-5>`_ will be used to generate the initial conformer. 

It is now also possible to generate the initial conformation using CORINA by adding the ``--corina`` flag. The user is asked to add the path to CORINA program as well as can set the default behavior of the program to use CORINA every time in the configuration file.


The energy-minimum conformer will then be used as the initial conformer for torsional sampling using the Monte Carlo (stochastic) method.

The program employs AMSOL 7.1 for assigning the desolvation penalties and partial charges of the ligand's atoms. OpenBabel is used for the conversion of SDF and MOL2 format. 

Finally, the information from the solvation file and the MOL2 file is aggregated using the `mol2db2.py <https://github.com/ryancoleman/mol2db2>`_ program.

A modified version of `TorsionLibrary v3 <https://pubs.acs.org/doi/10.1021/acs.jcim.2c00043>`_ is used to drive the generation of conformations. The modifications made and the full library can be obtained `here <https://github.com/Isra3l/MolSanitizer/blob/main/MolSanitizer/Data/modified_tor_lib_2020.xml>`_.

.. code-block:: console

    $ msani -i example.smi --protonation --stereoisomers --db2

It is possible to define the maximum number of conformers generated by MolSanitizer using the ``-nconfs`` or ``--numconfs`` flag (default: 2000). By default, the intermediate files (such as files for solvation and generation of initial conformations) are deleted. To prevent this, use the ``--nocleanup`` flag. The user is also able to define the timeout for the RDKit embedding using the ``--timeout`` flag (default: 2 minutes).


Running in batch mode
*********************


MolSanitizer now supports the batch mode ``msani_batch``, which allows handling bigger SMILES databases on the SLURM-based cluster. Nearly all the flags supported by the standalone MolSanitizer are supported by the batch mode. In principle, ``msani_batch`` will split the input file into chunks of smaller input files, which is defined by the ``-l`` or ``--lines_per_job`` flag (default: 200). The split files will then be submitted to the SLURM cluster using an array of jobs. By default, a maximum of 100 jobs will be submitted simultaneously to avoid interfering with other users within the same project, but you can change this limit with the ``--max_jobs`` flag.

The additional flags supported by ``msani_batch`` so far:

.. code-block:: console

    -n, --projectName           The account that will be charged by the SLURM cluster for running tasks (default: naiss2023-3-39)
    -l, --lines_per_job         Number of lines to process per job (default: 200)
    -t, --time                  Time limit in hours for each SLURM job (default: 96)
    --max_jobs                  Maximum number of jobs to run simultaneously (default: 500)

Usage
=====

.. code-block:: console

    $ msani_batch -i example.smi -l 50 --db2
    $ msani_batch -i example.smi -l 50 --stereosiomers --protonation --db2 --nocleanup
    $ msani_batch -i example.smi -l 50 -n snic2021-3-32 -t 2 --db2

It is also possible to submit the batch jobs for multiple input files. The program will automatically detect the input files and submit the jobs accordingly.

.. code-block:: console

    $ msani_batch -i example.smi example2.smi --db2 --protonation --stereoisomers


