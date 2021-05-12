from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User, MemberOfCongress, Rating
import bcrypt
from .utils import get_state_code_list, get_cid_list, get_candidate_summaries
openSecretsAPIKey = "a8551db7eb798ce16ca3413e4cb6a30d"
getLegislatorsURL = "http://www.opensecrets.org/api/?method=getLegislators"
opnSecretsUrl = "${getLegislatorsURL}&id=${code}&apikey=${openSecretsAPIKey}&output=json"
candidate_summary_url = "https://www.opensecrets.org/api/?method=candSummary"

# Create your views here.
def index(request):
  return render(request, 'index.html')

def register(request):
  if request.method == "POST":
    # validate user info
    errors = User.objects.validate_registration(request.POST)
    if errors:
      for e in errors.values():
        messages.error(request, e)
      return redirect('/register')
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    User.objects.create(first_name=first_name, last_name=last_name, email=email, password=pw_hash)
    return redirect('/register')  
  return render(request, 'register.html')

def login(request):
  if request.method == "POST":
    email = request.POST['email']
    password = request.POST['password']
    if not User.objects.authenticate(email, password):
      messages.error(request, 'Invalid email/password')
      return redirect('/login')
    user = User.objects.get(email=email)
    request.session['user_id'] = user.id
    messages.success(request, 'You have succesfully logged in')
    return redirect('/')
  return render(request, 'login.html')

# This is the view function that will add the contribution api data into the db


def members_contributions_table(request):
  all_members = MemberOfCongress.objects.all()
  print(all_members)
  context = {
    "all_members": all_members
  }
  return render(request, 'members_contributions.html', context)

def rate(request, cid):
  member_to_rate = MemberOfCongress.objects.get(cid=cid)
  print('USER IS:', request.session['user_id'])
  context = {
    "member": member_to_rate
  }
  return render(request, 'rate.html', context)

# Add user rating
def add_rating(request):
  if request.method == "POST":
    # Query member to rate
    cid = request.POST['member_cid']
    member_to_rate = MemberOfCongress.objects.get(cid=cid)
    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    rating = request.POST['rating']
    Rating.objects.create(rating=rating, user=user, member=member_to_rate)
  return redirect('/')



def add_api_data(request):
  if request.method == "POST":
    # 1. get list of US state codes
    state_code_list = get_state_code_list()
    # 1. get list of legislator unique id ("cid")
    cid_list = get_cid_list(state_code_list)
    print(len(cid_list))
    print(cid_list)
  # get list of dictionaries containing contribution data
    cand_summaries = get_candidate_summaries(cid_list)
    for i in cand_summaries:
      name = i["cand_name"]
      name_split = name.split(', ')
      first_name = name_split[1]
      last_name = name_split[0]
      MemberOfCongress.objects.create(first_name=first_name, last_name=last_name, cid=i["cid"], state=i["state"], party=i["party"], chamber=i["chamber"], first_elected=i["first_elected"], total_contributions=i["total"])
    return redirect("/")
  return render(request, 'add-api-data.html')

def deleteMemberData(request):
  MemberOfCongress.objects.all().delete()
  return redirect("/")