# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.credit_memo_item_from_write_off_invoice_finance_information import CreditMemoItemFromWriteOffInvoiceFinanceInformation  # noqa: F401,E501
from zuora_client.models.credit_memo_item_object_custom_fields import CreditMemoItemObjectCustomFields  # noqa: F401,E501


class CreditMemoItemFromWriteOffInvoice(object):
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
        'comment': 'str',
        'finance_information': 'CreditMemoItemFromWriteOffInvoiceFinanceInformation',
        'invoice_item_id': 'str',
        'service_end_date': 'date',
        'service_start_date': 'date',
        'sku_name': 'str',
        'unit_of_measure': 'str'
    }

    attribute_map = {
        'comment': 'comment',
        'finance_information': 'financeInformation',
        'invoice_item_id': 'invoiceItemId',
        'service_end_date': 'serviceEndDate',
        'service_start_date': 'serviceStartDate',
        'sku_name': 'skuName',
        'unit_of_measure': 'unitOfMeasure'
    }

    def __init__(self, comment=None, finance_information=None, invoice_item_id=None, service_end_date=None, service_start_date=None, sku_name=None, unit_of_measure=None):  # noqa: E501
        """CreditMemoItemFromWriteOffInvoice - a model defined in Swagger"""  # noqa: E501

        self._comment = None
        self._finance_information = None
        self._invoice_item_id = None
        self._service_end_date = None
        self._service_start_date = None
        self._sku_name = None
        self._unit_of_measure = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        if finance_information is not None:
            self.finance_information = finance_information
        if invoice_item_id is not None:
            self.invoice_item_id = invoice_item_id
        if service_end_date is not None:
            self.service_end_date = service_end_date
        if service_start_date is not None:
            self.service_start_date = service_start_date
        if sku_name is not None:
            self.sku_name = sku_name
        if unit_of_measure is not None:
            self.unit_of_measure = unit_of_measure

    @property
    def comment(self):
        """Gets the comment of this CreditMemoItemFromWriteOffInvoice.  # noqa: E501

        Comments about the credit memo item.   # noqa: E501

        :return: The comment of this CreditMemoItemFromWriteOffInvoice.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this CreditMemoItemFromWriteOffInvoice.

        Comments about the credit memo item.   # noqa: E501

        :param comment: The comment of this CreditMemoItemFromWriteOffInvoice.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def finance_information(self):
        """Gets the finance_information of this CreditMemoItemFromWriteOffInvoice.  # noqa: E501


        :return: The finance_information of this CreditMemoItemFromWriteOffInvoice.  # noqa: E501
        :rtype: CreditMemoItemFromWriteOffInvoiceFinanceInformation
        """
        return self._finance_information

    @finance_information.setter
    def finance_information(self, finance_information):
        """Sets the finance_information of this CreditMemoItemFromWriteOffInvoice.


        :param finance_information: The finance_information of this CreditMemoItemFromWriteOffInvoice.  # noqa: E501
        :type: CreditMemoItemFromWriteOffInvoiceFinanceInformation
        """

        self._finance_information = finance_information

    @property
    def invoice_item_id(self):
        """Gets the invoice_item_id of this CreditMemoItemFromWriteOffInvoice.  # noqa: E501

        The ID of the invoice item.   # noqa: E501

        :return: The invoice_item_id of this CreditMemoItemFromWriteOffInvoice.  # noqa: E501
        :rtype: str
        """
        return self._invoice_item_id

    @invoice_item_id.setter
    def invoice_item_id(self, invoice_item_id):
        """Sets the invoice_item_id of this CreditMemoItemFromWriteOffInvoice.

        The ID of the invoice item.   # noqa: E501

        :param invoice_item_id: The invoice_item_id of this CreditMemoItemFromWriteOffInvoice.  # noqa: E501
        :type: str
        """

        self._invoice_item_id = invoice_item_id

    @property
    def service_end_date(self):
        """Gets the service_end_date of this CreditMemoItemFromWriteOffInvoice.  # noqa: E501

        The service end date of the credit memo item.    # noqa: E501

        :return: The service_end_date of this CreditMemoItemFromWriteOffInvoice.  # noqa: E501
        :rtype: date
        """
        return self._service_end_date

    @service_end_date.setter
    def service_end_date(self, service_end_date):
        """Sets the service_end_date of this CreditMemoItemFromWriteOffInvoice.

        The service end date of the credit memo item.    # noqa: E501

        :param service_end_date: The service_end_date of this CreditMemoItemFromWriteOffInvoice.  # noqa: E501
        :type: date
        """

        self._service_end_date = service_end_date

    @property
    def service_start_date(self):
        """Gets the service_start_date of this CreditMemoItemFromWriteOffInvoice.  # noqa: E501

        The service start date of the credit memo item.    # noqa: E501

        :return: The service_start_date of this CreditMemoItemFromWriteOffInvoice.  # noqa: E501
        :rtype: date
        """
        return self._service_start_date

    @service_start_date.setter
    def service_start_date(self, service_start_date):
        """Sets the service_start_date of this CreditMemoItemFromWriteOffInvoice.

        The service start date of the credit memo item.    # noqa: E501

        :param service_start_date: The service_start_date of this CreditMemoItemFromWriteOffInvoice.  # noqa: E501
        :type: date
        """

        self._service_start_date = service_start_date

    @property
    def sku_name(self):
        """Gets the sku_name of this CreditMemoItemFromWriteOffInvoice.  # noqa: E501

        The name of the SKU.   # noqa: E501

        :return: The sku_name of this CreditMemoItemFromWriteOffInvoice.  # noqa: E501
        :rtype: str
        """
        return self._sku_name

    @sku_name.setter
    def sku_name(self, sku_name):
        """Sets the sku_name of this CreditMemoItemFromWriteOffInvoice.

        The name of the SKU.   # noqa: E501

        :param sku_name: The sku_name of this CreditMemoItemFromWriteOffInvoice.  # noqa: E501
        :type: str
        """

        self._sku_name = sku_name

    @property
    def unit_of_measure(self):
        """Gets the unit_of_measure of this CreditMemoItemFromWriteOffInvoice.  # noqa: E501

        The definable unit that you measure when determining charges.   # noqa: E501

        :return: The unit_of_measure of this CreditMemoItemFromWriteOffInvoice.  # noqa: E501
        :rtype: str
        """
        return self._unit_of_measure

    @unit_of_measure.setter
    def unit_of_measure(self, unit_of_measure):
        """Sets the unit_of_measure of this CreditMemoItemFromWriteOffInvoice.

        The definable unit that you measure when determining charges.   # noqa: E501

        :param unit_of_measure: The unit_of_measure of this CreditMemoItemFromWriteOffInvoice.  # noqa: E501
        :type: str
        """

        self._unit_of_measure = unit_of_measure

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
        if issubclass(CreditMemoItemFromWriteOffInvoice, dict):
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
        if not isinstance(other, CreditMemoItemFromWriteOffInvoice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
