# coding: utf-8




import pprint
import re  # noqa: F401

import six


class PUTSendUserAccessRequestType(object):
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
        'target_entity_ids': 'list[str]'
    }

    attribute_map = {
        'target_entity_ids': 'targetEntityIds'
    }

    def __init__(self, target_entity_ids=None):  # noqa: E501
        """PUTSendUserAccessRequestType - a model defined in Swagger"""  # noqa: E501

        self._target_entity_ids = None
        self.discriminator = None

        self.target_entity_ids = target_entity_ids

    @property
    def target_entity_ids(self):
        """Gets the target_entity_ids of this PUTSendUserAccessRequestType.  # noqa: E501

        The ID of the entities that the user wants to access.   # noqa: E501

        :return: The target_entity_ids of this PUTSendUserAccessRequestType.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_entity_ids

    @target_entity_ids.setter
    def target_entity_ids(self, target_entity_ids):
        """Sets the target_entity_ids of this PUTSendUserAccessRequestType.

        The ID of the entities that the user wants to access.   # noqa: E501

        :param target_entity_ids: The target_entity_ids of this PUTSendUserAccessRequestType.  # noqa: E501
        :type: list[str]
        """
        if target_entity_ids is None:
            raise ValueError("Invalid value for `target_entity_ids`, must not be `None`")  # noqa: E501

        self._target_entity_ids = target_entity_ids

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
        if issubclass(PUTSendUserAccessRequestType, dict):
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
        if not isinstance(other, PUTSendUserAccessRequestType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
