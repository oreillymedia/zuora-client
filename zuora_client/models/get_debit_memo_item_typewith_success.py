# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.debit_memo_item_object_custom_fields import DebitMemoItemObjectCustomFields  # noqa: F401,E501
from zuora_client.models.get_debit_memo_item_type_finance_information import GETDebitMemoItemTypeFinanceInformation  # noqa: F401,E501
from zuora_client.models.get_debit_memo_item_typewith_success_taxation_items import GETDebitMemoItemTypewithSuccessTaxationItems  # noqa: F401,E501
from zuora_client.models.getdm_tax_item_type import GETDMTaxItemType  # noqa: F401,E501


class GETDebitMemoItemTypewithSuccess(object):
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
        'amount_without_tax': 'float',
        'balance': 'float',
        'be_applied_amount': 'float',
        'comment': 'str',
        'created_by_id': 'str',
        'created_date': 'datetime',
        'finance_information': 'GETDebitMemoItemTypeFinanceInformation',
        'id': 'str',
        'service_end_date': 'date',
        'service_start_date': 'date',
        'sku': 'str',
        'sku_name': 'str',
        'source_item_id': 'str',
        'source_item_type': 'str',
        'subscription_id': 'str',
        'tax_items': 'list[GETDMTaxItemType]',
        'taxation_items': 'GETDebitMemoItemTypewithSuccessTaxationItems',
        'updated_by_id': 'str',
        'updated_date': 'datetime'
    }

    attribute_map = {
        'amount': 'amount',
        'amount_without_tax': 'amountWithoutTax',
        'balance': 'balance',
        'be_applied_amount': 'beAppliedAmount',
        'comment': 'comment',
        'created_by_id': 'createdById',
        'created_date': 'createdDate',
        'finance_information': 'financeInformation',
        'id': 'id',
        'service_end_date': 'serviceEndDate',
        'service_start_date': 'serviceStartDate',
        'sku': 'sku',
        'sku_name': 'skuName',
        'source_item_id': 'sourceItemId',
        'source_item_type': 'sourceItemType',
        'subscription_id': 'subscriptionId',
        'tax_items': 'taxItems',
        'taxation_items': 'taxationItems',
        'updated_by_id': 'updatedById',
        'updated_date': 'updatedDate'
    }

    def __init__(self, amount=None, amount_without_tax=None, balance=None, be_applied_amount=None, comment=None, created_by_id=None, created_date=None, finance_information=None, id=None, service_end_date=None, service_start_date=None, sku=None, sku_name=None, source_item_id=None, source_item_type=None, subscription_id=None, tax_items=None, taxation_items=None, updated_by_id=None, updated_date=None):  # noqa: E501
        """GETDebitMemoItemTypewithSuccess - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._amount_without_tax = None
        self._balance = None
        self._be_applied_amount = None
        self._comment = None
        self._created_by_id = None
        self._created_date = None
        self._finance_information = None
        self._id = None
        self._service_end_date = None
        self._service_start_date = None
        self._sku = None
        self._sku_name = None
        self._source_item_id = None
        self._source_item_type = None
        self._subscription_id = None
        self._tax_items = None
        self._taxation_items = None
        self._updated_by_id = None
        self._updated_date = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if amount_without_tax is not None:
            self.amount_without_tax = amount_without_tax
        if balance is not None:
            self.balance = balance
        if be_applied_amount is not None:
            self.be_applied_amount = be_applied_amount
        if comment is not None:
            self.comment = comment
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_date is not None:
            self.created_date = created_date
        if finance_information is not None:
            self.finance_information = finance_information
        if id is not None:
            self.id = id
        if service_end_date is not None:
            self.service_end_date = service_end_date
        if service_start_date is not None:
            self.service_start_date = service_start_date
        if sku is not None:
            self.sku = sku
        if sku_name is not None:
            self.sku_name = sku_name
        if source_item_id is not None:
            self.source_item_id = source_item_id
        if source_item_type is not None:
            self.source_item_type = source_item_type
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if tax_items is not None:
            self.tax_items = tax_items
        if taxation_items is not None:
            self.taxation_items = taxation_items
        if updated_by_id is not None:
            self.updated_by_id = updated_by_id
        if updated_date is not None:
            self.updated_date = updated_date

    @property
    def amount(self):
        """Gets the amount of this GETDebitMemoItemTypewithSuccess.  # noqa: E501

        The amount of the debit memo item. For tax-inclusive debit memo items, the amount indicates the debit memo item amount including tax. For tax-exclusive debit memo items, the amount indicates the debit memo item amount excluding tax.   # noqa: E501

        :return: The amount of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GETDebitMemoItemTypewithSuccess.

        The amount of the debit memo item. For tax-inclusive debit memo items, the amount indicates the debit memo item amount including tax. For tax-exclusive debit memo items, the amount indicates the debit memo item amount excluding tax.   # noqa: E501

        :param amount: The amount of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def amount_without_tax(self):
        """Gets the amount_without_tax of this GETDebitMemoItemTypewithSuccess.  # noqa: E501

        The debit memo item amount excluding tax.   # noqa: E501

        :return: The amount_without_tax of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :rtype: float
        """
        return self._amount_without_tax

    @amount_without_tax.setter
    def amount_without_tax(self, amount_without_tax):
        """Sets the amount_without_tax of this GETDebitMemoItemTypewithSuccess.

        The debit memo item amount excluding tax.   # noqa: E501

        :param amount_without_tax: The amount_without_tax of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :type: float
        """

        self._amount_without_tax = amount_without_tax

    @property
    def balance(self):
        """Gets the balance of this GETDebitMemoItemTypewithSuccess.  # noqa: E501

        The balance of the debit memo item.   # noqa: E501

        :return: The balance of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this GETDebitMemoItemTypewithSuccess.

        The balance of the debit memo item.   # noqa: E501

        :param balance: The balance of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :type: float
        """

        self._balance = balance

    @property
    def be_applied_amount(self):
        """Gets the be_applied_amount of this GETDebitMemoItemTypewithSuccess.  # noqa: E501

        The applied amount of the debit memo item.   # noqa: E501

        :return: The be_applied_amount of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :rtype: float
        """
        return self._be_applied_amount

    @be_applied_amount.setter
    def be_applied_amount(self, be_applied_amount):
        """Sets the be_applied_amount of this GETDebitMemoItemTypewithSuccess.

        The applied amount of the debit memo item.   # noqa: E501

        :param be_applied_amount: The be_applied_amount of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :type: float
        """

        self._be_applied_amount = be_applied_amount

    @property
    def comment(self):
        """Gets the comment of this GETDebitMemoItemTypewithSuccess.  # noqa: E501

        Comments about the debit memo item.   # noqa: E501

        :return: The comment of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this GETDebitMemoItemTypewithSuccess.

        Comments about the debit memo item.   # noqa: E501

        :param comment: The comment of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def created_by_id(self):
        """Gets the created_by_id of this GETDebitMemoItemTypewithSuccess.  # noqa: E501

        The ID of the Zuora user who created the debit memo item.   # noqa: E501

        :return: The created_by_id of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this GETDebitMemoItemTypewithSuccess.

        The ID of the Zuora user who created the debit memo item.   # noqa: E501

        :param created_by_id: The created_by_id of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def created_date(self):
        """Gets the created_date of this GETDebitMemoItemTypewithSuccess.  # noqa: E501

        The date and time when the debit memo item was created, in `yyyy-mm-dd hh:mm:ss` format. For example, 2017-03-01 15:31:10.   # noqa: E501

        :return: The created_date of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this GETDebitMemoItemTypewithSuccess.

        The date and time when the debit memo item was created, in `yyyy-mm-dd hh:mm:ss` format. For example, 2017-03-01 15:31:10.   # noqa: E501

        :param created_date: The created_date of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def finance_information(self):
        """Gets the finance_information of this GETDebitMemoItemTypewithSuccess.  # noqa: E501


        :return: The finance_information of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :rtype: GETDebitMemoItemTypeFinanceInformation
        """
        return self._finance_information

    @finance_information.setter
    def finance_information(self, finance_information):
        """Sets the finance_information of this GETDebitMemoItemTypewithSuccess.


        :param finance_information: The finance_information of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :type: GETDebitMemoItemTypeFinanceInformation
        """

        self._finance_information = finance_information

    @property
    def id(self):
        """Gets the id of this GETDebitMemoItemTypewithSuccess.  # noqa: E501

        The ID of the debit memo item.   # noqa: E501

        :return: The id of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GETDebitMemoItemTypewithSuccess.

        The ID of the debit memo item.   # noqa: E501

        :param id: The id of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def service_end_date(self):
        """Gets the service_end_date of this GETDebitMemoItemTypewithSuccess.  # noqa: E501

        The end date of the service period associated with this debit memo item. Service ends one second before the date specified in this field.   # noqa: E501

        :return: The service_end_date of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :rtype: date
        """
        return self._service_end_date

    @service_end_date.setter
    def service_end_date(self, service_end_date):
        """Sets the service_end_date of this GETDebitMemoItemTypewithSuccess.

        The end date of the service period associated with this debit memo item. Service ends one second before the date specified in this field.   # noqa: E501

        :param service_end_date: The service_end_date of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :type: date
        """

        self._service_end_date = service_end_date

    @property
    def service_start_date(self):
        """Gets the service_start_date of this GETDebitMemoItemTypewithSuccess.  # noqa: E501

        The start date of the service period associated with this debit memo item. If the associated charge is a one-time fee, this date is the date of that charge.   # noqa: E501

        :return: The service_start_date of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :rtype: date
        """
        return self._service_start_date

    @service_start_date.setter
    def service_start_date(self, service_start_date):
        """Sets the service_start_date of this GETDebitMemoItemTypewithSuccess.

        The start date of the service period associated with this debit memo item. If the associated charge is a one-time fee, this date is the date of that charge.   # noqa: E501

        :param service_start_date: The service_start_date of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :type: date
        """

        self._service_start_date = service_start_date

    @property
    def sku(self):
        """Gets the sku of this GETDebitMemoItemTypewithSuccess.  # noqa: E501

        The SKU for the product associated with the debit memo item.   # noqa: E501

        :return: The sku of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this GETDebitMemoItemTypewithSuccess.

        The SKU for the product associated with the debit memo item.   # noqa: E501

        :param sku: The sku of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._sku = sku

    @property
    def sku_name(self):
        """Gets the sku_name of this GETDebitMemoItemTypewithSuccess.  # noqa: E501

        The name of the SKU.   # noqa: E501

        :return: The sku_name of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._sku_name

    @sku_name.setter
    def sku_name(self, sku_name):
        """Sets the sku_name of this GETDebitMemoItemTypewithSuccess.

        The name of the SKU.   # noqa: E501

        :param sku_name: The sku_name of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._sku_name = sku_name

    @property
    def source_item_id(self):
        """Gets the source_item_id of this GETDebitMemoItemTypewithSuccess.  # noqa: E501

        The ID of the source item.   # noqa: E501

        :return: The source_item_id of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._source_item_id

    @source_item_id.setter
    def source_item_id(self, source_item_id):
        """Sets the source_item_id of this GETDebitMemoItemTypewithSuccess.

        The ID of the source item.   # noqa: E501

        :param source_item_id: The source_item_id of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._source_item_id = source_item_id

    @property
    def source_item_type(self):
        """Gets the source_item_type of this GETDebitMemoItemTypewithSuccess.  # noqa: E501

        The type of the source item.   # noqa: E501

        :return: The source_item_type of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._source_item_type

    @source_item_type.setter
    def source_item_type(self, source_item_type):
        """Sets the source_item_type of this GETDebitMemoItemTypewithSuccess.

        The type of the source item.   # noqa: E501

        :param source_item_type: The source_item_type of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :type: str
        """
        allowed_values = ["SubscriptionComponent", "InvoiceDetail", "ProductRatePlanCharge"]  # noqa: E501
        if source_item_type not in allowed_values:
            raise ValueError(
                "Invalid value for `source_item_type` ({0}), must be one of {1}"  # noqa: E501
                .format(source_item_type, allowed_values)
            )

        self._source_item_type = source_item_type

    @property
    def subscription_id(self):
        """Gets the subscription_id of this GETDebitMemoItemTypewithSuccess.  # noqa: E501

        The ID of the subscription associated with the debit memo item.   # noqa: E501

        :return: The subscription_id of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this GETDebitMemoItemTypewithSuccess.

        The ID of the subscription associated with the debit memo item.   # noqa: E501

        :param subscription_id: The subscription_id of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def tax_items(self):
        """Gets the tax_items of this GETDebitMemoItemTypewithSuccess.  # noqa: E501

        Container for the taxation items of the debit memo item.   **Note**: This field is not available if you set the `zuora-version` request header to `239.0` or later.   # noqa: E501

        :return: The tax_items of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :rtype: list[GETDMTaxItemType]
        """
        return self._tax_items

    @tax_items.setter
    def tax_items(self, tax_items):
        """Sets the tax_items of this GETDebitMemoItemTypewithSuccess.

        Container for the taxation items of the debit memo item.   **Note**: This field is not available if you set the `zuora-version` request header to `239.0` or later.   # noqa: E501

        :param tax_items: The tax_items of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :type: list[GETDMTaxItemType]
        """

        self._tax_items = tax_items

    @property
    def taxation_items(self):
        """Gets the taxation_items of this GETDebitMemoItemTypewithSuccess.  # noqa: E501


        :return: The taxation_items of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :rtype: GETDebitMemoItemTypewithSuccessTaxationItems
        """
        return self._taxation_items

    @taxation_items.setter
    def taxation_items(self, taxation_items):
        """Sets the taxation_items of this GETDebitMemoItemTypewithSuccess.


        :param taxation_items: The taxation_items of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :type: GETDebitMemoItemTypewithSuccessTaxationItems
        """

        self._taxation_items = taxation_items

    @property
    def updated_by_id(self):
        """Gets the updated_by_id of this GETDebitMemoItemTypewithSuccess.  # noqa: E501

        The ID of the Zuora user who last updated the debit memo item.   # noqa: E501

        :return: The updated_by_id of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """Sets the updated_by_id of this GETDebitMemoItemTypewithSuccess.

        The ID of the Zuora user who last updated the debit memo item.   # noqa: E501

        :param updated_by_id: The updated_by_id of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._updated_by_id = updated_by_id

    @property
    def updated_date(self):
        """Gets the updated_date of this GETDebitMemoItemTypewithSuccess.  # noqa: E501

        The date and time when the debit memo item was last updated, in `yyyy-mm-dd hh:mm:ss` format. For example, 2017-03-02 15:36:10.   # noqa: E501

        :return: The updated_date of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this GETDebitMemoItemTypewithSuccess.

        The date and time when the debit memo item was last updated, in `yyyy-mm-dd hh:mm:ss` format. For example, 2017-03-02 15:36:10.   # noqa: E501

        :param updated_date: The updated_date of this GETDebitMemoItemTypewithSuccess.  # noqa: E501
        :type: datetime
        """

        self._updated_date = updated_date

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
        if issubclass(GETDebitMemoItemTypewithSuccess, dict):
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
        if not isinstance(other, GETDebitMemoItemTypewithSuccess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
