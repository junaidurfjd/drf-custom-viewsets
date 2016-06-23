=============================
Rest Framework Custom ViewSets
=============================

.. image:: https://badge.fury.io/py/rest_framework_custom_viewsets.png
    :target: https://badge.fury.io/py/rest_framework_custom_viewsets

.. image:: https://travis-ci.org/Darwesh27/rest_framework_custom_viewsets.png?branch=master
    :target: https://travis-ci.org/Darwesh27/rest_framework_custom_viewsets

A very small library for extending the functionality of DRF ModelViewSet.
Viewsets
-------------

The first of out custom viewsets is the CustomSerializerViewSet that allows you to specify different serializers for different actions of a viewset.

Quickstart
----------

Install Rest Framework Custom ViewSets::

    pip install rest_framework_custom_viewsets

then extend you ViewSet class from viewsets.CustomSerializerViewSet

Example::

    from drf_custom_viewsets.viewsets.CustomSerializerViewSet
    from myapp.serializers import DefaltSerializer, CustomSerializer1, CustomSerializer2

    class MyViewSet(CustomSerializerViewSet):
        serializer_class = DefaultSerializer
        custom_serializer_classes = {
            'create':  CustomSerializer1,
            'update': CustomSerializer2,
        }



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
