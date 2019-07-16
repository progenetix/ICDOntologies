# podmd
# Script to read yml files and write an ods spreadsheet for mapping codes
# end_podmd

import yaml
import os
import collections
from pyexcel_ods import save_data

mapp = []
mapp.append(['diagnosistext']+['icdmorphologycode']+['icdmorphology']+['icdtopographycode']+['icdtopography']+['ncit:term']+['ncit:code'])
yamldir = '../current/'
odsdir = '../editing/'
for filename in os.listdir(yamldir): # Specify directory
    if filename.endswith("yaml"):
        yamlfile = yamldir + filename
        with open(yamlfile, "r") as stream:
            data = yaml.load(stream)
            #print data
            try:
                diagnosis = [data['examples'][0]['labels']]
                icdom_c = [data['input'][0]['id'].replace('icdom-','')]
                icdom = [data['input'][0]['label']]
                icdot_c = [data['input'][1]['id'].replace('icdot-','')]
                icdot = [data['input'][1]['label']]
                #seer = [data['equivalents'][1]['id'].replace('seer:','')]
                ncit = [data['equivalents'][0]['label']]
                ncit_c = [data['equivalents'][0]['id'].replace("ncit:","")]
                mapp.append(diagnosis+icdom_c+icdom+icdot_c+icdot+seer+ncit+ncit_c)
            except:
                pass

#print mapp

mapping = collections.OrderedDict()

sheetx = {"codes":mapp}
save_data(odsdir + "table_from_yaml.ods",sheetx)
