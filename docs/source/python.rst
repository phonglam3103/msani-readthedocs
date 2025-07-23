Python scripting
========
.. _python:

MolSanitizer is designed to be used as a Python package, allowing users to integrate its functionalities into their own scripts or applications. The package provides a set of functions and classes that can be imported and utilized for various molecular preparation tasks. There are several classes that can be used by the users, including:

- **Msani** 

The Msani class is the main entry point for using MolSanitizer. It provides methods for preparing molecules, and applying filters. Users can create an instance of this class and call its methods to perform various tasks.

.. code-block:: python

    import pandas as pd
    from msani.api import Msani
    
    df = pd.DataFrame({
            'smiles': smiles,
            'ids': names,
            'highlights': canonical_smiles,
        })

    # Process with msani
    molsani = Msani(removesalts = True,
                tautomers = True,
                protonation = True,
                pH = 7,
                unwanted = 'regular',
                pains = True, 
                stereoisomers=stereoisomers)
    processed_df = molsani.run(df)

- **Ionizer**

- **Tautomerizer**

- **Filters**

- **ConformerGenerator**