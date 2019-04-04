# coding: utf-8




import pprint
import re  # noqa: F401

import six


class POSTAccountResponseType(object):
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
        'account_number': 'str',
        'bill_to_contact_id': 'str',
        'contracted_mrr': 'str',
        'credit_memo_id': 'str',
        'invoice_id': 'str',
        'paid_amount': 'str',
        'payment_id': 'str',
        'payment_method_id': 'str',
        'sold_to_contact_id': 'str',
        'subscription_id': 'str',
        'subscription_number': 'str',
        'success': 'bool',
        'total_contracted_value': 'str'
    }

    attribute_map = {
        'account_id': 'accountId',
        'account_number': 'accountNumber',
        'bill_to_contact_id': 'billToContactId',
        'contracted_mrr': 'contractedMrr',
        'credit_memo_id': 'creditMemoId',
        'invoice_id': 'invoiceId',
        'paid_amount': 'paidAmount',
        'payment_id': 'paymentId',
        'payment_method_id': 'paymentMethodId',
        'sold_to_contact_id': 'soldToContactId',
        'subscription_id': 'subscriptionId',
        'subscription_number': 'subscriptionNumber',
        'success': 'success',
        'total_contracted_value': 'totalContractedValue'
    }

    def __init__(self, account_id=None, account_number=None, bill_to_contact_id=None, contracted_mrr=None, credit_memo_id=None, invoice_id=None, paid_amount=None, payment_id=None, payment_method_id=None, sold_to_contact_id=None, subscription_id=None, subscription_number=None, success=None, total_contracted_value=None):  # noqa: E501
        """POSTAccountResponseType - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._account_number = None
        self._bill_to_contact_id = None
        self._contracted_mrr = None
        self._credit_memo_id = None
        self._invoice_id = None
        self._paid_amount = None
        self._payment_id = None
        self._payment_method_id = None
        self._sold_to_contact_id = None
        self._subscription_id = None
        self._subscription_number = None
        self._success = None
        self._total_contracted_value = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if account_number is not None:
            self.account_number = account_number
        if bill_to_contact_id is not None:
            self.bill_to_contact_id = bill_to_contact_id
        if contracted_mrr is not None:
            self.contracted_mrr = contracted_mrr
        if credit_memo_id is not None:
            self.credit_memo_id = credit_memo_id
        if invoice_id is not None:
            self.invoice_id = invoice_id
        if paid_amount is not None:
            self.paid_amount = paid_amount
        if payment_id is not None:
            self.payment_id = payment_id
        if payment_method_id is not None:
            self.payment_method_id = payment_method_id
        if sold_to_contact_id is not None:
            self.sold_to_contact_id = sold_to_contact_id
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if subscription_number is not None:
            self.subscription_number = subscription_number
        if success is not None:
            self.success = success
        if total_contracted_value is not None:
            self.total_contracted_value = total_contracted_value

    @property
    def account_id(self):
        """Gets the account_id of this POSTAccountResponseType.  # noqa: E501

        Auto-generated account ID.   # noqa: E501

        :return: The account_id of this POSTAccountResponseType.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this POSTAccountResponseType.

        Auto-generated account ID.   # noqa: E501

        :param account_id: The account_id of this POSTAccountResponseType.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def account_number(self):
        """Gets the account_number of this POSTAccountResponseType.  # noqa: E501

        Account number.   # noqa: E501

        :return: The account_number of this POSTAccountResponseType.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this POSTAccountResponseType.

        Account number.   # noqa: E501

        :param account_number: The account_number of this POSTAccountResponseType.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def bill_to_contact_id(self):
        """Gets the bill_to_contact_id of this POSTAccountResponseType.  # noqa: E501

        The ID of the bill-to contact.   # noqa: E501

        :return: The bill_to_contact_id of this POSTAccountResponseType.  # noqa: E501
        :rtype: str
        """
        return self._bill_to_contact_id

    @bill_to_contact_id.setter
    def bill_to_contact_id(self, bill_to_contact_id):
        """Sets the bill_to_contact_id of this POSTAccountResponseType.

        The ID of the bill-to contact.   # noqa: E501

        :param bill_to_contact_id: The bill_to_contact_id of this POSTAccountResponseType.  # noqa: E501
        :type: str
        """

        self._bill_to_contact_id = bill_to_contact_id

    @property
    def contracted_mrr(self):
        """Gets the contracted_mrr of this POSTAccountResponseType.  # noqa: E501

        Contracted monthly recurring revenue of the subscription.   # noqa: E501

        :return: The contracted_mrr of this POSTAccountResponseType.  # noqa: E501
        :rtype: str
        """
        return self._contracted_mrr

    @contracted_mrr.setter
    def contracted_mrr(self, contracted_mrr):
        """Sets the contracted_mrr of this POSTAccountResponseType.

        Contracted monthly recurring revenue of the subscription.   # noqa: E501

        :param contracted_mrr: The contracted_mrr of this POSTAccountResponseType.  # noqa: E501
        :type: str
        """

        self._contracted_mrr = contracted_mrr

    @property
    def credit_memo_id(self):
        """Gets the credit_memo_id of this POSTAccountResponseType.  # noqa: E501

        The credit memo ID, if a credit memo is generated during the subscription process.  **Note:** This field is only available if you have the Invoice Settlements feature enabled.   # noqa: E501

        :return: The credit_memo_id of this POSTAccountResponseType.  # noqa: E501
        :rtype: str
        """
        return self._credit_memo_id

    @credit_memo_id.setter
    def credit_memo_id(self, credit_memo_id):
        """Sets the credit_memo_id of this POSTAccountResponseType.

        The credit memo ID, if a credit memo is generated during the subscription process.  **Note:** This field is only available if you have the Invoice Settlements feature enabled.   # noqa: E501

        :param credit_memo_id: The credit_memo_id of this POSTAccountResponseType.  # noqa: E501
        :type: str
        """

        self._credit_memo_id = credit_memo_id

    @property
    def invoice_id(self):
        """Gets the invoice_id of this POSTAccountResponseType.  # noqa: E501

        ID of the invoice generated at account creation, if applicable.   # noqa: E501

        :return: The invoice_id of this POSTAccountResponseType.  # noqa: E501
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """Sets the invoice_id of this POSTAccountResponseType.

        ID of the invoice generated at account creation, if applicable.   # noqa: E501

        :param invoice_id: The invoice_id of this POSTAccountResponseType.  # noqa: E501
        :type: str
        """

        self._invoice_id = invoice_id

    @property
    def paid_amount(self):
        """Gets the paid_amount of this POSTAccountResponseType.  # noqa: E501

        Amount collected on the invoice generated at account creation, if applicable.   # noqa: E501

        :return: The paid_amount of this POSTAccountResponseType.  # noqa: E501
        :rtype: str
        """
        return self._paid_amount

    @paid_amount.setter
    def paid_amount(self, paid_amount):
        """Sets the paid_amount of this POSTAccountResponseType.

        Amount collected on the invoice generated at account creation, if applicable.   # noqa: E501

        :param paid_amount: The paid_amount of this POSTAccountResponseType.  # noqa: E501
        :type: str
        """

        self._paid_amount = paid_amount

    @property
    def payment_id(self):
        """Gets the payment_id of this POSTAccountResponseType.  # noqa: E501

        ID of the payment collected on the invoice generated at account creation, if applicable.   # noqa: E501

        :return: The payment_id of this POSTAccountResponseType.  # noqa: E501
        :rtype: str
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """Sets the payment_id of this POSTAccountResponseType.

        ID of the payment collected on the invoice generated at account creation, if applicable.   # noqa: E501

        :param payment_id: The payment_id of this POSTAccountResponseType.  # noqa: E501
        :type: str
        """

        self._payment_id = payment_id

    @property
    def payment_method_id(self):
        """Gets the payment_method_id of this POSTAccountResponseType.  # noqa: E501

        ID of the payment method that was set up at account creation, which automatically becomes the default payment method for this account.   # noqa: E501

        :return: The payment_method_id of this POSTAccountResponseType.  # noqa: E501
        :rtype: str
        """
        return self._payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, payment_method_id):
        """Sets the payment_method_id of this POSTAccountResponseType.

        ID of the payment method that was set up at account creation, which automatically becomes the default payment method for this account.   # noqa: E501

        :param payment_method_id: The payment_method_id of this POSTAccountResponseType.  # noqa: E501
        :type: str
        """

        self._payment_method_id = payment_method_id

    @property
    def sold_to_contact_id(self):
        """Gets the sold_to_contact_id of this POSTAccountResponseType.  # noqa: E501

        The ID of the sold-to contact.   # noqa: E501

        :return: The sold_to_contact_id of this POSTAccountResponseType.  # noqa: E501
        :rtype: str
        """
        return self._sold_to_contact_id

    @sold_to_contact_id.setter
    def sold_to_contact_id(self, sold_to_contact_id):
        """Sets the sold_to_contact_id of this POSTAccountResponseType.

        The ID of the sold-to contact.   # noqa: E501

        :param sold_to_contact_id: The sold_to_contact_id of this POSTAccountResponseType.  # noqa: E501
        :type: str
        """

        self._sold_to_contact_id = sold_to_contact_id

    @property
    def subscription_id(self):
        """Gets the subscription_id of this POSTAccountResponseType.  # noqa: E501

        ID of the subscription that was set up at account creation, if applicable.   # noqa: E501

        :return: The subscription_id of this POSTAccountResponseType.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this POSTAccountResponseType.

        ID of the subscription that was set up at account creation, if applicable.   # noqa: E501

        :param subscription_id: The subscription_id of this POSTAccountResponseType.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def subscription_number(self):
        """Gets the subscription_number of this POSTAccountResponseType.  # noqa: E501

        Number of the subscription that was set up at account creation, if applicable.   # noqa: E501

        :return: The subscription_number of this POSTAccountResponseType.  # noqa: E501
        :rtype: str
        """
        return self._subscription_number

    @subscription_number.setter
    def subscription_number(self, subscription_number):
        """Sets the subscription_number of this POSTAccountResponseType.

        Number of the subscription that was set up at account creation, if applicable.   # noqa: E501

        :param subscription_number: The subscription_number of this POSTAccountResponseType.  # noqa: E501
        :type: str
        """

        self._subscription_number = subscription_number

    @property
    def success(self):
        """Gets the success of this POSTAccountResponseType.  # noqa: E501

        Returns `true` if the request was processed successfully.   # noqa: E501

        :return: The success of this POSTAccountResponseType.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this POSTAccountResponseType.

        Returns `true` if the request was processed successfully.   # noqa: E501

        :param success: The success of this POSTAccountResponseType.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def total_contracted_value(self):
        """Gets the total_contracted_value of this POSTAccountResponseType.  # noqa: E501

        Total contracted value of the subscription.   # noqa: E501

        :return: The total_contracted_value of this POSTAccountResponseType.  # noqa: E501
        :rtype: str
        """
        return self._total_contracted_value

    @total_contracted_value.setter
    def total_contracted_value(self, total_contracted_value):
        """Sets the total_contracted_value of this POSTAccountResponseType.

        Total contracted value of the subscription.   # noqa: E501

        :param total_contracted_value: The total_contracted_value of this POSTAccountResponseType.  # noqa: E501
        :type: str
        """

        self._total_contracted_value = total_contracted_value

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
        if issubclass(POSTAccountResponseType, dict):
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
        if not isinstance(other, POSTAccountResponseType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
