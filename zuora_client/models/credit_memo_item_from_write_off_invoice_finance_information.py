# coding: utf-8




import pprint
import re  # noqa: F401

import six


class CreditMemoItemFromWriteOffInvoiceFinanceInformation(object):
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
        'deferred_revenue_accounting_code': 'str',
        'on_account_accounting_code': 'str',
        'recognized_revenue_accounting_code': 'str',
        'revenue_recognition_rule_name': 'str'
    }

    attribute_map = {
        'deferred_revenue_accounting_code': 'deferredRevenueAccountingCode',
        'on_account_accounting_code': 'onAccountAccountingCode',
        'recognized_revenue_accounting_code': 'recognizedRevenueAccountingCode',
        'revenue_recognition_rule_name': 'revenueRecognitionRuleName'
    }

    def __init__(self, deferred_revenue_accounting_code=None, on_account_accounting_code=None, recognized_revenue_accounting_code=None, revenue_recognition_rule_name=None):  # noqa: E501
        """CreditMemoItemFromWriteOffInvoiceFinanceInformation - a model defined in Swagger"""  # noqa: E501

        self._deferred_revenue_accounting_code = None
        self._on_account_accounting_code = None
        self._recognized_revenue_accounting_code = None
        self._revenue_recognition_rule_name = None
        self.discriminator = None

        if deferred_revenue_accounting_code is not None:
            self.deferred_revenue_accounting_code = deferred_revenue_accounting_code
        if on_account_accounting_code is not None:
            self.on_account_accounting_code = on_account_accounting_code
        if recognized_revenue_accounting_code is not None:
            self.recognized_revenue_accounting_code = recognized_revenue_accounting_code
        if revenue_recognition_rule_name is not None:
            self.revenue_recognition_rule_name = revenue_recognition_rule_name

    @property
    def deferred_revenue_accounting_code(self):
        """Gets the deferred_revenue_accounting_code of this CreditMemoItemFromWriteOffInvoiceFinanceInformation.  # noqa: E501

        The accounting code for the deferred revenue, such as Monthly Recurring Liability.   # noqa: E501

        :return: The deferred_revenue_accounting_code of this CreditMemoItemFromWriteOffInvoiceFinanceInformation.  # noqa: E501
        :rtype: str
        """
        return self._deferred_revenue_accounting_code

    @deferred_revenue_accounting_code.setter
    def deferred_revenue_accounting_code(self, deferred_revenue_accounting_code):
        """Sets the deferred_revenue_accounting_code of this CreditMemoItemFromWriteOffInvoiceFinanceInformation.

        The accounting code for the deferred revenue, such as Monthly Recurring Liability.   # noqa: E501

        :param deferred_revenue_accounting_code: The deferred_revenue_accounting_code of this CreditMemoItemFromWriteOffInvoiceFinanceInformation.  # noqa: E501
        :type: str
        """
        if deferred_revenue_accounting_code is not None and len(deferred_revenue_accounting_code) > 100:
            raise ValueError("Invalid value for `deferred_revenue_accounting_code`, length must be less than or equal to `100`")  # noqa: E501
        if deferred_revenue_accounting_code is not None and len(deferred_revenue_accounting_code) < 0:
            raise ValueError("Invalid value for `deferred_revenue_accounting_code`, length must be greater than or equal to `0`")  # noqa: E501

        self._deferred_revenue_accounting_code = deferred_revenue_accounting_code

    @property
    def on_account_accounting_code(self):
        """Gets the on_account_accounting_code of this CreditMemoItemFromWriteOffInvoiceFinanceInformation.  # noqa: E501

        The accounting code that maps to an on account in your accounting system.   # noqa: E501

        :return: The on_account_accounting_code of this CreditMemoItemFromWriteOffInvoiceFinanceInformation.  # noqa: E501
        :rtype: str
        """
        return self._on_account_accounting_code

    @on_account_accounting_code.setter
    def on_account_accounting_code(self, on_account_accounting_code):
        """Sets the on_account_accounting_code of this CreditMemoItemFromWriteOffInvoiceFinanceInformation.

        The accounting code that maps to an on account in your accounting system.   # noqa: E501

        :param on_account_accounting_code: The on_account_accounting_code of this CreditMemoItemFromWriteOffInvoiceFinanceInformation.  # noqa: E501
        :type: str
        """
        if on_account_accounting_code is not None and len(on_account_accounting_code) > 100:
            raise ValueError("Invalid value for `on_account_accounting_code`, length must be less than or equal to `100`")  # noqa: E501
        if on_account_accounting_code is not None and len(on_account_accounting_code) < 0:
            raise ValueError("Invalid value for `on_account_accounting_code`, length must be greater than or equal to `0`")  # noqa: E501

        self._on_account_accounting_code = on_account_accounting_code

    @property
    def recognized_revenue_accounting_code(self):
        """Gets the recognized_revenue_accounting_code of this CreditMemoItemFromWriteOffInvoiceFinanceInformation.  # noqa: E501

        The accounting code for the recognized revenue, such as Monthly Recurring Charges or Overage Charges.   # noqa: E501

        :return: The recognized_revenue_accounting_code of this CreditMemoItemFromWriteOffInvoiceFinanceInformation.  # noqa: E501
        :rtype: str
        """
        return self._recognized_revenue_accounting_code

    @recognized_revenue_accounting_code.setter
    def recognized_revenue_accounting_code(self, recognized_revenue_accounting_code):
        """Sets the recognized_revenue_accounting_code of this CreditMemoItemFromWriteOffInvoiceFinanceInformation.

        The accounting code for the recognized revenue, such as Monthly Recurring Charges or Overage Charges.   # noqa: E501

        :param recognized_revenue_accounting_code: The recognized_revenue_accounting_code of this CreditMemoItemFromWriteOffInvoiceFinanceInformation.  # noqa: E501
        :type: str
        """
        if recognized_revenue_accounting_code is not None and len(recognized_revenue_accounting_code) > 100:
            raise ValueError("Invalid value for `recognized_revenue_accounting_code`, length must be less than or equal to `100`")  # noqa: E501
        if recognized_revenue_accounting_code is not None and len(recognized_revenue_accounting_code) < 0:
            raise ValueError("Invalid value for `recognized_revenue_accounting_code`, length must be greater than or equal to `0`")  # noqa: E501

        self._recognized_revenue_accounting_code = recognized_revenue_accounting_code

    @property
    def revenue_recognition_rule_name(self):
        """Gets the revenue_recognition_rule_name of this CreditMemoItemFromWriteOffInvoiceFinanceInformation.  # noqa: E501

        The name of the revenue recognition rule governing the revenue schedule.   # noqa: E501

        :return: The revenue_recognition_rule_name of this CreditMemoItemFromWriteOffInvoiceFinanceInformation.  # noqa: E501
        :rtype: str
        """
        return self._revenue_recognition_rule_name

    @revenue_recognition_rule_name.setter
    def revenue_recognition_rule_name(self, revenue_recognition_rule_name):
        """Sets the revenue_recognition_rule_name of this CreditMemoItemFromWriteOffInvoiceFinanceInformation.

        The name of the revenue recognition rule governing the revenue schedule.   # noqa: E501

        :param revenue_recognition_rule_name: The revenue_recognition_rule_name of this CreditMemoItemFromWriteOffInvoiceFinanceInformation.  # noqa: E501
        :type: str
        """
        if revenue_recognition_rule_name is not None and len(revenue_recognition_rule_name) > 100:
            raise ValueError("Invalid value for `revenue_recognition_rule_name`, length must be less than or equal to `100`")  # noqa: E501
        if revenue_recognition_rule_name is not None and len(revenue_recognition_rule_name) < 0:
            raise ValueError("Invalid value for `revenue_recognition_rule_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._revenue_recognition_rule_name = revenue_recognition_rule_name

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
        if issubclass(CreditMemoItemFromWriteOffInvoiceFinanceInformation, dict):
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
        if not isinstance(other, CreditMemoItemFromWriteOffInvoiceFinanceInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
