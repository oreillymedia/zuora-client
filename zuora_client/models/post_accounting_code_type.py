# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.accounting_code_object_custom_fields import AccountingCodeObjectCustomFields  # noqa: F401,E501


class POSTAccountingCodeType(object):
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
        'gl_account_name': 'str',
        'gl_account_number': 'str',
        'name': 'str',
        'notes': 'str',
        'type': 'str'
    }

    attribute_map = {
        'gl_account_name': 'glAccountName',
        'gl_account_number': 'glAccountNumber',
        'name': 'name',
        'notes': 'notes',
        'type': 'type'
    }

    def __init__(self, gl_account_name=None, gl_account_number=None, name=None, notes=None, type=None):  # noqa: E501
        """POSTAccountingCodeType - a model defined in Swagger"""  # noqa: E501

        self._gl_account_name = None
        self._gl_account_number = None
        self._name = None
        self._notes = None
        self._type = None
        self.discriminator = None

        if gl_account_name is not None:
            self.gl_account_name = gl_account_name
        if gl_account_number is not None:
            self.gl_account_number = gl_account_number
        self.name = name
        if notes is not None:
            self.notes = notes
        self.type = type

    @property
    def gl_account_name(self):
        """Gets the gl_account_name of this POSTAccountingCodeType.  # noqa: E501

        Name of the account in your general ledger.  Field only available if you have Zuora Finance enabled. Maximum of 255 characters.   # noqa: E501

        :return: The gl_account_name of this POSTAccountingCodeType.  # noqa: E501
        :rtype: str
        """
        return self._gl_account_name

    @gl_account_name.setter
    def gl_account_name(self, gl_account_name):
        """Sets the gl_account_name of this POSTAccountingCodeType.

        Name of the account in your general ledger.  Field only available if you have Zuora Finance enabled. Maximum of 255 characters.   # noqa: E501

        :param gl_account_name: The gl_account_name of this POSTAccountingCodeType.  # noqa: E501
        :type: str
        """

        self._gl_account_name = gl_account_name

    @property
    def gl_account_number(self):
        """Gets the gl_account_number of this POSTAccountingCodeType.  # noqa: E501

        Account number in your general ledger.  Field only available if you have Zuora Finance enabled. Maximum of 255 characters.   # noqa: E501

        :return: The gl_account_number of this POSTAccountingCodeType.  # noqa: E501
        :rtype: str
        """
        return self._gl_account_number

    @gl_account_number.setter
    def gl_account_number(self, gl_account_number):
        """Sets the gl_account_number of this POSTAccountingCodeType.

        Account number in your general ledger.  Field only available if you have Zuora Finance enabled. Maximum of 255 characters.   # noqa: E501

        :param gl_account_number: The gl_account_number of this POSTAccountingCodeType.  # noqa: E501
        :type: str
        """

        self._gl_account_number = gl_account_number

    @property
    def name(self):
        """Gets the name of this POSTAccountingCodeType.  # noqa: E501

        Name of the accounting code.  Accounting code name must be unique. Maximum of 100 characters.   # noqa: E501

        :return: The name of this POSTAccountingCodeType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this POSTAccountingCodeType.

        Name of the accounting code.  Accounting code name must be unique. Maximum of 100 characters.   # noqa: E501

        :param name: The name of this POSTAccountingCodeType.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this POSTAccountingCodeType.  # noqa: E501

        Maximum of 2,000 characters.   # noqa: E501

        :return: The notes of this POSTAccountingCodeType.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this POSTAccountingCodeType.

        Maximum of 2,000 characters.   # noqa: E501

        :param notes: The notes of this POSTAccountingCodeType.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def type(self):
        """Gets the type of this POSTAccountingCodeType.  # noqa: E501

        Accounting code type. You cannot create new accounting codes of type `AccountsReceivable`.   Note that `On-Account Receivable` is only available if you enable the Invoice Settlement feature.    # noqa: E501

        :return: The type of this POSTAccountingCodeType.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this POSTAccountingCodeType.

        Accounting code type. You cannot create new accounting codes of type `AccountsReceivable`.   Note that `On-Account Receivable` is only available if you enable the Invoice Settlement feature.    # noqa: E501

        :param type: The type of this POSTAccountingCodeType.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["AccountsReceivable", "On-Account Receivable", "Cash", "OtherAssets", "CustomerCashOnAccount", "DeferredRevenue", "SalesTaxPayable", "OtherLiabilities", "SalesRevenue", "SalesDiscounts", "OtherRevenue", "OtherEquity", "BadDebt", "OtherExpenses"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(POSTAccountingCodeType, dict):
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
        if not isinstance(other, POSTAccountingCodeType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
