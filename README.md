# exercise-recordly

test commit


- testing
- architecture
- cgi and ajax
- coded in github
- must be deployed and semi-functional
- talk about process
- where app and code will go


User Features:
- list
- search by name, by type, by favorite
- create entry
- tag/untag favorite

Engineering Features:
- authenication and sessions
- search and indexing
- data storage, record keeping

Front End:
user page

Back End:



Future:
- for such a simple application, would just create a more consistent SPA experience by removing the CGI and having everything be ajax, so the user feels like its an app rather than a series of webpages
- use indexing application like Sphinx, Solr, ElasticSearch to implement proper search and remove load from doing a database search, which is a terrible idea
- 



source /Users/stanchovy/me/local/dev/config/python-virtualenvwrapper-workon-home/django/bin/activate
django-admin.py startproject recordly-server
python manage.py startapp recordly

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

python manage.py runserver
