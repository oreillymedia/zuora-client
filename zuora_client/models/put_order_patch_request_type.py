# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.order_object_custom_fields import OrderObjectCustomFields  # noqa: F401,E501
from zuora_client.models.put_order_patch_request_type_subscriptions import PUTOrderPatchRequestTypeSubscriptions  # noqa: F401,E501


class PUTOrderPatchRequestType(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'custom_fields': 'OrderObjectCustomFields',
        'subscriptions': 'list[PUTOrderPatchRequestTypeSubscriptions]'
    }

    attribute_map = {
        'custom_fields': 'customFields',
        'subscriptions': 'subscriptions'
    }

    def __init__(self, custom_fields=None, subscriptions=None):  # noqa: E501
        """PUTOrderPatchRequestType - a model defined in Swagger"""  # noqa: E501

        self._custom_fields = None
        self._subscriptions = None
        self.discriminator = None

        if custom_fields is not None:
            self.custom_fields = custom_fields
        if subscriptions is not None:
            self.subscriptions = subscriptions

    @property
    def custom_fields(self):
        """Gets the custom_fields of this PUTOrderPatchRequestType.  # noqa: E501


        :return: The custom_fields of this PUTOrderPatchRequestType.  # noqa: E501
        :rtype: OrderObjectCustomFields
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this PUTOrderPatchRequestType.


        :param custom_fields: The custom_fields of this PUTOrderPatchRequestType.  # noqa: E501
        :type: OrderObjectCustomFields
        """

        self._custom_fields = custom_fields

    @property
    def subscriptions(self):
        """Gets the subscriptions of this PUTOrderPatchRequestType.  # noqa: E501


        :return: The subscriptions of this PUTOrderPatchRequestType.  # noqa: E501
        :rtype: list[PUTOrderPatchRequestTypeSubscriptions]
        """
        return self._subscriptions

    @subscriptions.setter
    def subscriptions(self, subscriptions):
        """Sets the subscriptions of this PUTOrderPatchRequestType.


        :param subscriptions: The subscriptions of this PUTOrderPatchRequestType.  # noqa: E501
        :type: list[PUTOrderPatchRequestTypeSubscriptions]
        """

        self._subscriptions = subscriptions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PUTOrderPatchRequestType, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PUTOrderPatchRequestType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
