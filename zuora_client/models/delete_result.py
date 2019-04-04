# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.actions_error_response import ActionsErrorResponse  # noqa: F401,E501


class DeleteResult(object):
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
        'errors': 'list[ActionsErrorResponse]',
        'id': 'str',
        'success': 'bool'
    }

    attribute_map = {
        'errors': 'errors',
        'id': 'id',
        'success': 'success'
    }

    def __init__(self, errors=None, id=None, success=None):  # noqa: E501
        """DeleteResult - a model defined in Swagger"""  # noqa: E501

        self._errors = None
        self._id = None
        self._success = None
        self.discriminator = None

        if errors is not None:
            self.errors = errors
        if id is not None:
            self.id = id
        if success is not None:
            self.success = success

    @property
    def errors(self):
        """Gets the errors of this DeleteResult.  # noqa: E501

        If the delete failed, this contains an array of Error objects.   # noqa: E501

        :return: The errors of this DeleteResult.  # noqa: E501
        :rtype: list[ActionsErrorResponse]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this DeleteResult.

        If the delete failed, this contains an array of Error objects.   # noqa: E501

        :param errors: The errors of this DeleteResult.  # noqa: E501
        :type: list[ActionsErrorResponse]
        """

        self._errors = errors

    @property
    def id(self):
        """Gets the id of this DeleteResult.  # noqa: E501

        ID of the deleted object.   # noqa: E501

        :return: The id of this DeleteResult.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeleteResult.

        ID of the deleted object.   # noqa: E501

        :param id: The id of this DeleteResult.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def success(self):
        """Gets the success of this DeleteResult.  # noqa: E501

        A boolean field indicating the success of the delete operation. If the delete was successful, it is `true`. Otherwise, `false`.   # noqa: E501

        :return: The success of this DeleteResult.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this DeleteResult.

        A boolean field indicating the success of the delete operation. If the delete was successful, it is `true`. Otherwise, `false`.   # noqa: E501

        :param success: The success of this DeleteResult.  # noqa: E501
        :type: bool
        """

        self._success = success

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
        if issubclass(DeleteResult, dict):
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
        if not isinstance(other, DeleteResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
