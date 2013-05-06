OpenUDC
-------

Please take a moment to read what OpenUDC means (http://www.openudc.org).
There is an already existing project hosted right there (https://github.com/Open-UDC/open-udc) and whose mission is to have a cross-platform and compatible implementation of OpenUDC protocols through several standard systems.

Goal
----

This project aims ONLY to provide an application of openudc protocol by using Django. If you would like to contribute either for a more general implementation please look at the official OpenUDC project repository.

Demo
----

There is an demonstration instance available at http://demo.openudc.org
This version is still in development so please forgive us in advance.

Installation
------------

### Dependencies

To make the project working on your own machine, there is several dependencies you have to install first:

* python2
* django 1.4/+
* python-sqlite
* python-pyme

### Get the repos

When your ready, you have to call the following command line in order to get the project repository:

    git clone git@github.com:canercandan/django-openudc.git

### Start the server

Go now to the new created directory and call the following command line in order to launch the web server:

    ./manage.py runserver

For IPv6 fan boys (add the option -6).

And then everything is ready to be used. Go to following address to use your OpenUDC instances:

<code>
http://127.0.0.1:8000/
</code>

or

<code>http://[::1]:8000</code> (for IPv6 users).

References
----------

* The official OpenUDC project website : http://www.openudc.org
* The official OpenUDC repository: https://github.com/Open-UDC/open-udc
