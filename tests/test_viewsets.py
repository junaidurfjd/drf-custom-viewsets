#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_rest_framework_custom_viewsets
------------

Tests for `rest_framework_custom_viewsets` models module.
"""

# Adding a comment for the sake of a push

from django.db import models

from test_plus.test import TestCase

from drf_custom_viewsets import viewsets

from rest_framework.test import APIRequestFactory

from rest_framework import status

from rest_framework.response import Response

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


class MyViewSet(viewsets.CustomSerializerViewSet):
    serializer_class = SerCreate
    queryset = []
    custom_serializer_classes = {
        'list': SerList,
    }

    def create(self, request, *args, **kwargs):
        return Response(SerCreate().data, status=status.HTTP_201_CREATED)


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

    def test_no_match_returns_default_serializer(self):
        request = factory.post('/fakeurl')
        my_view = MyViewSet.as_view(actions={
            'post': 'create',
        })

        response = my_view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['key'], "Create Serializer")

    def tearDown(self):
        pass
