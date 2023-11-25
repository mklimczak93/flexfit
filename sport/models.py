from django.db import models
from django.contrib.auth.models import AbstractUser, User
from multiselectfield import MultiSelectField
import datetime
import pytz
from geopy.geocoders import Nominatim
import json
from django import forms

# Create your models here.


class User(AbstractUser):
    available_cities = [
        ("WA", "Warszawa"),
        ("KR", "Kraków"),
        ("LO", "Łódź"),
        ("GD", "Gdańsk)"),
        ("WR", "Wrocław"),
        ("PO", "Poznań"),
	]

    available_plans = [
        ("9", "9 credits/mo"),
        ("25", "25 credits/mo"),
        ("47", "47 credits/mo"),
        ("64", "64 credits/mo"),
        ("80", "80 credits/mo"),
    ]

    id              = models.AutoField(primary_key=True)
    profile_photo   = models.ImageField(
        upload_to='user_profiles',
        height_field=None,
        width_field=None,
        default='user_profiles/MockupPhoto01.png'
        )
    city			= models.CharField(max_length=16, choices=available_cities, default="Warszawa")
    classes			= models.ManyToManyField('sport.Class', related_name='user_classes', blank=True)
    reviews			= models.ManyToManyField('sport.Review', related_name='user_reviews', blank=True)
    credits         = models.PositiveSmallIntegerField(default = 0)
    plan            = models.CharField(max_length=16, choices=available_plans, default="47 credits/mo")
    studio_owner    = models.BooleanField(default="False")

    def __str__(self):
        return f"User {self.id}: {self.last_name},{self.first_name}"

    def get_letter(self):
        #swaping first name with username, as user is not initially requested to fill all data
        if len(self.first_name) == 0:
            self.first_name = self.username
        name = self.first_name
        letter = name[0]
        return letter

    def get_plan_credits(self):
        credits = self.plan.strip(" credits/mo")
        return int(credits)

    def get_price(self):
        plan = self.plan.strip(" credits/mo")
        if plan == "9":
            price = 39
        elif plan == "25":
            price = 59
        elif plan == "47":
            price = 79
        elif plan == "64":
            price = 99
        elif plan == "80":
            price = 119
        return int(price)

    def serialize(self):
        return {
            "id"                : self.id,
            "username"          : self.username,
            "first_name"        : self.first_name,
            "last_name"         : self.last_name,
            "email"             : self.email,
            "profile_photo"     : self.profile_photo.url,
            "city"              : self.city,
            "classes"           : [this_class.id for this_class in self.classes.all()],
            "reviews"           : [review.id for review in self.reviews.all()],
            "credits"           : self.credits,
            "studio_owner"      : self.studio_owner,
        }

    def get_number_classes_taken(self):
        classes_all = []
        for i in self.classes.all():
            classes_all.append(i.time)
        classes_taken = []
        now = datetime.datetime.now()
        #localizing time needed using pytz module
        utc=pytz.UTC
        now = utc.localize(now)

        if int(len(classes_all)) == 0:
            return 0
        else:
            for i in classes_all:
                if now > i:
                    classes_taken.append(i)
            return len(classes_taken)

    def get_number_classes_upcoming(self):
        classes_all = []
        for i in self.classes.all():
            classes_all.append(i.time)
        classes_upcoming = []
        now = datetime.datetime.now()
        #localizing time needed using pytz module
        utc=pytz.UTC
        now = utc.localize(now)

        if int(len(classes_all)) == 0:
            return 0
        else:
            for i in classes_all:
                if now < i:
                    classes_upcoming.append(i)
            return len(classes_upcoming)

    def get_number_studios(self):
        studios = []
        for i in self.classes.all():
            studios.append(i.studio.id)
        return len(studios)

    def get_number_credits(self):
        return int(self.credits)

    def add_credits(self, amount):
        credits_number = int(self.credits)
        new_credits_number = credits_number + int(amount)
        self.credits = new_credits_number
        return new_credits_number

    def spend_credits(self, amount):
        credits_number = int(self.credits)
        new_credits_number = credits_number - int(amount)
        self.credits = new_credits_number
        return new_credits_number



