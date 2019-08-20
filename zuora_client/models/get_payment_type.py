# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.get_paid_invoices_type import GETPaidInvoicesType  # noqa: F401,E501
from zuora_client.models.payment_object_custom_fields import PaymentObjectCustomFields  # noqa: F401,E501
from zuora_client.models.payment_object_ns_fields import PaymentObjectNSFields  # noqa: F401,E501


class GETPaymentType(object):
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
        'account_id': 'str',
        'account_name': 'str',
        'account_number': 'str',
        'amount': 'str',
        'effective_date': 'date',
        'gateway_transaction_number': 'str',
        'id': 'str',
        'paid_invoices': 'list[GETPaidInvoicesType]',
        'payment_method_id': 'str',
        'payment_number': 'str',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'integration_id__ns': 'IntegrationId__NS',
        'integration_status__ns': 'IntegrationStatus__NS',
        'origin__ns': 'Origin__NS',
        'sync_date__ns': 'SyncDate__NS',
        'transaction__ns': 'Transaction__NS',
        'account_id': 'accountID',
        'account_name': 'accountName',
        'account_number': 'accountNumber',
        'amount': 'amount',
        'effective_date': 'effectiveDate',
        'gateway_transaction_number': 'gatewayTransactionNumber',
        'id': 'id',
        'paid_invoices': 'paidInvoices',
        'payment_method_id': 'paymentMethodID',
        'payment_number': 'paymentNumber',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, integration_id__ns=None, integration_status__ns=None, origin__ns=None, sync_date__ns=None, transaction__ns=None, account_id=None, account_name=None, account_number=None, amount=None, effective_date=None, gateway_transaction_number=None, id=None, paid_invoices=None, payment_method_id=None, payment_number=None, status=None, type=None):  # noqa: E501
        """GETPaymentType - a model defined in Swagger"""  # noqa: E501

        self._integration_id__ns = None
        self._integration_status__ns = None
        self._origin__ns = None
        self._sync_date__ns = None
        self._transaction__ns = None
        self._account_id = None
        self._account_name = None
        self._account_number = None
        self._amount = None
        self._effective_date = None
        self._gateway_transaction_number = None
        self._id = None
        self._paid_invoices = None
        self._payment_method_id = None
        self._payment_number = None
        self._status = None
        self._type = None
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
        if account_id is not None:
            self.account_id = account_id
        if account_name is not None:
            self.account_name = account_name
        if account_number is not None:
            self.account_number = account_number
        if amount is not None:
            self.amount = amount
        if effective_date is not None:
            self.effective_date = effective_date
        if gateway_transaction_number is not None:
            self.gateway_transaction_number = gateway_transaction_number
        if id is not None:
            self.id = id
        if paid_invoices is not None:
            self.paid_invoices = paid_invoices
        if payment_method_id is not None:
            self.payment_method_id = payment_method_id
        if payment_number is not None:
            self.payment_number = payment_number
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type

    @property
    def integration_id__ns(self):
        """Gets the integration_id__ns of this GETPaymentType.  # noqa: E501

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_id__ns of this GETPaymentType.  # noqa: E501
        :rtype: str
        """
        return self._integration_id__ns

    @integration_id__ns.setter
    def integration_id__ns(self, integration_id__ns):
        """Sets the integration_id__ns of this GETPaymentType.

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_id__ns: The integration_id__ns of this GETPaymentType.  # noqa: E501
        :type: str
        """
        if integration_id__ns is not None and len(integration_id__ns) > 255:
            raise ValueError("Invalid value for `integration_id__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_id__ns = integration_id__ns

    @property
    def integration_status__ns(self):
        """Gets the integration_status__ns of this GETPaymentType.  # noqa: E501

        Status of the payment's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_status__ns of this GETPaymentType.  # noqa: E501
        :rtype: str
        """
        return self._integration_status__ns

    @integration_status__ns.setter
    def integration_status__ns(self, integration_status__ns):
        """Sets the integration_status__ns of this GETPaymentType.

        Status of the payment's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_status__ns: The integration_status__ns of this GETPaymentType.  # noqa: E501
        :type: str
        """
        if integration_status__ns is not None and len(integration_status__ns) > 255:
            raise ValueError("Invalid value for `integration_status__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_status__ns = integration_status__ns

    @property
    def origin__ns(self):
        """Gets the origin__ns of this GETPaymentType.  # noqa: E501

        Origin of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The origin__ns of this GETPaymentType.  # noqa: E501
        :rtype: str
        """
        return self._origin__ns

    @origin__ns.setter
    def origin__ns(self, origin__ns):
        """Sets the origin__ns of this GETPaymentType.

        Origin of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param origin__ns: The origin__ns of this GETPaymentType.  # noqa: E501
        :type: str
        """
        if origin__ns is not None and len(origin__ns) > 255:
            raise ValueError("Invalid value for `origin__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._origin__ns = origin__ns

    @property
    def sync_date__ns(self):
        """Gets the sync_date__ns of this GETPaymentType.  # noqa: E501

        Date when the payment was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The sync_date__ns of this GETPaymentType.  # noqa: E501
        :rtype: str
        """
        return self._sync_date__ns

    @sync_date__ns.setter
    def sync_date__ns(self, sync_date__ns):
        """Sets the sync_date__ns of this GETPaymentType.

        Date when the payment was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param sync_date__ns: The sync_date__ns of this GETPaymentType.  # noqa: E501
        :type: str
        """
        if sync_date__ns is not None and len(sync_date__ns) > 255:
            raise ValueError("Invalid value for `sync_date__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._sync_date__ns = sync_date__ns

    @property
    def transaction__ns(self):
        """Gets the transaction__ns of this GETPaymentType.  # noqa: E501

        Related transaction in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The transaction__ns of this GETPaymentType.  # noqa: E501
        :rtype: str
        """
        return self._transaction__ns

    @transaction__ns.setter
    def transaction__ns(self, transaction__ns):
        """Sets the transaction__ns of this GETPaymentType.

        Related transaction in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param transaction__ns: The transaction__ns of this GETPaymentType.  # noqa: E501
        :type: str
        """
        if transaction__ns is not None and len(transaction__ns) > 255:
            raise ValueError("Invalid value for `transaction__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._transaction__ns = transaction__ns

    @property
    def account_id(self):
        """Gets the account_id of this GETPaymentType.  # noqa: E501

        Customer account ID.   # noqa: E501

        :return: The account_id of this GETPaymentType.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this GETPaymentType.

        Customer account ID.   # noqa: E501

        :param account_id: The account_id of this GETPaymentType.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def account_name(self):
        """Gets the account_name of this GETPaymentType.  # noqa: E501

        Customer account name.   # noqa: E501

        :return: The account_name of this GETPaymentType.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this GETPaymentType.

        Customer account name.   # noqa: E501

        :param account_name: The account_name of this GETPaymentType.  # noqa: E501
        :type: str
        """

        self._account_name = account_name

    @property
    def account_number(self):
        """Gets the account_number of this GETPaymentType.  # noqa: E501

        Customer account number.   # noqa: E501

        :return: The account_number of this GETPaymentType.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this GETPaymentType.

        Customer account number.   # noqa: E501

        :param account_number: The account_number of this GETPaymentType.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def amount(self):
        """Gets the amount of this GETPaymentType.  # noqa: E501

        Payment amount.   # noqa: E501

        :return: The amount of this GETPaymentType.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GETPaymentType.

        Payment amount.   # noqa: E501

        :param amount: The amount of this GETPaymentType.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def effective_date(self):
        """Gets the effective_date of this GETPaymentType.  # noqa: E501

        Effective payment date as _yyyy-mm-dd_.   # noqa: E501

        :return: The effective_date of this GETPaymentType.  # noqa: E501
        :rtype: date
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this GETPaymentType.

        Effective payment date as _yyyy-mm-dd_.   # noqa: E501

        :param effective_date: The effective_date of this GETPaymentType.  # noqa: E501
        :type: date
        """

        self._effective_date = effective_date

    @property
    def gateway_transaction_number(self):
        """Gets the gateway_transaction_number of this GETPaymentType.  # noqa: E501

        Transaction ID from payment gateway.   # noqa: E501

        :return: The gateway_transaction_number of this GETPaymentType.  # noqa: E501
        :rtype: str
        """
        return self._gateway_transaction_number

    @gateway_transaction_number.setter
    def gateway_transaction_number(self, gateway_transaction_number):
        """Sets the gateway_transaction_number of this GETPaymentType.

        Transaction ID from payment gateway.   # noqa: E501

        :param gateway_transaction_number: The gateway_transaction_number of this GETPaymentType.  # noqa: E501
        :type: str
        """

        self._gateway_transaction_number = gateway_transaction_number

    @property
    def id(self):
        """Gets the id of this GETPaymentType.  # noqa: E501

        PaymentID.   # noqa: E501

        :return: The id of this GETPaymentType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GETPaymentType.

        PaymentID.   # noqa: E501

        :param id: The id of this GETPaymentType.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def paid_invoices(self):
        """Gets the paid_invoices of this GETPaymentType.  # noqa: E501

        Information about one or more invoices to which this payment was applied:   # noqa: E501

        :return: The paid_invoices of this GETPaymentType.  # noqa: E501
        :rtype: list[GETPaidInvoicesType]
        """
        return self._paid_invoices

    @paid_invoices.setter
    def paid_invoices(self, paid_invoices):
        """Sets the paid_invoices of this GETPaymentType.

        Information about one or more invoices to which this payment was applied:   # noqa: E501

        :param paid_invoices: The paid_invoices of this GETPaymentType.  # noqa: E501
        :type: list[GETPaidInvoicesType]
        """

        self._paid_invoices = paid_invoices

    @property
    def payment_method_id(self):
        """Gets the payment_method_id of this GETPaymentType.  # noqa: E501

        Payment method.   # noqa: E501

        :return: The payment_method_id of this GETPaymentType.  # noqa: E501
        :rtype: str
        """
        return self._payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, payment_method_id):
        """Sets the payment_method_id of this GETPaymentType.

        Payment method.   # noqa: E501

        :param payment_method_id: The payment_method_id of this GETPaymentType.  # noqa: E501
        :type: str
        """

        self._payment_method_id = payment_method_id

    @property
    def payment_number(self):
        """Gets the payment_number of this GETPaymentType.  # noqa: E501

        Unique payment number.   # noqa: E501

        :return: The payment_number of this GETPaymentType.  # noqa: E501
        :rtype: str
        """
        return self._payment_number

    @payment_number.setter
    def payment_number(self, payment_number):
        """Sets the payment_number of this GETPaymentType.

        Unique payment number.   # noqa: E501

        :param payment_number: The payment_number of this GETPaymentType.  # noqa: E501
        :type: str
        """

        self._payment_number = payment_number

    @property
    def status(self):
        """Gets the status of this GETPaymentType.  # noqa: E501

        Possible values are: `Draft`, `Processing`, `Processed`, `Error`, `Voided`, `Canceled`, `Posted.   # noqa: E501

        :return: The status of this GETPaymentType.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GETPaymentType.

        Possible values are: `Draft`, `Processing`, `Processed`, `Error`, `Voided`, `Canceled`, `Posted.   # noqa: E501

        :param status: The status of this GETPaymentType.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this GETPaymentType.  # noqa: E501

        Possible values are: `External`, `Electronic`.   # noqa: E501

        :return: The type of this GETPaymentType.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GETPaymentType.

        Possible values are: `External`, `Electronic`.   # noqa: E501

        :param type: The type of this GETPaymentType.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(GETPaymentType, dict):
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
        if not isinstance(other, GETPaymentType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
