# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.credit_memo_item_from_invoice_item_type import CreditMemoItemFromInvoiceItemType  # noqa: F401,E501
from zuora_client.models.credit_memo_object_custom_fields import CreditMemoObjectCustomFields  # noqa: F401,E501
from zuora_client.models.credit_memo_object_ns_fields import CreditMemoObjectNSFields  # noqa: F401,E501


class CreditMemoFromInvoiceType(object):
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
        'origin__ns': 'str',
        'sync_date__ns': 'str',
        'transaction__ns': 'str',
        'auto_apply_to_invoice_upon_posting': 'bool',
        'comment': 'str',
        'effective_date': 'date',
        'exclude_from_auto_apply_rules': 'bool',
        'invoice_id': 'str',
        'items': 'list[CreditMemoItemFromInvoiceItemType]',
        'reason_code': 'str',
        'tax_auto_calculation': 'bool'
    }

    attribute_map = {
        'integration_id__ns': 'IntegrationId__NS',
        'integration_status__ns': 'IntegrationStatus__NS',
        'origin__ns': 'Origin__NS',
        'sync_date__ns': 'SyncDate__NS',
        'transaction__ns': 'Transaction__NS',
        'auto_apply_to_invoice_upon_posting': 'autoApplyToInvoiceUponPosting',
        'comment': 'comment',
        'effective_date': 'effectiveDate',
        'exclude_from_auto_apply_rules': 'excludeFromAutoApplyRules',
        'invoice_id': 'invoiceId',
        'items': 'items',
        'reason_code': 'reasonCode',
        'tax_auto_calculation': 'taxAutoCalculation'
    }

    def __init__(self, integration_id__ns=None, integration_status__ns=None, origin__ns=None, sync_date__ns=None, transaction__ns=None, auto_apply_to_invoice_upon_posting=None, comment=None, effective_date=None, exclude_from_auto_apply_rules=None, invoice_id=None, items=None, reason_code=None, tax_auto_calculation=True):  # noqa: E501
        """CreditMemoFromInvoiceType - a model defined in Swagger"""  # noqa: E501

        self._integration_id__ns = None
        self._integration_status__ns = None
        self._origin__ns = None
        self._sync_date__ns = None
        self._transaction__ns = None
        self._auto_apply_to_invoice_upon_posting = None
        self._comment = None
        self._effective_date = None
        self._exclude_from_auto_apply_rules = None
        self._invoice_id = None
        self._items = None
        self._reason_code = None
        self._tax_auto_calculation = None
        self.discriminator = None

        if integration_id__ns is not None:
            self.integration_id__ns = integration_id__ns
        if integration_status__ns is not None:
            self.integration_status__ns = integration_status__ns
        if origin__ns is not None:
            self.origin__ns = origin__ns
        if sync_date__ns is not None:
            self.sync_date__ns = sync_date__ns
        if transaction__ns is not None:
            self.transaction__ns = transaction__ns
        if auto_apply_to_invoice_upon_posting is not None:
            self.auto_apply_to_invoice_upon_posting = auto_apply_to_invoice_upon_posting
        if comment is not None:
            self.comment = comment
        if effective_date is not None:
            self.effective_date = effective_date
        if exclude_from_auto_apply_rules is not None:
            self.exclude_from_auto_apply_rules = exclude_from_auto_apply_rules
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
        """Gets the integration_id__ns of this CreditMemoFromInvoiceType.  # noqa: E501

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_id__ns of this CreditMemoFromInvoiceType.  # noqa: E501
        :rtype: str
        """
        return self._integration_id__ns

    @integration_id__ns.setter
    def integration_id__ns(self, integration_id__ns):
        """Sets the integration_id__ns of this CreditMemoFromInvoiceType.

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_id__ns: The integration_id__ns of this CreditMemoFromInvoiceType.  # noqa: E501
        :type: str
        """
        if integration_id__ns is not None and len(integration_id__ns) > 255:
            raise ValueError("Invalid value for `integration_id__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_id__ns = integration_id__ns

    @property
    def integration_status__ns(self):
        """Gets the integration_status__ns of this CreditMemoFromInvoiceType.  # noqa: E501

        Status of the credit memo's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_status__ns of this CreditMemoFromInvoiceType.  # noqa: E501
        :rtype: str
        """
        return self._integration_status__ns

    @integration_status__ns.setter
    def integration_status__ns(self, integration_status__ns):
        """Sets the integration_status__ns of this CreditMemoFromInvoiceType.

        Status of the credit memo's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_status__ns: The integration_status__ns of this CreditMemoFromInvoiceType.  # noqa: E501
        :type: str
        """
        if integration_status__ns is not None and len(integration_status__ns) > 255:
            raise ValueError("Invalid value for `integration_status__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_status__ns = integration_status__ns

    @property
    def origin__ns(self):
        """Gets the origin__ns of this CreditMemoFromInvoiceType.  # noqa: E501

        Origin of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The origin__ns of this CreditMemoFromInvoiceType.  # noqa: E501
        :rtype: str
        """
        return self._origin__ns

    @origin__ns.setter
    def origin__ns(self, origin__ns):
        """Sets the origin__ns of this CreditMemoFromInvoiceType.

        Origin of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param origin__ns: The origin__ns of this CreditMemoFromInvoiceType.  # noqa: E501
        :type: str
        """
        if origin__ns is not None and len(origin__ns) > 255:
            raise ValueError("Invalid value for `origin__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._origin__ns = origin__ns

    @property
    def sync_date__ns(self):
        """Gets the sync_date__ns of this CreditMemoFromInvoiceType.  # noqa: E501

        Date when the credit memo was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The sync_date__ns of this CreditMemoFromInvoiceType.  # noqa: E501
        :rtype: str
        """
        return self._sync_date__ns

    @sync_date__ns.setter
    def sync_date__ns(self, sync_date__ns):
        """Sets the sync_date__ns of this CreditMemoFromInvoiceType.

        Date when the credit memo was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param sync_date__ns: The sync_date__ns of this CreditMemoFromInvoiceType.  # noqa: E501
        :type: str
        """
        if sync_date__ns is not None and len(sync_date__ns) > 255:
            raise ValueError("Invalid value for `sync_date__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._sync_date__ns = sync_date__ns

    @property
    def transaction__ns(self):
        """Gets the transaction__ns of this CreditMemoFromInvoiceType.  # noqa: E501

        Related transaction in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The transaction__ns of this CreditMemoFromInvoiceType.  # noqa: E501
        :rtype: str
        """
        return self._transaction__ns

    @transaction__ns.setter
    def transaction__ns(self, transaction__ns):
        """Sets the transaction__ns of this CreditMemoFromInvoiceType.

        Related transaction in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param transaction__ns: The transaction__ns of this CreditMemoFromInvoiceType.  # noqa: E501
        :type: str
        """
        if transaction__ns is not None and len(transaction__ns) > 255:
            raise ValueError("Invalid value for `transaction__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._transaction__ns = transaction__ns

    @property
    def auto_apply_to_invoice_upon_posting(self):
        """Gets the auto_apply_to_invoice_upon_posting of this CreditMemoFromInvoiceType.  # noqa: E501

        Whether the credit memo automatically applies to the invoice upon posting.   # noqa: E501

        :return: The auto_apply_to_invoice_upon_posting of this CreditMemoFromInvoiceType.  # noqa: E501
        :rtype: bool
        """
        return self._auto_apply_to_invoice_upon_posting

    @auto_apply_to_invoice_upon_posting.setter
    def auto_apply_to_invoice_upon_posting(self, auto_apply_to_invoice_upon_posting):
        """Sets the auto_apply_to_invoice_upon_posting of this CreditMemoFromInvoiceType.

        Whether the credit memo automatically applies to the invoice upon posting.   # noqa: E501

        :param auto_apply_to_invoice_upon_posting: The auto_apply_to_invoice_upon_posting of this CreditMemoFromInvoiceType.  # noqa: E501
        :type: bool
        """

        self._auto_apply_to_invoice_upon_posting = auto_apply_to_invoice_upon_posting

    @property
    def comment(self):
        """Gets the comment of this CreditMemoFromInvoiceType.  # noqa: E501

        Comments about the credit memo.   # noqa: E501

        :return: The comment of this CreditMemoFromInvoiceType.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this CreditMemoFromInvoiceType.

        Comments about the credit memo.   # noqa: E501

        :param comment: The comment of this CreditMemoFromInvoiceType.  # noqa: E501
        :type: str
        """
        if comment is not None and len(comment) > 255:
            raise ValueError("Invalid value for `comment`, length must be less than or equal to `255`")  # noqa: E501
        if comment is not None and len(comment) < 0:
            raise ValueError("Invalid value for `comment`, length must be greater than or equal to `0`")  # noqa: E501

        self._comment = comment

    @property
    def effective_date(self):
        """Gets the effective_date of this CreditMemoFromInvoiceType.  # noqa: E501

        The date when the credit memo takes effect.   # noqa: E501

        :return: The effective_date of this CreditMemoFromInvoiceType.  # noqa: E501
        :rtype: date
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this CreditMemoFromInvoiceType.

        The date when the credit memo takes effect.   # noqa: E501

        :param effective_date: The effective_date of this CreditMemoFromInvoiceType.  # noqa: E501
        :type: date
        """

        self._effective_date = effective_date

    @property
    def exclude_from_auto_apply_rules(self):
        """Gets the exclude_from_auto_apply_rules of this CreditMemoFromInvoiceType.  # noqa: E501

        Whether the credit memo is excluded from the rule of automatically applying credit memos to invoices.   # noqa: E501

        :return: The exclude_from_auto_apply_rules of this CreditMemoFromInvoiceType.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_from_auto_apply_rules

    @exclude_from_auto_apply_rules.setter
    def exclude_from_auto_apply_rules(self, exclude_from_auto_apply_rules):
        """Sets the exclude_from_auto_apply_rules of this CreditMemoFromInvoiceType.

        Whether the credit memo is excluded from the rule of automatically applying credit memos to invoices.   # noqa: E501

        :param exclude_from_auto_apply_rules: The exclude_from_auto_apply_rules of this CreditMemoFromInvoiceType.  # noqa: E501
        :type: bool
        """

        self._exclude_from_auto_apply_rules = exclude_from_auto_apply_rules

    @property
    def invoice_id(self):
        """Gets the invoice_id of this CreditMemoFromInvoiceType.  # noqa: E501

        The ID of the invoice that the credit memo is created from.   # noqa: E501

        :return: The invoice_id of this CreditMemoFromInvoiceType.  # noqa: E501
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """Sets the invoice_id of this CreditMemoFromInvoiceType.

        The ID of the invoice that the credit memo is created from.   # noqa: E501

        :param invoice_id: The invoice_id of this CreditMemoFromInvoiceType.  # noqa: E501
        :type: str
        """

        self._invoice_id = invoice_id

    @property
    def items(self):
        """Gets the items of this CreditMemoFromInvoiceType.  # noqa: E501

        Container for items.   # noqa: E501

        :return: The items of this CreditMemoFromInvoiceType.  # noqa: E501
        :rtype: list[CreditMemoItemFromInvoiceItemType]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this CreditMemoFromInvoiceType.

        Container for items.   # noqa: E501

        :param items: The items of this CreditMemoFromInvoiceType.  # noqa: E501
        :type: list[CreditMemoItemFromInvoiceItemType]
        """

        self._items = items

    @property
    def reason_code(self):
        """Gets the reason_code of this CreditMemoFromInvoiceType.  # noqa: E501

        A code identifying the reason for the transaction. The value must be an existing reason code or empty. If you do not specify a value, Zuora uses the default reason code.   # noqa: E501

        :return: The reason_code of this CreditMemoFromInvoiceType.  # noqa: E501
        :rtype: str
        """
        return self._reason_code

    @reason_code.setter
    def reason_code(self, reason_code):
        """Sets the reason_code of this CreditMemoFromInvoiceType.

        A code identifying the reason for the transaction. The value must be an existing reason code or empty. If you do not specify a value, Zuora uses the default reason code.   # noqa: E501

        :param reason_code: The reason_code of this CreditMemoFromInvoiceType.  # noqa: E501
        :type: str
        """

        self._reason_code = reason_code

    @property
    def tax_auto_calculation(self):
        """Gets the tax_auto_calculation of this CreditMemoFromInvoiceType.  # noqa: E501

        Whether to automatically calculate taxes in the credit memo.   # noqa: E501

        :return: The tax_auto_calculation of this CreditMemoFromInvoiceType.  # noqa: E501
        :rtype: bool
        """
        return self._tax_auto_calculation

    @tax_auto_calculation.setter
    def tax_auto_calculation(self, tax_auto_calculation):
        """Sets the tax_auto_calculation of this CreditMemoFromInvoiceType.

        Whether to automatically calculate taxes in the credit memo.   # noqa: E501

        :param tax_auto_calculation: The tax_auto_calculation of this CreditMemoFromInvoiceType.  # noqa: E501
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
        if issubclass(CreditMemoFromInvoiceType, dict):
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
        if not isinstance(other, CreditMemoFromInvoiceType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
