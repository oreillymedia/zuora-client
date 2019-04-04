# coding: utf-8




import pprint
import re  # noqa: F401

import six


class PUTSubscriptionSuspendResponseType(object):
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
        'credit_memo_id': 'str',
        'invoice_id': 'str',
        'paid_amount': 'str',
        'payment_id': 'str',
        'resume_date': 'date',
        'subscription_id': 'str',
        'success': 'bool',
        'suspend_date': 'date',
        'term_end_date': 'date',
        'total_delta_tcv': 'str'
    }

    attribute_map = {
        'credit_memo_id': 'creditMemoId',
        'invoice_id': 'invoiceId',
        'paid_amount': 'paidAmount',
        'payment_id': 'paymentId',
        'resume_date': 'resumeDate',
        'subscription_id': 'subscriptionId',
        'success': 'success',
        'suspend_date': 'suspendDate',
        'term_end_date': 'termEndDate',
        'total_delta_tcv': 'totalDeltaTcv'
    }

    def __init__(self, credit_memo_id=None, invoice_id=None, paid_amount=None, payment_id=None, resume_date=None, subscription_id=None, success=None, suspend_date=None, term_end_date=None, total_delta_tcv=None):  # noqa: E501
        """PUTSubscriptionSuspendResponseType - a model defined in Swagger"""  # noqa: E501

        self._credit_memo_id = None
        self._invoice_id = None
        self._paid_amount = None
        self._payment_id = None
        self._resume_date = None
        self._subscription_id = None
        self._success = None
        self._suspend_date = None
        self._term_end_date = None
        self._total_delta_tcv = None
        self.discriminator = None

        if credit_memo_id is not None:
            self.credit_memo_id = credit_memo_id
        if invoice_id is not None:
            self.invoice_id = invoice_id
        if paid_amount is not None:
            self.paid_amount = paid_amount
        if payment_id is not None:
            self.payment_id = payment_id
        if resume_date is not None:
            self.resume_date = resume_date
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if success is not None:
            self.success = success
        if suspend_date is not None:
            self.suspend_date = suspend_date
        if term_end_date is not None:
            self.term_end_date = term_end_date
        if total_delta_tcv is not None:
            self.total_delta_tcv = total_delta_tcv

    @property
    def credit_memo_id(self):
        """Gets the credit_memo_id of this PUTSubscriptionSuspendResponseType.  # noqa: E501

        The credit memo ID, if a credit memo is generated during the subscription process.  **Note:** This field is only available if you have the Invoice Settlements feature enabled.   # noqa: E501

        :return: The credit_memo_id of this PUTSubscriptionSuspendResponseType.  # noqa: E501
        :rtype: str
        """
        return self._credit_memo_id

    @credit_memo_id.setter
    def credit_memo_id(self, credit_memo_id):
        """Sets the credit_memo_id of this PUTSubscriptionSuspendResponseType.

        The credit memo ID, if a credit memo is generated during the subscription process.  **Note:** This field is only available if you have the Invoice Settlements feature enabled.   # noqa: E501

        :param credit_memo_id: The credit_memo_id of this PUTSubscriptionSuspendResponseType.  # noqa: E501
        :type: str
        """

        self._credit_memo_id = credit_memo_id

    @property
    def invoice_id(self):
        """Gets the invoice_id of this PUTSubscriptionSuspendResponseType.  # noqa: E501

        Invoice ID, if an invoice is generated during the subscription process.   # noqa: E501

        :return: The invoice_id of this PUTSubscriptionSuspendResponseType.  # noqa: E501
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """Sets the invoice_id of this PUTSubscriptionSuspendResponseType.

        Invoice ID, if an invoice is generated during the subscription process.   # noqa: E501

        :param invoice_id: The invoice_id of this PUTSubscriptionSuspendResponseType.  # noqa: E501
        :type: str
        """

        self._invoice_id = invoice_id

    @property
    def paid_amount(self):
        """Gets the paid_amount of this PUTSubscriptionSuspendResponseType.  # noqa: E501

        Payment amount, if a payment is collected.   # noqa: E501

        :return: The paid_amount of this PUTSubscriptionSuspendResponseType.  # noqa: E501
        :rtype: str
        """
        return self._paid_amount

    @paid_amount.setter
    def paid_amount(self, paid_amount):
        """Sets the paid_amount of this PUTSubscriptionSuspendResponseType.

        Payment amount, if a payment is collected.   # noqa: E501

        :param paid_amount: The paid_amount of this PUTSubscriptionSuspendResponseType.  # noqa: E501
        :type: str
        """

        self._paid_amount = paid_amount

    @property
    def payment_id(self):
        """Gets the payment_id of this PUTSubscriptionSuspendResponseType.  # noqa: E501

        Payment ID, if a payment is collected.   # noqa: E501

        :return: The payment_id of this PUTSubscriptionSuspendResponseType.  # noqa: E501
        :rtype: str
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """Sets the payment_id of this PUTSubscriptionSuspendResponseType.

        Payment ID, if a payment is collected.   # noqa: E501

        :param payment_id: The payment_id of this PUTSubscriptionSuspendResponseType.  # noqa: E501
        :type: str
        """

        self._payment_id = payment_id

    @property
    def resume_date(self):
        """Gets the resume_date of this PUTSubscriptionSuspendResponseType.  # noqa: E501

        The date when subscription resumption takes effect, in the format yyyy-mm-dd.   # noqa: E501

        :return: The resume_date of this PUTSubscriptionSuspendResponseType.  # noqa: E501
        :rtype: date
        """
        return self._resume_date

    @resume_date.setter
    def resume_date(self, resume_date):
        """Sets the resume_date of this PUTSubscriptionSuspendResponseType.

        The date when subscription resumption takes effect, in the format yyyy-mm-dd.   # noqa: E501

        :param resume_date: The resume_date of this PUTSubscriptionSuspendResponseType.  # noqa: E501
        :type: date
        """

        self._resume_date = resume_date

    @property
    def subscription_id(self):
        """Gets the subscription_id of this PUTSubscriptionSuspendResponseType.  # noqa: E501

        The subscription ID.   # noqa: E501

        :return: The subscription_id of this PUTSubscriptionSuspendResponseType.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this PUTSubscriptionSuspendResponseType.

        The subscription ID.   # noqa: E501

        :param subscription_id: The subscription_id of this PUTSubscriptionSuspendResponseType.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def success(self):
        """Gets the success of this PUTSubscriptionSuspendResponseType.  # noqa: E501

        Returns `true` if the request was processed successfully.   # noqa: E501

        :return: The success of this PUTSubscriptionSuspendResponseType.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this PUTSubscriptionSuspendResponseType.

        Returns `true` if the request was processed successfully.   # noqa: E501

        :param success: The success of this PUTSubscriptionSuspendResponseType.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def suspend_date(self):
        """Gets the suspend_date of this PUTSubscriptionSuspendResponseType.  # noqa: E501

        The date when subscription suspension takes effect, in the format yyyy-mm-dd.   # noqa: E501

        :return: The suspend_date of this PUTSubscriptionSuspendResponseType.  # noqa: E501
        :rtype: date
        """
        return self._suspend_date

    @suspend_date.setter
    def suspend_date(self, suspend_date):
        """Sets the suspend_date of this PUTSubscriptionSuspendResponseType.

        The date when subscription suspension takes effect, in the format yyyy-mm-dd.   # noqa: E501

        :param suspend_date: The suspend_date of this PUTSubscriptionSuspendResponseType.  # noqa: E501
        :type: date
        """

        self._suspend_date = suspend_date

    @property
    def term_end_date(self):
        """Gets the term_end_date of this PUTSubscriptionSuspendResponseType.  # noqa: E501

        The date when the new subscription term ends, in the format yyyy-mm-dd.   # noqa: E501

        :return: The term_end_date of this PUTSubscriptionSuspendResponseType.  # noqa: E501
        :rtype: date
        """
        return self._term_end_date

    @term_end_date.setter
    def term_end_date(self, term_end_date):
        """Sets the term_end_date of this PUTSubscriptionSuspendResponseType.

        The date when the new subscription term ends, in the format yyyy-mm-dd.   # noqa: E501

        :param term_end_date: The term_end_date of this PUTSubscriptionSuspendResponseType.  # noqa: E501
        :type: date
        """

        self._term_end_date = term_end_date

    @property
    def total_delta_tcv(self):
        """Gets the total_delta_tcv of this PUTSubscriptionSuspendResponseType.  # noqa: E501

        Change in the total contracted value of the subscription as a result of the update.   # noqa: E501

        :return: The total_delta_tcv of this PUTSubscriptionSuspendResponseType.  # noqa: E501
        :rtype: str
        """
        return self._total_delta_tcv

    @total_delta_tcv.setter
    def total_delta_tcv(self, total_delta_tcv):
        """Sets the total_delta_tcv of this PUTSubscriptionSuspendResponseType.

        Change in the total contracted value of the subscription as a result of the update.   # noqa: E501

        :param total_delta_tcv: The total_delta_tcv of this PUTSubscriptionSuspendResponseType.  # noqa: E501
        :type: str
        """

        self._total_delta_tcv = total_delta_tcv

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
        if issubclass(PUTSubscriptionSuspendResponseType, dict):
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
        if not isinstance(other, PUTSubscriptionSuspendResponseType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
