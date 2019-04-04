# coding: utf-8




import pprint
import re  # noqa: F401

import six


class PutCreditMemoTaxItemTypeFinanceInformation(object):
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
        'on_account_accounting_code': 'str',
        'sales_tax_payable_accounting_code': 'str'
    }

    attribute_map = {
        'on_account_accounting_code': 'onAccountAccountingCode',
        'sales_tax_payable_accounting_code': 'salesTaxPayableAccountingCode'
    }

    def __init__(self, on_account_accounting_code=None, sales_tax_payable_accounting_code=None):  # noqa: E501
        """PutCreditMemoTaxItemTypeFinanceInformation - a model defined in Swagger"""  # noqa: E501

        self._on_account_accounting_code = None
        self._sales_tax_payable_accounting_code = None
        self.discriminator = None

        if on_account_accounting_code is not None:
            self.on_account_accounting_code = on_account_accounting_code
        if sales_tax_payable_accounting_code is not None:
            self.sales_tax_payable_accounting_code = sales_tax_payable_accounting_code

    @property
    def on_account_accounting_code(self):
        """Gets the on_account_accounting_code of this PutCreditMemoTaxItemTypeFinanceInformation.  # noqa: E501

        The accounting code that maps to an on account in your accounting system.   # noqa: E501

        :return: The on_account_accounting_code of this PutCreditMemoTaxItemTypeFinanceInformation.  # noqa: E501
        :rtype: str
        """
        return self._on_account_accounting_code

    @on_account_accounting_code.setter
    def on_account_accounting_code(self, on_account_accounting_code):
        """Sets the on_account_accounting_code of this PutCreditMemoTaxItemTypeFinanceInformation.

        The accounting code that maps to an on account in your accounting system.   # noqa: E501

        :param on_account_accounting_code: The on_account_accounting_code of this PutCreditMemoTaxItemTypeFinanceInformation.  # noqa: E501
        :type: str
        """
        if on_account_accounting_code is not None and len(on_account_accounting_code) > 100:
            raise ValueError("Invalid value for `on_account_accounting_code`, length must be less than or equal to `100`")  # noqa: E501
        if on_account_accounting_code is not None and len(on_account_accounting_code) < 0:
            raise ValueError("Invalid value for `on_account_accounting_code`, length must be greater than or equal to `0`")  # noqa: E501

        self._on_account_accounting_code = on_account_accounting_code

    @property
    def sales_tax_payable_accounting_code(self):
        """Gets the sales_tax_payable_accounting_code of this PutCreditMemoTaxItemTypeFinanceInformation.  # noqa: E501

        The accounting code for the sales taxes payable.   # noqa: E501

        :return: The sales_tax_payable_accounting_code of this PutCreditMemoTaxItemTypeFinanceInformation.  # noqa: E501
        :rtype: str
        """
        return self._sales_tax_payable_accounting_code

    @sales_tax_payable_accounting_code.setter
    def sales_tax_payable_accounting_code(self, sales_tax_payable_accounting_code):
        """Sets the sales_tax_payable_accounting_code of this PutCreditMemoTaxItemTypeFinanceInformation.

        The accounting code for the sales taxes payable.   # noqa: E501

        :param sales_tax_payable_accounting_code: The sales_tax_payable_accounting_code of this PutCreditMemoTaxItemTypeFinanceInformation.  # noqa: E501
        :type: str
        """
        if sales_tax_payable_accounting_code is not None and len(sales_tax_payable_accounting_code) > 100:
            raise ValueError("Invalid value for `sales_tax_payable_accounting_code`, length must be less than or equal to `100`")  # noqa: E501
        if sales_tax_payable_accounting_code is not None and len(sales_tax_payable_accounting_code) < 0:
            raise ValueError("Invalid value for `sales_tax_payable_accounting_code`, length must be greater than or equal to `0`")  # noqa: E501

        self._sales_tax_payable_accounting_code = sales_tax_payable_accounting_code

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
        if issubclass(PutCreditMemoTaxItemTypeFinanceInformation, dict):
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
        if not isinstance(other, PutCreditMemoTaxItemTypeFinanceInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
