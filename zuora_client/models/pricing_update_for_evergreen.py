# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.discount_pricing_update import DiscountPricingUpdate  # noqa: F401,E501
from zuora_client.models.recurring_flat_fee_pricing_update import RecurringFlatFeePricingUpdate  # noqa: F401,E501
from zuora_client.models.recurring_per_unit_pricing_update import RecurringPerUnitPricingUpdate  # noqa: F401,E501
from zuora_client.models.recurring_tiered_pricing_update import RecurringTieredPricingUpdate  # noqa: F401,E501
from zuora_client.models.recurring_volume_pricing_update import RecurringVolumePricingUpdate  # noqa: F401,E501
from zuora_client.models.usage_flat_fee_pricing_update import UsageFlatFeePricingUpdate  # noqa: F401,E501
from zuora_client.models.usage_overage_pricing_update import UsageOveragePricingUpdate  # noqa: F401,E501
from zuora_client.models.usage_per_unit_pricing_update import UsagePerUnitPricingUpdate  # noqa: F401,E501
from zuora_client.models.usage_tiered_pricing_update import UsageTieredPricingUpdate  # noqa: F401,E501
from zuora_client.models.usage_tiered_with_overage_pricing_update import UsageTieredWithOveragePricingUpdate  # noqa: F401,E501
from zuora_client.models.usage_volume_pricing_update import UsageVolumePricingUpdate  # noqa: F401,E501


