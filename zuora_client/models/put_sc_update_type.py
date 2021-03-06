# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.post_tier_type import POSTTierType  # noqa: F401,E501
from zuora_client.models.rate_plan_charge_object_custom_fields import RatePlanChargeObjectCustomFields  # noqa: F401,E501


class PUTScUpdateType(object):
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
        'billing_period_alignment': 'str',
        'description': 'str',
        'included_units': 'str',
        'overage_price': 'str',
        'price': 'str',
        'price_change_option': 'str',
        'price_increase_percentage': 'str',
        'quantity': 'str',
        'rate_plan_charge_id': 'str',
        'tiers': 'list[POSTTierType]',
        'trigger_date': 'date',
        'trigger_event': 'str'
    }

    attribute_map = {
        'billing_period_alignment': 'billingPeriodAlignment',
        'description': 'description',
        'included_units': 'includedUnits',
        'overage_price': 'overagePrice',
        'price': 'price',
        'price_change_option': 'priceChangeOption',
        'price_increase_percentage': 'priceIncreasePercentage',
        'quantity': 'quantity',
        'rate_plan_charge_id': 'ratePlanChargeId',
        'tiers': 'tiers',
        'trigger_date': 'triggerDate',
        'trigger_event': 'triggerEvent'
    }

    def __init__(self, billing_period_alignment=None, description=None, included_units=None, overage_price=None, price=None, price_change_option=None, price_increase_percentage=None, quantity=None, rate_plan_charge_id=None, tiers=None, trigger_date=None, trigger_event=None):  # noqa: E501
        """PUTScUpdateType - a model defined in Swagger"""  # noqa: E501

        self._billing_period_alignment = None
        self._description = None
        self._included_units = None
        self._overage_price = None
        self._price = None
        self._price_change_option = None
        self._price_increase_percentage = None
        self._quantity = None
        self._rate_plan_charge_id = None
        self._tiers = None
        self._trigger_date = None
        self._trigger_event = None
        self.discriminator = None

        if billing_period_alignment is not None:
            self.billing_period_alignment = billing_period_alignment
        if description is not None:
            self.description = description
        if included_units is not None:
            self.included_units = included_units
        if overage_price is not None:
            self.overage_price = overage_price
        if price is not None:
            self.price = price
        if price_change_option is not None:
            self.price_change_option = price_change_option
        if price_increase_percentage is not None:
            self.price_increase_percentage = price_increase_percentage
        if quantity is not None:
            self.quantity = quantity
        self.rate_plan_charge_id = rate_plan_charge_id
        if tiers is not None:
            self.tiers = tiers
        if trigger_date is not None:
            self.trigger_date = trigger_date
        if trigger_event is not None:
            self.trigger_event = trigger_event

    @property
    def billing_period_alignment(self):
        """Gets the billing_period_alignment of this PUTScUpdateType.  # noqa: E501

        Aligns charges within the same subscription if multiple charges begin on different dates.  Values:  * `AlignToCharge` * `AlignToSubscriptionStart` * `AlignToTermStart`  Available for the following charge types:  * Recurring * Usage-based   # noqa: E501

        :return: The billing_period_alignment of this PUTScUpdateType.  # noqa: E501
        :rtype: str
        """
        return self._billing_period_alignment

    @billing_period_alignment.setter
    def billing_period_alignment(self, billing_period_alignment):
        """Sets the billing_period_alignment of this PUTScUpdateType.

        Aligns charges within the same subscription if multiple charges begin on different dates.  Values:  * `AlignToCharge` * `AlignToSubscriptionStart` * `AlignToTermStart`  Available for the following charge types:  * Recurring * Usage-based   # noqa: E501

        :param billing_period_alignment: The billing_period_alignment of this PUTScUpdateType.  # noqa: E501
        :type: str
        """

        self._billing_period_alignment = billing_period_alignment

    @property
    def description(self):
        """Gets the description of this PUTScUpdateType.  # noqa: E501

        Description of the charge.   # noqa: E501

        :return: The description of this PUTScUpdateType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PUTScUpdateType.

        Description of the charge.   # noqa: E501

        :param description: The description of this PUTScUpdateType.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def included_units(self):
        """Gets the included_units of this PUTScUpdateType.  # noqa: E501

        Specifies the number of units in the base set of units for this charge. Must be >=0.  Available for the following charge types for the Overage charge model:  * `Recurring` * `Usage-based`   # noqa: E501

        :return: The included_units of this PUTScUpdateType.  # noqa: E501
        :rtype: str
        """
        return self._included_units

    @included_units.setter
    def included_units(self, included_units):
        """Sets the included_units of this PUTScUpdateType.

        Specifies the number of units in the base set of units for this charge. Must be >=0.  Available for the following charge types for the Overage charge model:  * `Recurring` * `Usage-based`   # noqa: E501

        :param included_units: The included_units of this PUTScUpdateType.  # noqa: E501
        :type: str
        """

        self._included_units = included_units

    @property
    def overage_price(self):
        """Gets the overage_price of this PUTScUpdateType.  # noqa: E501

        Price for units over the allowed amount.   Available for the following charge type for the Overage and Tiered with Overage charge models:  * Usage-based   # noqa: E501

        :return: The overage_price of this PUTScUpdateType.  # noqa: E501
        :rtype: str
        """
        return self._overage_price

    @overage_price.setter
    def overage_price(self, overage_price):
        """Sets the overage_price of this PUTScUpdateType.

        Price for units over the allowed amount.   Available for the following charge type for the Overage and Tiered with Overage charge models:  * Usage-based   # noqa: E501

        :param overage_price: The overage_price of this PUTScUpdateType.  # noqa: E501
        :type: str
        """

        self._overage_price = overage_price

    @property
    def price(self):
        """Gets the price of this PUTScUpdateType.  # noqa: E501

        Price for units in the subscription rate plan.  Supports all charge types for the Flat Fee and Per Unit charge models   # noqa: E501

        :return: The price of this PUTScUpdateType.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this PUTScUpdateType.

        Price for units in the subscription rate plan.  Supports all charge types for the Flat Fee and Per Unit charge models   # noqa: E501

        :param price: The price of this PUTScUpdateType.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def price_change_option(self):
        """Gets the price_change_option of this PUTScUpdateType.  # noqa: E501

        Applies an automatic price change when a termed subscription is renewed. The Billing Admin setting **Enable Automatic Price Change When Subscriptions are Renewed?** must be set to Yes to use this field.  Values:  * `NoChange` (default) * `SpecificPercentageValue` * `UseLatestProductCatalogPricing`  Available for the following charge types:  * Recurring * Usage-based  Not available for the Fixed-Amount Discount charge model.   # noqa: E501

        :return: The price_change_option of this PUTScUpdateType.  # noqa: E501
        :rtype: str
        """
        return self._price_change_option

    @price_change_option.setter
    def price_change_option(self, price_change_option):
        """Sets the price_change_option of this PUTScUpdateType.

        Applies an automatic price change when a termed subscription is renewed. The Billing Admin setting **Enable Automatic Price Change When Subscriptions are Renewed?** must be set to Yes to use this field.  Values:  * `NoChange` (default) * `SpecificPercentageValue` * `UseLatestProductCatalogPricing`  Available for the following charge types:  * Recurring * Usage-based  Not available for the Fixed-Amount Discount charge model.   # noqa: E501

        :param price_change_option: The price_change_option of this PUTScUpdateType.  # noqa: E501
        :type: str
        """

        self._price_change_option = price_change_option

    @property
    def price_increase_percentage(self):
        """Gets the price_increase_percentage of this PUTScUpdateType.  # noqa: E501

        Specifies the percentage to increase or decrease the price of a termed subscription's renewal. Required if you set the `PriceChangeOption` field to `SpecificPercentageValue`.  Decimal between `-100` and `100`.  Available for the following charge types:  * Recurring * Usage-based  Not available for the Fixed-Amount Discount charge model.   # noqa: E501

        :return: The price_increase_percentage of this PUTScUpdateType.  # noqa: E501
        :rtype: str
        """
        return self._price_increase_percentage

    @price_increase_percentage.setter
    def price_increase_percentage(self, price_increase_percentage):
        """Sets the price_increase_percentage of this PUTScUpdateType.

        Specifies the percentage to increase or decrease the price of a termed subscription's renewal. Required if you set the `PriceChangeOption` field to `SpecificPercentageValue`.  Decimal between `-100` and `100`.  Available for the following charge types:  * Recurring * Usage-based  Not available for the Fixed-Amount Discount charge model.   # noqa: E501

        :param price_increase_percentage: The price_increase_percentage of this PUTScUpdateType.  # noqa: E501
        :type: str
        """

        self._price_increase_percentage = price_increase_percentage

    @property
    def quantity(self):
        """Gets the quantity of this PUTScUpdateType.  # noqa: E501

        Quantity of units; must be greater than zero.   # noqa: E501

        :return: The quantity of this PUTScUpdateType.  # noqa: E501
        :rtype: str
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this PUTScUpdateType.

        Quantity of units; must be greater than zero.   # noqa: E501

        :param quantity: The quantity of this PUTScUpdateType.  # noqa: E501
        :type: str
        """

        self._quantity = quantity

    @property
    def rate_plan_charge_id(self):
        """Gets the rate_plan_charge_id of this PUTScUpdateType.  # noqa: E501

        ID of a rate-plan charge for this subscription.   # noqa: E501

        :return: The rate_plan_charge_id of this PUTScUpdateType.  # noqa: E501
        :rtype: str
        """
        return self._rate_plan_charge_id

    @rate_plan_charge_id.setter
    def rate_plan_charge_id(self, rate_plan_charge_id):
        """Sets the rate_plan_charge_id of this PUTScUpdateType.

        ID of a rate-plan charge for this subscription.   # noqa: E501

        :param rate_plan_charge_id: The rate_plan_charge_id of this PUTScUpdateType.  # noqa: E501
        :type: str
        """
        if rate_plan_charge_id is None:
            raise ValueError("Invalid value for `rate_plan_charge_id`, must not be `None`")  # noqa: E501

        self._rate_plan_charge_id = rate_plan_charge_id

    @property
    def tiers(self):
        """Gets the tiers of this PUTScUpdateType.  # noqa: E501

        Container for Volume, Tiered or Tiered with Overage charge models. Supports the following charge types:  * One-time * Recurring * Usage-based   # noqa: E501

        :return: The tiers of this PUTScUpdateType.  # noqa: E501
        :rtype: list[POSTTierType]
        """
        return self._tiers

    @tiers.setter
    def tiers(self, tiers):
        """Sets the tiers of this PUTScUpdateType.

        Container for Volume, Tiered or Tiered with Overage charge models. Supports the following charge types:  * One-time * Recurring * Usage-based   # noqa: E501

        :param tiers: The tiers of this PUTScUpdateType.  # noqa: E501
        :type: list[POSTTierType]
        """

        self._tiers = tiers

    @property
    def trigger_date(self):
        """Gets the trigger_date of this PUTScUpdateType.  # noqa: E501

        Specifies when to start billing the customer for the charge. Required if the `triggerEvent` field is set to USD.  `triggerDate` cannot be updated for the following using the REST update subscription call:  * One-time charge type * Discount-Fixed Amount charge model * Discount-Percentage charge model   # noqa: E501

        :return: The trigger_date of this PUTScUpdateType.  # noqa: E501
        :rtype: date
        """
        return self._trigger_date

    @trigger_date.setter
    def trigger_date(self, trigger_date):
        """Sets the trigger_date of this PUTScUpdateType.

        Specifies when to start billing the customer for the charge. Required if the `triggerEvent` field is set to USD.  `triggerDate` cannot be updated for the following using the REST update subscription call:  * One-time charge type * Discount-Fixed Amount charge model * Discount-Percentage charge model   # noqa: E501

        :param trigger_date: The trigger_date of this PUTScUpdateType.  # noqa: E501
        :type: date
        """

        self._trigger_date = trigger_date

    @property
    def trigger_event(self):
        """Gets the trigger_event of this PUTScUpdateType.  # noqa: E501

        Specifies when to start billing the customer for the charge.  Values:  * `UCE` * `USA` * `UCA` * `USD`  This is the date when charge changes in the REST request become effective.  `triggerEvent` cannot be updated for the following using the REST update subscription call:  * One-time charge type * Discount-Fixed Amount charge model * Discount-Percentage charge model   # noqa: E501

        :return: The trigger_event of this PUTScUpdateType.  # noqa: E501
        :rtype: str
        """
        return self._trigger_event

    @trigger_event.setter
    def trigger_event(self, trigger_event):
        """Sets the trigger_event of this PUTScUpdateType.

        Specifies when to start billing the customer for the charge.  Values:  * `UCE` * `USA` * `UCA` * `USD`  This is the date when charge changes in the REST request become effective.  `triggerEvent` cannot be updated for the following using the REST update subscription call:  * One-time charge type * Discount-Fixed Amount charge model * Discount-Percentage charge model   # noqa: E501

        :param trigger_event: The trigger_event of this PUTScUpdateType.  # noqa: E501
        :type: str
        """

        self._trigger_event = trigger_event

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
        if issubclass(PUTScUpdateType, dict):
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
        if not isinstance(other, PUTScUpdateType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
