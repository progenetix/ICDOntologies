# ICDOntologies

The _ICDOntologies_ repository provides a list of mapping files in YAML format, as input for mapping combinations of ICD-O 3 Morphology and Topography codes to single [NCIt neoplasm core](https://evs.nci.nih.gov/ftp1/NCI_Thesaurus/Neoplasm/About_Core.html) entities.

The repository is being developed by the [_Theoretical Oncogenomics_](http://info.baudisgroup.org) group at the [University of Zurich](http://uzh.ch). It reflects work performed for the [arrayMap](arraymap.org) and [Progenetix](progenetix.org) resources and as part of the Global Alliance for Genomics and Health ([GA4GH](http://ga4gh.org)).

This repository contains mappings that have been manually curated and aims to be an open source for use and contibutions. 

Currently, the mappings can also be accesible through the Progenetix API as seen in the examples:

- https://progenetix.org/api/progenetix/icdmaps/icdmaps/icdom-85003,icdot-C50/ncitcodes/ <br/>
  Retrieving the matching ncit code(s) from an input of comma-separated icdom and icdot values, as key (code) : value (label) objects
- https://progenetix.org/api/progenetix/icdmaps/icdmaps/icdom-85,icdot-C50/ <br/>
  As in the example above, but by a) stemmming the query parameters and b) removing the ncitcodes format argument, the response will now be a list of matched data objects (inputs and equivalents)
