# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.event_trigger import EventTrigger  # noqa: F401,E501


class InlineResponse2001(object):
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
        'data': 'list[EventTrigger]',
        'next': 'str'
    }

    attribute_map = {
        'data': 'data',
        'next': 'next'
    }

    def __init__(self, data=None, next=None):  # noqa: E501
        """InlineResponse2001 - a model defined in Swagger"""  # noqa: E501

        self._data = None
        self._next = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if next is not None:
            self.next = next

    @property
    def data(self):
        """Gets the data of this InlineResponse2001.  # noqa: E501


        :return: The data of this InlineResponse2001.  # noqa: E501
        :rtype: list[EventTrigger]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this InlineResponse2001.


        :param data: The data of this InlineResponse2001.  # noqa: E501
        :type: list[EventTrigger]
        """

        self._data = data

    @property
    def next(self):
        """Gets the next of this InlineResponse2001.  # noqa: E501

        The link to the next page. No value if it is last page.  # noqa: E501

        :return: The next of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this InlineResponse2001.

        The link to the next page. No value if it is last page.  # noqa: E501

        :param next: The next of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._next = next

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
        if issubclass(InlineResponse2001, dict):
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
        if not isinstance(other, InlineResponse2001):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other