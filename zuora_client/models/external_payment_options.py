# coding: utf-8




import pprint
import re  # noqa: F401

import six


class ExternalPaymentOptions(object):
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
        'effective_date': 'date',
        'gateway_order_id': 'str',
        'payment_method_id': 'str',
        'reference_id': 'str'
    }

    attribute_map = {
        'amount': 'Amount',
        'effective_date': 'EffectiveDate',
        'gateway_order_id': 'GatewayOrderId',
        'payment_method_id': 'PaymentMethodId',
        'reference_id': 'ReferenceId'
    }

    def __init__(self, amount=None, effective_date=None, gateway_order_id=None, payment_method_id=None, reference_id=None):  # noqa: E501
        """ExternalPaymentOptions - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._effective_date = None
        self._gateway_order_id = None
        self._payment_method_id = None
        self._reference_id = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if effective_date is not None:
            self.effective_date = effective_date
        if gateway_order_id is not None:
            self.gateway_order_id = gateway_order_id
        if payment_method_id is not None:
            self.payment_method_id = payment_method_id
        if reference_id is not None:
            self.reference_id = reference_id

    @property
    def amount(self):
        """Gets the amount of this ExternalPaymentOptions.  # noqa: E501

          # noqa: E501

        :return: The amount of this ExternalPaymentOptions.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ExternalPaymentOptions.

          # noqa: E501

        :param amount: The amount of this ExternalPaymentOptions.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def effective_date(self):
        """Gets the effective_date of this ExternalPaymentOptions.  # noqa: E501

          # noqa: E501

        :return: The effective_date of this ExternalPaymentOptions.  # noqa: E501
        :rtype: date
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this ExternalPaymentOptions.

          # noqa: E501

        :param effective_date: The effective_date of this ExternalPaymentOptions.  # noqa: E501
        :type: date
        """

        self._effective_date = effective_date

    @property
    def gateway_order_id(self):
        """Gets the gateway_order_id of this ExternalPaymentOptions.  # noqa: E501

          # noqa: E501

        :return: The gateway_order_id of this ExternalPaymentOptions.  # noqa: E501
        :rtype: str
        """
        return self._gateway_order_id

    @gateway_order_id.setter
    def gateway_order_id(self, gateway_order_id):
        """Sets the gateway_order_id of this ExternalPaymentOptions.

          # noqa: E501

        :param gateway_order_id: The gateway_order_id of this ExternalPaymentOptions.  # noqa: E501
        :type: str
        """

        self._gateway_order_id = gateway_order_id

    @property
    def payment_method_id(self):
        """Gets the payment_method_id of this ExternalPaymentOptions.  # noqa: E501

          # noqa: E501

        :return: The payment_method_id of this ExternalPaymentOptions.  # noqa: E501
        :rtype: str
        """
        return self._payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, payment_method_id):
        """Sets the payment_method_id of this ExternalPaymentOptions.

          # noqa: E501

        :param payment_method_id: The payment_method_id of this ExternalPaymentOptions.  # noqa: E501
        :type: str
        """

        self._payment_method_id = payment_method_id

    @property
    def reference_id(self):
        """Gets the reference_id of this ExternalPaymentOptions.  # noqa: E501

          # noqa: E501

        :return: The reference_id of this ExternalPaymentOptions.  # noqa: E501
        :rtype: str
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """Sets the reference_id of this ExternalPaymentOptions.

          # noqa: E501

        :param reference_id: The reference_id of this ExternalPaymentOptions.  # noqa: E501
        :type: str
        """

        self._reference_id = reference_id

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
        if issubclass(ExternalPaymentOptions, dict):
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
        if not isinstance(other, ExternalPaymentOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
