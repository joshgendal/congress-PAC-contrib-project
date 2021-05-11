import os, json, requests
from django.conf import settings
openSecretsAPIKey = "a8551db7eb798ce16ca3413e4cb6a30d"
getLegislatorsURL = "http://www.opensecrets.org/api/?method=getLegislators"
opnSecretsUrl = "${getLegislatorsURL}&id=${code}&apikey=${openSecretsAPIKey}&output=json"
candidate_summary_url = "https://www.opensecrets.org/api/?method=candSummary"

"""
A function to get US State Code List

Reads json file, packs state codes into list and returns it
"""
def get_state_code_list():
  print('GETTING STATE CODES')
  state_codes = []
  data = open(os.path.join(settings.BASE_DIR, 'congress_app/static/state_code_data.json'))
  data1 = json.load(data)
  for i in data1:
    state_codes.append(i["Code"])
  data.close()
  return state_codes

"""
Gets a list of cid (unique identifiers for all candidates for and members of Congress)

Arg: codes - a list of state codes from the function above
returns: list of cids
"""
def get_cid_list(codes):
  print('GETTING CID LIST')
  cid_list = []
  # loop through state codes
  for code in codes:
    # getlist  all elected members from the state
    r = requests.get(f"{getLegislatorsURL}&id={code}&apikey={openSecretsAPIKey}&output=json")
    # loop through this list and add cid to cid_list
    for i in r.json()["response"]["legislator"]:
      if isinstance(i, dict):
        cid_list.append(i["@attributes"]["cid"])
  print('FINISHED CID LIST')
  return cid_list

"""
get candidate contribution summary information from api

arg: list of cids
returns: list of dictionaries containing info on each elected member of congress
"""
def get_candidate_summaries(cids):
  print('GETTING CANDIDATE SUMMARY')
  data = []
  # r = requests.get(f"{candidate_summary_url}&cid={i}apikey={openSecretsAPIKey}&output=json")
  for i in cids:
    r = requests.get(f"{candidate_summary_url}&cid={i}&apikey={openSecretsAPIKey}&output=json")
    if r.status_code == 200:
      attributes = r.json()["response"]["summary"]["@attributes"]
      data.append(attributes)
      print(len(data))
      # print("================================================================")
  print('FINISHED CANDIDATE SUMMARY')
  return data
