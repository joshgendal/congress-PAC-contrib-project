from requests.api import get
# from congress.congress_app.utils.api.functions import get_state_code_list
from django.conf import settings
from django.shortcuts import render
import requests
import json
import os
from .utils import get_state_code_list, get_cid_list, get_candidate_summaries
openSecretsAPIKey = "a8551db7eb798ce16ca3413e4cb6a30d"
getLegislatorsURL = "http://www.opensecrets.org/api/?method=getLegislators"
opnSecretsUrl = "${getLegislatorsURL}&id=${code}&apikey=${openSecretsAPIKey}&output=json"
candidate_summary_url = "https://www.opensecrets.org/api/?method=candSummary"
# load state codes
state_code_list = get_state_code_list()
# get list of legislator unique id ("cid")
cid_list = get_cid_list(state_code_list)
# get list of dictionaries containing contribution data
cand_summaries = get_candidate_summaries(cid_list)
print(cand_summaries)


# Create your views here.
def index(request):
  # r = requests.get(f"{candidate_summary_url}&cid=N00007360&apikey={openSecretsAPIKey}&output=json")
  # print(r.json()["response"]["summary"]["@attributes"])
  # attributes = r.json()["response"]["summary"]["@attributes"]
  
  # cids = []

  


  # for i in r.json()["response"]["legislator"]:
  #   cids.append(i['@attributes']['cid'])
  #   # print(len(i['@attributes']['cid']))
  # print(len(cids))
  return render(request, "index.html")

