# Video Gaming Tracker

## [Link to Live Site](https://video-game-tracker-f52ca7e7c2d0.herokuapp.com)

## Contents
<!-- TODO: AI this  -->

## Introduction

This is a project to allow users to create an account so they can track which games they own and which have compeleted. They can also set their profile for other users to see, or even unregistered users.

###### [*Back to contents*](#contents)

## User Experience

###### [*Back to contents*](#contents)

### Stories

###### [*Back to contents*](#contents)

#### External User Story

- Create an account.
- Add which games that I own.
- Set my favourite game/platform.
- Set privacy of my profile so only people with the correct permissions can view it.

###### [*Back to contents*](#contents)

#### Site Owner User Story

- The website looks consistent across each page.

###### [*Back to contents*](#contents)

### Strategy

#### Agile

I used an agile methodology for the project, making use of a github project board which can be found [here](https://github.com/users/lcorndogl/projects/8/views/1).

###### [*Back to contents*](#contents)

#### MoSCoW

During my project I prioritised features of the site, defining whether features were a Must Have, Should Have or a Could Have priority.

###### [*Back to contents*](#contents)

### Scope

The main scope of the project was to create an interface for users to be able to interact with the database to store the games that they owned which ones they have completed.

###### [*Back to contents*](#contents)

#### Project Setup

To help speed up the setup of the project, I made a few lines of code that could be run in the terminal to create all of the basic files to form a basis for the project:

```command line
pip install Django~=4.2.1
pip3 install dj-database-url~=0.5 psycopg2
pip3 install gunicorn~=20.1
pip3 freeze --local > requirements.txt
django-admin startproject videoGameTracker .
echo "web: gunicorn videoGameTracker.wsgi" > Procfile
echo 'import os
os.environ["DATABASE_URL"]=""
os.environ["SECRET_KEY"]="nananana"
os.environ["DEBUG"]=1' > env.py
echo "
env.py" >> .gitignore
python3 manage.py migrate
python3 manage.py runserver
```

This allowed me to have only a few additional lines that I had to run to create the project. These tasks were:

- Adjust the allowed hosts
- Set CSRF_TRUSTER_ORIGINS
- Run the startapp command
- Add the app to the INSTALLED_APPS
- Create Database on CI Database Maker
- Deploy to Heroku (Steps later in the readme)

#### AI Influence

AI has been influential in getting my project to completion, through struggling at the start without using it, to then utilising CoPilot to help understand how the models/views/html files all link together. This sped up the generation of code massively as it helped to wrap my head around how Django all works together in an intricate manner, and providing me a better understanding of how to troubleshoot later problems that came up, as well as understanding what the errors were saying when referencing the specific file names when DEBUG was enabled.

#### Entity Relationship Diagrams

I started out with a simple idea for my ERD, looking at creating users and connecting them to a User_Library so they could mark which games they owned and had completed.

![Initial ERD](docs/readme/ERD/ERD-initial.png)

As the project developed, there were more models added, and as such the ERD became a bit more complex due to developments such as having users select a game and platforms from lists instead of having them input the data manually. I used CoPilot to generate an ERD for this as below:

### Entity Relationship Diagram

```plaintext
+-----------------+          +-----------------+          +-----------------+
|      User       |<-------->|  User_Profile   |<-------->|     Privacy     |
+-----------------+          +-----------------+          +-----------------+
| id (PK)         |          | id (PK)         |          | id (PK)         |
| username        |          | user (FK)       |          | privacy         |
| email           |          | game (FK)       |          +-----------------+
| password        |          | platform (FK)   |
+-----------------+          | created_on      |
                             | updated_on      |
                             | privacy (FK)    |
                             +-----------------+
                                    |
                                    |
                                    v
                             +-----------------+
                             |     Comment     |
                             +-----------------+
                             | id (PK)         |
                             | profile (FK)    |
                             | commenter (FK)  |
                             | body            |
                             | approved        |
                             | created_on      |
                             +-----------------+

+-----------------+          +-----------------+          +-----------------+
|      Game       |<-------->|  User_Library   |<-------->|    Platform     |
+-----------------+          +-----------------+          +-----------------+
| id (PK)         |          | id (PK)         |          | id (PK)         |
| game            |          | user (FK)       |          | platform        |
+-----------------+          | created_on      |          +-----------------+
                             | updated_on      |
                             | game (FK)       |
                             | platform (M2M)  |
                             | completed       |
                             +-----------------+
```

### Wireframes

###### [*Back to contents*](#contents)

#### Home Wireframe

![Home Wireframe](docs/wireframes/wf-home.png "Video Gaming Tracker Home")

###### [*Back to contents*](#contents)

#### Profiles Wireframe

![Profiles Wireframe](docs/wireframes/wf-profiles.png "Video Gaming Tracker Profiles")

###### [*Back to contents*](#contents)

#### User Profiles Wireframe

![Profiles Wireframe](docs/wireframes/wf-user-profile.png "Video Gaming Tracker Profiles")

###### [*Back to contents*](#contents)

#### Sign up Wireframe

![Sign up Wireframe](docs/wireframes/wf-sign-up.png "Video Gaming Tracker Sign up")

###### [*Back to contents*](#contents)

#### Login Wireframe

![Login Wireframe](docs/wireframes/wf-login.png "Video Gaming Tracker Login")

###### [*Back to contents*](#contents)

#### Logout Wireframe

![Logout Wireframe](docs/wireframes/wf-logout.png "Video Gaming Tracker Logout")

###### [*Back to contents*](#contents)

#### Edit Profile Wireframe

##### Logged In View

![Edit Profile Logged In Wireframe](docs/wireframes/wf-edit-loggedin.png "Video Gaming Tracker Edit Profile")

###### [*Back to contents*](#contents)

##### Logged Out View

![Edit Profile Logged Out Wireframe](docs/wireframes/wf-edit-loggedout.png "Video Gaming Tracker Edit Profile")

###### [*Back to contents*](#contents)

#### Mobile / Tablet / Desktop breakpoints

I have utilised the breakpoints that are specified in bootstrap using the grid feature, using the col-lg, col-md and col-sm classes

For avoidance of doubt - the breakpoints these refer to are 960px, 720px and 576px respectively.

###### [*Back to contents*](#contents)

## Design

###### [*Back to contents*](#contents)

### Colour Scheme

 I chose a dark theme for the site with colours like blue, yellow and red, as a homage to what an old arcade game machine would look like.

### Imagery

The game controller icon has been used via linking to it on the icons8 website.

###### [*Back to contents*](#contents)

### Typography

The typography I have used Google Fonts, I have searched on there and imported fonts that I think will add to the overall vision of the project, to round it out nicely for a better user experience.

###### [*Back to contents*](#contents)

## Website Features

###### [*Back to contents*](#contents)

### Home

When a user loads the site, a homepage is displayed, this page has a logo, site title & navbar, along with a brief overview of what is available with and without an account.

###### [*Back to contents*](#contents)

### Profiles

A page that is accessible by all, it allows to view all existing users who have marked their profile as public - being accessible without needing to be logged in.

### Sign Up

#### Logged In

Django does not allow a logged in user to access the sign up page and instead redirects to the homepage.

#### Logged Out

A page showing the sign up form, allowing a user to sign up to the website.

### Log In

#### Logged In

Django does not allow a logged in user to access the login page and instead redirects to the homepage.

#### Logged Out

A page showing a form to login to a created account, allowing users to login to their account on the website

### Log Out

#### Logged Out

A page showing a form to login to a created account, allowing users to login to their account on the website

#### Logged In

A page showing a page with the options to either go to the Home page, or confirm Logging out of the account

### Edit Profile

#### Logged In

A page allowing users to add games to their library and adjust the completed status or remove games, as well as set their favourites and account privacy

#### Logged Out

Django does not allow a logged out user to access the edit profile page and instead redirects to the homepage.

## Future Features

### Styling

In future I would like to amend the styling so it looks like the code from within the `<main>` section of the website was like it was in a retro arcade game machine

### User adding of games/platform

In future I would like a user to be able to add new games or platforms as they are released, being submitted for approval via a superuser.

### Model field name conflicts

There are some errors generated by crispy forms which I didn't have the time to fix yet as I tried customising the form in the manage.html to pull each field in individually, however it adds a div with an ID in at that point, and due to the favourites and add games both being fields from the 'Game' model it creates the same div ID for them, I plan to fix this as part of a future feature, either via some javascript to amend the div id on load, digging deeper into how crispy forms works, or adjusting the fields in the User_Library and User_Profile models so they aren't both called Game/Platform

###### [*Back to contents*](#contents)

## Technologies Used

###### [*Back to contents*](#contents)

### HTML Language

HTML is used as the base to the project, utilising [*Django*](#django) to piece the files together to dynamically serve the webpages to the user depending on if they are loggined in or not, as well as the actions they are performing.

###### [*Back to contents*](#contents)

### CSS Styling

CSS is used to provide style to the website to make it more visually appealing to the user of the website. I have also utilised [*Bootstrap*](#bootstrap) as part of the CSS Styling.

###### [*Back to contents*](#contents)

### bash terminal

I used bash as my terminal of choice, using it for various things from setting alias' for commonly used commands, creating directories and files, as well as interfacing with git to add, commit and push to [*GitHub*](#github).

###### [*Back to contents*](#contents)

### Bootstrap

I have utilised boostrap to provide a template for numerous IDs and classes for the formatting of the project.

###### [*Back to contents*](#contents)

### Django

Django framework has been used to dynamically load views and models via Django Template Language (DTL) based on if a user is logged in or not, as well as adding/removing entries from a database in a secure way and protecting from malicious attacks via backend server processing

###### [*Back to contents*](#contents)

### Git

Git has been used to allow for easy versioning of the project, as well as tracking changes which may become important for troubleshooting if any errors are introduced as the code is developed

### GitHub

GitHub has been used as a central repository where the code can be accessed online. It has also been linked to heroku allowing heroku to fetch the repository from GitHub to deploy the project into an online environment, as well as testing the project both locally and online as it is developed to ensure consistent behaviours

###### [*Back to contents*](#contents)

### Gitpod

Gitpod has been used as a remote workspace, allowing for a sandboxed environment where variables can be controlled to ensure no conflicts with other software that may be installed on my personal device

###### [*Back to contents*](#contents)

### Heroku

Heroku has been used to provide the back end processing of the project, allowing it to run Django and generate the HTML of the pages that the user is requesting dynamically

###### [*Back to contents*](#contents)

### Postgres

Data has been stored within a Postgres database that has been provided by [*CodeInstitute*](#codeinstitute).

###### [*Back to contents*](#contents)

### Visual Studio Code

Visual Studio Code has been used to create the project as a pseudo-IDE, allowing for the use of emmet commands to help create the code in an efficient manner, as well as CoPilot integration

###### [*Back to contents*](#contents)

### CoPilot

CoPilot has been used as the AI tool in this project, utilising it for both helping with code creation such as pulling bootstrap templates into the code rather than using a search engine and the documentation where possible. It has also been used to help troubleshoot any errors within the code, and helping with getting the layout of the project correct in places where I may have struggled without it.

###### [*Back to contents*](#contents)

## Deployment

1) Add the required files to the git repository with the command `git add .`

2) Commit the changes to the repository with the command commit command `git commit -m "Final project commit"`

3) [Create new app on Heroku](https://dashboard.heroku.com/new-app)

![Creating Heroku App](docs/readme/heroku-create-app.png)

4) Connect to GitHub repo

![Github Repository Linking](docs/readme/heroku-github-connect.png)

5) Set Config vars to replicate what is in env.py - heroku-config-vars.png
link to github

