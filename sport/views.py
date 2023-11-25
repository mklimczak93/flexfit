import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.core.paginator import Paginator
from markdown2 import Markdown
import markdown2
from django.core.files.storage import default_storage
from .models import User, Studio, Class, Review, Trainer, Studio_User
import calendar
from calendar import HTMLCalendar
from calendar import monthrange

# Create your views here.

def index(request):
    #rendering calendar
    now = datetime.datetime.now()
    day_number      = int(now.day)
    month_number    = int(now.month)
    year_number     = int(now.year)

    #getting basic data to display month in a calendar
    month_range             = monthrange(year_number, month_number)
    first_weekday           = month_range[0]
    days_in_month           = month_range[1]
    days_in_month_list      = [(i+1) for i in range(days_in_month)]
    previous_days           = int(first_weekday)+1
    previous_list           = [(i+1) for i in range(previous_days)]
    previous_month_range2   = monthrange(year_number, (month_number-1))
    previous_month_range    = previous_month_range2[1]
    previous_days_list      = [(int(previous_month_range)-(i)) for i in range(int(previous_days)-1)]
    previous_days_list.sort()
    future_days             = 35 - int(previous_days) - int(days_in_month)+1
    future_days_list        = [(i+1) for i in range(future_days)]
    month_name              = calendar.month_name[month_number]
    #marking days with classes in calendar
    #if the user is logged in:
    if request.user.is_authenticated:
        user = request.user
        days_with_classes = []
        for i in user.classes.all():
            date=i.get_date()
            classes_day = str(date[0])+str(date[1])
            #removing month 0 for comparison purposes in first 9 months
            if str(date[2]) == str(0):
                classes_month = str(date[3])
            else:
                classes_month = str(date[2]) + str(date[3])
            classes_year = str(date[4])+str(date[5])+str(date[6])+str(date[7])
            if str(classes_month) == str(month_number):
                days_with_classes.append(int(classes_day))
        #user classes only
        user_classes = user.classes.all()

    #if the user is NOT logged in:
    else:
        days_with_classes = []
        user_classes = []
        user = None

    #classes in general view
    classes = Class.objects.all().order_by("time")

    #getting current date for comparison in the personal classes list
    if month_number<10:
        month_number = str(0) + str(month_number)
    if day_number<10:
        day_number = str(0) + str(day_number)
    now_date_for_comparison = int(str(year_number)+str(month_number)+str(day_number))

    return render(request, "sport/index.html", {
        "now_date_for_comparison"   : now_date_for_comparison,
        "classes"                   : classes,
        "user"                      : user,
        "first_weekday"             : first_weekday,
        "days_in_month_list"        : days_in_month_list,
        "previous_days_list"        : previous_days_list,
        "future_days_list"          : future_days_list,
        "month_number"              : month_number,
        "month_name"                : month_name,
        "year_number"               : year_number,
        "day_number"                : day_number,
        "days_with_classes"         : days_with_classes,
        "user_classes"              : user_classes,
        })


