import os, json
from django.conf import settings

"""
A function to get US State Code List

Reads json file, packs state codes into list and returns it
"""
def get_state_code_list():
  state_codes = []
  data = open(os.path.join(settings.BASE_DIR, 'congress_app/static/state_code_data.json'))
  data1 = json.load(data)
  for i in data1:
    state_codes.append(i["Code"])
  data.close()
  return state_codes
  