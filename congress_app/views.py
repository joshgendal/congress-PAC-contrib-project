from django.shortcuts import render
import requests
openSecretsAPIKey = "a8551db7eb798ce16ca3413e4cb6a30d"
getLegislatorsURL = "http://www.opensecrets.org/api/?method=getLegislators"
opnSecretsUrl = "${getLegislatorsURL}&id=${code}&apikey=${openSecretsAPIKey}&output=json"

# Create your views here.
def index(request):
  r = requests.get(f"{getLegislatorsURL}&id=FL&apikey={openSecretsAPIKey}&output=json")
  cids = []
  for i in r.json()["response"]["legislator"]:
    cids.append(i['@attributes']['cid'])
    # print(len(i['@attributes']['cid']))
  print(len(cids))
  return render(request, "index.html")