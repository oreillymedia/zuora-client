# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.debit_memo_object_custom_fields import DebitMemoObjectCustomFields  # noqa: F401,E501
from zuora_client.models.debit_memo_object_ns_fields import DebitMemoObjectNSFields  # noqa: F401,E501
from zuora_client.models.put_debit_memo_item_type import PUTDebitMemoItemType  # noqa: F401,E501


class PUTDebitMemoType(object):
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
        'due_date': 'date',
        'effective_date': 'date',
        'items': 'list[PUTDebitMemoItemType]',
        'reason_code': 'str',
        'transferred_to_accounting': 'str'
    }

    attribute_map = {
        'integration_id__ns': 'IntegrationId__NS',
        'integration_status__ns': 'IntegrationStatus__NS',
        'sync_date__ns': 'SyncDate__NS',
        'auto_pay': 'autoPay',
        'comment': 'comment',
        'due_date': 'dueDate',
        'effective_date': 'effectiveDate',
        'items': 'items',
        'reason_code': 'reasonCode',
        'transferred_to_accounting': 'transferredToAccounting'
    }

    def __init__(self, integration_id__ns=None, integration_status__ns=None, sync_date__ns=None, auto_pay=None, comment=None, due_date=None, effective_date=None, items=None, reason_code=None, transferred_to_accounting=None):  # noqa: E501
        """PUTDebitMemoType - a model defined in Swagger"""  # noqa: E501

        self._integration_id__ns = None
        self._integration_status__ns = None
        self._sync_date__ns = None
        self._auto_pay = None
        self._comment = None
        self._due_date = None
        self._effective_date = None
        self._items = None
        self._reason_code = None
        self._transferred_to_accounting = None
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
        if due_date is not None:
            self.due_date = due_date
        if effective_date is not None:
            self.effective_date = effective_date
        if items is not None:
            self.items = items
        if reason_code is not None:
            self.reason_code = reason_code
        if transferred_to_accounting is not None:
            self.transferred_to_accounting = transferred_to_accounting

    @property
    def integration_id__ns(self):
        """Gets the integration_id__ns of this PUTDebitMemoType.  # noqa: E501

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_id__ns of this PUTDebitMemoType.  # noqa: E501
        :rtype: str
        """
        return self._integration_id__ns

    @integration_id__ns.setter
    def integration_id__ns(self, integration_id__ns):
        """Sets the integration_id__ns of this PUTDebitMemoType.

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_id__ns: The integration_id__ns of this PUTDebitMemoType.  # noqa: E501
        :type: str
        """
        if integration_id__ns is not None and len(integration_id__ns) > 255:
            raise ValueError("Invalid value for `integration_id__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_id__ns = integration_id__ns

    @property
    def integration_status__ns(self):
        """Gets the integration_status__ns of this PUTDebitMemoType.  # noqa: E501

        Status of the debit memo's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_status__ns of this PUTDebitMemoType.  # noqa: E501
        :rtype: str
        """
        return self._integration_status__ns

    @integration_status__ns.setter
    def integration_status__ns(self, integration_status__ns):
        """Sets the integration_status__ns of this PUTDebitMemoType.

        Status of the debit memo's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_status__ns: The integration_status__ns of this PUTDebitMemoType.  # noqa: E501
        :type: str
        """
        if integration_status__ns is not None and len(integration_status__ns) > 255:
            raise ValueError("Invalid value for `integration_status__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_status__ns = integration_status__ns

    @property
    def sync_date__ns(self):
        """Gets the sync_date__ns of this PUTDebitMemoType.  # noqa: E501

        Date when the debit memo was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The sync_date__ns of this PUTDebitMemoType.  # noqa: E501
        :rtype: str
        """
        return self._sync_date__ns

    @sync_date__ns.setter
    def sync_date__ns(self, sync_date__ns):
        """Sets the sync_date__ns of this PUTDebitMemoType.

        Date when the debit memo was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param sync_date__ns: The sync_date__ns of this PUTDebitMemoType.  # noqa: E501
        :type: str
        """
        if sync_date__ns is not None and len(sync_date__ns) > 255:
            raise ValueError("Invalid value for `sync_date__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._sync_date__ns = sync_date__ns

    @property
    def auto_pay(self):
        """Gets the auto_pay of this PUTDebitMemoType.  # noqa: E501

        Whether debit memos are automatically picked up for processing in the corresponding payment run.   By default, debit memos are automatically picked up for processing in the corresponding payment run.   # noqa: E501

        :return: The auto_pay of this PUTDebitMemoType.  # noqa: E501
        :rtype: bool
        """
        return self._auto_pay

    @auto_pay.setter
    def auto_pay(self, auto_pay):
        """Sets the auto_pay of this PUTDebitMemoType.

        Whether debit memos are automatically picked up for processing in the corresponding payment run.   By default, debit memos are automatically picked up for processing in the corresponding payment run.   # noqa: E501

        :param auto_pay: The auto_pay of this PUTDebitMemoType.  # noqa: E501
        :type: bool
        """

        self._auto_pay = auto_pay

    @property
    def comment(self):
        """Gets the comment of this PUTDebitMemoType.  # noqa: E501

        Comments about the debit memo.   # noqa: E501

        :return: The comment of this PUTDebitMemoType.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this PUTDebitMemoType.

        Comments about the debit memo.   # noqa: E501

        :param comment: The comment of this PUTDebitMemoType.  # noqa: E501
        :type: str
        """
        if comment is not None and len(comment) > 255:
            raise ValueError("Invalid value for `comment`, length must be less than or equal to `255`")  # noqa: E501
        if comment is not None and len(comment) < 0:
            raise ValueError("Invalid value for `comment`, length must be greater than or equal to `0`")  # noqa: E501

        self._comment = comment

    @property
    def due_date(self):
        """Gets the due_date of this PUTDebitMemoType.  # noqa: E501

        The date by which the payment for the debit memo is due, in `yyyy-mm-dd` format.   # noqa: E501

        :return: The due_date of this PUTDebitMemoType.  # noqa: E501
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this PUTDebitMemoType.

        The date by which the payment for the debit memo is due, in `yyyy-mm-dd` format.   # noqa: E501

        :param due_date: The due_date of this PUTDebitMemoType.  # noqa: E501
        :type: date
        """

        self._due_date = due_date

    @property
    def effective_date(self):
        """Gets the effective_date of this PUTDebitMemoType.  # noqa: E501

        The date when the debit memo takes effect.   # noqa: E501

        :return: The effective_date of this PUTDebitMemoType.  # noqa: E501
        :rtype: date
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this PUTDebitMemoType.

        The date when the debit memo takes effect.   # noqa: E501

        :param effective_date: The effective_date of this PUTDebitMemoType.  # noqa: E501
        :type: date
        """

        self._effective_date = effective_date

    @property
    def items(self):
        """Gets the items of this PUTDebitMemoType.  # noqa: E501

        Container for debit memo items.   # noqa: E501

        :return: The items of this PUTDebitMemoType.  # noqa: E501
        :rtype: list[PUTDebitMemoItemType]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this PUTDebitMemoType.

        Container for debit memo items.   # noqa: E501

        :param items: The items of this PUTDebitMemoType.  # noqa: E501
        :type: list[PUTDebitMemoItemType]
        """

        self._items = items

    @property
    def reason_code(self):
        """Gets the reason_code of this PUTDebitMemoType.  # noqa: E501

        A code identifying the reason for the transaction. The value must be an existing reason code or empty. If you do not specify a value, Zuora uses the default reason code   # noqa: E501

        :return: The reason_code of this PUTDebitMemoType.  # noqa: E501
        :rtype: str
        """
        return self._reason_code

    @reason_code.setter
    def reason_code(self, reason_code):
        """Sets the reason_code of this PUTDebitMemoType.

        A code identifying the reason for the transaction. The value must be an existing reason code or empty. If you do not specify a value, Zuora uses the default reason code   # noqa: E501

        :param reason_code: The reason_code of this PUTDebitMemoType.  # noqa: E501
        :type: str
        """

        self._reason_code = reason_code

    @property
    def transferred_to_accounting(self):
        """Gets the transferred_to_accounting of this PUTDebitMemoType.  # noqa: E501

        Whether the debit memo is transferred to an external accounting system. Use this field for integration with accounting systems, such as NetSuite.    # noqa: E501

        :return: The transferred_to_accounting of this PUTDebitMemoType.  # noqa: E501
        :rtype: str
        """
        return self._transferred_to_accounting

    @transferred_to_accounting.setter
    def transferred_to_accounting(self, transferred_to_accounting):
        """Sets the transferred_to_accounting of this PUTDebitMemoType.

        Whether the debit memo is transferred to an external accounting system. Use this field for integration with accounting systems, such as NetSuite.    # noqa: E501

        :param transferred_to_accounting: The transferred_to_accounting of this PUTDebitMemoType.  # noqa: E501
        :type: str
        """
        allowed_values = ["Processing", "Yes", "No", "Error", "Ignore"]  # noqa: E501
        if transferred_to_accounting not in allowed_values:
            raise ValueError(
                "Invalid value for `transferred_to_accounting` ({0}), must be one of {1}"  # noqa: E501
                .format(transferred_to_accounting, allowed_values)
            )

        self._transferred_to_accounting = transferred_to_accounting

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
        if issubclass(PUTDebitMemoType, dict):
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
        if not isinstance(other, PUTDebitMemoType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
