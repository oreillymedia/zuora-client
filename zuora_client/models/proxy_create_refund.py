# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.proxy_create_payment_gateway_option_data import ProxyCreatePaymentGatewayOptionData  # noqa: F401,E501
from zuora_client.models.proxy_create_refund_refund_invoice_payment_data import ProxyCreateRefundRefundInvoicePaymentData  # noqa: F401,E501
from zuora_client.models.refund_object_custom_fields import RefundObjectCustomFields  # noqa: F401,E501
from zuora_client.models.refund_object_ns_fields import RefundObjectNSFields  # noqa: F401,E501


class ProxyCreateRefund(object):
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
        'syncto_net_suite__ns': 'str',
        'account_id': 'str',
        'amount': 'float',
        'comment': 'str',
        'gateway_option_data': 'ProxyCreatePaymentGatewayOptionData',
        'gateway_state': 'str',
        'method_type': 'str',
        'payment_method_id': 'str',
        'reason_code': 'str',
        'refund_date': 'date',
        'refund_invoice_payment_data': 'ProxyCreateRefundRefundInvoicePaymentData',
        'soft_descriptor': 'str',
        'soft_descriptor_phone': 'str',
        'source_type': 'str',
        'type': 'str'
    }

    attribute_map = {
        'integration_id__ns': 'IntegrationId__NS',
        'integration_status__ns': 'IntegrationStatus__NS',
        'origin__ns': 'Origin__NS',
        'sync_date__ns': 'SyncDate__NS',
        'syncto_net_suite__ns': 'SynctoNetSuite__NS',
        'account_id': 'AccountId',
        'amount': 'Amount',
        'comment': 'Comment',
        'gateway_option_data': 'GatewayOptionData',
        'gateway_state': 'GatewayState',
        'method_type': 'MethodType',
        'payment_method_id': 'PaymentMethodId',
        'reason_code': 'ReasonCode',
        'refund_date': 'RefundDate',
        'refund_invoice_payment_data': 'RefundInvoicePaymentData',
        'soft_descriptor': 'SoftDescriptor',
        'soft_descriptor_phone': 'SoftDescriptorPhone',
        'source_type': 'SourceType',
        'type': 'Type'
    }

    def __init__(self, integration_id__ns=None, integration_status__ns=None, origin__ns=None, sync_date__ns=None, syncto_net_suite__ns=None, account_id=None, amount=None, comment=None, gateway_option_data=None, gateway_state=None, method_type=None, payment_method_id=None, reason_code=None, refund_date=None, refund_invoice_payment_data=None, soft_descriptor=None, soft_descriptor_phone=None, source_type=None, type=None):  # noqa: E501
        """ProxyCreateRefund - a model defined in Swagger"""  # noqa: E501

        self._integration_id__ns = None
        self._integration_status__ns = None
        self._origin__ns = None
        self._sync_date__ns = None
        self._syncto_net_suite__ns = None
        self._account_id = None
        self._amount = None
        self._comment = None
        self._gateway_option_data = None
        self._gateway_state = None
        self._method_type = None
        self._payment_method_id = None
        self._reason_code = None
        self._refund_date = None
        self._refund_invoice_payment_data = None
        self._soft_descriptor = None
        self._soft_descriptor_phone = None
        self._source_type = None
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
        if syncto_net_suite__ns is not None:
            self.syncto_net_suite__ns = syncto_net_suite__ns
        if account_id is not None:
            self.account_id = account_id
        self.amount = amount
        if comment is not None:
            self.comment = comment
        if gateway_option_data is not None:
            self.gateway_option_data = gateway_option_data
        if gateway_state is not None:
            self.gateway_state = gateway_state
        if method_type is not None:
            self.method_type = method_type
        if payment_method_id is not None:
            self.payment_method_id = payment_method_id
        if reason_code is not None:
            self.reason_code = reason_code
        if refund_date is not None:
            self.refund_date = refund_date
        if refund_invoice_payment_data is not None:
            self.refund_invoice_payment_data = refund_invoice_payment_data
        if soft_descriptor is not None:
            self.soft_descriptor = soft_descriptor
        if soft_descriptor_phone is not None:
            self.soft_descriptor_phone = soft_descriptor_phone
        if source_type is not None:
            self.source_type = source_type
        self.type = type

    @property
    def integration_id__ns(self):
        """Gets the integration_id__ns of this ProxyCreateRefund.  # noqa: E501

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_id__ns of this ProxyCreateRefund.  # noqa: E501
        :rtype: str
        """
        return self._integration_id__ns

    @integration_id__ns.setter
    def integration_id__ns(self, integration_id__ns):
        """Sets the integration_id__ns of this ProxyCreateRefund.

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_id__ns: The integration_id__ns of this ProxyCreateRefund.  # noqa: E501
        :type: str
        """
        if integration_id__ns is not None and len(integration_id__ns) > 255:
            raise ValueError("Invalid value for `integration_id__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_id__ns = integration_id__ns

    @property
    def integration_status__ns(self):
        """Gets the integration_status__ns of this ProxyCreateRefund.  # noqa: E501

        Status of the refund's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_status__ns of this ProxyCreateRefund.  # noqa: E501
        :rtype: str
        """
        return self._integration_status__ns

    @integration_status__ns.setter
    def integration_status__ns(self, integration_status__ns):
        """Sets the integration_status__ns of this ProxyCreateRefund.

        Status of the refund's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_status__ns: The integration_status__ns of this ProxyCreateRefund.  # noqa: E501
        :type: str
        """
        if integration_status__ns is not None and len(integration_status__ns) > 255:
            raise ValueError("Invalid value for `integration_status__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_status__ns = integration_status__ns

    @property
    def origin__ns(self):
        """Gets the origin__ns of this ProxyCreateRefund.  # noqa: E501

        Origin of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The origin__ns of this ProxyCreateRefund.  # noqa: E501
        :rtype: str
        """
        return self._origin__ns

    @origin__ns.setter
    def origin__ns(self, origin__ns):
        """Sets the origin__ns of this ProxyCreateRefund.

        Origin of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param origin__ns: The origin__ns of this ProxyCreateRefund.  # noqa: E501
        :type: str
        """
        if origin__ns is not None and len(origin__ns) > 255:
            raise ValueError("Invalid value for `origin__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._origin__ns = origin__ns

    @property
    def sync_date__ns(self):
        """Gets the sync_date__ns of this ProxyCreateRefund.  # noqa: E501

        Date when the refund was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The sync_date__ns of this ProxyCreateRefund.  # noqa: E501
        :rtype: str
        """
        return self._sync_date__ns

    @sync_date__ns.setter
    def sync_date__ns(self, sync_date__ns):
        """Sets the sync_date__ns of this ProxyCreateRefund.

        Date when the refund was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param sync_date__ns: The sync_date__ns of this ProxyCreateRefund.  # noqa: E501
        :type: str
        """
        if sync_date__ns is not None and len(sync_date__ns) > 255:
            raise ValueError("Invalid value for `sync_date__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._sync_date__ns = sync_date__ns

    @property
    def syncto_net_suite__ns(self):
        """Gets the syncto_net_suite__ns of this ProxyCreateRefund.  # noqa: E501

        Specifies whether the refund should be synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The syncto_net_suite__ns of this ProxyCreateRefund.  # noqa: E501
        :rtype: str
        """
        return self._syncto_net_suite__ns

    @syncto_net_suite__ns.setter
    def syncto_net_suite__ns(self, syncto_net_suite__ns):
        """Sets the syncto_net_suite__ns of this ProxyCreateRefund.

        Specifies whether the refund should be synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param syncto_net_suite__ns: The syncto_net_suite__ns of this ProxyCreateRefund.  # noqa: E501
        :type: str
        """
        if syncto_net_suite__ns is not None and len(syncto_net_suite__ns) > 255:
            raise ValueError("Invalid value for `syncto_net_suite__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._syncto_net_suite__ns = syncto_net_suite__ns

    @property
    def account_id(self):
        """Gets the account_id of this ProxyCreateRefund.  # noqa: E501

         The ID of the account associated with this refund. This field is only required if you create a non-referenced refund. Don't specify a value for any other type of refund; Zuora associates the refund automatically with the account from the associated payment. **Character limit**: 32 **Values**: a valid account ID   # noqa: E501

        :return: The account_id of this ProxyCreateRefund.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ProxyCreateRefund.

         The ID of the account associated with this refund. This field is only required if you create a non-referenced refund. Don't specify a value for any other type of refund; Zuora associates the refund automatically with the account from the associated payment. **Character limit**: 32 **Values**: a valid account ID   # noqa: E501

        :param account_id: The account_id of this ProxyCreateRefund.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def amount(self):
        """Gets the amount of this ProxyCreateRefund.  # noqa: E501

         The amount of the refund. The amount can't exceed the amount of the associated payment. If the original payment was applied to a single invoice, then you can create a partial refund. However, if the payment was applies to multiple invoices, then you can only make a partial refund through the web-based UI, not through the API. **Character limit**: 16 **Values**: a valid currency amount   # noqa: E501

        :return: The amount of this ProxyCreateRefund.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ProxyCreateRefund.

         The amount of the refund. The amount can't exceed the amount of the associated payment. If the original payment was applied to a single invoice, then you can create a partial refund. However, if the payment was applies to multiple invoices, then you can only make a partial refund through the web-based UI, not through the API. **Character limit**: 16 **Values**: a valid currency amount   # noqa: E501

        :param amount: The amount of this ProxyCreateRefund.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def comment(self):
        """Gets the comment of this ProxyCreateRefund.  # noqa: E501

         Use this field to record comments about the refund. **Character limit**: 255 **Values**: a string of 255 characters or fewer   # noqa: E501

        :return: The comment of this ProxyCreateRefund.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this ProxyCreateRefund.

         Use this field to record comments about the refund. **Character limit**: 255 **Values**: a string of 255 characters or fewer   # noqa: E501

        :param comment: The comment of this ProxyCreateRefund.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def gateway_option_data(self):
        """Gets the gateway_option_data of this ProxyCreateRefund.  # noqa: E501


        :return: The gateway_option_data of this ProxyCreateRefund.  # noqa: E501
        :rtype: ProxyCreatePaymentGatewayOptionData
        """
        return self._gateway_option_data

    @gateway_option_data.setter
    def gateway_option_data(self, gateway_option_data):
        """Sets the gateway_option_data of this ProxyCreateRefund.


        :param gateway_option_data: The gateway_option_data of this ProxyCreateRefund.  # noqa: E501
        :type: ProxyCreatePaymentGatewayOptionData
        """

        self._gateway_option_data = gateway_option_data

    @property
    def gateway_state(self):
        """Gets the gateway_state of this ProxyCreateRefund.  # noqa: E501

         The status of the payment in the gateway. **Character limit**: 19 **Values**: automatically generated   # noqa: E501

        :return: The gateway_state of this ProxyCreateRefund.  # noqa: E501
        :rtype: str
        """
        return self._gateway_state

    @gateway_state.setter
    def gateway_state(self, gateway_state):
        """Sets the gateway_state of this ProxyCreateRefund.

         The status of the payment in the gateway. **Character limit**: 19 **Values**: automatically generated   # noqa: E501

        :param gateway_state: The gateway_state of this ProxyCreateRefund.  # noqa: E501
        :type: str
        """

        self._gateway_state = gateway_state

    @property
    def method_type(self):
        """Gets the method_type of this ProxyCreateRefund.  # noqa: E501

         Indicates how an external refund was issued to a customer. This field is only required if the `Type` field is set to ` External`. You can issue an external refund on an electronic payment. **Character limit**: 30 **Values**:  - `ACH` - `Cash` - `Check` - `CreditCard` - `Other` - `PayPal` - `WireTransfer` - `DebitCard` - `CreditCardReferenceTransaction`   # noqa: E501

        :return: The method_type of this ProxyCreateRefund.  # noqa: E501
        :rtype: str
        """
        return self._method_type

    @method_type.setter
    def method_type(self, method_type):
        """Sets the method_type of this ProxyCreateRefund.

         Indicates how an external refund was issued to a customer. This field is only required if the `Type` field is set to ` External`. You can issue an external refund on an electronic payment. **Character limit**: 30 **Values**:  - `ACH` - `Cash` - `Check` - `CreditCard` - `Other` - `PayPal` - `WireTransfer` - `DebitCard` - `CreditCardReferenceTransaction`   # noqa: E501

        :param method_type: The method_type of this ProxyCreateRefund.  # noqa: E501
        :type: str
        """

        self._method_type = method_type

    @property
    def payment_method_id(self):
        """Gets the payment_method_id of this ProxyCreateRefund.  # noqa: E501

         The unique ID of the payment method that the customer used to make the payment. This field is only required if you create a non-referenced refund. **Character limit**: 32 **V****alues**: a valid payment method ID   # noqa: E501

        :return: The payment_method_id of this ProxyCreateRefund.  # noqa: E501
        :rtype: str
        """
        return self._payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, payment_method_id):
        """Sets the payment_method_id of this ProxyCreateRefund.

         The unique ID of the payment method that the customer used to make the payment. This field is only required if you create a non-referenced refund. **Character limit**: 32 **V****alues**: a valid payment method ID   # noqa: E501

        :param payment_method_id: The payment_method_id of this ProxyCreateRefund.  # noqa: E501
        :type: str
        """

        self._payment_method_id = payment_method_id

    @property
    def reason_code(self):
        """Gets the reason_code of this ProxyCreateRefund.  # noqa: E501

         A code identifying the reason for the transaction. Must be an existing reason code or empty. If you do not specify a value, Zuora uses the default reason code. **Character limit**: 32 **V****alues**: a valid reason code   # noqa: E501

        :return: The reason_code of this ProxyCreateRefund.  # noqa: E501
        :rtype: str
        """
        return self._reason_code

    @reason_code.setter
    def reason_code(self, reason_code):
        """Sets the reason_code of this ProxyCreateRefund.

         A code identifying the reason for the transaction. Must be an existing reason code or empty. If you do not specify a value, Zuora uses the default reason code. **Character limit**: 32 **V****alues**: a valid reason code   # noqa: E501

        :param reason_code: The reason_code of this ProxyCreateRefund.  # noqa: E501
        :type: str
        """

        self._reason_code = reason_code

    @property
    def refund_date(self):
        """Gets the refund_date of this ProxyCreateRefund.  # noqa: E501

         The date of the refund, in `yyyy-mm-dd` format. The date of the refund cannot be before the payment date. This field is only required if the `Type` field is set to ` External`. Zuora automatically generates this field for electronic refunds. **Character limit**: 29   # noqa: E501

        :return: The refund_date of this ProxyCreateRefund.  # noqa: E501
        :rtype: date
        """
        return self._refund_date

    @refund_date.setter
    def refund_date(self, refund_date):
        """Sets the refund_date of this ProxyCreateRefund.

         The date of the refund, in `yyyy-mm-dd` format. The date of the refund cannot be before the payment date. This field is only required if the `Type` field is set to ` External`. Zuora automatically generates this field for electronic refunds. **Character limit**: 29   # noqa: E501

        :param refund_date: The refund_date of this ProxyCreateRefund.  # noqa: E501
        :type: date
        """

        self._refund_date = refund_date

    @property
    def refund_invoice_payment_data(self):
        """Gets the refund_invoice_payment_data of this ProxyCreateRefund.  # noqa: E501


        :return: The refund_invoice_payment_data of this ProxyCreateRefund.  # noqa: E501
        :rtype: ProxyCreateRefundRefundInvoicePaymentData
        """
        return self._refund_invoice_payment_data

    @refund_invoice_payment_data.setter
    def refund_invoice_payment_data(self, refund_invoice_payment_data):
        """Sets the refund_invoice_payment_data of this ProxyCreateRefund.


        :param refund_invoice_payment_data: The refund_invoice_payment_data of this ProxyCreateRefund.  # noqa: E501
        :type: ProxyCreateRefundRefundInvoicePaymentData
        """

        self._refund_invoice_payment_data = refund_invoice_payment_data

    @property
    def soft_descriptor(self):
        """Gets the soft_descriptor of this ProxyCreateRefund.  # noqa: E501

         A payment gateway-specific field that maps Zuora to other gateways . **Character limit**: 35 **Values**:  - 3-byte company identifier &quot;*&quot; 18-byte descriptor - 7-byte company identifier &quot;*&quot; 14-byte descriptor - 12-byte company identifier &quot;*&quot; 9-byte descriptor   # noqa: E501

        :return: The soft_descriptor of this ProxyCreateRefund.  # noqa: E501
        :rtype: str
        """
        return self._soft_descriptor

    @soft_descriptor.setter
    def soft_descriptor(self, soft_descriptor):
        """Sets the soft_descriptor of this ProxyCreateRefund.

         A payment gateway-specific field that maps Zuora to other gateways . **Character limit**: 35 **Values**:  - 3-byte company identifier &quot;*&quot; 18-byte descriptor - 7-byte company identifier &quot;*&quot; 14-byte descriptor - 12-byte company identifier &quot;*&quot; 9-byte descriptor   # noqa: E501

        :param soft_descriptor: The soft_descriptor of this ProxyCreateRefund.  # noqa: E501
        :type: str
        """

        self._soft_descriptor = soft_descriptor

    @property
    def soft_descriptor_phone(self):
        """Gets the soft_descriptor_phone of this ProxyCreateRefund.  # noqa: E501

         A payment gateway-specific field that maps Zuora to other gateways . **Character limit**: 20 **Values**:  - Customer service phone number formatted as: `NNN-NNN-NNNN` or `NNN-AAAAAAA` - URL (non-e-Commerce): Transactions sent with a URL do not qualify for the best interchange rate - Email address   # noqa: E501

        :return: The soft_descriptor_phone of this ProxyCreateRefund.  # noqa: E501
        :rtype: str
        """
        return self._soft_descriptor_phone

    @soft_descriptor_phone.setter
    def soft_descriptor_phone(self, soft_descriptor_phone):
        """Sets the soft_descriptor_phone of this ProxyCreateRefund.

         A payment gateway-specific field that maps Zuora to other gateways . **Character limit**: 20 **Values**:  - Customer service phone number formatted as: `NNN-NNN-NNNN` or `NNN-AAAAAAA` - URL (non-e-Commerce): Transactions sent with a URL do not qualify for the best interchange rate - Email address   # noqa: E501

        :param soft_descriptor_phone: The soft_descriptor_phone of this ProxyCreateRefund.  # noqa: E501
        :type: str
        """

        self._soft_descriptor_phone = soft_descriptor_phone

    @property
    def source_type(self):
        """Gets the source_type of this ProxyCreateRefund.  # noqa: E501

         Specifies whether the refund is a refund payment or a credit balance. This field is only required if you create a non-referenced refund. If you creating an non-referenced refund, then set this value to `CreditBalance`. **Character limit**: 13 **Values**:  - `Payment` - `CreditBalance`   # noqa: E501

        :return: The source_type of this ProxyCreateRefund.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this ProxyCreateRefund.

         Specifies whether the refund is a refund payment or a credit balance. This field is only required if you create a non-referenced refund. If you creating an non-referenced refund, then set this value to `CreditBalance`. **Character limit**: 13 **Values**:  - `Payment` - `CreditBalance`   # noqa: E501

        :param source_type: The source_type of this ProxyCreateRefund.  # noqa: E501
        :type: str
        """

        self._source_type = source_type

    @property
    def type(self):
        """Gets the type of this ProxyCreateRefund.  # noqa: E501

         Specifies if the refund is electronic or external. **Character limit**: 10 **Values**:  - `Electronic` - External   # noqa: E501

        :return: The type of this ProxyCreateRefund.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProxyCreateRefund.

         Specifies if the refund is electronic or external. **Character limit**: 10 **Values**:  - `Electronic` - External   # noqa: E501

        :param type: The type of this ProxyCreateRefund.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

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
        if issubclass(ProxyCreateRefund, dict):
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
        if not isinstance(other, ProxyCreateRefund):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
