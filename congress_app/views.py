from requests.api import get
# from congress.congress_app.utils.api.functions import get_state_code_list
from django.conf import settings
from django.shortcuts import render
import requests
import json
import os
from .utils import get_state_code_list
openSecretsAPIKey = "a8551db7eb798ce16ca3413e4cb6a30d"
getLegislatorsURL = "http://www.opensecrets.org/api/?method=getLegislators"
opnSecretsUrl = "${getLegislatorsURL}&id=${code}&apikey=${openSecretsAPIKey}&output=json"

state_code_list = get_state_code_list()

# Create your views here.
def index(request):
  r = requests.get(f"{getLegislatorsURL}&id=FL&apikey={openSecretsAPIKey}&output=json")
  cids = []

  print(state_code_list)

  # get array of state codes
  # state_codes = []
  # data = open(os.path.join(settings.BASE_DIR, 'congress_app/static/state_code_data.json'))
  # data1 = json.load(data)
  # for i in data1:
  #   state_codes.append(i["Code"])
  # print(state_codes)
  # data.close()


  for i in r.json()["response"]["legislator"]:
    cids.append(i['@attributes']['cid'])
    # print(len(i['@attributes']['cid']))
  print(len(cids))
  return render(request, "index.html")

