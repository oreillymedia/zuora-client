# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.common_response_type import CommonResponseType  # noqa: F401,E501
from zuora_client.models.order_rated_result import OrderRatedResult  # noqa: F401,E501


class GetOrderRatedResultResponseType(object):
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
        'success': 'bool',
        'order_rated_result': 'OrderRatedResult'
    }

    attribute_map = {
        'success': 'success',
        'order_rated_result': 'orderRatedResult'
    }

    def __init__(self, success=None, order_rated_result=None):  # noqa: E501
        """GetOrderRatedResultResponseType - a model defined in Swagger"""  # noqa: E501

        self._success = None
        self._order_rated_result = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if order_rated_result is not None:
            self.order_rated_result = order_rated_result

    @property
    def success(self):
        """Gets the success of this GetOrderRatedResultResponseType.  # noqa: E501

        Indicates whether the call succeeded.   # noqa: E501

        :return: The success of this GetOrderRatedResultResponseType.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this GetOrderRatedResultResponseType.

        Indicates whether the call succeeded.   # noqa: E501

        :param success: The success of this GetOrderRatedResultResponseType.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def order_rated_result(self):
        """Gets the order_rated_result of this GetOrderRatedResultResponseType.  # noqa: E501


        :return: The order_rated_result of this GetOrderRatedResultResponseType.  # noqa: E501
        :rtype: OrderRatedResult
        """
        return self._order_rated_result

    @order_rated_result.setter
    def order_rated_result(self, order_rated_result):
        """Sets the order_rated_result of this GetOrderRatedResultResponseType.


        :param order_rated_result: The order_rated_result of this GetOrderRatedResultResponseType.  # noqa: E501
        :type: OrderRatedResult
        """

        self._order_rated_result = order_rated_result

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
        if issubclass(GetOrderRatedResultResponseType, dict):
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
        if not isinstance(other, GetOrderRatedResultResponseType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
