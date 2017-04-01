
# coding: utf-8

# In[32]:

get_ipython().run_cell_magic(u'bash', u'', u'\ngrep -E \'^ {2,6}"\' request.json')


# In[33]:

get_ipython().run_cell_magic(u'bash', u'', u'\nhead request.json')


# In[87]:

import json
jsonFile = open('request.json', 'r')
values = json.dumps(jsonFile)
[x.encode('utf-16') for x in jsonFile]

jsonFile.close()

columns = []
for status in values['statuses']:
    for value, key in statuses.iteritems():
        columns = values['statuses'];

requestData = values['statuses'];
type(requestData)
        


# In[45]:

import json
jsonFile = open('request.json', 'r')
full_json = ""
for line in jsonFile:
    full_json+=line
    


# In[49]:

json_obj = json.loads(full_json)


# In[128]:

user = {}
flattened_geo = []

for line in json_obj['statuses']:
    flattened_geo.append({"latitude": line["geo"]["coordinates"]})
    print flattened_geo


# In[119]:

user = {}
flattened_sn = []

for line in json_obj['statuses']:
    flattened_sn.append({"screen_name": line["user"]["screen_name"], "id": line["id"], "latitude": line["geo"]["coordinates"][0], "longtitude": line["geo"]["coordinates"][1]})
    print flattened_sn


# In[123]:

good_columns_a = [
    "text",
    "id"
]

good_columns_b = [

    "id"
]

good_columns_c = [
    "screen_name",
    "id",
    "latitude",
    "longtitude"
]


# In[114]:

import pandas as pd

df_a = pd.DataFrame(json_obj['statuses'], columns = good_columns_a)
df_a


# In[115]:

df_b = pd.DataFrame(flattened_geo, columns = good_columns_b)
df_b


# In[124]:

df_c = pd.DataFrame(flattened_sn, columns = good_columns_c)
df_c


# In[125]:

pd.merge(df_a, df_c, on='id')

