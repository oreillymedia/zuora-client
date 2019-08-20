# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.electronic_payment_options import ElectronicPaymentOptions  # noqa: F401,E501
from zuora_client.models.external_payment_options import ExternalPaymentOptions  # noqa: F401,E501
from zuora_client.models.invoice_processing_options import InvoiceProcessingOptions  # noqa: F401,E501


class AmendRequestAmendOptions(object):
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
        'electronic_payment_options': 'ElectronicPaymentOptions',
        'external_payment_options': 'ExternalPaymentOptions',
        'generate_invoice': 'bool',
        'invoice_processing_options': 'InvoiceProcessingOptions',
        'process_payments': 'bool'
    }

    attribute_map = {
        'apply_credit_balance': 'ApplyCreditBalance',
        'electronic_payment_options': 'ElectronicPaymentOptions',
        'external_payment_options': 'ExternalPaymentOptions',
        'generate_invoice': 'GenerateInvoice',
        'invoice_processing_options': 'InvoiceProcessingOptions',
        'process_payments': 'ProcessPayments'
    }

    def __init__(self, apply_credit_balance=None, electronic_payment_options=None, external_payment_options=None, generate_invoice=None, invoice_processing_options=None, process_payments=None):  # noqa: E501
        """AmendRequestAmendOptions - a model defined in Swagger"""  # noqa: E501

        self._apply_credit_balance = None
        self._electronic_payment_options = None
        self._external_payment_options = None
        self._generate_invoice = None
        self._invoice_processing_options = None
        self._process_payments = None
        self.discriminator = None

        if apply_credit_balance is not None:
            self.apply_credit_balance = apply_credit_balance
        if electronic_payment_options is not None:
            self.electronic_payment_options = electronic_payment_options
        if external_payment_options is not None:
            self.external_payment_options = external_payment_options
        if generate_invoice is not None:
            self.generate_invoice = generate_invoice
        if invoice_processing_options is not None:
            self.invoice_processing_options = invoice_processing_options
        if process_payments is not None:
            self.process_payments = process_payments

    @property
    def apply_credit_balance(self):
        """Gets the apply_credit_balance of this AmendRequestAmendOptions.  # noqa: E501

          # noqa: E501

        :return: The apply_credit_balance of this AmendRequestAmendOptions.  # noqa: E501
        :rtype: bool
        """
        return self._apply_credit_balance

    @apply_credit_balance.setter
    def apply_credit_balance(self, apply_credit_balance):
        """Sets the apply_credit_balance of this AmendRequestAmendOptions.

          # noqa: E501

        :param apply_credit_balance: The apply_credit_balance of this AmendRequestAmendOptions.  # noqa: E501
        :type: bool
        """

        self._apply_credit_balance = apply_credit_balance

    @property
    def electronic_payment_options(self):
        """Gets the electronic_payment_options of this AmendRequestAmendOptions.  # noqa: E501


        :return: The electronic_payment_options of this AmendRequestAmendOptions.  # noqa: E501
        :rtype: ElectronicPaymentOptions
        """
        return self._electronic_payment_options

    @electronic_payment_options.setter
    def electronic_payment_options(self, electronic_payment_options):
        """Sets the electronic_payment_options of this AmendRequestAmendOptions.


        :param electronic_payment_options: The electronic_payment_options of this AmendRequestAmendOptions.  # noqa: E501
        :type: ElectronicPaymentOptions
        """

        self._electronic_payment_options = electronic_payment_options

    @property
    def external_payment_options(self):
        """Gets the external_payment_options of this AmendRequestAmendOptions.  # noqa: E501


        :return: The external_payment_options of this AmendRequestAmendOptions.  # noqa: E501
        :rtype: ExternalPaymentOptions
        """
        return self._external_payment_options

    @external_payment_options.setter
    def external_payment_options(self, external_payment_options):
        """Sets the external_payment_options of this AmendRequestAmendOptions.


        :param external_payment_options: The external_payment_options of this AmendRequestAmendOptions.  # noqa: E501
        :type: ExternalPaymentOptions
        """

        self._external_payment_options = external_payment_options

    @property
    def generate_invoice(self):
        """Gets the generate_invoice of this AmendRequestAmendOptions.  # noqa: E501

          # noqa: E501

        :return: The generate_invoice of this AmendRequestAmendOptions.  # noqa: E501
        :rtype: bool
        """
        return self._generate_invoice

    @generate_invoice.setter
    def generate_invoice(self, generate_invoice):
        """Sets the generate_invoice of this AmendRequestAmendOptions.

          # noqa: E501

        :param generate_invoice: The generate_invoice of this AmendRequestAmendOptions.  # noqa: E501
        :type: bool
        """

        self._generate_invoice = generate_invoice

    @property
    def invoice_processing_options(self):
        """Gets the invoice_processing_options of this AmendRequestAmendOptions.  # noqa: E501


        :return: The invoice_processing_options of this AmendRequestAmendOptions.  # noqa: E501
        :rtype: InvoiceProcessingOptions
        """
        return self._invoice_processing_options

    @invoice_processing_options.setter
    def invoice_processing_options(self, invoice_processing_options):
        """Sets the invoice_processing_options of this AmendRequestAmendOptions.


        :param invoice_processing_options: The invoice_processing_options of this AmendRequestAmendOptions.  # noqa: E501
        :type: InvoiceProcessingOptions
        """

        self._invoice_processing_options = invoice_processing_options

    @property
    def process_payments(self):
        """Gets the process_payments of this AmendRequestAmendOptions.  # noqa: E501

          # noqa: E501

        :return: The process_payments of this AmendRequestAmendOptions.  # noqa: E501
        :rtype: bool
        """
        return self._process_payments

    @process_payments.setter
    def process_payments(self, process_payments):
        """Sets the process_payments of this AmendRequestAmendOptions.

          # noqa: E501

        :param process_payments: The process_payments of this AmendRequestAmendOptions.  # noqa: E501
        :type: bool
        """

        self._process_payments = process_payments

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
        if issubclass(AmendRequestAmendOptions, dict):
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
        if not isinstance(other, AmendRequestAmendOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
