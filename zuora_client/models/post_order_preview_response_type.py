# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.common_response_type import CommonResponseType  # noqa: F401,E501
from zuora_client.models.preview_result import PreviewResult  # noqa: F401,E501


class PostOrderPreviewResponseType(object):
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
        'preview_result': 'PreviewResult'
    }

    attribute_map = {
        'success': 'success',
        'preview_result': 'previewResult'
    }

    def __init__(self, success=None, preview_result=None):  # noqa: E501
        """PostOrderPreviewResponseType - a model defined in Swagger"""  # noqa: E501

        self._success = None
        self._preview_result = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if preview_result is not None:
            self.preview_result = preview_result

    @property
    def success(self):
        """Gets the success of this PostOrderPreviewResponseType.  # noqa: E501

        Indicates whether the call succeeded.   # noqa: E501

        :return: The success of this PostOrderPreviewResponseType.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this PostOrderPreviewResponseType.

        Indicates whether the call succeeded.   # noqa: E501

        :param success: The success of this PostOrderPreviewResponseType.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def preview_result(self):
        """Gets the preview_result of this PostOrderPreviewResponseType.  # noqa: E501


        :return: The preview_result of this PostOrderPreviewResponseType.  # noqa: E501
        :rtype: PreviewResult
        """
        return self._preview_result

    @preview_result.setter
    def preview_result(self, preview_result):
        """Sets the preview_result of this PostOrderPreviewResponseType.


        :param preview_result: The preview_result of this PostOrderPreviewResponseType.  # noqa: E501
        :type: PreviewResult
        """

        self._preview_result = preview_result

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
        if issubclass(PostOrderPreviewResponseType, dict):
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
        if not isinstance(other, PostOrderPreviewResponseType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