def index_studio(request):
    #if studio partner is logged in:
    user = request.user
    all_studio_users = Studio_User.objects.all()
    for i in all_studio_users:
        if i.user.id == user.id:
            studio = i.studio
        else:
            return render(request, "sport/index.html", {
                "message": "Studio not found"
            })
    # studio = user.studio
    #rendering calendar
    now = datetime.datetime.now()
    day_number      = int(now.day)
    month_number    = int(now.month)
    year_number     = int(now.year)

    #getting basic data to display month in a calendar
    month_range             = monthrange(year_number, month_number)
    first_weekday           = month_range[0]
    days_in_month           = month_range[1]
    days_in_month_list      = [(i+1) for i in range(days_in_month)]
    previous_days           = int(first_weekday)+1
    previous_list           = [(i+1) for i in range(previous_days)]
    previous_month_range2   = monthrange(year_number, (month_number-1))
    previous_month_range    = previous_month_range2[1]
    previous_days_list      = [(int(previous_month_range)-(i)) for i in range(int(previous_days)-1)]
    previous_days_list.sort()
    future_days             = 35 - int(previous_days) - int(days_in_month)+1
    future_days_list        = [(i+1) for i in range(future_days)]
    month_name              = calendar.month_name[month_number]


    #marking days with classes in calendar
    #if the user is logged in:
    if request.user.is_authenticated:
        user = request.user
        days_with_classes = []
        for i in user.classes.all():
            date=i.get_date()
            classes_day = str(date[0])+str(date[1])
            #removing month 0 for comparison purposes in first 9 months
            if str(date[2]) == str(0):
                classes_month = str(date[3])
            else:
                classes_month = str(date[2]) + str(date[3])
            classes_year = str(date[4])+str(date[5])+str(date[6])+str(date[7])
            if str(classes_month) == str(month_number):
                days_with_classes.append(int(classes_day))
        #user classes only
        user_classes = user.classes.all()

    #if the user is NOT logged in:
    else:
        days_with_classes = []
        user_classes = []
        user = None

    #classes in general view
    classes = Class.objects.all().order_by("time")

    #getting current date for comparison in the personal classes list
    if month_number<10:
        month_number = str(0) + str(month_number)
    if day_number<10:
        day_number = str(0) + str(day_number)
    now_date_for_comparison = int(str(year_number)+str(month_number)+str(day_number))


    return render(request, "sport/index-studio.html", {
        "studio"   : studio,
        "user"     : user,

        "now_date_for_comparison"   : now_date_for_comparison,
        "first_weekday"             : first_weekday,
        "days_in_month_list"        : days_in_month_list,
        "previous_days_list"        : previous_days_list,
        "future_days_list"          : future_days_list,
        "month_number"              : month_number,
        "month_name"                : month_name,
        "year_number"               : year_number,
        "day_number"                : day_number,
        "days_with_classes"         : days_with_classes,
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "sport/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "sport/login.html")

def login_view_partner(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        all_studio_users = Studio_User.objects.all()
        for i in all_studio_users:
            if i.user.id == user.id:
                studio = i.studio
            else:
                return render(request, "sport/index.html", {
                    "message": "Studio not found"
                })

        #check if user is a partner
        if user.studio_owner == "False":
            return render(request, "sport/login-partner.html", {
                "message": "You must be a studio partner in order to log in."
            })

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return render(request, "sport/index-studio.html", {
        "studio"   : studio,
        "user"     : user,
        })
        else:
            return render(request, "sport/login-partner.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "sport/login-partner.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "sport/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "sport/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "sport/register.html")


def register_studio(request):
    '''
    couldnt create two abstract users, or change the common user
    and studio to be models.Models with OneToOneField
    Abstract User connection.
    Added field "studio-owner" to user & created a new model
    combining User (with studio-owner set to "True") & Studio models.
    '''

    if request.method == "POST":
        studio_name        = request.POST["venue_name"]
        studio_city        = request.POST["studio_city"]
        email              = request.POST["email"]
        first_name         = request.POST["first_name"]
        last_name          = request.POST["last_name"]
        business_type      = request.POST["business_type"]

        # Ensure password matches confirmation
        password           = request.POST["password"]
        confirmation       = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "sport/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(studio_name, email, password)
            user.studio_owner = "True"
            user.save()
        except IntegrityError:
            return render(request, "sport/partner.html", {
                "message": "Username already taken."
            })
        login(request, user)

        #Create new studio object
        studio = Studio.objects.create(
            studio_name = studio_name,
            owner_fr_name = first_name,
            owner_lt_name = last_name,
            studio_type = business_type,
            studio_city = studio_city,
        )

        #Connect User and Studio in Studio_User

        studio_user = Studio_User.objects.create(
            user    = user,
            studio  = studio
        )


        return HttpResponseRedirect(reverse("partner-login"))
    else:
        return render(request, "sport/partner.html")


#--------------------------------------------------------- SPECIFIC FUNCTIONS -----------------------------------------------------------

def try_view(request):
     return render(request, "sport/try.html")

def plans_view(request):
     return render(request, "sport/plans.html")

def plans_studio_view(request):
     return render(request, "sport/plans-studio.html")

def credits_view(request):
     return render(request, "sport/credits.html")

def credits_studio_view(request):
    return render(request, "sport/credits-studio.html")

def aboutus_view(request):
    return render(request, "sport/aboutus.html")

def careers_view(request):
    return render(request, "sport/careers.html")

def press_view(request):
    return render(request, "sport/press.html")

def contactus_view(request):
    return render(request, "sport/contactus.html")

def helpcenter_view(request):
    return render(request, "sport/helpcenter.html")

def partner_view(request):
    return render(request, "sport/partner.html")

def partner_studio_view(request):
    return render(request, "sport/partner-studio.html")

def referfriend_view(request):
    return render(request, "sport/referfriend.html")

def locations_view(request):
    return render(request, "sport/locations.html")

#----------------------------------------------------- RENDERING TEXT-BASED PAGES ------------------------------------------------------

def get_entry(title):
    """
    Retrieves text entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode('utf-8', errors='ignore')
    except FileNotFoundError:
        return None

def convert_md(title):
    markdowner = markdown2.Markdown()
    title_converted = markdowner.convert(title)
    #markdowner = Markdown()
    #title_converted=markdowner.convert(title)
    return title_converted

def entry(request, title):
    text_attempt=get_entry(title)

    #if there isn't article of such name - return FNF
    if text_attempt==None:
        return render(request, "sport/filenotfound.html")

    #otherwise convert text and display entry
    else:
        entry=convert_md(text_attempt)

        return render(request, "sport/text.html", {
            "entry": entry,
            })



#----------------------------------------------------- PROFILE ------------------------------------------------------

def view_profile(request):
    user = request.user
    #rendering calendar
    now             = datetime.datetime.now()
    day_number      = int(now.day)
    month_number    = int(now.month)
    year_number     = int(now.year)
    #getting basic data to display month in a calendar
    month_range             = monthrange(year_number, month_number)
    first_weekday           = month_range[0]
    days_in_month           = month_range[1]
    days_in_month_list      = [(i+1) for i in range(days_in_month)]
    previous_days           = int(first_weekday)
    previous_list           = [(i+1) for i in range(previous_days)]
    previous_month_range2   = monthrange(year_number, (month_number-1))
    previous_month_range    = previous_month_range2[1]
    previous_days_list      = [(int(previous_month_range)-(i)) for i in range(int(previous_days)-1)]
    previous_days_list.sort()
    future_days             = 35 - int(previous_days) - int(days_in_month)+1
    future_days_list        = [(i+1) for i in range(future_days)]
    month_name              = calendar.month_name[month_number]

    return render(request, "sport/profile.html",{
        "user"               : user,
        "first_weekday"      : first_weekday,
        "days_in_month_list" : days_in_month_list,
        "previous_days_list" : previous_days_list,
        "future_days_list"   : future_days_list,
        "month_number"       : month_number,
        "month_name"         : month_name,
        "year_number"        : year_number,
        "day_number"         : day_number,
    })

def show_classes_for_day(request):
    #get all the classes of the user
    user = request.user
    classes = user.classes.all()
    return JsonResponse([this_class.serialize() for this_class in classes], safe=False)


def edit_profile_data(request):
    if request.method == "POST":
        user            = request.user
        new_first_name  = request.POST['first_name']
        new_last_name   = request.POST['last_name']
        new_email       = request.POST['email']
        new_city        = request.POST['city']

        #checking photo
        new_profile_photo   = request.FILES.get('profile_photo')
        if new_profile_photo == None:
            pass
        else:
            user.profile_photo      = new_profile_photo

        #alter user
        user.first_name         = new_first_name
        user.last_name          = new_last_name
        user.email              = new_email
        user.city               = new_city

        #save
        user.save()
        #redirect back
    return HttpResponseRedirect(reverse("index"))


def show_all_classes(request):
    classes = Class.objects.all()
    return JsonResponse([this_class.serialize() for this_class in classes], safe=False)

def show_chosen_class(request, class_id):
    chosen_class = Class.objects.get(pk=class_id)
    return JsonResponse(chosen_class.serialize())


#--- signing up for a class
@csrf_exempt
@login_required
def sign_up_for_class(request):

    # Signing up must be via POST
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    # Get signup class id
    data = json.loads(request.body)
    class_id = data.get("class_id")

    if data == [""]:
        return JsonResponse({
            "error": "At least one signup required."
        }, status=400)

    #get user's signed up classes
    user = request.user
    signed_up_classes = user.classes
    user_credits = user.credits

    #get class object based on id
    class_to_sign_up = Class.objects.get(pk=class_id)

    #check if user has enough credits to sign up
    if int(class_to_sign_up.price) > int(user.credits):
        return JsonResponse({
            "error": "Not enough credits left."
        }, status=400)

    #deduct credits from user's amount
    user.credits = int(user.credits) - int(class_to_sign_up.price)

    #add class object to user signedup classes
    user.classes.add(class_to_sign_up)

    #add user to class
    class_to_sign_up.users.add(user)

    #save
    user.save()
    class_to_sign_up.save()


    return JsonResponse({"message": "You successfully signed up for chosen class."}, status=201)


def get_signed_up_classes_list(request):
    if request.user.is_authenticated:
        signed_up_classes = request.user.classes.all()
        ids=[]
        for i in signed_up_classes:
            ids.append(i.id)
    else:
        ids = ["user_not_logged_in"]
    return JsonResponse(ids,safe=False)




#--- cancelling the signup for a class
@csrf_exempt
@login_required
def cancel_class(request):
    # Cancelling must be via POST
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    # Get cancelled class id
    data = json.loads(request.body)
    class_id = data.get("class_id")

    if data == [""]:
        return JsonResponse({
            "error": "At least one signup required."
        }, status=400)

    #get user's signed up classes
    user = request.user
    signed_up_classes = user.classes
    user_credits = user.credits

    #get class object based on id
    class_to_sign_up = Class.objects.get(pk=class_id)

    #remove class object to user signedup classes
    user.classes.remove(class_to_sign_up)

    #add credits back to user's amount
    user.credits = int(user.credits) + int(class_to_sign_up.price)

    #remove user to class
    class_to_sign_up.users.remove(user)

    #save
    user.save()
    class_to_sign_up.save()


    return JsonResponse({"message": "You successfully cancelled the sign up for this class."}, status=201)


def get_class_reviews(request, class_id):
    reviews_list=[]
    this_class = Class.objects.get(pk = class_id)
    #creating a query set of given class reviews objects
    reviews_objects = this_class.reviews.all()

    return JsonResponse([i.serialize() for i in reviews_objects], safe=False)





@login_required
def add_review(request):
    # Adding review must be via POST
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    # Get review class id
    data = json.loads(request.body)
    class_id = data.get("class_id")

    if data == [""]:
        return JsonResponse({
            "error": "At least one id required."
        }, status=400)

    request.session['class_id'] = class_id
    return JsonResponse({"message": "Class id sent."}, status=201)

def save_review(request):
    #create a review object
    class_id               = request.session['class_id']
    review_author          = request.user
    review_rate            = request.POST['rate']
    review_description     = request.POST['description']
    review_class           = Class.objects.get(pk=class_id)

    new_review          = Review.objects.create(
        author          = review_author,
        rate            = review_rate,
        description     = review_description,
        class_rated     = review_class)


    #adding review to class, user, studio & trainer
    review_class.reviews.add(new_review)
    review_author.reviews.add(new_review)
    review_studio = review_class.studio
    review_studio.reviews.add(new_review)
    review_trainer = review_class.trainer
    review_trainer.reviews.add(new_review)

    return HttpResponse(status=201)

def change_plan(request):
     # Changing plans must be via POST
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    # Get plan number
    data = json.loads(request.body)

    if data == [""]:
        return JsonResponse({
            "error": "At least one plan info required."
        }, status=400)

    plan_number = data.get("plan_no")


    #getting user and changing their plan
    user = request.user
    plan = plan_number.strip(" credits/mo")
    user.plan = plan
    #print(user.plan)
    user.save()

    return JsonResponse({"message": "Plan changed."}, status=201)



