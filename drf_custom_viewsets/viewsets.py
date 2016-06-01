from rest_framework.viewsets import ModelViewSet


class CustomSerializerViewSet(ModelViewSet):

    def get_serializer_class(self):
        # """
        # Return the class to use for the serializer.
        # Defaults to using `self.serializer_class`.
        # You may want to override this if you need to provide different
        # serializations depending on the incoming request.
        # (Eg. admins get full serialization, others get basic serialization)
        # """
        # assert self.serializer_class is not None, (
        #     "'%s' should either include a `serializer_class` attribute, "
        #     "or override the `get_serializer_class()` method."
        #     % self.__class__.__name__
        # )
        #
        # return self.serializer_class

        """ Return the class to use for serializer w.r.t to the request method."""

        # if self.custom_serializer_classes is None:
        #     return super.get_serializer_class()
        # else:
        #     if self.request.method in self.custom_serializer_classes:
        #         return self.custom_serializer_classes[self.request.method]
        #     else:
        #         return super.get_serializer_class()

        try:
            return self.custom_serializer_classes[self.action]
        except (KeyError, AttributeError):
            return super(CustomSerializerViewSet, self).get_serializer_class()

