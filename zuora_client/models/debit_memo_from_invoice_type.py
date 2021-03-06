# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.debit_memo_item_from_invoice_item_type import DebitMemoItemFromInvoiceItemType  # noqa: F401,E501
from zuora_client.models.debit_memo_object_custom_fields import DebitMemoObjectCustomFields  # noqa: F401,E501
from zuora_client.models.debit_memo_object_ns_fields import DebitMemoObjectNSFields  # noqa: F401,E501


class DebitMemoFromInvoiceType(object):
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
        'integration_id__ns': 'str',
        'integration_status__ns': 'str',
        'sync_date__ns': 'str',
        'auto_pay': 'bool',
        'comment': 'str',
        'effective_date': 'date',
        'invoice_id': 'str',
        'items': 'list[DebitMemoItemFromInvoiceItemType]',
        'reason_code': 'str',
        'tax_auto_calculation': 'bool'
    }

    attribute_map = {
        'integration_id__ns': 'IntegrationId__NS',
        'integration_status__ns': 'IntegrationStatus__NS',
        'sync_date__ns': 'SyncDate__NS',
        'auto_pay': 'autoPay',
        'comment': 'comment',
        'effective_date': 'effectiveDate',
        'invoice_id': 'invoiceId',
        'items': 'items',
        'reason_code': 'reasonCode',
        'tax_auto_calculation': 'taxAutoCalculation'
    }

    def __init__(self, integration_id__ns=None, integration_status__ns=None, sync_date__ns=None, auto_pay=None, comment=None, effective_date=None, invoice_id=None, items=None, reason_code=None, tax_auto_calculation=True):  # noqa: E501
        """DebitMemoFromInvoiceType - a model defined in Swagger"""  # noqa: E501

        self._integration_id__ns = None
        self._integration_status__ns = None
        self._sync_date__ns = None
        self._auto_pay = None
        self._comment = None
        self._effective_date = None
        self._invoice_id = None
        self._items = None
        self._reason_code = None
        self._tax_auto_calculation = None
        self.discriminator = None

        if integration_id__ns is not None:
            self.integration_id__ns = integration_id__ns
        if integration_status__ns is not None:
            self.integration_status__ns = integration_status__ns
        if sync_date__ns is not None:
            self.sync_date__ns = sync_date__ns
        if auto_pay is not None:
            self.auto_pay = auto_pay
        if comment is not None:
            self.comment = comment
        if effective_date is not None:
            self.effective_date = effective_date
        if invoice_id is not None:
            self.invoice_id = invoice_id
        if items is not None:
            self.items = items
        if reason_code is not None:
            self.reason_code = reason_code
        if tax_auto_calculation is not None:
            self.tax_auto_calculation = tax_auto_calculation

    @property
    def integration_id__ns(self):
        """Gets the integration_id__ns of this DebitMemoFromInvoiceType.  # noqa: E501

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_id__ns of this DebitMemoFromInvoiceType.  # noqa: E501
        :rtype: str
        """
        return self._integration_id__ns

    @integration_id__ns.setter
    def integration_id__ns(self, integration_id__ns):
        """Sets the integration_id__ns of this DebitMemoFromInvoiceType.

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_id__ns: The integration_id__ns of this DebitMemoFromInvoiceType.  # noqa: E501
        :type: str
        """
        if integration_id__ns is not None and len(integration_id__ns) > 255:
            raise ValueError("Invalid value for `integration_id__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_id__ns = integration_id__ns

    @property
    def integration_status__ns(self):
        """Gets the integration_status__ns of this DebitMemoFromInvoiceType.  # noqa: E501

        Status of the debit memo's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_status__ns of this DebitMemoFromInvoiceType.  # noqa: E501
        :rtype: str
        """
        return self._integration_status__ns

    @integration_status__ns.setter
    def integration_status__ns(self, integration_status__ns):
        """Sets the integration_status__ns of this DebitMemoFromInvoiceType.

        Status of the debit memo's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_status__ns: The integration_status__ns of this DebitMemoFromInvoiceType.  # noqa: E501
        :type: str
        """
        if integration_status__ns is not None and len(integration_status__ns) > 255:
            raise ValueError("Invalid value for `integration_status__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_status__ns = integration_status__ns

    @property
    def sync_date__ns(self):
        """Gets the sync_date__ns of this DebitMemoFromInvoiceType.  # noqa: E501

        Date when the debit memo was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The sync_date__ns of this DebitMemoFromInvoiceType.  # noqa: E501
        :rtype: str
        """
        return self._sync_date__ns

    @sync_date__ns.setter
    def sync_date__ns(self, sync_date__ns):
        """Sets the sync_date__ns of this DebitMemoFromInvoiceType.

        Date when the debit memo was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param sync_date__ns: The sync_date__ns of this DebitMemoFromInvoiceType.  # noqa: E501
        :type: str
        """
        if sync_date__ns is not None and len(sync_date__ns) > 255:
            raise ValueError("Invalid value for `sync_date__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._sync_date__ns = sync_date__ns

    @property
    def auto_pay(self):
        """Gets the auto_pay of this DebitMemoFromInvoiceType.  # noqa: E501

        Whether debit memos are automatically picked up for processing in the corresponding payment run.   By default, debit memos are automatically picked up for processing in the corresponding payment run.   # noqa: E501

        :return: The auto_pay of this DebitMemoFromInvoiceType.  # noqa: E501
        :rtype: bool
        """
        return self._auto_pay

    @auto_pay.setter
    def auto_pay(self, auto_pay):
        """Sets the auto_pay of this DebitMemoFromInvoiceType.

        Whether debit memos are automatically picked up for processing in the corresponding payment run.   By default, debit memos are automatically picked up for processing in the corresponding payment run.   # noqa: E501

        :param auto_pay: The auto_pay of this DebitMemoFromInvoiceType.  # noqa: E501
        :type: bool
        """

        self._auto_pay = auto_pay

    @property
    def comment(self):
        """Gets the comment of this DebitMemoFromInvoiceType.  # noqa: E501

        Comments about the debit memo.    # noqa: E501

        :return: The comment of this DebitMemoFromInvoiceType.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this DebitMemoFromInvoiceType.

        Comments about the debit memo.    # noqa: E501

        :param comment: The comment of this DebitMemoFromInvoiceType.  # noqa: E501
        :type: str
        """
        if comment is not None and len(comment) > 255:
            raise ValueError("Invalid value for `comment`, length must be less than or equal to `255`")  # noqa: E501
        if comment is not None and len(comment) < 0:
            raise ValueError("Invalid value for `comment`, length must be greater than or equal to `0`")  # noqa: E501

        self._comment = comment

    @property
    def effective_date(self):
        """Gets the effective_date of this DebitMemoFromInvoiceType.  # noqa: E501

        The date when the debit memo takes effect.   # noqa: E501

        :return: The effective_date of this DebitMemoFromInvoiceType.  # noqa: E501
        :rtype: date
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this DebitMemoFromInvoiceType.

        The date when the debit memo takes effect.   # noqa: E501

        :param effective_date: The effective_date of this DebitMemoFromInvoiceType.  # noqa: E501
        :type: date
        """

        self._effective_date = effective_date

    @property
    def invoice_id(self):
        """Gets the invoice_id of this DebitMemoFromInvoiceType.  # noqa: E501

        The ID of the invoice that the debit memo is created from.   # noqa: E501

        :return: The invoice_id of this DebitMemoFromInvoiceType.  # noqa: E501
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """Sets the invoice_id of this DebitMemoFromInvoiceType.

        The ID of the invoice that the debit memo is created from.   # noqa: E501

        :param invoice_id: The invoice_id of this DebitMemoFromInvoiceType.  # noqa: E501
        :type: str
        """

        self._invoice_id = invoice_id

    @property
    def items(self):
        """Gets the items of this DebitMemoFromInvoiceType.  # noqa: E501

        Container for items.   # noqa: E501

        :return: The items of this DebitMemoFromInvoiceType.  # noqa: E501
        :rtype: list[DebitMemoItemFromInvoiceItemType]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this DebitMemoFromInvoiceType.

        Container for items.   # noqa: E501

        :param items: The items of this DebitMemoFromInvoiceType.  # noqa: E501
        :type: list[DebitMemoItemFromInvoiceItemType]
        """

        self._items = items

    @property
    def reason_code(self):
        """Gets the reason_code of this DebitMemoFromInvoiceType.  # noqa: E501

        A code identifying the reason for the transaction. The value must be an existing reason code or empty. If you do not specify a value, Zuora uses the default reason code.   # noqa: E501

        :return: The reason_code of this DebitMemoFromInvoiceType.  # noqa: E501
        :rtype: str
        """
        return self._reason_code

    @reason_code.setter
    def reason_code(self, reason_code):
        """Sets the reason_code of this DebitMemoFromInvoiceType.

        A code identifying the reason for the transaction. The value must be an existing reason code or empty. If you do not specify a value, Zuora uses the default reason code.   # noqa: E501

        :param reason_code: The reason_code of this DebitMemoFromInvoiceType.  # noqa: E501
        :type: str
        """

        self._reason_code = reason_code

    @property
    def tax_auto_calculation(self):
        """Gets the tax_auto_calculation of this DebitMemoFromInvoiceType.  # noqa: E501

        Whether to automatically calculate taxes in the debit memo.   # noqa: E501

        :return: The tax_auto_calculation of this DebitMemoFromInvoiceType.  # noqa: E501
        :rtype: bool
        """
        return self._tax_auto_calculation

    @tax_auto_calculation.setter
    def tax_auto_calculation(self, tax_auto_calculation):
        """Sets the tax_auto_calculation of this DebitMemoFromInvoiceType.

        Whether to automatically calculate taxes in the debit memo.   # noqa: E501

        :param tax_auto_calculation: The tax_auto_calculation of this DebitMemoFromInvoiceType.  # noqa: E501
        :type: bool
        """

        self._tax_auto_calculation = tax_auto_calculation

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
        if issubclass(DebitMemoFromInvoiceType, dict):
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
        if not isinstance(other, DebitMemoFromInvoiceType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
