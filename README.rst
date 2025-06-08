Base Skeleton to start your application using Flask-AppBuilder
--------------------------------------------------------------

- Install it::

	pip install flask-appbuilder
	git clone https://github.com/dpgaspar/Flask-AppBuilder-Skeleton.git

- Run it::

    $ export FLASK_APP=app
    # Create an admin user
    $ flask fab create-admin
    # Run dev server
    $ flask run


That's it!!

Note:

1. **For local development:**
   - Set `FLASK_ENV=development` and run `docker build`/`docker run` as usual, or just use `flask run` directly outside Docker.

2. **For production:**
   - Ensure `FLASK_ENV` is not set to `development` (default is `production`), so `gunicorn` will be used.

**Summary:**  
This approach lets you control the server used via the `FLASK_ENV` environment variable, using `flask run` for development and `gunicorn` for production, without changing your codebase.
