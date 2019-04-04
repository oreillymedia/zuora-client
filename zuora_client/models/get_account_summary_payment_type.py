# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.get_account_summary_payment_invoice_type import GETAccountSummaryPaymentInvoiceType  # noqa: F401,E501


class GETAccountSummaryPaymentType(object):
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
        'effective_date': 'date',
        'id': 'str',
        'paid_invoices': 'list[GETAccountSummaryPaymentInvoiceType]',
        'payment_number': 'str',
        'payment_type': 'str',
        'status': 'str'
    }

    attribute_map = {
        'effective_date': 'effectiveDate',
        'id': 'id',
        'paid_invoices': 'paidInvoices',
        'payment_number': 'paymentNumber',
        'payment_type': 'paymentType',
        'status': 'status'
    }

    def __init__(self, effective_date=None, id=None, paid_invoices=None, payment_number=None, payment_type=None, status=None):  # noqa: E501
        """GETAccountSummaryPaymentType - a model defined in Swagger"""  # noqa: E501

        self._effective_date = None
        self._id = None
        self._paid_invoices = None
        self._payment_number = None
        self._payment_type = None
        self._status = None
        self.discriminator = None

        if effective_date is not None:
            self.effective_date = effective_date
        if id is not None:
            self.id = id
        if paid_invoices is not None:
            self.paid_invoices = paid_invoices
        if payment_number is not None:
            self.payment_number = payment_number
        if payment_type is not None:
            self.payment_type = payment_type
        if status is not None:
            self.status = status

    @property
    def effective_date(self):
        """Gets the effective_date of this GETAccountSummaryPaymentType.  # noqa: E501

        Effective date as `yyyy-mm-dd`.   # noqa: E501

        :return: The effective_date of this GETAccountSummaryPaymentType.  # noqa: E501
        :rtype: date
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this GETAccountSummaryPaymentType.

        Effective date as `yyyy-mm-dd`.   # noqa: E501

        :param effective_date: The effective_date of this GETAccountSummaryPaymentType.  # noqa: E501
        :type: date
        """

        self._effective_date = effective_date

    @property
    def id(self):
        """Gets the id of this GETAccountSummaryPaymentType.  # noqa: E501

        Payment ID.   # noqa: E501

        :return: The id of this GETAccountSummaryPaymentType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GETAccountSummaryPaymentType.

        Payment ID.   # noqa: E501

        :param id: The id of this GETAccountSummaryPaymentType.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def paid_invoices(self):
        """Gets the paid_invoices of this GETAccountSummaryPaymentType.  # noqa: E501

        Container for paid invoices for this subscription.   # noqa: E501

        :return: The paid_invoices of this GETAccountSummaryPaymentType.  # noqa: E501
        :rtype: list[GETAccountSummaryPaymentInvoiceType]
        """
        return self._paid_invoices

    @paid_invoices.setter
    def paid_invoices(self, paid_invoices):
        """Sets the paid_invoices of this GETAccountSummaryPaymentType.

        Container for paid invoices for this subscription.   # noqa: E501

        :param paid_invoices: The paid_invoices of this GETAccountSummaryPaymentType.  # noqa: E501
        :type: list[GETAccountSummaryPaymentInvoiceType]
        """

        self._paid_invoices = paid_invoices

    @property
    def payment_number(self):
        """Gets the payment_number of this GETAccountSummaryPaymentType.  # noqa: E501

        Payment number.   # noqa: E501

        :return: The payment_number of this GETAccountSummaryPaymentType.  # noqa: E501
        :rtype: str
        """
        return self._payment_number

    @payment_number.setter
    def payment_number(self, payment_number):
        """Sets the payment_number of this GETAccountSummaryPaymentType.

        Payment number.   # noqa: E501

        :param payment_number: The payment_number of this GETAccountSummaryPaymentType.  # noqa: E501
        :type: str
        """

        self._payment_number = payment_number

    @property
    def payment_type(self):
        """Gets the payment_type of this GETAccountSummaryPaymentType.  # noqa: E501

        Payment type; possible values are: `External`, `Electronic`.   # noqa: E501

        :return: The payment_type of this GETAccountSummaryPaymentType.  # noqa: E501
        :rtype: str
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """Sets the payment_type of this GETAccountSummaryPaymentType.

        Payment type; possible values are: `External`, `Electronic`.   # noqa: E501

        :param payment_type: The payment_type of this GETAccountSummaryPaymentType.  # noqa: E501
        :type: str
        """

        self._payment_type = payment_type

    @property
    def status(self):
        """Gets the status of this GETAccountSummaryPaymentType.  # noqa: E501

        Payment status. Possible values are: `Draft`, `Processing`, `Processed`, `Error`, `Voided`, `Canceled`, `Posted`.   # noqa: E501

        :return: The status of this GETAccountSummaryPaymentType.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GETAccountSummaryPaymentType.

        Payment status. Possible values are: `Draft`, `Processing`, `Processed`, `Error`, `Voided`, `Canceled`, `Posted`.   # noqa: E501

        :param status: The status of this GETAccountSummaryPaymentType.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(GETAccountSummaryPaymentType, dict):
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
        if not isinstance(other, GETAccountSummaryPaymentType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
