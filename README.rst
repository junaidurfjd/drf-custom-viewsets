=============================
Rest Framework Custom ViewSets
=============================

.. image:: https://badge.fury.io/py/rest_framework_custom_viewsets.png
    :target: https://badge.fury.io/py/rest_framework_custom_viewsets

.. image:: https://travis-ci.org/Darwesh27/rest_framework_custom_viewsets.png?branch=master
    :target: https://travis-ci.org/Darwesh27/rest_framework_custom_viewsets

Django ModelViewSet extended for per view base extensions like Serializer Classes etc.

Documentation
-------------

The full documentation is at https://rest_framework_custom_viewsets.readthedocs.org.

Quickstart
----------

Install Rest Framework Custom ViewSets::

    pip install rest_framework_custom_viewsets
Add it to the INSTALLED_APPS setting::

    INSTALLED_APPS += ('drf_custom_viewsets')

Example::

    from drf_custom_viewsets.viewsets.CustomSerializerViewSet
    from myapp.serializers import CustomSerializer1, CustomSerializer2

    class MyViewSet(CustomSerializerViewSet):
        custom_serializer_class = {
            'GET':  CustomSerializer1,
            'POST': CustomSerializer2,
        }


Then import it in a project::

    import drf_custom_viewsets
Features
--------

* TODO

Running Tests
--------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements-test.txt
    (myenv) $ python runtests.py

Credits
---------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
