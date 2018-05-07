# Read mappings from ods into yaml file

from pyexcel_ods import get_data

# TODO: input file specification

data = get_data("manual_mapping.ods")
table = data['Sheet1']

import yaml
for i in range(0, len(table)):

    try:
        diagnosis = table[i][0]
        icdom_c = 'icdom:'+(table[i][1]).replace("/","_")
        icdom = table[i][2]
        icdot_c = 'icdot:'+(table[i][3]).replace(".","_")
        icdot = table[i][4]
        seer = 'seer:'+ str(table[i][5])
        ncit = table[i][6]
        ncit_c = 'ncit:'+table[i][7]

        mapping = {
            'input':[
                {'term_id' : icdom_c,
                'term' : icdom
                },
                {
                    'term_id' : icdot_c,
                    'term' : icdot
                }
            ],

            'equivalents':[
                {
                    'term_id' : ncit_c,
                    'term' : ncit
                },
                {
                    'term_id' : seer
                }
            ],

            'examples':[
            {
                'label' : diagnosis
            }
            ]
        }

        with open((icdom_c).replace("/","_").replace(":","_") +','+ ((icdot_c).replace("/","_").replace(":","_")) +'.yaml','w') as outfile:
            yaml.safe_dump(mapping, outfile, default_flow_style=False)

    except:
        pass
