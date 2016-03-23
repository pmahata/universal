# Django API with Django Rest Framework, AngularJS-Resource and SQLite

This sample project is an update to the sample project in 
https://github.com/kevinastone/django-api-rest-and-angular.

The updates are as follows:

1. Requirements include extra facilities that are necessary for using ipython.
2. Django api (example/api/api.py and example/api/api.py) are updated to correct some errors for editing functionalities.
    1. NewPostSerializer is added to differentiate between serializer required for showing posts and saving posts.
    2. Consequently, PostList class is amended to have a get_serializer_class method which chooses a serializer depended on request.method. If it is 'POST', then we choose NewPostSerializer, otherwise PostSerializer is default one.
    3. PostPhotoList view's get_queryset method is corrected to avoid the following AssertionError: 'PostPhotoList' should either include a `queryset` attribute, or override the `get_queryset()` method.

  

## Dependencies

To setup and run the sample code, you're going to need `npm` from NodeJS available to install the frontend code.

## Setup

You're encouraged to setup a `virtualenv` to work in prior to configuring the dependencies.

1. Install Python Requirements

        pip install -r requirements.txt
        python setup.py develop

2. Install Bower + Grunt

		npm install -g grunt-cli bower

3. Install Assets

        npm install
        bower install

4. Compile Assets

        grunt

5. Setup the Database

        make create_database; make make_fixtures

6. Run the Server

        ./manage.py runserver

