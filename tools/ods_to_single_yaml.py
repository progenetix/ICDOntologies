# Read mappings from ods into yaml file

from pyexcel_ods import get_data
from tqdm import tqdm
import yaml

data = get_data("../editing/progenetix_maps.ods")

table = data['Sheet1']
mapping = {}

for i in tqdm(range(0, len(table))):

    diagnosis = table[i][1]
    icdom_c = 'icdom-'+(table[i][2]).replace("/","")
    icdom = table[i][3]
    icdot_c = 'icdot-'+(table[i][4])
    icdot = table[i][5]
    #seer = 'seer:'+ str(table[i][8])
    ncit_c = 'NCIT:'+table[i][6]
    ncit = table[i][7]

    if (icdom_c, icdot_c) in mapping:
        for eq in mapping[(icdom_c, icdot_c)]['equivalents']:
            if ncit_c == eq['term_id']:
                eq['examples'].append(diagnosis)
                break
        else:
            mapping[(icdom_c, icdot_c)]['equivalents'].append(
            {
                'term_id' : ncit_c,
                'term' : ncit,
                'examples': [diagnosis]
            }
            )
        

    else:
        mapping[(icdom_c, icdot_c)] = {
            'input':[
                    {   'term_id' : icdom_c,
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
                        'term' : ncit,
                        'examples': [diagnosis]
                    }
                    ]

        }

with open('../current/icdo_ncit.yaml','w') as outfile:
    yaml.dump(list(mapping.values()), outfile, default_flow_style=False)


