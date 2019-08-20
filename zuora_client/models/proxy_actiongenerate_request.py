# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.z_object import ZObject  # noqa: F401,E501


class ProxyActiongenerateRequest(object):
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
        'objects': 'list[ZObject]',
        'type': 'str'
    }

    attribute_map = {
        'objects': 'objects',
        'type': 'type'
    }

    def __init__(self, objects=None, type=None):  # noqa: E501
        """ProxyActiongenerateRequest - a model defined in Swagger"""  # noqa: E501

        self._objects = None
        self._type = None
        self.discriminator = None

        self.objects = objects
        self.type = type

    @property
    def objects(self):
        """Gets the objects of this ProxyActiongenerateRequest.  # noqa: E501

          # noqa: E501

        :return: The objects of this ProxyActiongenerateRequest.  # noqa: E501
        :rtype: list[ZObject]
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        """Sets the objects of this ProxyActiongenerateRequest.

          # noqa: E501

        :param objects: The objects of this ProxyActiongenerateRequest.  # noqa: E501
        :type: list[ZObject]
        """
        if objects is None:
            raise ValueError("Invalid value for `objects`, must not be `None`")  # noqa: E501

        self._objects = objects

    @property
    def type(self):
        """Gets the type of this ProxyActiongenerateRequest.  # noqa: E501

          # noqa: E501

        :return: The type of this ProxyActiongenerateRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProxyActiongenerateRequest.

          # noqa: E501

        :param type: The type of this ProxyActiongenerateRequest.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Invoice"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(ProxyActiongenerateRequest, dict):
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
        if not isinstance(other, ProxyActiongenerateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other