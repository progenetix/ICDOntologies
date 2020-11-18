# ICDOntologies

The _ICDOntologies_ repository provides a list of mapping files in YAML format, as input for mapping combinations of ICD-O 3 Morphology and Topography codes to [NCIt neoplasm core](https://evs.nci.nih.gov/ftp1/NCI_Thesaurus/Neoplasm/About_Core.html) entities.

The repository is being developed by the [_Theoretical Oncogenomics_](http://info.baudisgroup.org) group at the [University of Zurich](http://uzh.ch). It reflects work performed for the [arrayMap](http://arraymap.progenetix.org) and [Progenetix](http://progenetix.org) resources and as part of the Global Alliance for Genomics and Health ([GA4GH](http://ga4gh.org)).

This repository contains mappings that have been manually curated and aims to be an open source for use and contibutions. 

## API Access

The mappings can be accessed through the [Progenetix API](https://info.progenetix.org/doc/services/ontologymaps.html), as seen in these examples:

* [progenetix.org/services/ontologymaps/?filters=icdom-85003,icdot-C50.9](https://progenetix.org/services/ontologymaps/?filters=icdom-85003,icdot-C50.9)  
    - Retrieving the matching ncit code(s) from an input of comma-separated icdom and icdot values, as key (code) : value (label) objects
* [progenetix.org/services/ontologymaps/?filters=icdom-85,icdot-C50&filterPrecision=start](https://progenetix.org/services/ontologymaps/?filters=icdom-85,icdot-C50&filterPrecision=start)  
    - As in the example above, but by stemmming the query parameters the response will now be a list of matched data objects (inputs and equivalents)
    
Further documentation about the Progenetix API can be accessed through the resource's [documentation pages](https://info.progenetix.org/tags/API.html).