class PricingUpdateForEvergreen(object):
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
        'discount': 'DiscountPricingUpdate',
        'recurring_flat_fee': 'RecurringFlatFeePricingUpdate',
        'recurring_per_unit': 'RecurringPerUnitPricingUpdate',
        'recurring_tiered': 'RecurringTieredPricingUpdate',
        'recurring_volume': 'RecurringVolumePricingUpdate',
        'usage_flat_fee': 'UsageFlatFeePricingUpdate',
        'usage_overage': 'UsageOveragePricingUpdate',
        'usage_per_unit': 'UsagePerUnitPricingUpdate',
        'usage_tiered': 'UsageTieredPricingUpdate',
        'usage_tiered_with_overage': 'UsageTieredWithOveragePricingUpdate',
        'usage_volume': 'UsageVolumePricingUpdate'
    }

    attribute_map = {
        'discount': 'discount',
        'recurring_flat_fee': 'recurringFlatFee',
        'recurring_per_unit': 'recurringPerUnit',
        'recurring_tiered': 'recurringTiered',
        'recurring_volume': 'recurringVolume',
        'usage_flat_fee': 'usageFlatFee',
        'usage_overage': 'usageOverage',
        'usage_per_unit': 'usagePerUnit',
        'usage_tiered': 'usageTiered',
        'usage_tiered_with_overage': 'usageTieredWithOverage',
        'usage_volume': 'usageVolume'
    }

    def __init__(self, discount=None, recurring_flat_fee=None, recurring_per_unit=None, recurring_tiered=None, recurring_volume=None, usage_flat_fee=None, usage_overage=None, usage_per_unit=None, usage_tiered=None, usage_tiered_with_overage=None, usage_volume=None):  # noqa: E501
        """PricingUpdateForEvergreen - a model defined in Swagger"""  # noqa: E501

        self._discount = None
        self._recurring_flat_fee = None
        self._recurring_per_unit = None
        self._recurring_tiered = None
        self._recurring_volume = None
        self._usage_flat_fee = None
        self._usage_overage = None
        self._usage_per_unit = None
        self._usage_tiered = None
        self._usage_tiered_with_overage = None
        self._usage_volume = None
        self.discriminator = None

        if discount is not None:
            self.discount = discount
        if recurring_flat_fee is not None:
            self.recurring_flat_fee = recurring_flat_fee
        if recurring_per_unit is not None:
            self.recurring_per_unit = recurring_per_unit
        if recurring_tiered is not None:
            self.recurring_tiered = recurring_tiered
        if recurring_volume is not None:
            self.recurring_volume = recurring_volume
        if usage_flat_fee is not None:
            self.usage_flat_fee = usage_flat_fee
        if usage_overage is not None:
            self.usage_overage = usage_overage
        if usage_per_unit is not None:
            self.usage_per_unit = usage_per_unit
        if usage_tiered is not None:
            self.usage_tiered = usage_tiered
        if usage_tiered_with_overage is not None:
            self.usage_tiered_with_overage = usage_tiered_with_overage
        if usage_volume is not None:
            self.usage_volume = usage_volume

    @property
    def discount(self):
        """Gets the discount of this PricingUpdateForEvergreen.  # noqa: E501


        :return: The discount of this PricingUpdateForEvergreen.  # noqa: E501
        :rtype: DiscountPricingUpdate
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Sets the discount of this PricingUpdateForEvergreen.


        :param discount: The discount of this PricingUpdateForEvergreen.  # noqa: E501
        :type: DiscountPricingUpdate
        """

        self._discount = discount

    @property
    def recurring_flat_fee(self):
        """Gets the recurring_flat_fee of this PricingUpdateForEvergreen.  # noqa: E501


        :return: The recurring_flat_fee of this PricingUpdateForEvergreen.  # noqa: E501
        :rtype: RecurringFlatFeePricingUpdate
        """
        return self._recurring_flat_fee

    @recurring_flat_fee.setter
    def recurring_flat_fee(self, recurring_flat_fee):
        """Sets the recurring_flat_fee of this PricingUpdateForEvergreen.


        :param recurring_flat_fee: The recurring_flat_fee of this PricingUpdateForEvergreen.  # noqa: E501
        :type: RecurringFlatFeePricingUpdate
        """

        self._recurring_flat_fee = recurring_flat_fee

    @property
    def recurring_per_unit(self):
        """Gets the recurring_per_unit of this PricingUpdateForEvergreen.  # noqa: E501


        :return: The recurring_per_unit of this PricingUpdateForEvergreen.  # noqa: E501
        :rtype: RecurringPerUnitPricingUpdate
        """
        return self._recurring_per_unit

    @recurring_per_unit.setter
    def recurring_per_unit(self, recurring_per_unit):
        """Sets the recurring_per_unit of this PricingUpdateForEvergreen.


        :param recurring_per_unit: The recurring_per_unit of this PricingUpdateForEvergreen.  # noqa: E501
        :type: RecurringPerUnitPricingUpdate
        """

        self._recurring_per_unit = recurring_per_unit

    @property
    def recurring_tiered(self):
        """Gets the recurring_tiered of this PricingUpdateForEvergreen.  # noqa: E501


        :return: The recurring_tiered of this PricingUpdateForEvergreen.  # noqa: E501
        :rtype: RecurringTieredPricingUpdate
        """
        return self._recurring_tiered

    @recurring_tiered.setter
    def recurring_tiered(self, recurring_tiered):
        """Sets the recurring_tiered of this PricingUpdateForEvergreen.


        :param recurring_tiered: The recurring_tiered of this PricingUpdateForEvergreen.  # noqa: E501
        :type: RecurringTieredPricingUpdate
        """

        self._recurring_tiered = recurring_tiered

    @property
    def recurring_volume(self):
        """Gets the recurring_volume of this PricingUpdateForEvergreen.  # noqa: E501


        :return: The recurring_volume of this PricingUpdateForEvergreen.  # noqa: E501
        :rtype: RecurringVolumePricingUpdate
        """
        return self._recurring_volume

    @recurring_volume.setter
    def recurring_volume(self, recurring_volume):
        """Sets the recurring_volume of this PricingUpdateForEvergreen.


        :param recurring_volume: The recurring_volume of this PricingUpdateForEvergreen.  # noqa: E501
        :type: RecurringVolumePricingUpdate
        """

        self._recurring_volume = recurring_volume

    @property
    def usage_flat_fee(self):
        """Gets the usage_flat_fee of this PricingUpdateForEvergreen.  # noqa: E501


        :return: The usage_flat_fee of this PricingUpdateForEvergreen.  # noqa: E501
        :rtype: UsageFlatFeePricingUpdate
        """
        return self._usage_flat_fee

    @usage_flat_fee.setter
    def usage_flat_fee(self, usage_flat_fee):
        """Sets the usage_flat_fee of this PricingUpdateForEvergreen.


        :param usage_flat_fee: The usage_flat_fee of this PricingUpdateForEvergreen.  # noqa: E501
        :type: UsageFlatFeePricingUpdate
        """

        self._usage_flat_fee = usage_flat_fee

    @property
    def usage_overage(self):
        """Gets the usage_overage of this PricingUpdateForEvergreen.  # noqa: E501


        :return: The usage_overage of this PricingUpdateForEvergreen.  # noqa: E501
        :rtype: UsageOveragePricingUpdate
        """
        return self._usage_overage

    @usage_overage.setter
    def usage_overage(self, usage_overage):
        """Sets the usage_overage of this PricingUpdateForEvergreen.


        :param usage_overage: The usage_overage of this PricingUpdateForEvergreen.  # noqa: E501
        :type: UsageOveragePricingUpdate
        """

        self._usage_overage = usage_overage

    @property
    def usage_per_unit(self):
        """Gets the usage_per_unit of this PricingUpdateForEvergreen.  # noqa: E501


        :return: The usage_per_unit of this PricingUpdateForEvergreen.  # noqa: E501
        :rtype: UsagePerUnitPricingUpdate
        """
        return self._usage_per_unit

    @usage_per_unit.setter
    def usage_per_unit(self, usage_per_unit):
        """Sets the usage_per_unit of this PricingUpdateForEvergreen.


        :param usage_per_unit: The usage_per_unit of this PricingUpdateForEvergreen.  # noqa: E501
        :type: UsagePerUnitPricingUpdate
        """

        self._usage_per_unit = usage_per_unit

    @property
    def usage_tiered(self):
        """Gets the usage_tiered of this PricingUpdateForEvergreen.  # noqa: E501


        :return: The usage_tiered of this PricingUpdateForEvergreen.  # noqa: E501
        :rtype: UsageTieredPricingUpdate
        """
        return self._usage_tiered

    @usage_tiered.setter
    def usage_tiered(self, usage_tiered):
        """Sets the usage_tiered of this PricingUpdateForEvergreen.


        :param usage_tiered: The usage_tiered of this PricingUpdateForEvergreen.  # noqa: E501
        :type: UsageTieredPricingUpdate
        """

        self._usage_tiered = usage_tiered

    @property
    def usage_tiered_with_overage(self):
        """Gets the usage_tiered_with_overage of this PricingUpdateForEvergreen.  # noqa: E501


        :return: The usage_tiered_with_overage of this PricingUpdateForEvergreen.  # noqa: E501
        :rtype: UsageTieredWithOveragePricingUpdate
        """
        return self._usage_tiered_with_overage

    @usage_tiered_with_overage.setter
    def usage_tiered_with_overage(self, usage_tiered_with_overage):
        """Sets the usage_tiered_with_overage of this PricingUpdateForEvergreen.


        :param usage_tiered_with_overage: The usage_tiered_with_overage of this PricingUpdateForEvergreen.  # noqa: E501
        :type: UsageTieredWithOveragePricingUpdate
        """

        self._usage_tiered_with_overage = usage_tiered_with_overage

    @property
    def usage_volume(self):
        """Gets the usage_volume of this PricingUpdateForEvergreen.  # noqa: E501


        :return: The usage_volume of this PricingUpdateForEvergreen.  # noqa: E501
        :rtype: UsageVolumePricingUpdate
        """
        return self._usage_volume

    @usage_volume.setter
    def usage_volume(self, usage_volume):
        """Sets the usage_volume of this PricingUpdateForEvergreen.


        :param usage_volume: The usage_volume of this PricingUpdateForEvergreen.  # noqa: E501
        :type: UsageVolumePricingUpdate
        """

        self._usage_volume = usage_volume

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
        if issubclass(PricingUpdateForEvergreen, dict):
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
        if not isinstance(other, PricingUpdateForEvergreen):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
