# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.price_change_params import PriceChangeParams  # noqa: F401,E501


class UsagePerUnitPricingUpdate(object):
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
        'price_change_option': 'str',
        'price_increase_percentage': 'float',
        'list_price': 'float'
    }

    attribute_map = {
        'price_change_option': 'priceChangeOption',
        'price_increase_percentage': 'priceIncreasePercentage',
        'list_price': 'listPrice'
    }

    def __init__(self, price_change_option=None, price_increase_percentage=None, list_price=None):  # noqa: E501
        """UsagePerUnitPricingUpdate - a model defined in Swagger"""  # noqa: E501

        self._price_change_option = None
        self._price_increase_percentage = None
        self._list_price = None
        self.discriminator = None

        if price_change_option is not None:
            self.price_change_option = price_change_option
        if price_increase_percentage is not None:
            self.price_increase_percentage = price_increase_percentage
        if list_price is not None:
            self.list_price = list_price

    @property
    def price_change_option(self):
        """Gets the price_change_option of this UsagePerUnitPricingUpdate.  # noqa: E501

        Specifies how Zuora changes the price of the charge each time the subscription renews.  If the value of this field is `SpecificPercentageValue`, use the `priceIncreasePercentage` field to specify how much the price of the charge should change.   # noqa: E501

        :return: The price_change_option of this UsagePerUnitPricingUpdate.  # noqa: E501
        :rtype: str
        """
        return self._price_change_option

    @price_change_option.setter
    def price_change_option(self, price_change_option):
        """Sets the price_change_option of this UsagePerUnitPricingUpdate.

        Specifies how Zuora changes the price of the charge each time the subscription renews.  If the value of this field is `SpecificPercentageValue`, use the `priceIncreasePercentage` field to specify how much the price of the charge should change.   # noqa: E501

        :param price_change_option: The price_change_option of this UsagePerUnitPricingUpdate.  # noqa: E501
        :type: str
        """
        allowed_values = ["NoChange", "SpecificPercentageValue", "UseLatestProductCatalogPricing"]  # noqa: E501
        if price_change_option not in allowed_values:
            raise ValueError(
                "Invalid value for `price_change_option` ({0}), must be one of {1}"  # noqa: E501
                .format(price_change_option, allowed_values)
            )

        self._price_change_option = price_change_option

    @property
    def price_increase_percentage(self):
        """Gets the price_increase_percentage of this UsagePerUnitPricingUpdate.  # noqa: E501

        Specifies the percentage by which the price of the charge should change each time the subscription renews. Only applicable if the value of the `priceChangeOption` field is `SpecificPercentageValue`.   # noqa: E501

        :return: The price_increase_percentage of this UsagePerUnitPricingUpdate.  # noqa: E501
        :rtype: float
        """
        return self._price_increase_percentage

    @price_increase_percentage.setter
    def price_increase_percentage(self, price_increase_percentage):
        """Sets the price_increase_percentage of this UsagePerUnitPricingUpdate.

        Specifies the percentage by which the price of the charge should change each time the subscription renews. Only applicable if the value of the `priceChangeOption` field is `SpecificPercentageValue`.   # noqa: E501

        :param price_increase_percentage: The price_increase_percentage of this UsagePerUnitPricingUpdate.  # noqa: E501
        :type: float
        """
        if price_increase_percentage is not None and price_increase_percentage < -100:  # noqa: E501
            raise ValueError("Invalid value for `price_increase_percentage`, must be a value greater than or equal to `-100`")  # noqa: E501

        self._price_increase_percentage = price_increase_percentage

    @property
    def list_price(self):
        """Gets the list_price of this UsagePerUnitPricingUpdate.  # noqa: E501


        :return: The list_price of this UsagePerUnitPricingUpdate.  # noqa: E501
        :rtype: float
        """
        return self._list_price

    @list_price.setter
    def list_price(self, list_price):
        """Sets the list_price of this UsagePerUnitPricingUpdate.


        :param list_price: The list_price of this UsagePerUnitPricingUpdate.  # noqa: E501
        :type: float
        """

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
        if issubclass(UsagePerUnitPricingUpdate, dict):
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
        if not isinstance(other, UsagePerUnitPricingUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
