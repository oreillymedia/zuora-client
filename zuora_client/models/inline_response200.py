# coding: utf-8




import pprint
import re  # noqa: F401

import six


class InlineResponse200(object):
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
        'billing_preview_run_id': 'str'
    }

    attribute_map = {
        'success': 'success',
        'billing_preview_run_id': 'billingPreviewRunId'
    }

    def __init__(self, success=None, billing_preview_run_id=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger"""  # noqa: E501

        self._success = None
        self._billing_preview_run_id = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if billing_preview_run_id is not None:
            self.billing_preview_run_id = billing_preview_run_id

    @property
    def success(self):
        """Gets the success of this InlineResponse200.  # noqa: E501

        Returns `true` if the request was processed successfully.   # noqa: E501

        :return: The success of this InlineResponse200.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this InlineResponse200.

        Returns `true` if the request was processed successfully.   # noqa: E501

        :param success: The success of this InlineResponse200.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def billing_preview_run_id(self):
        """Gets the billing_preview_run_id of this InlineResponse200.  # noqa: E501

        Id of the billing preview run.   # noqa: E501

        :return: The billing_preview_run_id of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._billing_preview_run_id

    @billing_preview_run_id.setter
    def billing_preview_run_id(self, billing_preview_run_id):
        """Sets the billing_preview_run_id of this InlineResponse200.

        Id of the billing preview run.   # noqa: E501

        :param billing_preview_run_id: The billing_preview_run_id of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._billing_preview_run_id = billing_preview_run_id

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
        if issubclass(InlineResponse200, dict):
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
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
