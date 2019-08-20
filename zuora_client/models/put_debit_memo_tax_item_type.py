# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.put_debit_memo_tax_item_type_finance_information import PutDebitMemoTaxItemTypeFinanceInformation  # noqa: F401,E501


class PutDebitMemoTaxItemType(object):
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
        'finance_information': 'PutDebitMemoTaxItemTypeFinanceInformation',
        'id': 'str',
        'jurisdiction': 'str',
        'location_code': 'str',
        'tax_code': 'str',
        'tax_code_description': 'str',
        'tax_date': 'date',
        'tax_exempt_amount': 'float',
        'tax_name': 'str',
        'tax_rate': 'float',
        'tax_rate_description': 'str',
        'tax_rate_type': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'finance_information': 'financeInformation',
        'id': 'id',
        'jurisdiction': 'jurisdiction',
        'location_code': 'locationCode',
        'tax_code': 'taxCode',
        'tax_code_description': 'taxCodeDescription',
        'tax_date': 'taxDate',
        'tax_exempt_amount': 'taxExemptAmount',
        'tax_name': 'taxName',
        'tax_rate': 'taxRate',
        'tax_rate_description': 'taxRateDescription',
        'tax_rate_type': 'taxRateType'
    }

    def __init__(self, amount=None, finance_information=None, id=None, jurisdiction=None, location_code=None, tax_code=None, tax_code_description=None, tax_date=None, tax_exempt_amount=None, tax_name=None, tax_rate=None, tax_rate_description=None, tax_rate_type=None):  # noqa: E501
        """PutDebitMemoTaxItemType - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._finance_information = None
        self._id = None
        self._jurisdiction = None
        self._location_code = None
        self._tax_code = None
        self._tax_code_description = None
        self._tax_date = None
        self._tax_exempt_amount = None
        self._tax_name = None
        self._tax_rate = None
        self._tax_rate_description = None
        self._tax_rate_type = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if finance_information is not None:
            self.finance_information = finance_information
        self.id = id
        if jurisdiction is not None:
            self.jurisdiction = jurisdiction
        if location_code is not None:
            self.location_code = location_code
        if tax_code is not None:
            self.tax_code = tax_code
        if tax_code_description is not None:
            self.tax_code_description = tax_code_description
        if tax_date is not None:
            self.tax_date = tax_date
        if tax_exempt_amount is not None:
            self.tax_exempt_amount = tax_exempt_amount
        if tax_name is not None:
            self.tax_name = tax_name
        if tax_rate is not None:
            self.tax_rate = tax_rate
        if tax_rate_description is not None:
            self.tax_rate_description = tax_rate_description
        if tax_rate_type is not None:
            self.tax_rate_type = tax_rate_type

    @property
    def amount(self):
        """Gets the amount of this PutDebitMemoTaxItemType.  # noqa: E501

        The amount of the taxation item in the debit memo item.   # noqa: E501

        :return: The amount of this PutDebitMemoTaxItemType.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PutDebitMemoTaxItemType.

        The amount of the taxation item in the debit memo item.   # noqa: E501

        :param amount: The amount of this PutDebitMemoTaxItemType.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def finance_information(self):
        """Gets the finance_information of this PutDebitMemoTaxItemType.  # noqa: E501


        :return: The finance_information of this PutDebitMemoTaxItemType.  # noqa: E501
        :rtype: PutDebitMemoTaxItemTypeFinanceInformation
        """
        return self._finance_information

    @finance_information.setter
    def finance_information(self, finance_information):
        """Sets the finance_information of this PutDebitMemoTaxItemType.


        :param finance_information: The finance_information of this PutDebitMemoTaxItemType.  # noqa: E501
        :type: PutDebitMemoTaxItemTypeFinanceInformation
        """

        self._finance_information = finance_information

    @property
    def id(self):
        """Gets the id of this PutDebitMemoTaxItemType.  # noqa: E501

        The ID of the taxation item in the debit memo item.   # noqa: E501

        :return: The id of this PutDebitMemoTaxItemType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PutDebitMemoTaxItemType.

        The ID of the taxation item in the debit memo item.   # noqa: E501

        :param id: The id of this PutDebitMemoTaxItemType.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def jurisdiction(self):
        """Gets the jurisdiction of this PutDebitMemoTaxItemType.  # noqa: E501

        The jurisdiction that applies the tax or VAT. This value is typically a state, province, county, or city.   # noqa: E501

        :return: The jurisdiction of this PutDebitMemoTaxItemType.  # noqa: E501
        :rtype: str
        """
        return self._jurisdiction

    @jurisdiction.setter
    def jurisdiction(self, jurisdiction):
        """Sets the jurisdiction of this PutDebitMemoTaxItemType.

        The jurisdiction that applies the tax or VAT. This value is typically a state, province, county, or city.   # noqa: E501

        :param jurisdiction: The jurisdiction of this PutDebitMemoTaxItemType.  # noqa: E501
        :type: str
        """

        self._jurisdiction = jurisdiction

    @property
    def location_code(self):
        """Gets the location_code of this PutDebitMemoTaxItemType.  # noqa: E501

        The identifier for the location based on the value of the `taxCode` field.   # noqa: E501

        :return: The location_code of this PutDebitMemoTaxItemType.  # noqa: E501
        :rtype: str
        """
        return self._location_code

    @location_code.setter
    def location_code(self, location_code):
        """Sets the location_code of this PutDebitMemoTaxItemType.

        The identifier for the location based on the value of the `taxCode` field.   # noqa: E501

        :param location_code: The location_code of this PutDebitMemoTaxItemType.  # noqa: E501
        :type: str
        """

        self._location_code = location_code

    @property
    def tax_code(self):
        """Gets the tax_code of this PutDebitMemoTaxItemType.  # noqa: E501

        The tax code identifies which tax rules and tax rates to apply to a specific debit memo.   # noqa: E501

        :return: The tax_code of this PutDebitMemoTaxItemType.  # noqa: E501
        :rtype: str
        """
        return self._tax_code

    @tax_code.setter
    def tax_code(self, tax_code):
        """Sets the tax_code of this PutDebitMemoTaxItemType.

        The tax code identifies which tax rules and tax rates to apply to a specific debit memo.   # noqa: E501

        :param tax_code: The tax_code of this PutDebitMemoTaxItemType.  # noqa: E501
        :type: str
        """

        self._tax_code = tax_code

    @property
    def tax_code_description(self):
        """Gets the tax_code_description of this PutDebitMemoTaxItemType.  # noqa: E501

        The description of the tax code.   # noqa: E501

        :return: The tax_code_description of this PutDebitMemoTaxItemType.  # noqa: E501
        :rtype: str
        """
        return self._tax_code_description

    @tax_code_description.setter
    def tax_code_description(self, tax_code_description):
        """Sets the tax_code_description of this PutDebitMemoTaxItemType.

        The description of the tax code.   # noqa: E501

        :param tax_code_description: The tax_code_description of this PutDebitMemoTaxItemType.  # noqa: E501
        :type: str
        """

        self._tax_code_description = tax_code_description

    @property
    def tax_date(self):
        """Gets the tax_date of this PutDebitMemoTaxItemType.  # noqa: E501

        The date that the tax is applied to the debit memo, in `yyyy-mm-dd` format.   # noqa: E501

        :return: The tax_date of this PutDebitMemoTaxItemType.  # noqa: E501
        :rtype: date
        """
        return self._tax_date

    @tax_date.setter
    def tax_date(self, tax_date):
        """Sets the tax_date of this PutDebitMemoTaxItemType.

        The date that the tax is applied to the debit memo, in `yyyy-mm-dd` format.   # noqa: E501

        :param tax_date: The tax_date of this PutDebitMemoTaxItemType.  # noqa: E501
        :type: date
        """

        self._tax_date = tax_date

    @property
    def tax_exempt_amount(self):
        """Gets the tax_exempt_amount of this PutDebitMemoTaxItemType.  # noqa: E501

        The amount of taxes or VAT for which the customer has an exemption.   # noqa: E501

        :return: The tax_exempt_amount of this PutDebitMemoTaxItemType.  # noqa: E501
        :rtype: float
        """
        return self._tax_exempt_amount

    @tax_exempt_amount.setter
    def tax_exempt_amount(self, tax_exempt_amount):
        """Sets the tax_exempt_amount of this PutDebitMemoTaxItemType.

        The amount of taxes or VAT for which the customer has an exemption.   # noqa: E501

        :param tax_exempt_amount: The tax_exempt_amount of this PutDebitMemoTaxItemType.  # noqa: E501
        :type: float
        """

        self._tax_exempt_amount = tax_exempt_amount

    @property
    def tax_name(self):
        """Gets the tax_name of this PutDebitMemoTaxItemType.  # noqa: E501

        The name of taxation.   # noqa: E501

        :return: The tax_name of this PutDebitMemoTaxItemType.  # noqa: E501
        :rtype: str
        """
        return self._tax_name

    @tax_name.setter
    def tax_name(self, tax_name):
        """Sets the tax_name of this PutDebitMemoTaxItemType.

        The name of taxation.   # noqa: E501

        :param tax_name: The tax_name of this PutDebitMemoTaxItemType.  # noqa: E501
        :type: str
        """

        self._tax_name = tax_name

    @property
    def tax_rate(self):
        """Gets the tax_rate of this PutDebitMemoTaxItemType.  # noqa: E501

        The tax rate applied to the debit memo.   # noqa: E501

        :return: The tax_rate of this PutDebitMemoTaxItemType.  # noqa: E501
        :rtype: float
        """
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        """Sets the tax_rate of this PutDebitMemoTaxItemType.

        The tax rate applied to the debit memo.   # noqa: E501

        :param tax_rate: The tax_rate of this PutDebitMemoTaxItemType.  # noqa: E501
        :type: float
        """

        self._tax_rate = tax_rate

    @property
    def tax_rate_description(self):
        """Gets the tax_rate_description of this PutDebitMemoTaxItemType.  # noqa: E501

        The description of the tax rate.   # noqa: E501

        :return: The tax_rate_description of this PutDebitMemoTaxItemType.  # noqa: E501
        :rtype: str
        """
        return self._tax_rate_description

    @tax_rate_description.setter
    def tax_rate_description(self, tax_rate_description):
        """Sets the tax_rate_description of this PutDebitMemoTaxItemType.

        The description of the tax rate.   # noqa: E501

        :param tax_rate_description: The tax_rate_description of this PutDebitMemoTaxItemType.  # noqa: E501
        :type: str
        """

        self._tax_rate_description = tax_rate_description

    @property
    def tax_rate_type(self):
        """Gets the tax_rate_type of this PutDebitMemoTaxItemType.  # noqa: E501

        The type of the tax rate applied to the debit memo.   # noqa: E501

        :return: The tax_rate_type of this PutDebitMemoTaxItemType.  # noqa: E501
        :rtype: str
        """
        return self._tax_rate_type

    @tax_rate_type.setter
    def tax_rate_type(self, tax_rate_type):
        """Sets the tax_rate_type of this PutDebitMemoTaxItemType.

        The type of the tax rate applied to the debit memo.   # noqa: E501

        :param tax_rate_type: The tax_rate_type of this PutDebitMemoTaxItemType.  # noqa: E501
        :type: str
        """
        allowed_values = ["Percentage", "FlatFee"]  # noqa: E501
        if tax_rate_type not in allowed_values:
            raise ValueError(
                "Invalid value for `tax_rate_type` ({0}), must be one of {1}"  # noqa: E501
                .format(tax_rate_type, allowed_values)
            )

        self._tax_rate_type = tax_rate_type

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
        if issubclass(PutDebitMemoTaxItemType, dict):
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
        if not isinstance(other, PutDebitMemoTaxItemType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
