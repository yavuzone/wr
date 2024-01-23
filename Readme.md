# Testing Task for a Python Expert Test Day

## Overall Information

### Description

* Read the complete list of follow up tasks, to get an idea of the complete process. Feel free to ask any questions if something is unclear.
* Try to estimate the amount of time that you would need to fulfill all the tasks with there given acceptance criteria.
* Create a simple, formless estimate.txt (can be pure ASCII or markdown. You could also create spreadsheet. Form really don't matter here its about the content), where the single efforts and the complete effort is listed.
* If the estimated time is bigger then the time you can spend (which very well might be the case), please also make a short notice about the number of tasks that you are optimistic to fulfill over the day.
* create a (probably local) git repository and check in the file that contains the estimation.

### Acceptance criteria

* A Git Repository exists
* It contains an file named estimate.txt (file suffix might be different if non ASCII text is used).
* The file contains an effort estimation for the given tasks

### Help

* For the following Tasks please always use at least one commit. If you do multiple commits for one task that fine. Just give a short notice in the commit that completely fulfills the task so that we can later have a look at code at this point in time.
* If you find any Bugs later in the process that you want to fix, just do so and comment that it the commit.

## Tasks

### Task 1

#### Description

* Setup a basic Django Instance. Will will not need Django admin for this project so feel free to leave it out.
* Create a Superuser with the credentials:

  ```
  email: admin@webrunners.de
  password: admin
  ```
* Store this User in fixtures, so that it can be inserted via python manage.py loaddata <your_app_name>, and can also be used in tests.
* Provide a Readme/setup/install File that documents the steps that are necessary to get an local checkout of the repository up and running

#### Acceptance criteria

* the git repository has a commit in which the commit message contains a note that the task is fulfilled.
* a Django Instance without any content besides the initial test side is up and running.
* a superuser can be injected into the database via fixtures

#### Tips

* Just use django-admin startproject - lets not "waste" a lot of time by fine tuning the django installation
* DB Setup and fiddling with docker containers also uses up a lot of time. Lets stick with SQLite to save time.
* Djangos default User Model whats a username instead of an email as the user identifier. You can either create your own user model that inherits from djangos BaseUserModel or use some external lib like  django-emailuser to change that. If you have another idea on how to solve this feel free to do so.

### Task 2

#### Description

* get rid of djangos default test page
* Create a Login Page that asks for a Username and Password. The Login Page should be the default Page when the Project URL is visited.
* After Login successful login redirect the User to /restricted_content page. Here the UserEmail and a working logout button is shown
* Write some tests to ensure proper behavior

#### Acceptance criteria

* login / logout and restricted_content pages are working
* the Admin user can successfully login with the credentials given in Task 1.
* Don't use Django Admin - we want to play with custom sites here.
* If you use some external libs please note that in your readme/setup/whatever file, together with a short comment about your reason to include them. No explicit explanation for sub-dependencies needed.

#### Tips

* this backend is meant to be used via API later. Don't get ultra fancy with django templates. Basic HTML5 is fine
* If you can't stand the ugliness of RAW HTML Sites just integrate some CSS Framework like Bootstrap or AntDesign, to make it look a little bit better. You can also use something like django-crispy-forms and e.g. crispy-bootstrap-5.

### Task 3

#### Description

Now lets create the API that the "real" frontend will use later:

* create an api endpoint that accepts an username and a password. The response should contain a token that can be used in the frontend for further requests. The token should not be valid forever and there should be a variable in settings.py which can change the time span in which a token is valid.
* create a second api endpoint that responses with 403 if no valid token is given. If a valid token is given (probably in the request header) the page response should have an HTTP Code 200 and the content should contain the email address of the logged in user
* provide some tests for this

#### Acceptance criteria

* there are two new endpoints that are meant to be used by an API
* Token based authorization is possible
* Tests ensure the correct behavior
* document the api endpoints somehow

#### Tips

* The kind of token is not important. E.g. you can find libs for jwt-token authorization
* Choose an API Format of your liking. It might be JSON or XML based REST, Graphql or even SOAP if want.

### Task 4

#### Description

* create new api endpoints that is only valid for users that have is_superuser=True
* the should have appropriate paths and enable admins to CRUD (Create, Read, Update Delete) new Users. Users should be created with the required fields (email, password) and already be activated (is_active=True), everything else can stay in there default state (e.g. is_superuser=False, is_admin=False, first and last_name blank)

#### Acceptance criteria

* as an admin I can CRUD new users via the API
* created Users are login with a username and password that the admin used in create or update views
* as an admin I can see a list of all currently existing users in the system

#### Tips

* The Django-Rest-Framework can really save some time here.
* If you want to go the Graphql route have a look at SerializerMutations
* Yes the Admin sets the password for other Users here. We now that this is very bad practice but in limited time we have to make some compromises.

### Task 5

#### Description

Bonus:
If you still have some time left we feel free to note down a better solution for the "admin sets the users password" problem. You don't have to fully implement it.
Just some text in the Readme that roughly explains the implementation idea. Some effort estimation for that would be interesting to see too.
If there is still time left feel free to implement it. You could also improve the CRUD endpoints to contain more fields and cover that with tests.
If there is still a lot of time left you could also scribble down some Frontend that makes use of the API

#### Acceptance criteria

None. This is Bonus content.