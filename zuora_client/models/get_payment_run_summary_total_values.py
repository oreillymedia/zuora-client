# coding: utf-8




import pprint
import re  # noqa: F401

import six


class GETPaymentRunSummaryTotalValues(object):
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
        'total_value_of_credit_balance': 'str',
        'total_value_of_credit_memos': 'str',
        'total_value_of_debit_memos': 'str',
        'total_value_of_errors': 'str',
        'total_value_of_invoices': 'str',
        'total_value_of_payments': 'str',
        'total_value_of_receivables': 'str',
        'total_value_of_unapplied_payments': 'int',
        'total_value_of_unprocessed_debit_memos': 'str',
        'total_value_of_unprocessed_invoices': 'str',
        'total_value_of_unprocessed_receivables': 'str'
    }

    attribute_map = {
        'total_value_of_credit_balance': 'totalValueOfCreditBalance',
        'total_value_of_credit_memos': 'totalValueOfCreditMemos',
        'total_value_of_debit_memos': 'totalValueOfDebitMemos',
        'total_value_of_errors': 'totalValueOfErrors',
        'total_value_of_invoices': 'totalValueOfInvoices',
        'total_value_of_payments': 'totalValueOfPayments',
        'total_value_of_receivables': 'totalValueOfReceivables',
        'total_value_of_unapplied_payments': 'totalValueOfUnappliedPayments',
        'total_value_of_unprocessed_debit_memos': 'totalValueOfUnprocessedDebitMemos',
        'total_value_of_unprocessed_invoices': 'totalValueOfUnprocessedInvoices',
        'total_value_of_unprocessed_receivables': 'totalValueOfUnprocessedReceivables'
    }

    def __init__(self, total_value_of_credit_balance=None, total_value_of_credit_memos=None, total_value_of_debit_memos=None, total_value_of_errors=None, total_value_of_invoices=None, total_value_of_payments=None, total_value_of_receivables=None, total_value_of_unapplied_payments=None, total_value_of_unprocessed_debit_memos=None, total_value_of_unprocessed_invoices=None, total_value_of_unprocessed_receivables=None):  # noqa: E501
        """GETPaymentRunSummaryTotalValues - a model defined in Swagger"""  # noqa: E501

        self._total_value_of_credit_balance = None
        self._total_value_of_credit_memos = None
        self._total_value_of_debit_memos = None
        self._total_value_of_errors = None
        self._total_value_of_invoices = None
        self._total_value_of_payments = None
        self._total_value_of_receivables = None
        self._total_value_of_unapplied_payments = None
        self._total_value_of_unprocessed_debit_memos = None
        self._total_value_of_unprocessed_invoices = None
        self._total_value_of_unprocessed_receivables = None
        self.discriminator = None

        if total_value_of_credit_balance is not None:
            self.total_value_of_credit_balance = total_value_of_credit_balance
        if total_value_of_credit_memos is not None:
            self.total_value_of_credit_memos = total_value_of_credit_memos
        if total_value_of_debit_memos is not None:
            self.total_value_of_debit_memos = total_value_of_debit_memos
        if total_value_of_errors is not None:
            self.total_value_of_errors = total_value_of_errors
        if total_value_of_invoices is not None:
            self.total_value_of_invoices = total_value_of_invoices
        if total_value_of_payments is not None:
            self.total_value_of_payments = total_value_of_payments
        if total_value_of_receivables is not None:
            self.total_value_of_receivables = total_value_of_receivables
        if total_value_of_unapplied_payments is not None:
            self.total_value_of_unapplied_payments = total_value_of_unapplied_payments
        if total_value_of_unprocessed_debit_memos is not None:
            self.total_value_of_unprocessed_debit_memos = total_value_of_unprocessed_debit_memos
        if total_value_of_unprocessed_invoices is not None:
            self.total_value_of_unprocessed_invoices = total_value_of_unprocessed_invoices
        if total_value_of_unprocessed_receivables is not None:
            self.total_value_of_unprocessed_receivables = total_value_of_unprocessed_receivables

    @property
    def total_value_of_credit_balance(self):
        """Gets the total_value_of_credit_balance of this GETPaymentRunSummaryTotalValues.  # noqa: E501

        **Note:** This field is only available if you have the Credit Balance feature enabled.  The total amount of credit balance after the payment run is completed.   # noqa: E501

        :return: The total_value_of_credit_balance of this GETPaymentRunSummaryTotalValues.  # noqa: E501
        :rtype: str
        """
        return self._total_value_of_credit_balance

    @total_value_of_credit_balance.setter
    def total_value_of_credit_balance(self, total_value_of_credit_balance):
        """Sets the total_value_of_credit_balance of this GETPaymentRunSummaryTotalValues.

        **Note:** This field is only available if you have the Credit Balance feature enabled.  The total amount of credit balance after the payment run is completed.   # noqa: E501

        :param total_value_of_credit_balance: The total_value_of_credit_balance of this GETPaymentRunSummaryTotalValues.  # noqa: E501
        :type: str
        """

        self._total_value_of_credit_balance = total_value_of_credit_balance

    @property
    def total_value_of_credit_memos(self):
        """Gets the total_value_of_credit_memos of this GETPaymentRunSummaryTotalValues.  # noqa: E501

        **Note:** This field is only available if you have the Invoice Settlement feature enabled.  The total amount of credit memos that are successfully processed in the payment run.   # noqa: E501

        :return: The total_value_of_credit_memos of this GETPaymentRunSummaryTotalValues.  # noqa: E501
        :rtype: str
        """
        return self._total_value_of_credit_memos

    @total_value_of_credit_memos.setter
    def total_value_of_credit_memos(self, total_value_of_credit_memos):
        """Sets the total_value_of_credit_memos of this GETPaymentRunSummaryTotalValues.

        **Note:** This field is only available if you have the Invoice Settlement feature enabled.  The total amount of credit memos that are successfully processed in the payment run.   # noqa: E501

        :param total_value_of_credit_memos: The total_value_of_credit_memos of this GETPaymentRunSummaryTotalValues.  # noqa: E501
        :type: str
        """

        self._total_value_of_credit_memos = total_value_of_credit_memos

    @property
    def total_value_of_debit_memos(self):
        """Gets the total_value_of_debit_memos of this GETPaymentRunSummaryTotalValues.  # noqa: E501

        **Note:** This field is only available if you have the Invoice Settlement feature enabled.  The total amount of debit memos that are picked up for processing in the payment run.   # noqa: E501

        :return: The total_value_of_debit_memos of this GETPaymentRunSummaryTotalValues.  # noqa: E501
        :rtype: str
        """
        return self._total_value_of_debit_memos

    @total_value_of_debit_memos.setter
    def total_value_of_debit_memos(self, total_value_of_debit_memos):
        """Sets the total_value_of_debit_memos of this GETPaymentRunSummaryTotalValues.

        **Note:** This field is only available if you have the Invoice Settlement feature enabled.  The total amount of debit memos that are picked up for processing in the payment run.   # noqa: E501

        :param total_value_of_debit_memos: The total_value_of_debit_memos of this GETPaymentRunSummaryTotalValues.  # noqa: E501
        :type: str
        """

        self._total_value_of_debit_memos = total_value_of_debit_memos

    @property
    def total_value_of_errors(self):
        """Gets the total_value_of_errors of this GETPaymentRunSummaryTotalValues.  # noqa: E501

        The total amount of receivables associated with the payments with the status of `Error` and `Processing`.   # noqa: E501

        :return: The total_value_of_errors of this GETPaymentRunSummaryTotalValues.  # noqa: E501
        :rtype: str
        """
        return self._total_value_of_errors

    @total_value_of_errors.setter
    def total_value_of_errors(self, total_value_of_errors):
        """Sets the total_value_of_errors of this GETPaymentRunSummaryTotalValues.

        The total amount of receivables associated with the payments with the status of `Error` and `Processing`.   # noqa: E501

        :param total_value_of_errors: The total_value_of_errors of this GETPaymentRunSummaryTotalValues.  # noqa: E501
        :type: str
        """

        self._total_value_of_errors = total_value_of_errors

    @property
    def total_value_of_invoices(self):
        """Gets the total_value_of_invoices of this GETPaymentRunSummaryTotalValues.  # noqa: E501

        **Note:** This field is only available if you have the Invoice Settlement feature enabled.  The total amount of invoices that are picked up for processing in the payment run.   # noqa: E501

        :return: The total_value_of_invoices of this GETPaymentRunSummaryTotalValues.  # noqa: E501
        :rtype: str
        """
        return self._total_value_of_invoices

    @total_value_of_invoices.setter
    def total_value_of_invoices(self, total_value_of_invoices):
        """Sets the total_value_of_invoices of this GETPaymentRunSummaryTotalValues.

        **Note:** This field is only available if you have the Invoice Settlement feature enabled.  The total amount of invoices that are picked up for processing in the payment run.   # noqa: E501

        :param total_value_of_invoices: The total_value_of_invoices of this GETPaymentRunSummaryTotalValues.  # noqa: E501
        :type: str
        """

        self._total_value_of_invoices = total_value_of_invoices

    @property
    def total_value_of_payments(self):
        """Gets the total_value_of_payments of this GETPaymentRunSummaryTotalValues.  # noqa: E501

        The total amount of payments that are successfully processed in the payment run.   # noqa: E501

        :return: The total_value_of_payments of this GETPaymentRunSummaryTotalValues.  # noqa: E501
        :rtype: str
        """
        return self._total_value_of_payments

    @total_value_of_payments.setter
    def total_value_of_payments(self, total_value_of_payments):
        """Sets the total_value_of_payments of this GETPaymentRunSummaryTotalValues.

        The total amount of payments that are successfully processed in the payment run.   # noqa: E501

        :param total_value_of_payments: The total_value_of_payments of this GETPaymentRunSummaryTotalValues.  # noqa: E501
        :type: str
        """

        self._total_value_of_payments = total_value_of_payments

    @property
    def total_value_of_receivables(self):
        """Gets the total_value_of_receivables of this GETPaymentRunSummaryTotalValues.  # noqa: E501

        The total amount of receivables associated with the payment run.  The value of this field is the sum of the value of the `totalValueOfInvoices` field and that of the `totalValueOfDebitMemos` field.   # noqa: E501

        :return: The total_value_of_receivables of this GETPaymentRunSummaryTotalValues.  # noqa: E501
        :rtype: str
        """
        return self._total_value_of_receivables

    @total_value_of_receivables.setter
    def total_value_of_receivables(self, total_value_of_receivables):
        """Sets the total_value_of_receivables of this GETPaymentRunSummaryTotalValues.

        The total amount of receivables associated with the payment run.  The value of this field is the sum of the value of the `totalValueOfInvoices` field and that of the `totalValueOfDebitMemos` field.   # noqa: E501

        :param total_value_of_receivables: The total_value_of_receivables of this GETPaymentRunSummaryTotalValues.  # noqa: E501
        :type: str
        """

        self._total_value_of_receivables = total_value_of_receivables

    @property
    def total_value_of_unapplied_payments(self):
        """Gets the total_value_of_unapplied_payments of this GETPaymentRunSummaryTotalValues.  # noqa: E501

        **Note:** This field is only available if you have the Invoice Settlement feature enabled.  The total amount of unapplied payments that are successfully processed in the payment run.   # noqa: E501

        :return: The total_value_of_unapplied_payments of this GETPaymentRunSummaryTotalValues.  # noqa: E501
        :rtype: int
        """
        return self._total_value_of_unapplied_payments

    @total_value_of_unapplied_payments.setter
    def total_value_of_unapplied_payments(self, total_value_of_unapplied_payments):
        """Sets the total_value_of_unapplied_payments of this GETPaymentRunSummaryTotalValues.

        **Note:** This field is only available if you have the Invoice Settlement feature enabled.  The total amount of unapplied payments that are successfully processed in the payment run.   # noqa: E501

        :param total_value_of_unapplied_payments: The total_value_of_unapplied_payments of this GETPaymentRunSummaryTotalValues.  # noqa: E501
        :type: int
        """

        self._total_value_of_unapplied_payments = total_value_of_unapplied_payments

    @property
    def total_value_of_unprocessed_debit_memos(self):
        """Gets the total_value_of_unprocessed_debit_memos of this GETPaymentRunSummaryTotalValues.  # noqa: E501

        **Note:** This field is only available if you have the Invoice Settlement feature enabled.  The total amount of debit memos with remaining positive balances after the payment run is completed.  # noqa: E501

        :return: The total_value_of_unprocessed_debit_memos of this GETPaymentRunSummaryTotalValues.  # noqa: E501
        :rtype: str
        """
        return self._total_value_of_unprocessed_debit_memos

    @total_value_of_unprocessed_debit_memos.setter
    def total_value_of_unprocessed_debit_memos(self, total_value_of_unprocessed_debit_memos):
        """Sets the total_value_of_unprocessed_debit_memos of this GETPaymentRunSummaryTotalValues.

        **Note:** This field is only available if you have the Invoice Settlement feature enabled.  The total amount of debit memos with remaining positive balances after the payment run is completed.  # noqa: E501

        :param total_value_of_unprocessed_debit_memos: The total_value_of_unprocessed_debit_memos of this GETPaymentRunSummaryTotalValues.  # noqa: E501
        :type: str
        """

        self._total_value_of_unprocessed_debit_memos = total_value_of_unprocessed_debit_memos

    @property
    def total_value_of_unprocessed_invoices(self):
        """Gets the total_value_of_unprocessed_invoices of this GETPaymentRunSummaryTotalValues.  # noqa: E501

        **Note:** This field is only available if you have the Invoice Settlement feature enabled.  The total amount of invoices with remaining positive balances after the payment run is completed.   # noqa: E501

        :return: The total_value_of_unprocessed_invoices of this GETPaymentRunSummaryTotalValues.  # noqa: E501
        :rtype: str
        """
        return self._total_value_of_unprocessed_invoices

    @total_value_of_unprocessed_invoices.setter
    def total_value_of_unprocessed_invoices(self, total_value_of_unprocessed_invoices):
        """Sets the total_value_of_unprocessed_invoices of this GETPaymentRunSummaryTotalValues.

        **Note:** This field is only available if you have the Invoice Settlement feature enabled.  The total amount of invoices with remaining positive balances after the payment run is completed.   # noqa: E501

        :param total_value_of_unprocessed_invoices: The total_value_of_unprocessed_invoices of this GETPaymentRunSummaryTotalValues.  # noqa: E501
        :type: str
        """

        self._total_value_of_unprocessed_invoices = total_value_of_unprocessed_invoices

    @property
    def total_value_of_unprocessed_receivables(self):
        """Gets the total_value_of_unprocessed_receivables of this GETPaymentRunSummaryTotalValues.  # noqa: E501

        The total amount of receivables with remaining positive balances after the payment run is completed.   # noqa: E501

        :return: The total_value_of_unprocessed_receivables of this GETPaymentRunSummaryTotalValues.  # noqa: E501
        :rtype: str
        """
        return self._total_value_of_unprocessed_receivables

    @total_value_of_unprocessed_receivables.setter
    def total_value_of_unprocessed_receivables(self, total_value_of_unprocessed_receivables):
        """Sets the total_value_of_unprocessed_receivables of this GETPaymentRunSummaryTotalValues.

        The total amount of receivables with remaining positive balances after the payment run is completed.   # noqa: E501

        :param total_value_of_unprocessed_receivables: The total_value_of_unprocessed_receivables of this GETPaymentRunSummaryTotalValues.  # noqa: E501
        :type: str
        """

        self._total_value_of_unprocessed_receivables = total_value_of_unprocessed_receivables

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
        if issubclass(GETPaymentRunSummaryTotalValues, dict):
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
        if not isinstance(other, GETPaymentRunSummaryTotalValues):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
