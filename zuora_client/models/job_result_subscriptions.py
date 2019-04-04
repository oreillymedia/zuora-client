# coding: utf-8




import pprint
import re  # noqa: F401

import six


class JobResultSubscriptions(object):
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
        'status': 'str',
        'subscription_number': 'str'
    }

    attribute_map = {
        'status': 'status',
        'subscription_number': 'subscriptionNumber'
    }

    def __init__(self, status=None, subscription_number=None):  # noqa: E501
        """JobResultSubscriptions - a model defined in Swagger"""  # noqa: E501

        self._status = None
        self._subscription_number = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if subscription_number is not None:
            self.subscription_number = subscription_number

    @property
    def status(self):
        """Gets the status of this JobResultSubscriptions.  # noqa: E501

        Status of the subscription. `Pending Activation` and `Pending Acceptance` are only applicable for an order that contains a `CreateSubscription` order action.  # noqa: E501

        :return: The status of this JobResultSubscriptions.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JobResultSubscriptions.

        Status of the subscription. `Pending Activation` and `Pending Acceptance` are only applicable for an order that contains a `CreateSubscription` order action.  # noqa: E501

        :param status: The status of this JobResultSubscriptions.  # noqa: E501
        :type: str
        """
        allowed_values = ["Active", "Pending Activation", "Pending Acceptance", "Cancelled"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def subscription_number(self):
        """Gets the subscription_number of this JobResultSubscriptions.  # noqa: E501

        Subscription number of the subscription included in this order.  # noqa: E501

        :return: The subscription_number of this JobResultSubscriptions.  # noqa: E501
        :rtype: str
        """
        return self._subscription_number

    @subscription_number.setter
    def subscription_number(self, subscription_number):
        """Sets the subscription_number of this JobResultSubscriptions.

        Subscription number of the subscription included in this order.  # noqa: E501

        :param subscription_number: The subscription_number of this JobResultSubscriptions.  # noqa: E501
        :type: str
        """

        self._subscription_number = subscription_number

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
        if issubclass(JobResultSubscriptions, dict):
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
        if not isinstance(other, JobResultSubscriptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
