# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.preview_result_charge_metrics import PreviewResultChargeMetrics  # noqa: F401,E501
from zuora_client.models.preview_result_credit_memos import PreviewResultCreditMemos  # noqa: F401,E501
from zuora_client.models.preview_result_invoices import PreviewResultInvoices  # noqa: F401,E501
from zuora_client.models.preview_result_order_metrics import PreviewResultOrderMetrics  # noqa: F401,E501


class PreviewResult(object):
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
        'charge_metrics': 'list[PreviewResultChargeMetrics]',
        'credit_memos': 'list[PreviewResultCreditMemos]',
        'invoices': 'list[PreviewResultInvoices]',
        'order_metrics': 'list[PreviewResultOrderMetrics]'
    }

    attribute_map = {
        'charge_metrics': 'chargeMetrics',
        'credit_memos': 'creditMemos',
        'invoices': 'invoices',
        'order_metrics': 'orderMetrics'
    }

    def __init__(self, charge_metrics=None, credit_memos=None, invoices=None, order_metrics=None):  # noqa: E501
        """PreviewResult - a model defined in Swagger"""  # noqa: E501

        self._charge_metrics = None
        self._credit_memos = None
        self._invoices = None
        self._order_metrics = None
        self.discriminator = None

        if charge_metrics is not None:
            self.charge_metrics = charge_metrics
        if credit_memos is not None:
            self.credit_memos = credit_memos
        if invoices is not None:
            self.invoices = invoices
        if order_metrics is not None:
            self.order_metrics = order_metrics

    @property
    def charge_metrics(self):
        """Gets the charge_metrics of this PreviewResult.  # noqa: E501


        :return: The charge_metrics of this PreviewResult.  # noqa: E501
        :rtype: list[PreviewResultChargeMetrics]
        """
        return self._charge_metrics

    @charge_metrics.setter
    def charge_metrics(self, charge_metrics):
        """Sets the charge_metrics of this PreviewResult.


        :param charge_metrics: The charge_metrics of this PreviewResult.  # noqa: E501
        :type: list[PreviewResultChargeMetrics]
        """

        self._charge_metrics = charge_metrics

    @property
    def credit_memos(self):
        """Gets the credit_memos of this PreviewResult.  # noqa: E501

        This field is only available if you have the Invoice Settlement feature enabled.  # noqa: E501

        :return: The credit_memos of this PreviewResult.  # noqa: E501
        :rtype: list[PreviewResultCreditMemos]
        """
        return self._credit_memos

    @credit_memos.setter
    def credit_memos(self, credit_memos):
        """Sets the credit_memos of this PreviewResult.

        This field is only available if you have the Invoice Settlement feature enabled.  # noqa: E501

        :param credit_memos: The credit_memos of this PreviewResult.  # noqa: E501
        :type: list[PreviewResultCreditMemos]
        """

        self._credit_memos = credit_memos

    @property
    def invoices(self):
        """Gets the invoices of this PreviewResult.  # noqa: E501


        :return: The invoices of this PreviewResult.  # noqa: E501
        :rtype: list[PreviewResultInvoices]
        """
        return self._invoices

    @invoices.setter
    def invoices(self, invoices):
        """Sets the invoices of this PreviewResult.


        :param invoices: The invoices of this PreviewResult.  # noqa: E501
        :type: list[PreviewResultInvoices]
        """

        self._invoices = invoices

    @property
    def order_metrics(self):
        """Gets the order_metrics of this PreviewResult.  # noqa: E501


        :return: The order_metrics of this PreviewResult.  # noqa: E501
        :rtype: list[PreviewResultOrderMetrics]
        """
        return self._order_metrics

    @order_metrics.setter
    def order_metrics(self, order_metrics):
        """Sets the order_metrics of this PreviewResult.


        :param order_metrics: The order_metrics of this PreviewResult.  # noqa: E501
        :type: list[PreviewResultOrderMetrics]
        """

        self._order_metrics = order_metrics

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
        if issubclass(PreviewResult, dict):
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
        if not isinstance(other, PreviewResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
