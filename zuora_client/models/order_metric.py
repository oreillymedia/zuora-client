# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.time_sliced_elp_net_metrics import TimeSlicedElpNetMetrics  # noqa: F401,E501
from zuora_client.models.time_sliced_metrics import TimeSlicedMetrics  # noqa: F401,E501
from zuora_client.models.time_sliced_net_metrics import TimeSlicedNetMetrics  # noqa: F401,E501
from zuora_client.models.time_sliced_tcb_net_metrics import TimeSlicedTcbNetMetrics  # noqa: F401,E501


class OrderMetric(object):
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
        'charge_number': 'str',
        'elp': 'list[TimeSlicedElpNetMetrics]',
        'mrr': 'list[TimeSlicedNetMetrics]',
        'origin_rate_plan_id': 'str',
        'product_rate_plan_charge_id': 'str',
        'product_rate_plan_id': 'str',
        'quantity': 'list[TimeSlicedMetrics]',
        'tcb': 'list[TimeSlicedTcbNetMetrics]',
        'tcv': 'list[TimeSlicedNetMetrics]'
    }

    attribute_map = {
        'charge_number': 'chargeNumber',
        'elp': 'elp',
        'mrr': 'mrr',
        'origin_rate_plan_id': 'originRatePlanId',
        'product_rate_plan_charge_id': 'productRatePlanChargeId',
        'product_rate_plan_id': 'productRatePlanId',
        'quantity': 'quantity',
        'tcb': 'tcb',
        'tcv': 'tcv'
    }

    def __init__(self, charge_number=None, elp=None, mrr=None, origin_rate_plan_id=None, product_rate_plan_charge_id=None, product_rate_plan_id=None, quantity=None, tcb=None, tcv=None):  # noqa: E501
        """OrderMetric - a model defined in Swagger"""  # noqa: E501

        self._charge_number = None
        self._elp = None
        self._mrr = None
        self._origin_rate_plan_id = None
        self._product_rate_plan_charge_id = None
        self._product_rate_plan_id = None
        self._quantity = None
        self._tcb = None
        self._tcv = None
        self.discriminator = None

        if charge_number is not None:
            self.charge_number = charge_number
        if elp is not None:
            self.elp = elp
        if mrr is not None:
            self.mrr = mrr
        if origin_rate_plan_id is not None:
            self.origin_rate_plan_id = origin_rate_plan_id
        if product_rate_plan_charge_id is not None:
            self.product_rate_plan_charge_id = product_rate_plan_charge_id
        if product_rate_plan_id is not None:
            self.product_rate_plan_id = product_rate_plan_id
        if quantity is not None:
            self.quantity = quantity
        if tcb is not None:
            self.tcb = tcb
        if tcv is not None:
            self.tcv = tcv

    @property
    def charge_number(self):
        """Gets the charge_number of this OrderMetric.  # noqa: E501


        :return: The charge_number of this OrderMetric.  # noqa: E501
        :rtype: str
        """
        return self._charge_number

    @charge_number.setter
    def charge_number(self, charge_number):
        """Sets the charge_number of this OrderMetric.


        :param charge_number: The charge_number of this OrderMetric.  # noqa: E501
        :type: str
        """

        self._charge_number = charge_number

    @property
    def elp(self):
        """Gets the elp of this OrderMetric.  # noqa: E501

        The extended list price which is calculated by the original product catalog list price multiplied by the delta quantity.  # noqa: E501

        :return: The elp of this OrderMetric.  # noqa: E501
        :rtype: list[TimeSlicedElpNetMetrics]
        """
        return self._elp

    @elp.setter
    def elp(self, elp):
        """Sets the elp of this OrderMetric.

        The extended list price which is calculated by the original product catalog list price multiplied by the delta quantity.  # noqa: E501

        :param elp: The elp of this OrderMetric.  # noqa: E501
        :type: list[TimeSlicedElpNetMetrics]
        """

        self._elp = elp

    @property
    def mrr(self):
        """Gets the mrr of this OrderMetric.  # noqa: E501


        :return: The mrr of this OrderMetric.  # noqa: E501
        :rtype: list[TimeSlicedNetMetrics]
        """
        return self._mrr

    @mrr.setter
    def mrr(self, mrr):
        """Sets the mrr of this OrderMetric.


        :param mrr: The mrr of this OrderMetric.  # noqa: E501
        :type: list[TimeSlicedNetMetrics]
        """

        self._mrr = mrr

    @property
    def origin_rate_plan_id(self):
        """Gets the origin_rate_plan_id of this OrderMetric.  # noqa: E501


        :return: The origin_rate_plan_id of this OrderMetric.  # noqa: E501
        :rtype: str
        """
        return self._origin_rate_plan_id

    @origin_rate_plan_id.setter
    def origin_rate_plan_id(self, origin_rate_plan_id):
        """Sets the origin_rate_plan_id of this OrderMetric.


        :param origin_rate_plan_id: The origin_rate_plan_id of this OrderMetric.  # noqa: E501
        :type: str
        """

        self._origin_rate_plan_id = origin_rate_plan_id

    @property
    def product_rate_plan_charge_id(self):
        """Gets the product_rate_plan_charge_id of this OrderMetric.  # noqa: E501


        :return: The product_rate_plan_charge_id of this OrderMetric.  # noqa: E501
        :rtype: str
        """
        return self._product_rate_plan_charge_id

    @product_rate_plan_charge_id.setter
    def product_rate_plan_charge_id(self, product_rate_plan_charge_id):
        """Sets the product_rate_plan_charge_id of this OrderMetric.


        :param product_rate_plan_charge_id: The product_rate_plan_charge_id of this OrderMetric.  # noqa: E501
        :type: str
        """

        self._product_rate_plan_charge_id = product_rate_plan_charge_id

    @property
    def product_rate_plan_id(self):
        """Gets the product_rate_plan_id of this OrderMetric.  # noqa: E501


        :return: The product_rate_plan_id of this OrderMetric.  # noqa: E501
        :rtype: str
        """
        return self._product_rate_plan_id

    @product_rate_plan_id.setter
    def product_rate_plan_id(self, product_rate_plan_id):
        """Sets the product_rate_plan_id of this OrderMetric.


        :param product_rate_plan_id: The product_rate_plan_id of this OrderMetric.  # noqa: E501
        :type: str
        """

        self._product_rate_plan_id = product_rate_plan_id

    @property
    def quantity(self):
        """Gets the quantity of this OrderMetric.  # noqa: E501


        :return: The quantity of this OrderMetric.  # noqa: E501
        :rtype: list[TimeSlicedMetrics]
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this OrderMetric.


        :param quantity: The quantity of this OrderMetric.  # noqa: E501
        :type: list[TimeSlicedMetrics]
        """

        self._quantity = quantity

    @property
    def tcb(self):
        """Gets the tcb of this OrderMetric.  # noqa: E501

        Total contracted billing which is the forecast value for the total invoice amount.  # noqa: E501

        :return: The tcb of this OrderMetric.  # noqa: E501
        :rtype: list[TimeSlicedTcbNetMetrics]
        """
        return self._tcb

    @tcb.setter
    def tcb(self, tcb):
        """Sets the tcb of this OrderMetric.

        Total contracted billing which is the forecast value for the total invoice amount.  # noqa: E501

        :param tcb: The tcb of this OrderMetric.  # noqa: E501
        :type: list[TimeSlicedTcbNetMetrics]
        """

        self._tcb = tcb

    @property
    def tcv(self):
        """Gets the tcv of this OrderMetric.  # noqa: E501

        Total contracted value.  # noqa: E501

        :return: The tcv of this OrderMetric.  # noqa: E501
        :rtype: list[TimeSlicedNetMetrics]
        """
        return self._tcv

    @tcv.setter
    def tcv(self, tcv):
        """Sets the tcv of this OrderMetric.

        Total contracted value.  # noqa: E501

        :param tcv: The tcv of this OrderMetric.  # noqa: E501
        :type: list[TimeSlicedNetMetrics]
        """

        self._tcv = tcv

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
        if issubclass(OrderMetric, dict):
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
        if not isinstance(other, OrderMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
