# coding: utf-8




import pprint
import re  # noqa: F401

import six


class OneTimeFlatFeePricingOverride(object):
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
        'list_price': 'float'
    }

    attribute_map = {
        'list_price': 'listPrice'
    }

    def __init__(self, list_price=None):  # noqa: E501
        """OneTimeFlatFeePricingOverride - a model defined in Swagger"""  # noqa: E501

        self._list_price = None
        self.discriminator = None

        self.list_price = list_price

    @property
    def list_price(self):
        """Gets the list_price of this OneTimeFlatFeePricingOverride.  # noqa: E501

        Price of the charge.   # noqa: E501

        :return: The list_price of this OneTimeFlatFeePricingOverride.  # noqa: E501
        :rtype: float
        """
        return self._list_price

    @list_price.setter
    def list_price(self, list_price):
        """Sets the list_price of this OneTimeFlatFeePricingOverride.

        Price of the charge.   # noqa: E501

        :param list_price: The list_price of this OneTimeFlatFeePricingOverride.  # noqa: E501
        :type: float
        """
        if list_price is None:
            raise ValueError("Invalid value for `list_price`, must not be `None`")  # noqa: E501

        self._list_price = list_price

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
        if issubclass(OneTimeFlatFeePricingOverride, dict):
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
        if not isinstance(other, OneTimeFlatFeePricingOverride):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other