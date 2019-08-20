# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.getrs_detail_without_success_type import GETRSDetailWithoutSuccessType  # noqa: F401,E501


class GETRSDetailsByChargeType(object):
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
        'revenue_schedules': 'list[GETRSDetailWithoutSuccessType]',
        'success': 'bool'
    }

    attribute_map = {
        'next_page': 'nextPage',
        'revenue_schedules': 'revenueSchedules',
        'success': 'success'
    }

    def __init__(self, next_page=None, revenue_schedules=None, success=None):  # noqa: E501
        """GETRSDetailsByChargeType - a model defined in Swagger"""  # noqa: E501

        self._next_page = None
        self._revenue_schedules = None
        self._success = None
        self.discriminator = None

        if next_page is not None:
            self.next_page = next_page
        if revenue_schedules is not None:
            self.revenue_schedules = revenue_schedules
        if success is not None:
            self.success = success

    @property
    def next_page(self):
        """Gets the next_page of this GETRSDetailsByChargeType.  # noqa: E501

        URL to retrieve the next page of the response if it exists; otherwise absent.   # noqa: E501

        :return: The next_page of this GETRSDetailsByChargeType.  # noqa: E501
        :rtype: str
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this GETRSDetailsByChargeType.

        URL to retrieve the next page of the response if it exists; otherwise absent.   # noqa: E501

        :param next_page: The next_page of this GETRSDetailsByChargeType.  # noqa: E501
        :type: str
        """

        self._next_page = next_page

    @property
    def revenue_schedules(self):
        """Gets the revenue_schedules of this GETRSDetailsByChargeType.  # noqa: E501

        Represents how revenue will be recognized over time.  This contains the details of a revenue schedule. If you do not specify the `pageSize` variable, the default number of revenue schedules returned per invocation is 8, and if there are more than 8 revenue schedules to be returned, the `nextPage` field will provide a hyperlink to view the next page(s) of revenue events. The order of revenue schedules is descending by the `updatedOn` field.   # noqa: E501

        :return: The revenue_schedules of this GETRSDetailsByChargeType.  # noqa: E501
        :rtype: list[GETRSDetailWithoutSuccessType]
        """
        return self._revenue_schedules

    @revenue_schedules.setter
    def revenue_schedules(self, revenue_schedules):
        """Sets the revenue_schedules of this GETRSDetailsByChargeType.

        Represents how revenue will be recognized over time.  This contains the details of a revenue schedule. If you do not specify the `pageSize` variable, the default number of revenue schedules returned per invocation is 8, and if there are more than 8 revenue schedules to be returned, the `nextPage` field will provide a hyperlink to view the next page(s) of revenue events. The order of revenue schedules is descending by the `updatedOn` field.   # noqa: E501

        :param revenue_schedules: The revenue_schedules of this GETRSDetailsByChargeType.  # noqa: E501
        :type: list[GETRSDetailWithoutSuccessType]
        """

        self._revenue_schedules = revenue_schedules

    @property
    def success(self):
        """Gets the success of this GETRSDetailsByChargeType.  # noqa: E501

        Returns `true` if the request was processed successfully.   # noqa: E501

        :return: The success of this GETRSDetailsByChargeType.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this GETRSDetailsByChargeType.

        Returns `true` if the request was processed successfully.   # noqa: E501

        :param success: The success of this GETRSDetailsByChargeType.  # noqa: E501
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
        if issubclass(GETRSDetailsByChargeType, dict):
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
        if not isinstance(other, GETRSDetailsByChargeType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other