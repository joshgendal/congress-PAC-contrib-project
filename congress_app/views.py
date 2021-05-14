from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User, MemberOfCongress, Rating, Opinion
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
    return redirect('/dashboard')
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
  return render(request, 'rate_and_comment.html', context)

# Add user rating
def add_rating(request):
  if request.method == "POST":
    # Query member to rate
    cid = request.POST['member_cid']
    member_to_rate = MemberOfCongress.objects.get(cid=cid)
    user_id = request.session['user_id']
    opinion = request.POST['opinion']
    user = User.objects.get(id=user_id)
    Opinion.objects.create(text=opinion, user=user, member=member_to_rate)
    rating = request.POST['rating']
    Rating.objects.create(rating=rating, user=user, member=member_to_rate)
    return redirect("/dashboard")
  return redirect('/')

def dashboard(request):
  user = User.objects.get(id=request.session['user_id'])
  all_members = MemberOfCongress.objects.all()
  all_opinions = Opinion.objects.all()
  context = {
    "user": user,
    "all_members": all_members,
    "all_opinions": all_opinions
  }
  return render(request, 'dashboard.html', context)

def edit_rating_opinion(request, member_cid):  
  member = MemberOfCongress.objects.get(cid=member_cid)
  member_rating = Rating.objects.get(member=member)
  member_opinion = Opinion.objects.get(member=member)
  context = {
    "rating": member_rating,
    "opinion": member_opinion
  }
  return render(request, 'edit_rating_opinion.html', context)

def modify_edit_opinion(request):
  if request.method == "POST":
    member_cid = request.POST['member_cid']
    edited_rating = request.POST['rating']
    edited_opinion = request.POST['opinion']
    member = MemberOfCongress.objects.get(cid=member_cid)
    rating_to_edit = Rating.objects.get(member=member)
    opinion_to_edit = Opinion.objects.get(member=member)
    rating_to_edit.rating = edited_rating
    rating_to_edit.save()
    opinion_to_edit.text = edited_opinion
    opinion_to_edit.save()
  return redirect('/dashboard')

def change_chamber(request):
  members = MemberOfCongress.objects.all()
  for i in members:
    if i.chamber == "H":
      i.chamber = "House"
      i.save()
    if i.chamber == "S":
      i.chamber = "Senate"
      i.save()
    
  return redirect('/members-contributions-table')

def change_party(request):
  members = MemberOfCongress.objects.all()
  for i in members:
    if i.party == "D":
      i.party = "Democrat"
      i.save()
    if i.party == "R":
      i.party = "Republican"
      i.save()
    if i.party == "I":
      i.pary = "Independent"
      i.save()
  return redirect('/members-contributions-table')

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