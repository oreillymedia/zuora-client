# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.price_change_params import PriceChangeParams  # noqa: F401,E501


class UsageOveragePricingOverride(object):
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
        'included_units': 'float',
        'number_of_periods': 'int',
        'overage_price': 'float',
        'overage_unused_units_credit_option': 'str',
        'unused_units_credit_rates': 'float'
    }

    attribute_map = {
        'price_change_option': 'priceChangeOption',
        'price_increase_percentage': 'priceIncreasePercentage',
        'included_units': 'includedUnits',
        'number_of_periods': 'numberOfPeriods',
        'overage_price': 'overagePrice',
        'overage_unused_units_credit_option': 'overageUnusedUnitsCreditOption',
        'unused_units_credit_rates': 'unusedUnitsCreditRates'
    }

    def __init__(self, price_change_option=None, price_increase_percentage=None, included_units=None, number_of_periods=None, overage_price=None, overage_unused_units_credit_option=None, unused_units_credit_rates=None):  # noqa: E501
        """UsageOveragePricingOverride - a model defined in Swagger"""  # noqa: E501

        self._price_change_option = None
        self._price_increase_percentage = None
        self._included_units = None
        self._number_of_periods = None
        self._overage_price = None
        self._overage_unused_units_credit_option = None
        self._unused_units_credit_rates = None
        self.discriminator = None

        if price_change_option is not None:
            self.price_change_option = price_change_option
        if price_increase_percentage is not None:
            self.price_increase_percentage = price_increase_percentage
        if included_units is not None:
            self.included_units = included_units
        if number_of_periods is not None:
            self.number_of_periods = number_of_periods
        if overage_price is not None:
            self.overage_price = overage_price
        if overage_unused_units_credit_option is not None:
            self.overage_unused_units_credit_option = overage_unused_units_credit_option
        if unused_units_credit_rates is not None:
            self.unused_units_credit_rates = unused_units_credit_rates

    @property
    def price_change_option(self):
        """Gets the price_change_option of this UsageOveragePricingOverride.  # noqa: E501

        Specifies how Zuora changes the price of the charge each time the subscription renews.  If the value of this field is `SpecificPercentageValue`, use the `priceIncreasePercentage` field to specify how much the price of the charge should change.   # noqa: E501

        :return: The price_change_option of this UsageOveragePricingOverride.  # noqa: E501
        :rtype: str
        """
        return self._price_change_option

    @price_change_option.setter
    def price_change_option(self, price_change_option):
        """Sets the price_change_option of this UsageOveragePricingOverride.

        Specifies how Zuora changes the price of the charge each time the subscription renews.  If the value of this field is `SpecificPercentageValue`, use the `priceIncreasePercentage` field to specify how much the price of the charge should change.   # noqa: E501

        :param price_change_option: The price_change_option of this UsageOveragePricingOverride.  # noqa: E501
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
        """Gets the price_increase_percentage of this UsageOveragePricingOverride.  # noqa: E501

        Specifies the percentage by which the price of the charge should change each time the subscription renews. Only applicable if the value of the `priceChangeOption` field is `SpecificPercentageValue`.   # noqa: E501

        :return: The price_increase_percentage of this UsageOveragePricingOverride.  # noqa: E501
        :rtype: float
        """
        return self._price_increase_percentage

    @price_increase_percentage.setter
    def price_increase_percentage(self, price_increase_percentage):
        """Sets the price_increase_percentage of this UsageOveragePricingOverride.

        Specifies the percentage by which the price of the charge should change each time the subscription renews. Only applicable if the value of the `priceChangeOption` field is `SpecificPercentageValue`.   # noqa: E501

        :param price_increase_percentage: The price_increase_percentage of this UsageOveragePricingOverride.  # noqa: E501
        :type: float
        """
        if price_increase_percentage is not None and price_increase_percentage < -100:  # noqa: E501
            raise ValueError("Invalid value for `price_increase_percentage`, must be a value greater than or equal to `-100`")  # noqa: E501

        self._price_increase_percentage = price_increase_percentage

    @property
    def included_units(self):
        """Gets the included_units of this UsageOveragePricingOverride.  # noqa: E501

        Number of free units that may be consumed.   # noqa: E501

        :return: The included_units of this UsageOveragePricingOverride.  # noqa: E501
        :rtype: float
        """
        return self._included_units

    @included_units.setter
    def included_units(self, included_units):
        """Sets the included_units of this UsageOveragePricingOverride.

        Number of free units that may be consumed.   # noqa: E501

        :param included_units: The included_units of this UsageOveragePricingOverride.  # noqa: E501
        :type: float
        """
        if included_units is not None and included_units < 0:  # noqa: E501
            raise ValueError("Invalid value for `included_units`, must be a value greater than or equal to `0`")  # noqa: E501

        self._included_units = included_units

    @property
    def number_of_periods(self):
        """Gets the number_of_periods of this UsageOveragePricingOverride.  # noqa: E501

        Number of periods that Zuora considers when calculating overage charges with overage smoothing.   # noqa: E501

        :return: The number_of_periods of this UsageOveragePricingOverride.  # noqa: E501
        :rtype: int
        """
        return self._number_of_periods

    @number_of_periods.setter
    def number_of_periods(self, number_of_periods):
        """Sets the number_of_periods of this UsageOveragePricingOverride.

        Number of periods that Zuora considers when calculating overage charges with overage smoothing.   # noqa: E501

        :param number_of_periods: The number_of_periods of this UsageOveragePricingOverride.  # noqa: E501
        :type: int
        """
        if number_of_periods is not None and number_of_periods < 1:  # noqa: E501
            raise ValueError("Invalid value for `number_of_periods`, must be a value greater than or equal to `1`")  # noqa: E501

        self._number_of_periods = number_of_periods

    @property
    def overage_price(self):
        """Gets the overage_price of this UsageOveragePricingOverride.  # noqa: E501

        Price per overage unit consumed.   # noqa: E501

        :return: The overage_price of this UsageOveragePricingOverride.  # noqa: E501
        :rtype: float
        """
        return self._overage_price

    @overage_price.setter
    def overage_price(self, overage_price):
        """Sets the overage_price of this UsageOveragePricingOverride.

        Price per overage unit consumed.   # noqa: E501

        :param overage_price: The overage_price of this UsageOveragePricingOverride.  # noqa: E501
        :type: float
        """

        self._overage_price = overage_price

    @property
    def overage_unused_units_credit_option(self):
        """Gets the overage_unused_units_credit_option of this UsageOveragePricingOverride.  # noqa: E501

        Specifies whether to credit the customer for unused units.  If the value of this field is `CreditBySpecificRate`, use the `unusedUnitsCreditRates` field to specify the rate at which to credit the customer for unused units.   # noqa: E501

        :return: The overage_unused_units_credit_option of this UsageOveragePricingOverride.  # noqa: E501
        :rtype: str
        """
        return self._overage_unused_units_credit_option

    @overage_unused_units_credit_option.setter
    def overage_unused_units_credit_option(self, overage_unused_units_credit_option):
        """Sets the overage_unused_units_credit_option of this UsageOveragePricingOverride.

        Specifies whether to credit the customer for unused units.  If the value of this field is `CreditBySpecificRate`, use the `unusedUnitsCreditRates` field to specify the rate at which to credit the customer for unused units.   # noqa: E501

        :param overage_unused_units_credit_option: The overage_unused_units_credit_option of this UsageOveragePricingOverride.  # noqa: E501
        :type: str
        """
        allowed_values = ["NoCredit", "CreditBySpecificRate"]  # noqa: E501
        if overage_unused_units_credit_option not in allowed_values:
            raise ValueError(
                "Invalid value for `overage_unused_units_credit_option` ({0}), must be one of {1}"  # noqa: E501
                .format(overage_unused_units_credit_option, allowed_values)
            )

        self._overage_unused_units_credit_option = overage_unused_units_credit_option

    @property
    def unused_units_credit_rates(self):
        """Gets the unused_units_credit_rates of this UsageOveragePricingOverride.  # noqa: E501

        Per-unit rate at which to credit the customer for unused units. Only applicable if the value of the `overageUnusedUnitsCreditOption` field is `CreditBySpecificRate`.   # noqa: E501

        :return: The unused_units_credit_rates of this UsageOveragePricingOverride.  # noqa: E501
        :rtype: float
        """
        return self._unused_units_credit_rates

    @unused_units_credit_rates.setter
    def unused_units_credit_rates(self, unused_units_credit_rates):
        """Sets the unused_units_credit_rates of this UsageOveragePricingOverride.

        Per-unit rate at which to credit the customer for unused units. Only applicable if the value of the `overageUnusedUnitsCreditOption` field is `CreditBySpecificRate`.   # noqa: E501

        :param unused_units_credit_rates: The unused_units_credit_rates of this UsageOveragePricingOverride.  # noqa: E501
        :type: float
        """

        self._unused_units_credit_rates = unused_units_credit_rates

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
        if issubclass(UsageOveragePricingOverride, dict):
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
        if not isinstance(other, UsageOveragePricingOverride):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
