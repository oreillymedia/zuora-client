# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.breakdown_detail import BreakdownDetail  # noqa: F401,E501


class CreditMemoItemBreakdown(object):
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
        'amount': 'float',
        'apply_to_charge_number': 'str',
        'breakdown_details': 'list[BreakdownDetail]',
        'charge_number': 'str',
        'credit_memo_item_id': 'str',
        'end_date': 'date',
        'is_negative_price': 'bool',
        'start_date': 'date',
        'subscription_number': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'apply_to_charge_number': 'applyToChargeNumber',
        'breakdown_details': 'breakdownDetails',
        'charge_number': 'chargeNumber',
        'credit_memo_item_id': 'creditMemoItemId',
        'end_date': 'endDate',
        'is_negative_price': 'isNegativePrice',
        'start_date': 'startDate',
        'subscription_number': 'subscriptionNumber'
    }

    def __init__(self, amount=None, apply_to_charge_number=None, breakdown_details=None, charge_number=None, credit_memo_item_id=None, end_date=None, is_negative_price=None, start_date=None, subscription_number=None):  # noqa: E501
        """CreditMemoItemBreakdown - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._apply_to_charge_number = None
        self._breakdown_details = None
        self._charge_number = None
        self._credit_memo_item_id = None
        self._end_date = None
        self._is_negative_price = None
        self._start_date = None
        self._subscription_number = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if apply_to_charge_number is not None:
            self.apply_to_charge_number = apply_to_charge_number
        if breakdown_details is not None:
            self.breakdown_details = breakdown_details
        if charge_number is not None:
            self.charge_number = charge_number
        if credit_memo_item_id is not None:
            self.credit_memo_item_id = credit_memo_item_id
        if end_date is not None:
            self.end_date = end_date
        if is_negative_price is not None:
            self.is_negative_price = is_negative_price
        if start_date is not None:
            self.start_date = start_date
        if subscription_number is not None:
            self.subscription_number = subscription_number

    @property
    def amount(self):
        """Gets the amount of this CreditMemoItemBreakdown.  # noqa: E501


        :return: The amount of this CreditMemoItemBreakdown.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CreditMemoItemBreakdown.


        :param amount: The amount of this CreditMemoItemBreakdown.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def apply_to_charge_number(self):
        """Gets the apply_to_charge_number of this CreditMemoItemBreakdown.  # noqa: E501

        Available only when the credit memo item represents a discount invoice item.  # noqa: E501

        :return: The apply_to_charge_number of this CreditMemoItemBreakdown.  # noqa: E501
        :rtype: str
        """
        return self._apply_to_charge_number

    @apply_to_charge_number.setter
    def apply_to_charge_number(self, apply_to_charge_number):
        """Sets the apply_to_charge_number of this CreditMemoItemBreakdown.

        Available only when the credit memo item represents a discount invoice item.  # noqa: E501

        :param apply_to_charge_number: The apply_to_charge_number of this CreditMemoItemBreakdown.  # noqa: E501
        :type: str
        """

        self._apply_to_charge_number = apply_to_charge_number

    @property
    def breakdown_details(self):
        """Gets the breakdown_details of this CreditMemoItemBreakdown.  # noqa: E501


        :return: The breakdown_details of this CreditMemoItemBreakdown.  # noqa: E501
        :rtype: list[BreakdownDetail]
        """
        return self._breakdown_details

    @breakdown_details.setter
    def breakdown_details(self, breakdown_details):
        """Sets the breakdown_details of this CreditMemoItemBreakdown.


        :param breakdown_details: The breakdown_details of this CreditMemoItemBreakdown.  # noqa: E501
        :type: list[BreakdownDetail]
        """

        self._breakdown_details = breakdown_details

    @property
    def charge_number(self):
        """Gets the charge_number of this CreditMemoItemBreakdown.  # noqa: E501


        :return: The charge_number of this CreditMemoItemBreakdown.  # noqa: E501
        :rtype: str
        """
        return self._charge_number

    @charge_number.setter
    def charge_number(self, charge_number):
        """Sets the charge_number of this CreditMemoItemBreakdown.


        :param charge_number: The charge_number of this CreditMemoItemBreakdown.  # noqa: E501
        :type: str
        """

        self._charge_number = charge_number

    @property
    def credit_memo_item_id(self):
        """Gets the credit_memo_item_id of this CreditMemoItemBreakdown.  # noqa: E501


        :return: The credit_memo_item_id of this CreditMemoItemBreakdown.  # noqa: E501
        :rtype: str
        """
        return self._credit_memo_item_id

    @credit_memo_item_id.setter
    def credit_memo_item_id(self, credit_memo_item_id):
        """Sets the credit_memo_item_id of this CreditMemoItemBreakdown.


        :param credit_memo_item_id: The credit_memo_item_id of this CreditMemoItemBreakdown.  # noqa: E501
        :type: str
        """

        self._credit_memo_item_id = credit_memo_item_id

    @property
    def end_date(self):
        """Gets the end_date of this CreditMemoItemBreakdown.  # noqa: E501


        :return: The end_date of this CreditMemoItemBreakdown.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this CreditMemoItemBreakdown.


        :param end_date: The end_date of this CreditMemoItemBreakdown.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def is_negative_price(self):
        """Gets the is_negative_price of this CreditMemoItemBreakdown.  # noqa: E501

        Whether the amount of the product rate plan charge, which the credit memo is created from, is negative.   # noqa: E501

        :return: The is_negative_price of this CreditMemoItemBreakdown.  # noqa: E501
        :rtype: bool
        """
        return self._is_negative_price

    @is_negative_price.setter
    def is_negative_price(self, is_negative_price):
        """Sets the is_negative_price of this CreditMemoItemBreakdown.

        Whether the amount of the product rate plan charge, which the credit memo is created from, is negative.   # noqa: E501

        :param is_negative_price: The is_negative_price of this CreditMemoItemBreakdown.  # noqa: E501
        :type: bool
        """

        self._is_negative_price = is_negative_price

    @property
    def start_date(self):
        """Gets the start_date of this CreditMemoItemBreakdown.  # noqa: E501


        :return: The start_date of this CreditMemoItemBreakdown.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this CreditMemoItemBreakdown.


        :param start_date: The start_date of this CreditMemoItemBreakdown.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def subscription_number(self):
        """Gets the subscription_number of this CreditMemoItemBreakdown.  # noqa: E501


        :return: The subscription_number of this CreditMemoItemBreakdown.  # noqa: E501
        :rtype: str
        """
        return self._subscription_number

    @subscription_number.setter
    def subscription_number(self, subscription_number):
        """Sets the subscription_number of this CreditMemoItemBreakdown.


        :param subscription_number: The subscription_number of this CreditMemoItemBreakdown.  # noqa: E501
        :type: str
        """

        self._subscription_number = subscription_number

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
        if issubclass(CreditMemoItemBreakdown, dict):
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
        if not isinstance(other, CreditMemoItemBreakdown):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
