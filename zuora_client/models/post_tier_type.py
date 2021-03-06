# coding: utf-8




import pprint
import re  # noqa: F401

import six


class POSTTierType(object):
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
        'ending_unit': 'str',
        'price': 'str',
        'price_format': 'str',
        'starting_unit': 'str',
        'tier': 'int'
    }

    attribute_map = {
        'ending_unit': 'endingUnit',
        'price': 'price',
        'price_format': 'priceFormat',
        'starting_unit': 'startingUnit',
        'tier': 'tier'
    }

    def __init__(self, ending_unit=None, price=None, price_format=None, starting_unit=None, tier=None):  # noqa: E501
        """POSTTierType - a model defined in Swagger"""  # noqa: E501

        self._ending_unit = None
        self._price = None
        self._price_format = None
        self._starting_unit = None
        self._tier = None
        self.discriminator = None

        if ending_unit is not None:
            self.ending_unit = ending_unit
        self.price = price
        if price_format is not None:
            self.price_format = price_format
        if starting_unit is not None:
            self.starting_unit = starting_unit
        self.tier = tier

    @property
    def ending_unit(self):
        """Gets the ending_unit of this POSTTierType.  # noqa: E501

        End number of a range of units for the tier.   # noqa: E501

        :return: The ending_unit of this POSTTierType.  # noqa: E501
        :rtype: str
        """
        return self._ending_unit

    @ending_unit.setter
    def ending_unit(self, ending_unit):
        """Sets the ending_unit of this POSTTierType.

        End number of a range of units for the tier.   # noqa: E501

        :param ending_unit: The ending_unit of this POSTTierType.  # noqa: E501
        :type: str
        """

        self._ending_unit = ending_unit

    @property
    def price(self):
        """Gets the price of this POSTTierType.  # noqa: E501

        Price of the tier if the charge is a flat fee, or the price of each unit in the tier if the charge model is tiered pricing.   # noqa: E501

        :return: The price of this POSTTierType.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this POSTTierType.

        Price of the tier if the charge is a flat fee, or the price of each unit in the tier if the charge model is tiered pricing.   # noqa: E501

        :param price: The price of this POSTTierType.  # noqa: E501
        :type: str
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def price_format(self):
        """Gets the price_format of this POSTTierType.  # noqa: E501

        Indicates if pricing is a flat fee or is per unit.  Values:  * `FlatFee` * `PerUnit`   # noqa: E501

        :return: The price_format of this POSTTierType.  # noqa: E501
        :rtype: str
        """
        return self._price_format

    @price_format.setter
    def price_format(self, price_format):
        """Sets the price_format of this POSTTierType.

        Indicates if pricing is a flat fee or is per unit.  Values:  * `FlatFee` * `PerUnit`   # noqa: E501

        :param price_format: The price_format of this POSTTierType.  # noqa: E501
        :type: str
        """

        self._price_format = price_format

    @property
    def starting_unit(self):
        """Gets the starting_unit of this POSTTierType.  # noqa: E501

        Starting number of a range of units for the tier.   # noqa: E501

        :return: The starting_unit of this POSTTierType.  # noqa: E501
        :rtype: str
        """
        return self._starting_unit

    @starting_unit.setter
    def starting_unit(self, starting_unit):
        """Sets the starting_unit of this POSTTierType.

        Starting number of a range of units for the tier.   # noqa: E501

        :param starting_unit: The starting_unit of this POSTTierType.  # noqa: E501
        :type: str
        """

        self._starting_unit = starting_unit

    @property
    def tier(self):
        """Gets the tier of this POSTTierType.  # noqa: E501

        Unique number that identifies the tier that the price applies to.   # noqa: E501

        :return: The tier of this POSTTierType.  # noqa: E501
        :rtype: int
        """
        return self._tier

    @tier.setter
    def tier(self, tier):
        """Sets the tier of this POSTTierType.

        Unique number that identifies the tier that the price applies to.   # noqa: E501

        :param tier: The tier of this POSTTierType.  # noqa: E501
        :type: int
        """
        if tier is None:
            raise ValueError("Invalid value for `tier`, must not be `None`")  # noqa: E501

        self._tier = tier

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
        if issubclass(POSTTierType, dict):
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
        if not isinstance(other, POSTTierType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
