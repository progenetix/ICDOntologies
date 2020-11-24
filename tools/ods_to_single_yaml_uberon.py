# Read mappings from ods into yaml file

from pyexcel_ods import get_data
from tqdm import tqdm
import yaml

data = get_data("../editing/progenetix_maps_uberon.ods")

table = data['Sheet1']
mapping = []

for i in tqdm(range(1, len(table))):

    icdot_c = table[i][0].strip()
    icdot = table[i][1].strip()
    uberon_c = table[i][2].strip()
    uberon = table[i][3].strip()
    
    mapping.append(
        {'input':{
                'term_id':icdot_c,
                'term': icdot
                },
        'equivalent': {
                'term_id':uberon_c,
                'term': uberon
                }
        }
    )

with open('../current/icdo_uberon.yaml','w') as outfile:
    yaml.dump(mapping, outfile, default_flow_style=False)