class Studio(models.Model):
    available_cities = [
        ("WA", "Warszawa"),
        ("KR", "Kraków"),
        ("LO", "Łódź"),
        ("GD", "Gdańsk)"),
        ("WR", "Wrocław"),
        ("PO", "Poznań"),
	]

    id              = models.AutoField(primary_key=True)
    studio_name	    = models.CharField(max_length=60, default="")
    owner_fr_name   = models.CharField(max_length=60, default="")
    owner_lt_name   = models.CharField(max_length=60, default="")
    password        = forms.CharField(widget=forms.PasswordInput)
    studio_type	    = models.CharField(max_length=60, default="")
    address 	    = models.CharField(max_length=120, default="")
    location        = models.CharField(max_length=24, default="21.01, 52.23")
    studio_city     = models.CharField(max_length=16, choices=available_cities, default="Warszawa")
    description     = models.TextField(default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
    logo 		    = models.ImageField(
        upload_to='studio_profiles',
        height_field=None,
        width_field=None,
        default='sport/static/MockupPhoto01.png'
        )
    studio_photo    = models.ImageField(
        upload_to='studio_profiles',
        height_field=None,
        width_field=None,
        default='sport/static/MockupPhoto01.png'
        )
    trainers	    = models.ManyToManyField('sport.Trainer', related_name='studio_trainers', blank=True, default="")
    studio_classes  = models.ManyToManyField('sport.Class', related_name='studio_classes', blank=True, default="")
    studio_reviews	= models.ManyToManyField('sport.Review', related_name='studio_reviews', blank=True, default="")
    credits         = models.PositiveSmallIntegerField(default = 0)

    def __str__(self):
        return f"{self.studio_name}"

    '''
    def get_location(self):
        geolocator = Nominatim(user_agent="http")
        location = geolocator.geocode(self.address)
        return location.latitude, location.longitude
    '''

    def get_number_classes(self):
        classes = []
        for i in self.studio_classes.all():
            classes.append("class")
        return len(classes)

    def get_number_credits(self):
        return int(self.credits)

    def serialize(self):
        return {
            "id"            : self.id,
            "studio_name"   : self.studio_name,
            "owner_fr_name" : self.owner_fr_name,
            "owner_lt_name" : self.owner_lt_name,
            "password"      : self.password,
            "studio_type"   : self.studio_type,
            "address"       : self.address,
            "location"      : self.location,
            "city"          : self.studio_city,
            "description"   : self.description,
            "logo"          : self.logo.url,
            "studio_photo"  : self.studio_photo.url,
            "trainers"      : [trainer.id for trainer in self.trainers.all()],
            "classes"       : [this_class.id for this_class in self.studio_classes.all()],
            "reviews"       : [review.id for review in self.studio_reviews.all()],
            "credits"       : self.credits,
        }


class Studio_User(models.Model):
    user    = models.OneToOneField('sport.User', on_delete = models.CASCADE)
    studio  = models.OneToOneField('sport.Studio', on_delete = models.CASCADE)

class Class(models.Model):
    days_of_the_week = [
        ("MO", "Monday"),
        ("TU", "Tuesday"),
        ("WE", "Wednesday"),
        ("TH", "Thursday"),
        ("FR", "Friday"),
        ("SA", "Saturday"),
        ("SU", "Sunday"),
	]
    id 			= models.AutoField(primary_key=True)
    name 		= models.CharField(max_length=60)
    class_type  = models.CharField(max_length=60, default="")
    description = models.TextField(default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
    studio 		= models.ForeignKey('sport.Studio', related_name='class_studio', on_delete=models.CASCADE)
    address 	= models.CharField(max_length=120)
    time        = models.DateTimeField(auto_now = False, default=datetime.datetime.now())
    date        = datetime.datetime.now().strftime("%d%m%Y")
    duration 	= models.PositiveSmallIntegerField()
    trainer 	= models.ForeignKey('sport.Trainer', related_name='class_trainer',on_delete=models.CASCADE)
    reviews 	= models.ManyToManyField('sport.Review', related_name='class_reviews', blank=True)
    price       = models.PositiveSmallIntegerField(default = 3)
    users       = models.ManyToManyField('sport.User', related_name='class_signed_up_users', blank=True)
    photo 		= models.ImageField(
        upload_to='class_profiles',
        height_field=None,
        width_field=None,
        default='sport/static/MockupPhoto01.png'
        )

    class Meta:
        #ordering classes by date
        ordering = ['time']

    def __str__(self):
        return f"Class {self.id}: {self.name} in {self.studio}"

    def get_class_rating(self):
        if len(self.reviews.all()) == 0:
        #if self.reviews.all() == []:
        #if reviews.exists() == "false":
            return 0
        else:
            rates_list = []
            for i in self.reviews.all():
                rates_list.append(int(i.rate))
            rating = sum(rates_list) / len(rates_list)
            return rating

    def get_ratings_amount(self):
        if len(self.reviews.all()) == 0:
            return 0
        else:
            rates_list = []
            for i in self.reviews.all():
                rates_list.append(int(i.rate))
            rat_amount = len(rates_list)
            return rat_amount

    def get_ratings_spread(self):
        if len(self.reviews.all()) == 0:
            return 0, 0, 0, 0, 0
        #getting all rates
        rates_list = []
        for i in self.reviews.all():
            rates_list.append(int(i.rate))

        #getting list of separate numbers
        fives = []
        fours = []
        threes = []
        twos = []
        ones = []
        for i in rates_list:
            if i == 5:
                fives.append(i)
            elif i == 4:
                fours.append(i)
            elif i == 3:
                threes.append(i)
            elif i == 2:
                twos.append(i)
            elif i == 1:
                ones.append(i)
            else:
                pass

        #getting amounts of each score
        fract_fives     = (len(fives)/len(rates_list))*100
        fract_fours     = (len(fours)/len(rates_list))*100
        fract_threes    = (len(threes)/len(rates_list))*100
        fract_twos      = (len(twos)/len(rates_list))*100
        fract_ones      = (len(ones)/len(rates_list))*100

        return fract_fives, fract_fours, fract_threes, fract_twos, fract_ones


    def get_weekday(self):
        day_of_class = self.time
        return day_of_class.weekday()

    def get_hour(self):
        time_of_class = self.time.strftime("%H:%M")
        #return time_of_class.time()
        return time_of_class

    def get_date(self):
        date = self.time.strftime("%d.%m.%Y")
        return date

    def get_date_simple(self):
        date = self.time.strftime("%Y%m%d")
        return int(date)

    def get_location(self):
        location = self.studio.location
        return location

    def serialize(self):
        return {
            "id"            : self.id,
            "name"          : self.name,
            "class_type"    : self.class_type,
            "description"   : self.description,
            "studio"        : self.studio.id,
            "studio_name"   : self.studio.studio_name,
            "studio_logo"   : self.studio.logo.url,
            "address"       : self.address,
            "location"      : self.studio.location,
            "time"          : self.time,
            "date"          : self.get_date(),
            "hour"          : self.get_hour(),
            "duration"      : self.duration,
            "trainer"       : self.trainer.id,
            "trainer_name"  : self.trainer.name,
            "photo"         : self.photo.url,
            "reviews"       : [review.id for review in self.reviews.all()],
            "rating"        : self.get_class_rating(),
            "rating_amount" : self.get_ratings_amount(),
            "fives"         : self.get_ratings_spread()[0],
            "fours"         : self.get_ratings_spread()[1],
            "threes"        : self.get_ratings_spread()[2],
            "twos"          : self.get_ratings_spread()[3],
            "ones"          : self.get_ratings_spread()[4],
            "price"         : self.price,
        }




class Trainer(models.Model):
    id 		= models.AutoField(primary_key=True)
    name 	= models.CharField(max_length=60)
    studio 	= models.ForeignKey('sport.Studio', related_name='trainer_studio', on_delete=models.CASCADE)
    reviews = models.ManyToManyField('sport.Review', related_name='trainer_reviews', blank=True)

    def __str__(self):
        return f"Trainer {self.id}: {self.name} in {self.studio}"

    def serialize(self):
        return {
            "id"        : self.id,
            "name"      : self.name,
            "studio"    : self.studio,
            "reviews"   : [review.id for review in self.reviews.all()]
        }


def get_user():
    return User.objects.get(pk=1)
#default=User.objects.get(id=1)

def get_class():
    return Class.objects.get(pk=1)

class Review(models.Model):
    rates = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5")
	]

    id          = models.AutoField(primary_key=True)
    author      = models.ForeignKey('sport.User', related_name = "review_author", default = 1, on_delete=models.PROTECT, db_constraint=False)
    rate 		= models.IntegerField(choices=rates)
    description = models.CharField(max_length=120, blank=True)
    date 		= models.DateField(auto_now_add=True)
    class_rated = models.ForeignKey('sport.Class', related_name = "class_rated", default = 1, on_delete=models.PROTECT, db_constraint=False)


    def __str__(self):
            return f"Review {self.id} of {self.class_rated} by {self.author}"


    def serialize(self):
        return {
            "id"            : self.id,
            "author"        : self.author.username,
            "rate"          : self.rate,
            "description"   : self.description,
            "date"          : self.date,
            "class_rated"   : self.class_rated.name,

        }
