# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.get_rs_revenue_item_type import GETRsRevenueItemType  # noqa: F401,E501
from zuora_client.models.revenue_schedule_object_custom_fields import RevenueScheduleObjectCustomFields  # noqa: F401,E501


class GETRSDetailForProductChargeType(object):
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
        'account_id': 'str',
        'amount': 'str',
        'created_on': 'datetime',
        'currency': 'str',
        'linked_transaction_id': 'str',
        'linked_transaction_number': 'str',
        'linked_transaction_type': 'str',
        'notes': 'str',
        'number': 'str',
        'product_charge_id': 'str',
        'recognition_rule_name': 'str',
        'recognized_revenue': 'str',
        'reference_id': 'str',
        'revenue_items': 'list[GETRsRevenueItemType]',
        'revenue_schedule_date': 'date',
        'undistributed_unrecognized_revenue': 'str',
        'unrecognized_revenue': 'str',
        'updated_on': 'datetime'
    }

    attribute_map = {
        'account_id': 'accountId',
        'amount': 'amount',
        'created_on': 'createdOn',
        'currency': 'currency',
        'linked_transaction_id': 'linkedTransactionId',
        'linked_transaction_number': 'linkedTransactionNumber',
        'linked_transaction_type': 'linkedTransactionType',
        'notes': 'notes',
        'number': 'number',
        'product_charge_id': 'productChargeId',
        'recognition_rule_name': 'recognitionRuleName',
        'recognized_revenue': 'recognizedRevenue',
        'reference_id': 'referenceId',
        'revenue_items': 'revenueItems',
        'revenue_schedule_date': 'revenueScheduleDate',
        'undistributed_unrecognized_revenue': 'undistributedUnrecognizedRevenue',
        'unrecognized_revenue': 'unrecognizedRevenue',
        'updated_on': 'updatedOn'
    }

    def __init__(self, account_id=None, amount=None, created_on=None, currency=None, linked_transaction_id=None, linked_transaction_number=None, linked_transaction_type=None, notes=None, number=None, product_charge_id=None, recognition_rule_name=None, recognized_revenue=None, reference_id=None, revenue_items=None, revenue_schedule_date=None, undistributed_unrecognized_revenue=None, unrecognized_revenue=None, updated_on=None):  # noqa: E501
        """GETRSDetailForProductChargeType - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._amount = None
        self._created_on = None
        self._currency = None
        self._linked_transaction_id = None
        self._linked_transaction_number = None
        self._linked_transaction_type = None
        self._notes = None
        self._number = None
        self._product_charge_id = None
        self._recognition_rule_name = None
        self._recognized_revenue = None
        self._reference_id = None
        self._revenue_items = None
        self._revenue_schedule_date = None
        self._undistributed_unrecognized_revenue = None
        self._unrecognized_revenue = None
        self._updated_on = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if amount is not None:
            self.amount = amount
        if created_on is not None:
            self.created_on = created_on
        if currency is not None:
            self.currency = currency
        if linked_transaction_id is not None:
            self.linked_transaction_id = linked_transaction_id
        if linked_transaction_number is not None:
            self.linked_transaction_number = linked_transaction_number
        if linked_transaction_type is not None:
            self.linked_transaction_type = linked_transaction_type
        if notes is not None:
            self.notes = notes
        if number is not None:
            self.number = number
        if product_charge_id is not None:
            self.product_charge_id = product_charge_id
        if recognition_rule_name is not None:
            self.recognition_rule_name = recognition_rule_name
        if recognized_revenue is not None:
            self.recognized_revenue = recognized_revenue
        if reference_id is not None:
            self.reference_id = reference_id
        if revenue_items is not None:
            self.revenue_items = revenue_items
        if revenue_schedule_date is not None:
            self.revenue_schedule_date = revenue_schedule_date
        if undistributed_unrecognized_revenue is not None:
            self.undistributed_unrecognized_revenue = undistributed_unrecognized_revenue
        if unrecognized_revenue is not None:
            self.unrecognized_revenue = unrecognized_revenue
        if updated_on is not None:
            self.updated_on = updated_on

    @property
    def account_id(self):
        """Gets the account_id of this GETRSDetailForProductChargeType.  # noqa: E501

        The ID of a customer account.   # noqa: E501

        :return: The account_id of this GETRSDetailForProductChargeType.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this GETRSDetailForProductChargeType.

        The ID of a customer account.   # noqa: E501

        :param account_id: The account_id of this GETRSDetailForProductChargeType.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def amount(self):
        """Gets the amount of this GETRSDetailForProductChargeType.  # noqa: E501

        The revenue schedule amount, which is the sum of all revenue items.   This field cannot be null and must be formatted based on the currency, such as `JPY 30` or `USD 30.15`. Test out the currency to ensure you are using the proper formatting; otherwise, the response will fail and this error message is returned: `Allocation amount with wrong decimal places`.   # noqa: E501

        :return: The amount of this GETRSDetailForProductChargeType.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GETRSDetailForProductChargeType.

        The revenue schedule amount, which is the sum of all revenue items.   This field cannot be null and must be formatted based on the currency, such as `JPY 30` or `USD 30.15`. Test out the currency to ensure you are using the proper formatting; otherwise, the response will fail and this error message is returned: `Allocation amount with wrong decimal places`.   # noqa: E501

        :param amount: The amount of this GETRSDetailForProductChargeType.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def created_on(self):
        """Gets the created_on of this GETRSDetailForProductChargeType.  # noqa: E501

        The date and time when the record was created, in `yyyy-mm-dd hh:mm:ss` format.   # noqa: E501

        :return: The created_on of this GETRSDetailForProductChargeType.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this GETRSDetailForProductChargeType.

        The date and time when the record was created, in `yyyy-mm-dd hh:mm:ss` format.   # noqa: E501

        :param created_on: The created_on of this GETRSDetailForProductChargeType.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def currency(self):
        """Gets the currency of this GETRSDetailForProductChargeType.  # noqa: E501

        The type of currency used.   # noqa: E501

        :return: The currency of this GETRSDetailForProductChargeType.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this GETRSDetailForProductChargeType.

        The type of currency used.   # noqa: E501

        :param currency: The currency of this GETRSDetailForProductChargeType.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def linked_transaction_id(self):
        """Gets the linked_transaction_id of this GETRSDetailForProductChargeType.  # noqa: E501

        The linked transaction ID for billing transactions. This field is used for all rules except for the custom unlimited or manual recognition rule models. If using the custom unlimited rule model, then the field value must be null. If the field is not null, then the referenceId field must be null.   # noqa: E501

        :return: The linked_transaction_id of this GETRSDetailForProductChargeType.  # noqa: E501
        :rtype: str
        """
        return self._linked_transaction_id

    @linked_transaction_id.setter
    def linked_transaction_id(self, linked_transaction_id):
        """Sets the linked_transaction_id of this GETRSDetailForProductChargeType.

        The linked transaction ID for billing transactions. This field is used for all rules except for the custom unlimited or manual recognition rule models. If using the custom unlimited rule model, then the field value must be null. If the field is not null, then the referenceId field must be null.   # noqa: E501

        :param linked_transaction_id: The linked_transaction_id of this GETRSDetailForProductChargeType.  # noqa: E501
        :type: str
        """

        self._linked_transaction_id = linked_transaction_id

    @property
    def linked_transaction_number(self):
        """Gets the linked_transaction_number of this GETRSDetailForProductChargeType.  # noqa: E501

        The number for the linked invoice item, invoice item adjustment, or debit memo item transaction. This field is used for all rules except for the custom unlimited or manual recognition rule models. If using the custom unlimited or manual recognition rule models, then the field value is null.   # noqa: E501

        :return: The linked_transaction_number of this GETRSDetailForProductChargeType.  # noqa: E501
        :rtype: str
        """
        return self._linked_transaction_number

    @linked_transaction_number.setter
    def linked_transaction_number(self, linked_transaction_number):
        """Sets the linked_transaction_number of this GETRSDetailForProductChargeType.

        The number for the linked invoice item, invoice item adjustment, or debit memo item transaction. This field is used for all rules except for the custom unlimited or manual recognition rule models. If using the custom unlimited or manual recognition rule models, then the field value is null.   # noqa: E501

        :param linked_transaction_number: The linked_transaction_number of this GETRSDetailForProductChargeType.  # noqa: E501
        :type: str
        """

        self._linked_transaction_number = linked_transaction_number

    @property
    def linked_transaction_type(self):
        """Gets the linked_transaction_type of this GETRSDetailForProductChargeType.  # noqa: E501

        The type of linked transaction for billing transactions, which can be invoice item, invoice item adjustment, or debit memo item. This field is used for all rules except for the custom unlimited or manual recognition rule models.   # noqa: E501

        :return: The linked_transaction_type of this GETRSDetailForProductChargeType.  # noqa: E501
        :rtype: str
        """
        return self._linked_transaction_type

    @linked_transaction_type.setter
    def linked_transaction_type(self, linked_transaction_type):
        """Sets the linked_transaction_type of this GETRSDetailForProductChargeType.

        The type of linked transaction for billing transactions, which can be invoice item, invoice item adjustment, or debit memo item. This field is used for all rules except for the custom unlimited or manual recognition rule models.   # noqa: E501

        :param linked_transaction_type: The linked_transaction_type of this GETRSDetailForProductChargeType.  # noqa: E501
        :type: str
        """

        self._linked_transaction_type = linked_transaction_type

    @property
    def notes(self):
        """Gets the notes of this GETRSDetailForProductChargeType.  # noqa: E501

        Additional information about this record.   # noqa: E501

        :return: The notes of this GETRSDetailForProductChargeType.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this GETRSDetailForProductChargeType.

        Additional information about this record.   # noqa: E501

        :param notes: The notes of this GETRSDetailForProductChargeType.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def number(self):
        """Gets the number of this GETRSDetailForProductChargeType.  # noqa: E501

        The revenue schedule number. The revenue schedule number is always prefixed with \"RS\", for example, \"RS-00000001\".   # noqa: E501

        :return: The number of this GETRSDetailForProductChargeType.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this GETRSDetailForProductChargeType.

        The revenue schedule number. The revenue schedule number is always prefixed with \"RS\", for example, \"RS-00000001\".   # noqa: E501

        :param number: The number of this GETRSDetailForProductChargeType.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def product_charge_id(self):
        """Gets the product_charge_id of this GETRSDetailForProductChargeType.  # noqa: E501

        The ID of a product rate plan charge.   # noqa: E501

        :return: The product_charge_id of this GETRSDetailForProductChargeType.  # noqa: E501
        :rtype: str
        """
        return self._product_charge_id

    @product_charge_id.setter
    def product_charge_id(self, product_charge_id):
        """Sets the product_charge_id of this GETRSDetailForProductChargeType.

        The ID of a product rate plan charge.   # noqa: E501

        :param product_charge_id: The product_charge_id of this GETRSDetailForProductChargeType.  # noqa: E501
        :type: str
        """

        self._product_charge_id = product_charge_id

    @property
    def recognition_rule_name(self):
        """Gets the recognition_rule_name of this GETRSDetailForProductChargeType.  # noqa: E501

        The name of the recognition rule.   # noqa: E501

        :return: The recognition_rule_name of this GETRSDetailForProductChargeType.  # noqa: E501
        :rtype: str
        """
        return self._recognition_rule_name

    @recognition_rule_name.setter
    def recognition_rule_name(self, recognition_rule_name):
        """Sets the recognition_rule_name of this GETRSDetailForProductChargeType.

        The name of the recognition rule.   # noqa: E501

        :param recognition_rule_name: The recognition_rule_name of this GETRSDetailForProductChargeType.  # noqa: E501
        :type: str
        """

        self._recognition_rule_name = recognition_rule_name

    @property
    def recognized_revenue(self):
        """Gets the recognized_revenue of this GETRSDetailForProductChargeType.  # noqa: E501

        The revenue that was distributed in a closed accounting period.   # noqa: E501

        :return: The recognized_revenue of this GETRSDetailForProductChargeType.  # noqa: E501
        :rtype: str
        """
        return self._recognized_revenue

    @recognized_revenue.setter
    def recognized_revenue(self, recognized_revenue):
        """Sets the recognized_revenue of this GETRSDetailForProductChargeType.

        The revenue that was distributed in a closed accounting period.   # noqa: E501

        :param recognized_revenue: The recognized_revenue of this GETRSDetailForProductChargeType.  # noqa: E501
        :type: str
        """

        self._recognized_revenue = recognized_revenue

    @property
    def reference_id(self):
        """Gets the reference_id of this GETRSDetailForProductChargeType.  # noqa: E501

        The reference ID is used only in the custom unlimited rule to create a revenue schedule. In this scenario, the revenue schedule is not linked to a credit memo item.   # noqa: E501

        :return: The reference_id of this GETRSDetailForProductChargeType.  # noqa: E501
        :rtype: str
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """Sets the reference_id of this GETRSDetailForProductChargeType.

        The reference ID is used only in the custom unlimited rule to create a revenue schedule. In this scenario, the revenue schedule is not linked to a credit memo item.   # noqa: E501

        :param reference_id: The reference_id of this GETRSDetailForProductChargeType.  # noqa: E501
        :type: str
        """

        self._reference_id = reference_id

    @property
    def revenue_items(self):
        """Gets the revenue_items of this GETRSDetailForProductChargeType.  # noqa: E501

        Revenue items are listed in ascending order by the accounting period start date.   # noqa: E501

        :return: The revenue_items of this GETRSDetailForProductChargeType.  # noqa: E501
        :rtype: list[GETRsRevenueItemType]
        """
        return self._revenue_items

    @revenue_items.setter
    def revenue_items(self, revenue_items):
        """Sets the revenue_items of this GETRSDetailForProductChargeType.

        Revenue items are listed in ascending order by the accounting period start date.   # noqa: E501

        :param revenue_items: The revenue_items of this GETRSDetailForProductChargeType.  # noqa: E501
        :type: list[GETRsRevenueItemType]
        """

        self._revenue_items = revenue_items

    @property
    def revenue_schedule_date(self):
        """Gets the revenue_schedule_date of this GETRSDetailForProductChargeType.  # noqa: E501

        The effective date of the revenue schedule. For example, the revenue schedule date for bookings-based revenue recognition is typically set to the order date or contract date.  The date cannot be in a closed accounting period. The date must be in `yyyy-mm-dd` format.   # noqa: E501

        :return: The revenue_schedule_date of this GETRSDetailForProductChargeType.  # noqa: E501
        :rtype: date
        """
        return self._revenue_schedule_date

    @revenue_schedule_date.setter
    def revenue_schedule_date(self, revenue_schedule_date):
        """Sets the revenue_schedule_date of this GETRSDetailForProductChargeType.

        The effective date of the revenue schedule. For example, the revenue schedule date for bookings-based revenue recognition is typically set to the order date or contract date.  The date cannot be in a closed accounting period. The date must be in `yyyy-mm-dd` format.   # noqa: E501

        :param revenue_schedule_date: The revenue_schedule_date of this GETRSDetailForProductChargeType.  # noqa: E501
        :type: date
        """

        self._revenue_schedule_date = revenue_schedule_date

    @property
    def undistributed_unrecognized_revenue(self):
        """Gets the undistributed_unrecognized_revenue of this GETRSDetailForProductChargeType.  # noqa: E501

        The revenue in the open-ended accounting period.   # noqa: E501

        :return: The undistributed_unrecognized_revenue of this GETRSDetailForProductChargeType.  # noqa: E501
        :rtype: str
        """
        return self._undistributed_unrecognized_revenue

    @undistributed_unrecognized_revenue.setter
    def undistributed_unrecognized_revenue(self, undistributed_unrecognized_revenue):
        """Sets the undistributed_unrecognized_revenue of this GETRSDetailForProductChargeType.

        The revenue in the open-ended accounting period.   # noqa: E501

        :param undistributed_unrecognized_revenue: The undistributed_unrecognized_revenue of this GETRSDetailForProductChargeType.  # noqa: E501
        :type: str
        """

        self._undistributed_unrecognized_revenue = undistributed_unrecognized_revenue

    @property
    def unrecognized_revenue(self):
        """Gets the unrecognized_revenue of this GETRSDetailForProductChargeType.  # noqa: E501

        The revenue distributed in all open accounting periods, which includes the open-ended accounting period.   # noqa: E501

        :return: The unrecognized_revenue of this GETRSDetailForProductChargeType.  # noqa: E501
        :rtype: str
        """
        return self._unrecognized_revenue

    @unrecognized_revenue.setter
    def unrecognized_revenue(self, unrecognized_revenue):
        """Sets the unrecognized_revenue of this GETRSDetailForProductChargeType.

        The revenue distributed in all open accounting periods, which includes the open-ended accounting period.   # noqa: E501

        :param unrecognized_revenue: The unrecognized_revenue of this GETRSDetailForProductChargeType.  # noqa: E501
        :type: str
        """

        self._unrecognized_revenue = unrecognized_revenue

    @property
    def updated_on(self):
        """Gets the updated_on of this GETRSDetailForProductChargeType.  # noqa: E501

        The date and time when the revenue automation start date was set, in `yyyy-mm-dd hh:mm:ss` format.   # noqa: E501

        :return: The updated_on of this GETRSDetailForProductChargeType.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this GETRSDetailForProductChargeType.

        The date and time when the revenue automation start date was set, in `yyyy-mm-dd hh:mm:ss` format.   # noqa: E501

        :param updated_on: The updated_on of this GETRSDetailForProductChargeType.  # noqa: E501
        :type: datetime
        """

        self._updated_on = updated_on

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
        if issubclass(GETRSDetailForProductChargeType, dict):
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
        if not isinstance(other, GETRSDetailForProductChargeType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
