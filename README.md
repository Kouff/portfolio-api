## Portfolio API Server

Frameworks:

* [Django](https://www.djangoproject.com/)
* [Django-rest-framework](https://www.django-rest-framework.org/)
* [Simple-JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
* [Django-cors-headers](https://github.com/adamchainz/django-cors-headers#setup)
* [Drf-yasg](https://drf-yasg.readthedocs.io/en/stable/)

Clone a project and move to it:

    $ git clone https://github.com/Kouff/portfolio-api.git
    $ cd portfolio-api

Create a [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html#via-pip)
and [activate](https://virtualenv.pypa.io/en/latest/user_guide.html#activators) it and install the requirements:

    $ pip install -r requirements.txt

Run the server:

    $ gunicorn settings.wsgi

OpenAPI (Swagger): http://127.0.0.1:8000/swagger/

###Comments:
POST /comments/ - Create a new comment;

PATCH /comments/{id}/ - Edit a comment (for the comment author only);

DELETE /comments/{id}/ - Delete a comment (for the comment author only).

###Images:
GET /images/ - Show all the images;

POST /images/ - Create a new image;

GET /images/my/ - Show all images of the current user;

GET /images/{id}/ - Show an image with comments;

PATCH /images/{id}/ - Edit an image (for the image owner only);

DELETE /images/{id}/ - Delete an image (for the image owner only).

###Portfolios:
GET /portfolios/ - Show all the portfolios;

POST /portfolios/ - Create a new portfolio;

GET /portfolios/my/ - Show all portfolios of the current user;

GET /portfolios/{id}/ - Show a portfolio with images;

PATCH /portfolios/{id}/ - Edit a portfolio (for the portfolio owner only);

DELETE /portfolios/{id}/ - Delete a portfolio (for the portfolio owner only).

###Registration:
POST /registration/ - Registration / Create a new user.

###Token:
POST /token/ - Get JWT (access and refresh tokens);

POST /token/refresh/ - Refresh access token.

###Users:
GET /users/me/ - Show the current user;

PATCH /users/me/ - Edit the current user;

DELETE /users/me/ - Delete the current user.

