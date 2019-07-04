# Read mappings from ods into yaml file

from pyexcel_ods import get_data

# TODO: input file specification

data = get_data("arrayMap&progenetix_maps.ods")
table = data['Sheet1']

import yaml
for i in range(0, len(table)):

    try:
        diagnosis = table[i][1]
        icdom_c = 'icdom-'+(table[i][2]).replace("/","")
        icdom = table[i][3]
        icdot_c = 'icdot-'+(table[i][4])
        icdot = table[i][5]
        #seer = 'seer:'+ str(table[i][8])
        ncit_c = 'ncit:'+table[i][6]
        ncit = table[i][7]


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
                }
            ],

            'examples':[
            {
                'labels' : diagnosis
            }
            ]
        }

        with open(icdom_c +','+ icdot_c +'.yaml','w') as outfile:
            yaml.safe_dump(mapping, outfile, default_flow_style=False)

    except:
        pass
