# coding: utf-8




import pprint
import re  # noqa: F401

import six


class ProxyGetInvoicePayment(object):
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
        'created_by_id': 'str',
        'created_date': 'datetime',
        'id': 'str',
        'invoice_id': 'str',
        'payment_id': 'str',
        'refund_amount': 'float',
        'updated_by_id': 'str',
        'updated_date': 'datetime'
    }

    attribute_map = {
        'amount': 'Amount',
        'created_by_id': 'CreatedById',
        'created_date': 'CreatedDate',
        'id': 'Id',
        'invoice_id': 'InvoiceId',
        'payment_id': 'PaymentId',
        'refund_amount': 'RefundAmount',
        'updated_by_id': 'UpdatedById',
        'updated_date': 'UpdatedDate'
    }

    def __init__(self, amount=None, created_by_id=None, created_date=None, id=None, invoice_id=None, payment_id=None, refund_amount=None, updated_by_id=None, updated_date=None):  # noqa: E501
        """ProxyGetInvoicePayment - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._created_by_id = None
        self._created_date = None
        self._id = None
        self._invoice_id = None
        self._payment_id = None
        self._refund_amount = None
        self._updated_by_id = None
        self._updated_date = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_date is not None:
            self.created_date = created_date
        if id is not None:
            self.id = id
        if invoice_id is not None:
            self.invoice_id = invoice_id
        if payment_id is not None:
            self.payment_id = payment_id
        if refund_amount is not None:
            self.refund_amount = refund_amount
        if updated_by_id is not None:
            self.updated_by_id = updated_by_id
        if updated_date is not None:
            self.updated_date = updated_date

    @property
    def amount(self):
        """Gets the amount of this ProxyGetInvoicePayment.  # noqa: E501

         The amount of the payment. **Character limit**: 16 **Values**: a valid currency amount   # noqa: E501

        :return: The amount of this ProxyGetInvoicePayment.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ProxyGetInvoicePayment.

         The amount of the payment. **Character limit**: 16 **Values**: a valid currency amount   # noqa: E501

        :param amount: The amount of this ProxyGetInvoicePayment.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def created_by_id(self):
        """Gets the created_by_id of this ProxyGetInvoicePayment.  # noqa: E501

         The user ID of the person who created the invoice payment. **Character limit**: 32 **V****alues**: automatically generated   # noqa: E501

        :return: The created_by_id of this ProxyGetInvoicePayment.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this ProxyGetInvoicePayment.

         The user ID of the person who created the invoice payment. **Character limit**: 32 **V****alues**: automatically generated   # noqa: E501

        :param created_by_id: The created_by_id of this ProxyGetInvoicePayment.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def created_date(self):
        """Gets the created_date of this ProxyGetInvoicePayment.  # noqa: E501

         The date when the invoice payment was generated. **Character limit**: 29 **V****alues**: automatically generated   # noqa: E501

        :return: The created_date of this ProxyGetInvoicePayment.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this ProxyGetInvoicePayment.

         The date when the invoice payment was generated. **Character limit**: 29 **V****alues**: automatically generated   # noqa: E501

        :param created_date: The created_date of this ProxyGetInvoicePayment.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def id(self):
        """Gets the id of this ProxyGetInvoicePayment.  # noqa: E501

        Object identifier.  # noqa: E501

        :return: The id of this ProxyGetInvoicePayment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProxyGetInvoicePayment.

        Object identifier.  # noqa: E501

        :param id: The id of this ProxyGetInvoicePayment.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def invoice_id(self):
        """Gets the invoice_id of this ProxyGetInvoicePayment.  # noqa: E501

         The unique ID of the invoice associated with this invoice payment. **Character limit**: 32 **Values**: a valid invoice ID   # noqa: E501

        :return: The invoice_id of this ProxyGetInvoicePayment.  # noqa: E501
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """Sets the invoice_id of this ProxyGetInvoicePayment.

         The unique ID of the invoice associated with this invoice payment. **Character limit**: 32 **Values**: a valid invoice ID   # noqa: E501

        :param invoice_id: The invoice_id of this ProxyGetInvoicePayment.  # noqa: E501
        :type: str
        """

        self._invoice_id = invoice_id

    @property
    def payment_id(self):
        """Gets the payment_id of this ProxyGetInvoicePayment.  # noqa: E501

         The unique ID of the payment associated with this invoice payment. **Character limit**: 32 **V****alues**: a valid payment ID   # noqa: E501

        :return: The payment_id of this ProxyGetInvoicePayment.  # noqa: E501
        :rtype: str
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """Sets the payment_id of this ProxyGetInvoicePayment.

         The unique ID of the payment associated with this invoice payment. **Character limit**: 32 **V****alues**: a valid payment ID   # noqa: E501

        :param payment_id: The payment_id of this ProxyGetInvoicePayment.  # noqa: E501
        :type: str
        """

        self._payment_id = payment_id

    @property
    def refund_amount(self):
        """Gets the refund_amount of this ProxyGetInvoicePayment.  # noqa: E501

        Specifies the amount of a refund applied against this InvoicePayment. **Character limit**: 16 **Values**: automatically generated   # noqa: E501

        :return: The refund_amount of this ProxyGetInvoicePayment.  # noqa: E501
        :rtype: float
        """
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, refund_amount):
        """Sets the refund_amount of this ProxyGetInvoicePayment.

        Specifies the amount of a refund applied against this InvoicePayment. **Character limit**: 16 **Values**: automatically generated   # noqa: E501

        :param refund_amount: The refund_amount of this ProxyGetInvoicePayment.  # noqa: E501
        :type: float
        """

        self._refund_amount = refund_amount

    @property
    def updated_by_id(self):
        """Gets the updated_by_id of this ProxyGetInvoicePayment.  # noqa: E501

         The ID of the user who last updated the invoice payment. **Character limit**: 32 **V****alues**: automatically generated   # noqa: E501

        :return: The updated_by_id of this ProxyGetInvoicePayment.  # noqa: E501
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """Sets the updated_by_id of this ProxyGetInvoicePayment.

         The ID of the user who last updated the invoice payment. **Character limit**: 32 **V****alues**: automatically generated   # noqa: E501

        :param updated_by_id: The updated_by_id of this ProxyGetInvoicePayment.  # noqa: E501
        :type: str
        """

        self._updated_by_id = updated_by_id

    @property
    def updated_date(self):
        """Gets the updated_date of this ProxyGetInvoicePayment.  # noqa: E501

         The date when the invoice payment was last updated. **Character limit**: 29 **V****alues**: automatically generated   # noqa: E501

        :return: The updated_date of this ProxyGetInvoicePayment.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this ProxyGetInvoicePayment.

         The date when the invoice payment was last updated. **Character limit**: 29 **V****alues**: automatically generated   # noqa: E501

        :param updated_date: The updated_date of this ProxyGetInvoicePayment.  # noqa: E501
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
        if issubclass(ProxyGetInvoicePayment, dict):
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
        if not isinstance(other, ProxyGetInvoicePayment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
