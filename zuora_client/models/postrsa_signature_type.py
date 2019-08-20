# coding: utf-8




import pprint
import re  # noqa: F401

import six


class POSTRSASignatureType(object):
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
        'method': 'str',
        'page_id': 'str',
        'uri': 'str'
    }

    attribute_map = {
        'method': 'method',
        'page_id': 'pageId',
        'uri': 'uri'
    }

    def __init__(self, method=None, page_id=None, uri=None):  # noqa: E501
        """POSTRSASignatureType - a model defined in Swagger"""  # noqa: E501

        self._method = None
        self._page_id = None
        self._uri = None
        self.discriminator = None

        self.method = method
        self.page_id = page_id
        self.uri = uri

    @property
    def method(self):
        """Gets the method of this POSTRSASignatureType.  # noqa: E501

        The type of the request. Set it to POST.   # noqa: E501

        :return: The method of this POSTRSASignatureType.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this POSTRSASignatureType.

        The type of the request. Set it to POST.   # noqa: E501

        :param method: The method of this POSTRSASignatureType.  # noqa: E501
        :type: str
        """
        if method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501

        self._method = method

    @property
    def page_id(self):
        """Gets the page_id of this POSTRSASignatureType.  # noqa: E501

        The page id of your Payment Pages 2.0 form. Click **Show Page Id** next to the Payment Page name in the Hosted Page List to retrieve the page id.   # noqa: E501

        :return: The page_id of this POSTRSASignatureType.  # noqa: E501
        :rtype: str
        """
        return self._page_id

    @page_id.setter
    def page_id(self, page_id):
        """Sets the page_id of this POSTRSASignatureType.

        The page id of your Payment Pages 2.0 form. Click **Show Page Id** next to the Payment Page name in the Hosted Page List to retrieve the page id.   # noqa: E501

        :param page_id: The page_id of this POSTRSASignatureType.  # noqa: E501
        :type: str
        """
        if page_id is None:
            raise ValueError("Invalid value for `page_id`, must not be `None`")  # noqa: E501

        self._page_id = page_id

    @property
    def uri(self):
        """Gets the uri of this POSTRSASignatureType.  # noqa: E501

        The URL that the Payment Page will be served from. Set it to:  * https://www.zuora.com/apps/PublicHostedPageLite.do if you are on the production environment. * https://apisandbox.zuora.com/apps/PublicHostedPageLite.do if you are on the API Sandbox environment.   # noqa: E501

        :return: The uri of this POSTRSASignatureType.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this POSTRSASignatureType.

        The URL that the Payment Page will be served from. Set it to:  * https://www.zuora.com/apps/PublicHostedPageLite.do if you are on the production environment. * https://apisandbox.zuora.com/apps/PublicHostedPageLite.do if you are on the API Sandbox environment.   # noqa: E501

        :param uri: The uri of this POSTRSASignatureType.  # noqa: E501
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

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
        if issubclass(POSTRSASignatureType, dict):
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
        if not isinstance(other, POSTRSASignatureType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