![Heroku Config Vars](docs/readme/heroku-config-vars.png)

6) Manual deploy on heroku - heroku-deploy.png

![Heroku Deployment](docs/readme/heroku-deploy.png)

7) Check project deployed as expected

![Heroku Deployment Check](docs/readme/heroku-check.png)

###### [*Back to contents*](#contents)

## Testing

###### [*Back to contents*](#contents)

### Manual Testing

I was manually testing all throughout the project, making sure a new feature or fix was working as intended before each commit. As such you can infer that each commit message is a test in itself, describing the tests that were done.

### Automated Testing

I used CoPilot at the end of the project to perform some automated testing via the tests.py file, you can see this later in the Readme [in the Python Section](#python)

###### [*Back to contents*](#contents)

### Validation

###### [*Back to contents*](#contents)

#### HTML

##### Home

###### Logged In W3 Schools

![Homepage](docs/readme/validation/W3S-LI-Index.png)

###### Logged In WAVE

![Homepage](docs/readme/validation/WAVE-LI-Home.png)

###### Logged Out W3 Schools

![Homepage](docs/readme/validation/W3S-LO-Index.png)

###### Logged Out WAVE

![Homepage](docs/readme/validation/WAVE-LO-Home.png)

##### Profiles

###### Logged In W3 Schools

![Homepage](docs/readme/validation/W3S-LI-Profiles.png)

###### Logged In WAVE

![Homepage](docs/readme/validation/WAVE-LI-Profiles.png)

###### Logged Out W3 Schools

![Homepage](docs/readme/validation/W3S-LO-Profiles.png)

###### Logged Out WAVE

![Homepage](docs/readme/validation/WAVE-LO-Profiles.png)

##### Detailed Profiles

###### Logged In W3 Schools

![Homepage](docs/readme/validation/W3S-LI-Detailed.png)

###### Logged In WAVE

![Homepage](docs/readme/validation/WAVE-LI-Detailed.png)

###### Logged Out W3 Schools

![Homepage](docs/readme/validation/W3S-LO-Detailed.png)

###### Logged Out WAVE

![Homepage](docs/readme/validation/WAVE-LO-Detailed.png)

##### Sign Up

###### Logged Out W3 Schools

![Homepage](docs/readme/validation/W3S-LO-Signup.png)

###### Logged Out WAVE

![Homepage](docs/readme/validation/WAVE-Signup.png)

##### Login

###### Logged Out W3 Schools

![Homepage](docs/readme/validation/W3S-LO-Login.png)

###### Logged Out WAVE

![Homepage](docs/readme/validation/WAVE-Login.png)

##### Edit Profile

###### Logged In W3 Schools

There are some errors generated by crispy forms which I didn't have the time to fix yet as I tried customising the form in the manage.html to pull each field in individually, however it adds a div with an ID in at that point, and due to the favourites and add games both being fields from the 'Game' model it creates the same div ID for them, I plan to fix this as part of a future feature, either via some javascript to amend the div id on load, digging deeper into how crispy forms works, or adjusting the fields in the User_Library and User_Profile models so they aren't both called Game/Platform

![Homepage](docs/readme/validation/W3S-LI-Edit-Profiles.png)

###### Logged In WAVE

![Homepage](docs/readme/validation/WAVE-Modify.png)

##### Logout

###### Logged In W3 Schools

![Homepage](docs/readme/validation/W3S-Logout.png)

###### Logged In WAVE

![Homepage](docs/readme/validation/WAVE-Logout.png)

#### CSS

##### Codestar CSS

![Codestar CSS](docs/readme/validation/Jig-codestar.png)

##### Custom CSS

![Custom CSS](docs/readme/validation/Jig-style.png)

### Lighthouse Scores

#### Home

###### Mobile

![Lighthouse Test](docs/readme/validation/LH-LI-M-Home.png)

###### Desktop

![Lighthouse Test](docs/readme/validation/LH-LI-D-Home.png)

##### Logged Out

###### Mobile

![Lighthouse Test](docs/readme/validation/LH-LO-M-Home.png)

###### Desktop

![Lighthouse Test](docs/readme/validation/LH-LO-D-Home.png)

#### Profiles

###### Mobile

![Lighthouse Test](docs/readme/validation/LH-LI-M-Profiles.png)

###### Desktop

![Lighthouse Test](docs/readme/validation/LH-LI-D-Profiles.png)

##### Logged Out

###### Mobile

![Lighthouse Test](docs/readme/validation/LH-LO-M-Profiles.png)

###### Desktop

![Lighthouse Test](docs/readme/validation/LH-LO-D-Profiles.png)

#### Detailed Profile

##### Logged In

###### Mobile

![Lighthouse Test](docs/readme/validation/LH-LI-M-Detailed.png)

###### Desktop

![Lighthouse Test](docs/readme/validation/LH-LI-D-Detailed.png)

##### Logged Out

###### Mobile

![Lighthouse Test](docs/readme/validation/LH-LO-M-Detailed.png)

###### Desktop

![Lighthouse Test](docs/readme/validation/LH-LO-D-Detailed.png)

#### Sign Up

##### Logged Out

###### Mobile

![Lighthouse Test](docs/readme/validation/LH-M-Signup.png)

###### Desktop

![Lighthouse Test](docs/readme/validation/LH-D-Signup.png)

#### Login

##### Logged Out

###### Mobile

![Lighthouse Test](docs/readme/validation/LH-M-Signin.png)

###### Desktop

![Lighthouse Test](docs/readme/validation/LH-D-Signin.png)

#### Edit Profile

##### Logged In

###### Mobile

![Lighthouse Test](docs/readme/validation/LH-M-Modify.png)

###### Desktop

![Lighthouse Test](docs/readme/validation/LH-D-Modify.png)

#### Logout

##### Logged In

###### Mobile

![Lighthouse Test](docs/readme/validation/LH-M-Logout.png)

###### Desktop

![Lighthouse Test](docs/readme/validation/LH-D-Logout.png)

###### [*Back to contents*](#contents)

### Javascript

#### Comments

This was code taken from the CodeInstitute to create the commenting functionality on user profiles

![JS Hint Validation](docs/readme/validation/JSH-comments.png)

#### Library

This is the code that is used to allow users to remove a game from their library, the unused variable is in there as it is called from an external file, triggered via a user clicking on a button.

![JS Hint Validation](docs/readme/validation/JSH-library.png)

#### Python

##### settings.py

![Pep8 Validation](docs/readme/validation/PEP-settings.png)

##### forms.py

![Pep8 Validation](docs/readme/validation/PEP-forms.png)

##### models.py

![Pep8 Validation](docs/readme/validation/PEP-models.png)

##### tests.py

![Pep8 Validation](docs/readme/validation/PEP-tests.png)

##### urls.py

###### videoGameTracker/urls.py

![Pep8 Validation](docs/readme/validation/PEP-vGT-urls.png)

###### profiles/urls.py

![Pep8 Validation](docs/readme/validation/PEP-prof-urls.png)

##### views.py

![Pep8 Validation](docs/readme/validation/PEP-views.png)

### Automated Testing

I used copilot to generate tests to validate my User_Profiles and User_Library Model, these tests came back as passed, as seen below

![Automated Testing](docs/readme/validation/Automated-AI-Testing.png)

## Bugs/Troubleshooting

### Model fields the same in two models

There are some errors generated by crispy forms which I didn't have the time to fix yet as I tried customising the form in the manage.html to pull each field in individually, however it adds a div with an ID in at that point, and due to the favourites and add games both being fields from the 'Game' model it creates the same div ID for them, I plan to fix this as part of a future feature, either via some javascript to amend the div id on load, digging deeper into how crispy forms works, or adjusting the fields in the User_Library and User_Profile models so they aren't both called Game/Platform

### Copilot importing bootstrap incorrectly

CoPilot tried to import bootstrap from the corect CDN, trying to import it from Stackpath CDN rather than JSDeliver CDN.

![CoPilot Bootstrap Fail](docs/ai/ai-bootstrap-failed-import.png)

![CoPilot Bootstrap CDN Fix attempt 1](docs/ai/ai-bootstrap-fix-attempt1.png)

![CoPilot Bootstrap CDN Fix Resolved](docs/ai/ai-bootsrap-fix-attempt2-solved.png)

### base.html doesn't exist - CoPilot steps

At the beginning of the project, I had issues understanding how the files linked together, to help with this I used CoPilot to help identify, explain and resolve the issue

![CoPilot base.html Issue](docs/bugs/ai-basebug3-error.png)

![CoPilot base.html Issue](docs/bugs/ai-basebug-1.png)

![CoPilot base.html Issue](docs/bugs/ai-basebug-2.png)

![CoPilot base.html Issue](docs/bugs/ai-basebug-3-settings-before.png)

![CoPilot base.html Issue](docs/bugs/ai-basebug-3-settings-after.png)

![CoPilot base.html Issue](docs/bugs/ai-basebug3-solved.png)

### no User_Profile created when registering

As I used django AllAuth the User model and the User_Profile models were separate. This caused issues when clicking on the Edit Profile page, returning an error stating that a User_Profile doesn't exist. To overcome this I inserted an if statement to check if a profile exists, and if it doesn't then it will create one before trying to load it. This then caused a follow up issue where it would create new entries in the Privacy model, rather than picking from one of the existing 3 entries, which I used CoPilot to correct.

![CoPilot User_Profile Issue](docs/bugs/ai-signup_no_user_profile.png)

![CoPilot User_Profile Issue](docs/bugs/ai-signup-no_profile_incorrect_setting.png)

![CoPilot User_Profile Issue](docs/bugs/ai-signup-no_profile-creating-new-privacy-records.png)

![CoPilot User_Profile Issue](docs/bugs/ai-signup-no_profile-privacy2.png)

Here you can see that the profile doesn't exist in the admin panel but the manage.html page now loads, and on refreshing the admin panel the new user 'Poe' has been created

![CoPilot User_Profile Issue](docs/bugs/ai-signup-no_profile_fixed.png)

![CoPilot User_Profile Issue](docs/bugs/ai-signup-no_profile_fixed2.png)

###### [*Back to contents*](#contents)

## Credits

###### [*Back to contents*](#contents)

### [Bootstrap](https://www.getbootstrap.com) - [Version 5.3.3](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

###### [*Back to contents*](#contents)

### CodeInstitute

###### [*Back to contents*](#contents)

#### Codestar Walkthrough Blog

I have used the content from the Django walkthrough as a guide for creating the project, including it's apps, to have a guide on where to start with the ability to change field names to amend the functionality from a blog post to being a video game tracker! I have also used the comment section of the blog to implement comments onto user profiles, as well as used this as a basis for my other models to achieve CRUD functionality in other areas of the site - primarily the "Edit Profile" page

#### [Postgres Database](#postgres)

###### [*Back to contents*](#contents)

### [Coolors for the colour scheme](https://coolors.co/d62828-beb8eb-ffba08-2a2b2a)

###### [*Back to contents*](#contents)

### [Django Documentation](https://docs.djangoproject.com/en/4.2/)

###### [*Back to contents*](#contents)

### Eraser.io

#### [Diagram GPT](https://www.eraser.io/diagramgpt)

Diagram GPT was used to create my planned ERD using the prompt below

```plaintext
A table called user containing Unique UserID (autoincrementing), username (String), favourite console (String) & favourite game (String)
A tabled called backlog, containing the UserID from the User table as a foreign key, and a game field (String)
A table called completed, containing the UserID from the User table as a foreign key, and a game field (String)
```

### Icons8

#### [Icons8 game controller for the favicon and banner](https://img.icons8.com/?size=100&id=J2AwyRUPwjyg&format=png)

### Stackoverflow

#### [Undserstanding related_name](https://stackoverflow.com/questions/44160983/what-does-related-name-do)

###### [*Back to contents*](#contents)

### W3 Schools

#### [Refresher on Forms (Checkboxes)](https://www.w3schools.com/tags/att_input_type_checkbox.asp)

###### [*Back to contents*](#contents)

### Fonts

I chose two fonts from google fonts to use in the font family that looked fun/gaming inspired. DynaPuff is the font that is set first in the body via the CSS, and Press Start 2P is there as a backup if for any reason the DynaPuff font cannot be loaded.

###### [*Back to contents*](#contents)

#### [DynaPuff](https://fonts.google.com/specimen/DynaPuff)

###### [*Back to contents*](#contents)

#### [Press Start 2P](https://fonts.google.com/specimen/Press+Start+2P)

###### [*Back to contents*](#contents)
