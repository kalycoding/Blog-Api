# Blog API using django and django rest framework and graphql



This project was done in order to deepen my rest-api and graphql skills.

Also understand how rest framework works, handling json data
<h4>Part 1:</h4>
<ol>
    <li>Create a Blog API where a user can post a blog.</li>
    <li>Used django rest framework to serialize the model into Json</li>
     <li>Used graphene djangopackage to to add support for graphql</li>
    
</ol>



    

    
<h2>Additional Python Modules Required:</h2>
<ul>
    <li>Django</li>
    <li>django-rest-framework</li>
    <li>django-rest-auth</li>
    <li>django jwt library</li>
    <li>graphene-django</li>
    
</ul>
  


<h2>Usage :</h2>

    pip install -r requirments.txt
    
    python blogpost/manage.py makemigrations

    python blogpost/manage.py migrate

    python blogpost/manage.py runserver
    
   In your web browser enter the address : http://localhost:8000 or http://127.0.0.1:8000/
   
   
   or enter https://blogger-aping.herokuapp.com/ for the hosted API on heroku
