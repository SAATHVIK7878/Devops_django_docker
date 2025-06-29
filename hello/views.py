from django.shortcuts import render

from .models import Greeting

# Create your views here.


def index(request):
    return render(request, "index.html")


def db(request):
    # If you encounter errors visiting the `/db/` page on the example app, check that:
    #
    # When running the app on Heroku:
    #   1. You have added the Postgres database to your app.
    #   2. You have uncommented the `psycopg` dependency in `requirements.txt`, and the `release`
    #      process entry in `Procfile`, git committed your changes and re-deployed the app.
    #
    # When running the app locally:
    #   1. You have run `./manage.py migrate` to create the `hello_greeting` database table.

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


from django.http import HttpResponse

def index(request):
    return HttpResponse("""
        <h1>Hello from Saathvik K and Team!</h1>
        <p>We have developed a <strong>simple website</strong> which says 'Hello' to the user.</p>
        <p>We containerized it using <strong>Docker</strong> and pushed the code in to a <strong>GitHub repository</strong>.</p>
        <br>
        <h2>THANK YOU!</h2>
        <h3>Team Members:</h3>
        <ul>
            <li>23951A057W - Saathvik K</li>
            <li>23951A057U - T Rukesh Kumar</li>
        </ul>
    """)
    
    
    

