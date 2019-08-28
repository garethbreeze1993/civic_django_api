# civic_django_api
Simple REST API built in django. Has the option of being rendered with a custom HTML template, 
JSON or Django Rest Framework Browsable API.

I have made a simple model that tracks a subject of a vote the date it was taken the ayes and nays to the vote. 
The scenario was they wanted an app that tracked the votes and the ayes and nays passed.

I then used the django rest framework model serializer to create a simple serializer to allow people to pass api requests to the endpoint and then get the information into the database.
I then created the views which use django rest framework generic views for two endoints one for a list of all votes cast, and one for each specific instance.

I created a html template so I could use a html renderer to make a form so users could add new instances via this form rather than an API request.

I added permissions via the django rest framework generic permissions so a user has to be authenticated to do a post, put or delete request.
However any users can perform a get request.

Finally I added a condition that only staff users could use the browsable API that django rest framework provides. 
Anyone can use the HTML renderer or JSON Renderer

