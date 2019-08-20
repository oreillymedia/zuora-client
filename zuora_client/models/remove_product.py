# coding: utf-8




import pprint
import re  # noqa: F401

import six


class RemoveProduct(object):
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
        'rate_plan_id': 'str',
        'unique_token': 'str'
    }

    attribute_map = {
        'rate_plan_id': 'ratePlanId',
        'unique_token': 'uniqueToken'
    }

    def __init__(self, rate_plan_id=None, unique_token=None):  # noqa: E501
        """RemoveProduct - a model defined in Swagger"""  # noqa: E501

        self._rate_plan_id = None
        self._unique_token = None
        self.discriminator = None

        if rate_plan_id is not None:
            self.rate_plan_id = rate_plan_id
        if unique_token is not None:
            self.unique_token = unique_token

    @property
    def rate_plan_id(self):
        """Gets the rate_plan_id of this RemoveProduct.  # noqa: E501

        Internal identifier of the rate plan to remove.   # noqa: E501

        :return: The rate_plan_id of this RemoveProduct.  # noqa: E501
        :rtype: str
        """
        return self._rate_plan_id

    @rate_plan_id.setter
    def rate_plan_id(self, rate_plan_id):
        """Sets the rate_plan_id of this RemoveProduct.

        Internal identifier of the rate plan to remove.   # noqa: E501

        :param rate_plan_id: The rate_plan_id of this RemoveProduct.  # noqa: E501
        :type: str
        """

        self._rate_plan_id = rate_plan_id

    @property
    def unique_token(self):
        """Gets the unique_token of this RemoveProduct.  # noqa: E501

        A unique string to represent the rate plan charge in the order. The unique token is used to perform multiple actions against a newly added rate plan. For example, if you want to add and update a product in the same order, you would assign a unique token to the product rate plan when added and use that token in future order actions.A unique string in the order to represent the rate plan.  # noqa: E501

        :return: The unique_token of this RemoveProduct.  # noqa: E501
        :rtype: str
        """
        return self._unique_token

    @unique_token.setter
    def unique_token(self, unique_token):
        """Sets the unique_token of this RemoveProduct.

        A unique string to represent the rate plan charge in the order. The unique token is used to perform multiple actions against a newly added rate plan. For example, if you want to add and update a product in the same order, you would assign a unique token to the product rate plan when added and use that token in future order actions.A unique string in the order to represent the rate plan.  # noqa: E501

        :param unique_token: The unique_token of this RemoveProduct.  # noqa: E501
        :type: str
        """

        self._unique_token = unique_token

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
        if issubclass(RemoveProduct, dict):
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
        if not isinstance(other, RemoveProduct):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other