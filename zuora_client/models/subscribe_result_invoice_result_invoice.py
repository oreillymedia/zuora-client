# coding: utf-8




import pprint
import re  # noqa: F401

import six


class SubscribeResultInvoiceResultInvoice(object):
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
        'id': 'str',
        'invoice_number': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'invoice_number': 'InvoiceNumber'
    }

    def __init__(self, id=None, invoice_number=None):  # noqa: E501
        """SubscribeResultInvoiceResultInvoice - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._invoice_number = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if invoice_number is not None:
            self.invoice_number = invoice_number

    @property
    def id(self):
        """Gets the id of this SubscribeResultInvoiceResultInvoice.  # noqa: E501

          # noqa: E501

        :return: The id of this SubscribeResultInvoiceResultInvoice.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscribeResultInvoiceResultInvoice.

          # noqa: E501

        :param id: The id of this SubscribeResultInvoiceResultInvoice.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def invoice_number(self):
        """Gets the invoice_number of this SubscribeResultInvoiceResultInvoice.  # noqa: E501

          # noqa: E501

        :return: The invoice_number of this SubscribeResultInvoiceResultInvoice.  # noqa: E501
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """Sets the invoice_number of this SubscribeResultInvoiceResultInvoice.

          # noqa: E501

        :param invoice_number: The invoice_number of this SubscribeResultInvoiceResultInvoice.  # noqa: E501
        :type: str
        """

        self._invoice_number = invoice_number

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
        if issubclass(SubscribeResultInvoiceResultInvoice, dict):
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
        if not isinstance(other, SubscribeResultInvoiceResultInvoice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
