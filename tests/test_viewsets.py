#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_rest_framework_custom_viewsets
------------

Tests for `rest_framework_custom_viewsets` models module.
"""

# Adding a comment for the sake of a push

from test_plus.test import TestCase

from drf_custom_viewsets import viewsets

from rest_framework.test import APIRequestFactory

from rest_framework import status

factory = APIRequestFactory()


class SerList(object):
    def __init__(self, *args, **kwargs):
        pass

    data = {
        'key': 'List Serializer',
    }


class SerCreate(object):
    def __init__(self, *args, **kwargs):
        pass

    data = {
        'key': 'Create Serializer',
    }


class MyQuerySet(object):
    pass


class MyViewSet(viewsets.CustomSerializerViewSet):
    serializer_class = SerCreate
    queryset = []
    custom_serializer_classes = {
        'list': SerList,
        'create': SerCreate,
    }


class TestCustomSerializerViewSet(TestCase):

    def setUp(self):
        pass

    def test_update_action_has_update_serializer(self):
        request = factory.get('/fakeurl')
        my_view = MyViewSet.as_view(actions={
            'get': 'list',
        })

        response = my_view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['key'], "List Serializer")

    def tearDown(self):
        pass
