# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.get_refund_typewith_success import GETRefundTypewithSuccess  # noqa: F401,E501


class GETRefundCollectionType(object):
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
        'next_page': 'str',
        'refunds': 'list[GETRefundTypewithSuccess]',
        'success': 'bool'
    }

    attribute_map = {
        'next_page': 'nextPage',
        'refunds': 'refunds',
        'success': 'success'
    }

    def __init__(self, next_page=None, refunds=None, success=None):  # noqa: E501
        """GETRefundCollectionType - a model defined in Swagger"""  # noqa: E501

        self._next_page = None
        self._refunds = None
        self._success = None
        self.discriminator = None

        if next_page is not None:
            self.next_page = next_page
        if refunds is not None:
            self.refunds = refunds
        if success is not None:
            self.success = success

    @property
    def next_page(self):
        """Gets the next_page of this GETRefundCollectionType.  # noqa: E501

        URL to retrieve the next page of the response if it exists; otherwise absent.   # noqa: E501

        :return: The next_page of this GETRefundCollectionType.  # noqa: E501
        :rtype: str
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this GETRefundCollectionType.

        URL to retrieve the next page of the response if it exists; otherwise absent.   # noqa: E501

        :param next_page: The next_page of this GETRefundCollectionType.  # noqa: E501
        :type: str
        """

        self._next_page = next_page

    @property
    def refunds(self):
        """Gets the refunds of this GETRefundCollectionType.  # noqa: E501

        Container for refunds.   # noqa: E501

        :return: The refunds of this GETRefundCollectionType.  # noqa: E501
        :rtype: list[GETRefundTypewithSuccess]
        """
        return self._refunds

    @refunds.setter
    def refunds(self, refunds):
        """Sets the refunds of this GETRefundCollectionType.

        Container for refunds.   # noqa: E501

        :param refunds: The refunds of this GETRefundCollectionType.  # noqa: E501
        :type: list[GETRefundTypewithSuccess]
        """

        self._refunds = refunds

    @property
    def success(self):
        """Gets the success of this GETRefundCollectionType.  # noqa: E501

        Returns `true` if the request was processed successfully.  # noqa: E501

        :return: The success of this GETRefundCollectionType.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this GETRefundCollectionType.

        Returns `true` if the request was processed successfully.  # noqa: E501

        :param success: The success of this GETRefundCollectionType.  # noqa: E501
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
        if issubclass(GETRefundCollectionType, dict):
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
        if not isinstance(other, GETRefundCollectionType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
