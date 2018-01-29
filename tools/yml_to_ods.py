# Script to read yml files and write an ods spreadsheet for mapping codes

import yaml
import os
import collections
from pyexcel_ods import save_data

mapp = []
mapp.append(['diagnosistext']+['icdmorphologycode']+['icdmorphology']+['icdtopographycode']+['icdtopography']+['seer']+['ncit:term']+['ncit:code'])
yamldir = '../current/'
odsdir = '../editing/'
for filename in os.listdir(yamldir): # Specify directory
    if filename.endswith("yml"):
        yamlfile = yamldir + filename
        with open(yamlfile, "r") as stream:
            data = yaml.load(stream)
            #print data
            try:
                diagnosis = [data['examples'][0]['term']]
                icdom_c = [data['input'][0]['term_id'].replace('icdom:','').replace("_","/")]
                icdom = [data['input'][0]['term']]
                icdot_c = [data['input'][1]['term_id'].replace('icdot:','').replace("_",".")]
                icdot = [data['input'][1]['term']]
                seer = [data['equivalents'][1]['term_id'].replace('seer:','')]
                ncit = [data['equivalents'][0]['term']]
                ncit_c = [data['equivalents'][0]['term_id'].replace("ncit:","")]
                mapp.append(diagnosis+icdom_c+icdom+icdot_c+icdot+seer+ncit+ncit_c)
            except:
                pass

#print mapp

mapping = collections.OrderedDict()

sheetx = {"codes":mapp}
save_data(odsdir + "table_from_yaml.ods",sheetx)
