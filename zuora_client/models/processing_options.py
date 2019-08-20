# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.billing_options import BillingOptions  # noqa: F401,E501
from zuora_client.models.processing_options_electronic_payment_options import ProcessingOptionsElectronicPaymentOptions  # noqa: F401,E501


class ProcessingOptions(object):
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
        'apply_credit_balance': 'bool',
        'billing_options': 'BillingOptions',
        'collect_payment': 'bool',
        'electronic_payment_options': 'ProcessingOptionsElectronicPaymentOptions',
        'run_billing': 'bool'
    }

    attribute_map = {
        'apply_credit_balance': 'applyCreditBalance',
        'billing_options': 'billingOptions',
        'collect_payment': 'collectPayment',
        'electronic_payment_options': 'electronicPaymentOptions',
        'run_billing': 'runBilling'
    }

    def __init__(self, apply_credit_balance=None, billing_options=None, collect_payment=None, electronic_payment_options=None, run_billing=None):  # noqa: E501
        """ProcessingOptions - a model defined in Swagger"""  # noqa: E501

        self._apply_credit_balance = None
        self._billing_options = None
        self._collect_payment = None
        self._electronic_payment_options = None
        self._run_billing = None
        self.discriminator = None

        if apply_credit_balance is not None:
            self.apply_credit_balance = apply_credit_balance
        if billing_options is not None:
            self.billing_options = billing_options
        if collect_payment is not None:
            self.collect_payment = collect_payment
        if electronic_payment_options is not None:
            self.electronic_payment_options = electronic_payment_options
        if run_billing is not None:
            self.run_billing = run_billing

    @property
    def apply_credit_balance(self):
        """Gets the apply_credit_balance of this ProcessingOptions.  # noqa: E501

        Indicates if any credit balance on a customer's account is automatically applied to invoices. If no value is specified then this field defaults to false. This feature is not available if you have enabled the Invoice Settlement feature.  # noqa: E501

        :return: The apply_credit_balance of this ProcessingOptions.  # noqa: E501
        :rtype: bool
        """
        return self._apply_credit_balance

    @apply_credit_balance.setter
    def apply_credit_balance(self, apply_credit_balance):
        """Sets the apply_credit_balance of this ProcessingOptions.

        Indicates if any credit balance on a customer's account is automatically applied to invoices. If no value is specified then this field defaults to false. This feature is not available if you have enabled the Invoice Settlement feature.  # noqa: E501

        :param apply_credit_balance: The apply_credit_balance of this ProcessingOptions.  # noqa: E501
        :type: bool
        """

        self._apply_credit_balance = apply_credit_balance

    @property
    def billing_options(self):
        """Gets the billing_options of this ProcessingOptions.  # noqa: E501


        :return: The billing_options of this ProcessingOptions.  # noqa: E501
        :rtype: BillingOptions
        """
        return self._billing_options

    @billing_options.setter
    def billing_options(self, billing_options):
        """Sets the billing_options of this ProcessingOptions.


        :param billing_options: The billing_options of this ProcessingOptions.  # noqa: E501
        :type: BillingOptions
        """

        self._billing_options = billing_options

    @property
    def collect_payment(self):
        """Gets the collect_payment of this ProcessingOptions.  # noqa: E501

        Indicates if the current request needs to collect payments. This value can not be 'true' when 'runBilling' flag is 'false'.  # noqa: E501

        :return: The collect_payment of this ProcessingOptions.  # noqa: E501
        :rtype: bool
        """
        return self._collect_payment

    @collect_payment.setter
    def collect_payment(self, collect_payment):
        """Sets the collect_payment of this ProcessingOptions.

        Indicates if the current request needs to collect payments. This value can not be 'true' when 'runBilling' flag is 'false'.  # noqa: E501

        :param collect_payment: The collect_payment of this ProcessingOptions.  # noqa: E501
        :type: bool
        """

        self._collect_payment = collect_payment

    @property
    def electronic_payment_options(self):
        """Gets the electronic_payment_options of this ProcessingOptions.  # noqa: E501


        :return: The electronic_payment_options of this ProcessingOptions.  # noqa: E501
        :rtype: ProcessingOptionsElectronicPaymentOptions
        """
        return self._electronic_payment_options

    @electronic_payment_options.setter
    def electronic_payment_options(self, electronic_payment_options):
        """Sets the electronic_payment_options of this ProcessingOptions.


        :param electronic_payment_options: The electronic_payment_options of this ProcessingOptions.  # noqa: E501
        :type: ProcessingOptionsElectronicPaymentOptions
        """

        self._electronic_payment_options = electronic_payment_options

    @property
    def run_billing(self):
        """Gets the run_billing of this ProcessingOptions.  # noqa: E501

        Indicates if the current request needs to generate an invoice. The invoice will be generated against all subscriptions included in this order.  # noqa: E501

        :return: The run_billing of this ProcessingOptions.  # noqa: E501
        :rtype: bool
        """
        return self._run_billing

    @run_billing.setter
    def run_billing(self, run_billing):
        """Sets the run_billing of this ProcessingOptions.

        Indicates if the current request needs to generate an invoice. The invoice will be generated against all subscriptions included in this order.  # noqa: E501

        :param run_billing: The run_billing of this ProcessingOptions.  # noqa: E501
        :type: bool
        """

        self._run_billing = run_billing

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
        if issubclass(ProcessingOptions, dict):
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
        if not isinstance(other, ProcessingOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other