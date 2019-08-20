# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.preview_order_order_action import PreviewOrderOrderAction  # noqa: F401,E501
from zuora_client.models.subscription_object_custom_fields import SubscriptionObjectCustomFields  # noqa: F401,E501


class POSTOrderPreviewRequestTypeSubscriptions(object):
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
        'custom_fields': 'SubscriptionObjectCustomFields',
        'order_actions': 'list[PreviewOrderOrderAction]',
        'subscription_number': 'str'
    }

    attribute_map = {
        'custom_fields': 'customFields',
        'order_actions': 'orderActions',
        'subscription_number': 'subscriptionNumber'
    }

    def __init__(self, custom_fields=None, order_actions=None, subscription_number=None):  # noqa: E501
        """POSTOrderPreviewRequestTypeSubscriptions - a model defined in Swagger"""  # noqa: E501

        self._custom_fields = None
        self._order_actions = None
        self._subscription_number = None
        self.discriminator = None

        if custom_fields is not None:
            self.custom_fields = custom_fields
        if order_actions is not None:
            self.order_actions = order_actions
        if subscription_number is not None:
            self.subscription_number = subscription_number

    @property
    def custom_fields(self):
        """Gets the custom_fields of this POSTOrderPreviewRequestTypeSubscriptions.  # noqa: E501


        :return: The custom_fields of this POSTOrderPreviewRequestTypeSubscriptions.  # noqa: E501
        :rtype: SubscriptionObjectCustomFields
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this POSTOrderPreviewRequestTypeSubscriptions.


        :param custom_fields: The custom_fields of this POSTOrderPreviewRequestTypeSubscriptions.  # noqa: E501
        :type: SubscriptionObjectCustomFields
        """

        self._custom_fields = custom_fields

    @property
    def order_actions(self):
        """Gets the order_actions of this POSTOrderPreviewRequestTypeSubscriptions.  # noqa: E501

        The actions to be applied to the subscription. Order actions will be stored with the sequence when it was provided in the request.  # noqa: E501

        :return: The order_actions of this POSTOrderPreviewRequestTypeSubscriptions.  # noqa: E501
        :rtype: list[PreviewOrderOrderAction]
        """
        return self._order_actions

    @order_actions.setter
    def order_actions(self, order_actions):
        """Sets the order_actions of this POSTOrderPreviewRequestTypeSubscriptions.

        The actions to be applied to the subscription. Order actions will be stored with the sequence when it was provided in the request.  # noqa: E501

        :param order_actions: The order_actions of this POSTOrderPreviewRequestTypeSubscriptions.  # noqa: E501
        :type: list[PreviewOrderOrderAction]
        """

        self._order_actions = order_actions

    @property
    def subscription_number(self):
        """Gets the subscription_number of this POSTOrderPreviewRequestTypeSubscriptions.  # noqa: E501

        Leave this field empty to represent new subscription creation, or specify a subscription number to update an existing subscription.   # noqa: E501

        :return: The subscription_number of this POSTOrderPreviewRequestTypeSubscriptions.  # noqa: E501
        :rtype: str
        """
        return self._subscription_number

    @subscription_number.setter
    def subscription_number(self, subscription_number):
        """Sets the subscription_number of this POSTOrderPreviewRequestTypeSubscriptions.

        Leave this field empty to represent new subscription creation, or specify a subscription number to update an existing subscription.   # noqa: E501

        :param subscription_number: The subscription_number of this POSTOrderPreviewRequestTypeSubscriptions.  # noqa: E501
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
        if issubclass(POSTOrderPreviewRequestTypeSubscriptions, dict):
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
        if not isinstance(other, POSTOrderPreviewRequestTypeSubscriptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
