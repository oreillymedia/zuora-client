# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.order_item import OrderItem  # noqa: F401,E501
from zuora_client.models.order_metric import OrderMetric  # noqa: F401,E501


class PreviewResultOrderActions(object):
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
        'order_items': 'list[OrderItem]',
        'order_metrics': 'list[OrderMetric]',
        'sequence': 'str',
        'type': 'str'
    }

    attribute_map = {
        'order_items': 'orderItems',
        'order_metrics': 'orderMetrics',
        'sequence': 'sequence',
        'type': 'type'
    }

    def __init__(self, order_items=None, order_metrics=None, sequence=None, type=None):  # noqa: E501
        """PreviewResultOrderActions - a model defined in Swagger"""  # noqa: E501

        self._order_items = None
        self._order_metrics = None
        self._sequence = None
        self._type = None
        self.discriminator = None

        if order_items is not None:
            self.order_items = order_items
        if order_metrics is not None:
            self.order_metrics = order_metrics
        if sequence is not None:
            self.sequence = sequence
        if type is not None:
            self.type = type

    @property
    def order_items(self):
        """Gets the order_items of this PreviewResultOrderActions.  # noqa: E501


        :return: The order_items of this PreviewResultOrderActions.  # noqa: E501
        :rtype: list[OrderItem]
        """
        return self._order_items

    @order_items.setter
    def order_items(self, order_items):
        """Sets the order_items of this PreviewResultOrderActions.


        :param order_items: The order_items of this PreviewResultOrderActions.  # noqa: E501
        :type: list[OrderItem]
        """

        self._order_items = order_items

    @property
    def order_metrics(self):
        """Gets the order_metrics of this PreviewResultOrderActions.  # noqa: E501


        :return: The order_metrics of this PreviewResultOrderActions.  # noqa: E501
        :rtype: list[OrderMetric]
        """
        return self._order_metrics

    @order_metrics.setter
    def order_metrics(self, order_metrics):
        """Sets the order_metrics of this PreviewResultOrderActions.


        :param order_metrics: The order_metrics of this PreviewResultOrderActions.  # noqa: E501
        :type: list[OrderMetric]
        """

        self._order_metrics = order_metrics

    @property
    def sequence(self):
        """Gets the sequence of this PreviewResultOrderActions.  # noqa: E501


        :return: The sequence of this PreviewResultOrderActions.  # noqa: E501
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this PreviewResultOrderActions.


        :param sequence: The sequence of this PreviewResultOrderActions.  # noqa: E501
        :type: str
        """

        self._sequence = sequence

    @property
    def type(self):
        """Gets the type of this PreviewResultOrderActions.  # noqa: E501


        :return: The type of this PreviewResultOrderActions.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PreviewResultOrderActions.


        :param type: The type of this PreviewResultOrderActions.  # noqa: E501
        :type: str
        """

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
        if issubclass(PreviewResultOrderActions, dict):
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
        if not isinstance(other, PreviewResultOrderActions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
