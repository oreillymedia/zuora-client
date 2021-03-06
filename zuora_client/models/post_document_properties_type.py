# coding: utf-8




import pprint
import re  # noqa: F401

import six


class POSTDocumentPropertiesType(object):
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
        'custom_file_name': 'str',
        'document_id': 'str',
        'document_type': 'str'
    }

    attribute_map = {
        'custom_file_name': 'customFileName',
        'document_id': 'documentId',
        'document_type': 'documentType'
    }

    def __init__(self, custom_file_name=None, document_id=None, document_type=None):  # noqa: E501
        """POSTDocumentPropertiesType - a model defined in Swagger"""  # noqa: E501

        self._custom_file_name = None
        self._document_id = None
        self._document_type = None
        self.discriminator = None

        if custom_file_name is not None:
            self.custom_file_name = custom_file_name
        if document_id is not None:
            self.document_id = document_id
        if document_type is not None:
            self.document_type = document_type

    @property
    def custom_file_name(self):
        """Gets the custom_file_name of this POSTDocumentPropertiesType.  # noqa: E501

        The custom file name to use to generate new Word or PDF files for the billing document.   # noqa: E501

        :return: The custom_file_name of this POSTDocumentPropertiesType.  # noqa: E501
        :rtype: str
        """
        return self._custom_file_name

    @custom_file_name.setter
    def custom_file_name(self, custom_file_name):
        """Sets the custom_file_name of this POSTDocumentPropertiesType.

        The custom file name to use to generate new Word or PDF files for the billing document.   # noqa: E501

        :param custom_file_name: The custom_file_name of this POSTDocumentPropertiesType.  # noqa: E501
        :type: str
        """

        self._custom_file_name = custom_file_name

    @property
    def document_id(self):
        """Gets the document_id of this POSTDocumentPropertiesType.  # noqa: E501

        The unique ID of a billing document that you want to create document properties for.   # noqa: E501

        :return: The document_id of this POSTDocumentPropertiesType.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this POSTDocumentPropertiesType.

        The unique ID of a billing document that you want to create document properties for.   # noqa: E501

        :param document_id: The document_id of this POSTDocumentPropertiesType.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def document_type(self):
        """Gets the document_type of this POSTDocumentPropertiesType.  # noqa: E501

        The type of the billing document.    # noqa: E501

        :return: The document_type of this POSTDocumentPropertiesType.  # noqa: E501
        :rtype: str
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """Sets the document_type of this POSTDocumentPropertiesType.

        The type of the billing document.    # noqa: E501

        :param document_type: The document_type of this POSTDocumentPropertiesType.  # noqa: E501
        :type: str
        """
        allowed_values = ["Invoice", "CreditMemo", "DebitMemo"]  # noqa: E501
        if document_type not in allowed_values:
            raise ValueError(
                "Invalid value for `document_type` ({0}), must be one of {1}"  # noqa: E501
                .format(document_type, allowed_values)
            )

        self._document_type = document_type

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
        if issubclass(POSTDocumentPropertiesType, dict):
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
        if not isinstance(other, POSTDocumentPropertiesType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
