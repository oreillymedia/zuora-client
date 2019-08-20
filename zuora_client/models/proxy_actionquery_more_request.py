# coding: utf-8




import pprint
import re  # noqa: F401

import six


class ProxyActionqueryMoreRequest(object):
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
        'query_locator': 'str'
    }

    attribute_map = {
        'query_locator': 'queryLocator'
    }

    def __init__(self, query_locator=None):  # noqa: E501
        """ProxyActionqueryMoreRequest - a model defined in Swagger"""  # noqa: E501

        self._query_locator = None
        self.discriminator = None

        self.query_locator = query_locator

    @property
    def query_locator(self):
        """Gets the query_locator of this ProxyActionqueryMoreRequest.  # noqa: E501

          # noqa: E501

        :return: The query_locator of this ProxyActionqueryMoreRequest.  # noqa: E501
        :rtype: str
        """
        return self._query_locator

    @query_locator.setter
    def query_locator(self, query_locator):
        """Sets the query_locator of this ProxyActionqueryMoreRequest.

          # noqa: E501

        :param query_locator: The query_locator of this ProxyActionqueryMoreRequest.  # noqa: E501
        :type: str
        """
        if query_locator is None:
            raise ValueError("Invalid value for `query_locator`, must not be `None`")  # noqa: E501

        self._query_locator = query_locator

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
        if issubclass(ProxyActionqueryMoreRequest, dict):
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
        if not isinstance(other, ProxyActionqueryMoreRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other