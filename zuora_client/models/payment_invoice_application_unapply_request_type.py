# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.payment_invoice_application_item_unapply_request_type import PaymentInvoiceApplicationItemUnapplyRequestType  # noqa: F401,E501


class PaymentInvoiceApplicationUnapplyRequestType(object):
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
        'invoice_id': 'str',
        'items': 'list[PaymentInvoiceApplicationItemUnapplyRequestType]'
    }

    attribute_map = {
        'amount': 'amount',
        'invoice_id': 'invoiceId',
        'items': 'items'
    }

    def __init__(self, amount=None, invoice_id=None, items=None):  # noqa: E501
        """PaymentInvoiceApplicationUnapplyRequestType - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._invoice_id = None
        self._items = None
        self.discriminator = None

        self.amount = amount
        if invoice_id is not None:
            self.invoice_id = invoice_id
        if items is not None:
            self.items = items

    @property
    def amount(self):
        """Gets the amount of this PaymentInvoiceApplicationUnapplyRequestType.  # noqa: E501

        The amount of the payment that is unapplied from the invoice.   # noqa: E501

        :return: The amount of this PaymentInvoiceApplicationUnapplyRequestType.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PaymentInvoiceApplicationUnapplyRequestType.

        The amount of the payment that is unapplied from the invoice.   # noqa: E501

        :param amount: The amount of this PaymentInvoiceApplicationUnapplyRequestType.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def invoice_id(self):
        """Gets the invoice_id of this PaymentInvoiceApplicationUnapplyRequestType.  # noqa: E501

        The unique ID of the invoice that the payment is unapplied from.   # noqa: E501

        :return: The invoice_id of this PaymentInvoiceApplicationUnapplyRequestType.  # noqa: E501
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """Sets the invoice_id of this PaymentInvoiceApplicationUnapplyRequestType.

        The unique ID of the invoice that the payment is unapplied from.   # noqa: E501

        :param invoice_id: The invoice_id of this PaymentInvoiceApplicationUnapplyRequestType.  # noqa: E501
        :type: str
        """

        self._invoice_id = invoice_id

    @property
    def items(self):
        """Gets the items of this PaymentInvoiceApplicationUnapplyRequestType.  # noqa: E501

        Container for invoice items.  **Note:** The Invoice Item Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   # noqa: E501

        :return: The items of this PaymentInvoiceApplicationUnapplyRequestType.  # noqa: E501
        :rtype: list[PaymentInvoiceApplicationItemUnapplyRequestType]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this PaymentInvoiceApplicationUnapplyRequestType.

        Container for invoice items.  **Note:** The Invoice Item Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   # noqa: E501

        :param items: The items of this PaymentInvoiceApplicationUnapplyRequestType.  # noqa: E501
        :type: list[PaymentInvoiceApplicationItemUnapplyRequestType]
        """

        self._items = items

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
        if issubclass(PaymentInvoiceApplicationUnapplyRequestType, dict):
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
        if not isinstance(other, PaymentInvoiceApplicationUnapplyRequestType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
