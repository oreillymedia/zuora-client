# coding: utf-8




import pprint
import re  # noqa: F401

import six


class ProxyGetInvoiceSplitItem(object):
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
        'created_by_id': 'str',
        'created_date': 'datetime',
        'id': 'str',
        'invoice_date': 'date',
        'invoice_id': 'str',
        'invoice_split_id': 'str',
        'payment_term': 'str',
        'split_percentage': 'float',
        'updated_by_id': 'str',
        'updated_date': 'datetime'
    }

    attribute_map = {
        'created_by_id': 'CreatedById',
        'created_date': 'CreatedDate',
        'id': 'Id',
        'invoice_date': 'InvoiceDate',
        'invoice_id': 'InvoiceId',
        'invoice_split_id': 'InvoiceSplitId',
        'payment_term': 'PaymentTerm',
        'split_percentage': 'SplitPercentage',
        'updated_by_id': 'UpdatedById',
        'updated_date': 'UpdatedDate'
    }

    def __init__(self, created_by_id=None, created_date=None, id=None, invoice_date=None, invoice_id=None, invoice_split_id=None, payment_term=None, split_percentage=None, updated_by_id=None, updated_date=None):  # noqa: E501
        """ProxyGetInvoiceSplitItem - a model defined in Swagger"""  # noqa: E501

        self._created_by_id = None
        self._created_date = None
        self._id = None
        self._invoice_date = None
        self._invoice_id = None
        self._invoice_split_id = None
        self._payment_term = None
        self._split_percentage = None
        self._updated_by_id = None
        self._updated_date = None
        self.discriminator = None

        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_date is not None:
            self.created_date = created_date
        if id is not None:
            self.id = id
        if invoice_date is not None:
            self.invoice_date = invoice_date
        if invoice_id is not None:
            self.invoice_id = invoice_id
        if invoice_split_id is not None:
            self.invoice_split_id = invoice_split_id
        if payment_term is not None:
            self.payment_term = payment_term
        if split_percentage is not None:
            self.split_percentage = split_percentage
        if updated_by_id is not None:
            self.updated_by_id = updated_by_id
        if updated_date is not None:
            self.updated_date = updated_date

    @property
    def created_by_id(self):
        """Gets the created_by_id of this ProxyGetInvoiceSplitItem.  # noqa: E501

         The ID of the Zuora user who created the InvoiceSplitItem object. **Character limit**: 32 **Values**: automatically generated   # noqa: E501

        :return: The created_by_id of this ProxyGetInvoiceSplitItem.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this ProxyGetInvoiceSplitItem.

         The ID of the Zuora user who created the InvoiceSplitItem object. **Character limit**: 32 **Values**: automatically generated   # noqa: E501

        :param created_by_id: The created_by_id of this ProxyGetInvoiceSplitItem.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def created_date(self):
        """Gets the created_date of this ProxyGetInvoiceSplitItem.  # noqa: E501

         The date when the InvoiceSplitItem was created. **Values**: automatically generated   # noqa: E501

        :return: The created_date of this ProxyGetInvoiceSplitItem.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this ProxyGetInvoiceSplitItem.

         The date when the InvoiceSplitItem was created. **Values**: automatically generated   # noqa: E501

        :param created_date: The created_date of this ProxyGetInvoiceSplitItem.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def id(self):
        """Gets the id of this ProxyGetInvoiceSplitItem.  # noqa: E501

        Object identifier.  # noqa: E501

        :return: The id of this ProxyGetInvoiceSplitItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProxyGetInvoiceSplitItem.

        Object identifier.  # noqa: E501

        :param id: The id of this ProxyGetInvoiceSplitItem.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def invoice_date(self):
        """Gets the invoice_date of this ProxyGetInvoiceSplitItem.  # noqa: E501

         The generation date of the new split invoice, in `yyyy-mm-dd` format. **Character limit**: 29   # noqa: E501

        :return: The invoice_date of this ProxyGetInvoiceSplitItem.  # noqa: E501
        :rtype: date
        """
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, invoice_date):
        """Sets the invoice_date of this ProxyGetInvoiceSplitItem.

         The generation date of the new split invoice, in `yyyy-mm-dd` format. **Character limit**: 29   # noqa: E501

        :param invoice_date: The invoice_date of this ProxyGetInvoiceSplitItem.  # noqa: E501
        :type: date
        """

        self._invoice_date = invoice_date

    @property
    def invoice_id(self):
        """Gets the invoice_id of this ProxyGetInvoiceSplitItem.  # noqa: E501

         The new invoice after the split. **Character limit**: 32 **Values**: automatically generated   # noqa: E501

        :return: The invoice_id of this ProxyGetInvoiceSplitItem.  # noqa: E501
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """Sets the invoice_id of this ProxyGetInvoiceSplitItem.

         The new invoice after the split. **Character limit**: 32 **Values**: automatically generated   # noqa: E501

        :param invoice_id: The invoice_id of this ProxyGetInvoiceSplitItem.  # noqa: E501
        :type: str
        """

        self._invoice_id = invoice_id

    @property
    def invoice_split_id(self):
        """Gets the invoice_split_id of this ProxyGetInvoiceSplitItem.  # noqa: E501

         The ID of the invoice split associated with the individual invoice split item. **Character limit**: 32 **Values**: a valid invoice split ID   # noqa: E501

        :return: The invoice_split_id of this ProxyGetInvoiceSplitItem.  # noqa: E501
        :rtype: str
        """
        return self._invoice_split_id

    @invoice_split_id.setter
    def invoice_split_id(self, invoice_split_id):
        """Sets the invoice_split_id of this ProxyGetInvoiceSplitItem.

         The ID of the invoice split associated with the individual invoice split item. **Character limit**: 32 **Values**: a valid invoice split ID   # noqa: E501

        :param invoice_split_id: The invoice_split_id of this ProxyGetInvoiceSplitItem.  # noqa: E501
        :type: str
        """

        self._invoice_split_id = invoice_split_id

    @property
    def payment_term(self):
        """Gets the payment_term of this ProxyGetInvoiceSplitItem.  # noqa: E501

         Indicates when the customer pays the split invoice. **Values**: a valid, active payment term   # noqa: E501

        :return: The payment_term of this ProxyGetInvoiceSplitItem.  # noqa: E501
        :rtype: str
        """
        return self._payment_term

    @payment_term.setter
    def payment_term(self, payment_term):
        """Sets the payment_term of this ProxyGetInvoiceSplitItem.

         Indicates when the customer pays the split invoice. **Values**: a valid, active payment term   # noqa: E501

        :param payment_term: The payment_term of this ProxyGetInvoiceSplitItem.  # noqa: E501
        :type: str
        """

        self._payment_term = payment_term

    @property
    def split_percentage(self):
        """Gets the split_percentage of this ProxyGetInvoiceSplitItem.  # noqa: E501

         Specifies the percentage of the original invoice that you want to be the balance of the split invoice. The total of the SplitPercentage field values for all of the InvoiceSplitItem objects in an InvoiceSplit object must equal 100. **Values**:   # noqa: E501

        :return: The split_percentage of this ProxyGetInvoiceSplitItem.  # noqa: E501
        :rtype: float
        """
        return self._split_percentage

    @split_percentage.setter
    def split_percentage(self, split_percentage):
        """Sets the split_percentage of this ProxyGetInvoiceSplitItem.

         Specifies the percentage of the original invoice that you want to be the balance of the split invoice. The total of the SplitPercentage field values for all of the InvoiceSplitItem objects in an InvoiceSplit object must equal 100. **Values**:   # noqa: E501

        :param split_percentage: The split_percentage of this ProxyGetInvoiceSplitItem.  # noqa: E501
        :type: float
        """

        self._split_percentage = split_percentage

    @property
    def updated_by_id(self):
        """Gets the updated_by_id of this ProxyGetInvoiceSplitItem.  # noqa: E501

         The ID of the Zuora user who last updated the invoice split. **Character limit**: 32 **Values**: automatically generated   # noqa: E501

        :return: The updated_by_id of this ProxyGetInvoiceSplitItem.  # noqa: E501
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """Sets the updated_by_id of this ProxyGetInvoiceSplitItem.

         The ID of the Zuora user who last updated the invoice split. **Character limit**: 32 **Values**: automatically generated   # noqa: E501

        :param updated_by_id: The updated_by_id of this ProxyGetInvoiceSplitItem.  # noqa: E501
        :type: str
        """

        self._updated_by_id = updated_by_id

    @property
    def updated_date(self):
        """Gets the updated_date of this ProxyGetInvoiceSplitItem.  # noqa: E501

         The date when the invoice split was last updated. **Values**: automatically generated   # noqa: E501

        :return: The updated_date of this ProxyGetInvoiceSplitItem.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this ProxyGetInvoiceSplitItem.

         The date when the invoice split was last updated. **Values**: automatically generated   # noqa: E501

        :param updated_date: The updated_date of this ProxyGetInvoiceSplitItem.  # noqa: E501
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
        if issubclass(ProxyGetInvoiceSplitItem, dict):
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
        if not isinstance(other, ProxyGetInvoiceSplitItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other