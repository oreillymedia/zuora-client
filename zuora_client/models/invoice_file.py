# coding: utf-8




import pprint
import re  # noqa: F401

import six


class InvoiceFile(object):
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
        'id': 'str',
        'pdf_file_url': 'str',
        'version_number': 'int'
    }

    attribute_map = {
        'id': 'id',
        'pdf_file_url': 'pdfFileUrl',
        'version_number': 'versionNumber'
    }

    def __init__(self, id=None, pdf_file_url=None, version_number=None):  # noqa: E501
        """InvoiceFile - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._pdf_file_url = None
        self._version_number = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if pdf_file_url is not None:
            self.pdf_file_url = pdf_file_url
        if version_number is not None:
            self.version_number = version_number

    @property
    def id(self):
        """Gets the id of this InvoiceFile.  # noqa: E501

        The ID of the invoice PDF file. This is the ID for the file object and different from the file handle ID in the `pdfFileUrl` field. To open a file, you have to use the file handle ID.   # noqa: E501

        :return: The id of this InvoiceFile.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InvoiceFile.

        The ID of the invoice PDF file. This is the ID for the file object and different from the file handle ID in the `pdfFileUrl` field. To open a file, you have to use the file handle ID.   # noqa: E501

        :param id: The id of this InvoiceFile.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def pdf_file_url(self):
        """Gets the pdf_file_url of this InvoiceFile.  # noqa: E501

        The REST URL for the invoice PDF file. Click the URL to open the invoice PDF file.   # noqa: E501

        :return: The pdf_file_url of this InvoiceFile.  # noqa: E501
        :rtype: str
        """
        return self._pdf_file_url

    @pdf_file_url.setter
    def pdf_file_url(self, pdf_file_url):
        """Sets the pdf_file_url of this InvoiceFile.

        The REST URL for the invoice PDF file. Click the URL to open the invoice PDF file.   # noqa: E501

        :param pdf_file_url: The pdf_file_url of this InvoiceFile.  # noqa: E501
        :type: str
        """

        self._pdf_file_url = pdf_file_url

    @property
    def version_number(self):
        """Gets the version_number of this InvoiceFile.  # noqa: E501

        The version number of the invoice PDF file.   # noqa: E501

        :return: The version_number of this InvoiceFile.  # noqa: E501
        :rtype: int
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """Sets the version_number of this InvoiceFile.

        The version number of the invoice PDF file.   # noqa: E501

        :param version_number: The version_number of this InvoiceFile.  # noqa: E501
        :type: int
        """

        self._version_number = version_number

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
        if issubclass(InvoiceFile, dict):
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
        if not isinstance(other, InvoiceFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
