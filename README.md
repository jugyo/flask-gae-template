flask-gae-template
======

Setup
------

    git clone http://github.com/jugyo/flask-gae-template.git app
    cd app
    ./setup.sh

Run
------

    dev_appserver.py .

and open 'http://localhost:8080/hello'.

Deploy
------

You should fix application name of app.yaml before deploy.

    appcfg.py update .

TODO
------

* sample for test

See Also
------

[http://flask.pocoo.org/](http://flask.pocoo.org/)
