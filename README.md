** FLEXFIT – Flexible fitness classes booking app **

#### Video Demo:  https://youtu.be/Ed9B-PfPLDM

 **Description**

Flexfit is a sport classes booking application - inspired by ClassPass, an app that I have used often while living in Amsterdam and found it missing back in Warsaw. It is a platform offering its services to both everyday sport enjoyers and sport studio owners. On one hand it allows to search for the sport classes offered in the area, on the other hand – to promote various activities presented by the studios.

**Functionalities**

The main functionalities of the website – sport user side:
-	Finding classes in the area,
-	Viewing detailed description of the class & its rating,
-	Signing up for classes,
-	Viewing their own calendar,
-	Rating classes they have been to,
-	Choosing subscription plan,
-	Using the platform subscription plan to pay for the classes.

The main functionalities – studio owner side:
-	Offering classes to the platform users,
-	Adding description & information of the classes,
-	Viewing list of offered classes,
-	Viewing ratings given by the users,
-	Seeing the list of sign-uped users,
-	Receive funds from the sign-ups.


![01  Login](https://github.com/mklimczak93/flexfit/assets/123643355/f2a323bb-8b26-4543-b5e3-22f9572d4bc0)
01. Login page

![02  Main page](https://github.com/mklimczak93/flexfit/assets/123643355/52cfcf07-4a59-432c-a4b8-1da6552f6f9d)
02. Main page

![03  Class details](https://github.com/mklimczak93/flexfit/assets/123643355/b455906a-d857-4a5c-be2d-1df6c720cfbd)
03. Class details

![04  Calendar](https://github.com/mklimczak93/flexfit/assets/123643355/63170502-1b51-4bc6-b920-f69837bde838)
04. User's calendar

![05  List](https://github.com/mklimczak93/flexfit/assets/123643355/4c63e4dc-5955-4dda-8e43-9f1678f1309d)
05. User's classes list

![06  Edit profile](https://github.com/mklimczak93/flexfit/assets/123643355/0385ea3c-5863-4a96-87b6-372f43077bfa)
06. Editing profile

![07  Plans](https://github.com/mklimczak93/flexfit/assets/123643355/f64f39be-aaf2-49d4-a63b-66f9a0e6f42c)
07. Changing user subsciprion plan

![09  Partner login](https://github.com/mklimczak93/flexfit/assets/123643355/b2aeebcd-e9f5-495d-a3b7-b6472b2d1ca5)
08. Studio Partner login

![08  Studio main page](https://github.com/mklimczak93/flexfit/assets/123643355/9e1dfb2e-2cc8-4dd5-bf99-de56449fd1f5)
09. Studio owner overview page

**Distinctiveness and Complexity**

Although the general idea of the functionality of the designed web application was inspired by an existing platform, both frontend and its design, and backend and its solutions were written from scratch.
One of the functions of the platform is to search the classes through seeing where the studios are positioned in the city, marked on the map. In order to provide that solution TomTom API was used for displaying the map, customizing it to fit the UI design and marking the studio locations with pins.
Then there is a function allowing the user to sign up for the class. This could be probably a better design function. Right now it takes into consideration  whether user has enough credits to sign up for the class, and add the class to user’s classes field, and user to class’s user field, but there should be also a capacity-checking function, to see whether the users limit was not crossed. On the front end side, the user does get a popup saying that they signed-up or cancelled the signup, and their credits number is visibly changing.
Another functionality is for the user to see all the classes they signed up to both in calendar and list view. Although both datetime and calendar python modules were used here, creating a calendar view as a part of the bigger app was needlessly time-consuming and probably could be optimised, especially that the function of showing next/previous month does not work and should be fixed in the next version.
Next, there was also an attempt to re-create the subscription based character of the original platform. So the Flexfit platform as well allows the class participant user to choose which monthly plan they want to follow and adds “credits” according to their account allowing for booking the classes. It would be great to connect that to an actual payment system API eg. Paypal.
Additionally, we also have the studio-owner interface, where they can log in and see their control panel. They can add classes and view their studio classes list. However, this part is not entirely developed, as the application scope was becoming too big. Some of the functions therefor are not really working well here.
Finally, the mobile-responsiveness of the website could be optimised. It was designed from desktop-first perspective, and while the desktop layout is well designed, the mobile could be definitely developed further.

**Limitations**

Although the project was written with care, there are some limitations to it. First of all – its scope of creating interfaces for both sport users and studio owners was too big. Even as a final project, creating that big of an app by one person proved to be quite time consuming, and at the same time there were some repeatable steps, which weren’t particularly challenging when done again. Therefore, the second interface, for studio owners, was simplified from original idea and limited options were actually executed.
The most interesting part project-wise of providing options for creating a service for both parties (classes participants and studio owners) was creating good models. Originally, I have planned to have two AbstractUsers models: one for classes participants and one for studio owners. However, it could not be done. Later on, I tried to create a custom “User” models.Model for the studio owners, with its own username and password fields, but it would require re-writing a lot of functionality that Django originally offers with its AbstractUser. So after some research, I have decided to add a special bolean field – “studio_onwer” to already existing User model and use its functions for both classes participants and studio owners, and then create a linking models.Model called “Studio_User”, which connected a user model and a studio model. That, although awkward in its design, was in the end successful in allowing to create two logging in systems, one for classes participants and one for studio owners, and therefore give them two different interfaces with different functionalities. If I would be building this app from scratch again, I would create one AbstractUser for logging in, and separate models for classParticipant and studioOwner with AbstractUser “linked” as “models.OneToOneField”.
Furthermore, all the experimentations with creating the right models while already there were created many positions in the database, caused a bit of problems with migrations. At some point, a “nuclear” option of deleting all migrations was used and migrating process was started again, with new models.
Finally, there are some things that I have learnt along the way that I would design differently, a lot of them e.g. in CSS & HTML files (creating eg. :root, different structuring of some parts, not repeating certain parts).
I must conclude that despite the app was quite time-consuming to finish, I have definitely learnt a lot from it, especially when it comes to planning everything out. I think with gained experience, it will be easier for me to predict certain “bottle necks” and avoid having to make “awkward” optimisations, but also I think I would like to definitely devote more time to planning out all layouts, mobile, tablet and desktop, thinking carefully about all the functionalities and what they would require from models, and deliberating how to structure my main models well from the beginning.

**How to run**

This application was designed with Django. To run project please use:

python manage.py runserver

**APIs, packages, modules and libraries required**

- datetime module,
- pytz library,
- markdown2,
- calendar module,
- json,
- popper.js,
- Bootstrap,
- jquery,
- fontawesome,
- Google Font API,
- TomTom API.

