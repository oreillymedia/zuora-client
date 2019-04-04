# coding: utf-8




import pprint
import re  # noqa: F401

import six


class ProxyGetCommunicationProfile(object):
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
        'created_by_id': 'str',
        'created_date': 'datetime',
        'description': 'str',
        'id': 'str',
        'profile_name': 'str',
        'updated_by_id': 'str',
        'updated_date': 'datetime'
    }

    attribute_map = {
        'created_by_id': 'CreatedById',
        'created_date': 'CreatedDate',
        'description': 'Description',
        'id': 'Id',
        'profile_name': 'ProfileName',
        'updated_by_id': 'UpdatedById',
        'updated_date': 'UpdatedDate'
    }

    def __init__(self, created_by_id=None, created_date=None, description=None, id=None, profile_name=None, updated_by_id=None, updated_date=None):  # noqa: E501
        """ProxyGetCommunicationProfile - a model defined in Swagger"""  # noqa: E501

        self._created_by_id = None
        self._created_date = None
        self._description = None
        self._id = None
        self._profile_name = None
        self._updated_by_id = None
        self._updated_date = None
        self.discriminator = None

        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_date is not None:
            self.created_date = created_date
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if profile_name is not None:
            self.profile_name = profile_name
        if updated_by_id is not None:
            self.updated_by_id = updated_by_id
        if updated_date is not None:
            self.updated_date = updated_date

    @property
    def created_by_id(self):
        """Gets the created_by_id of this ProxyGetCommunicationProfile.  # noqa: E501

          # noqa: E501

        :return: The created_by_id of this ProxyGetCommunicationProfile.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this ProxyGetCommunicationProfile.

          # noqa: E501

        :param created_by_id: The created_by_id of this ProxyGetCommunicationProfile.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def created_date(self):
        """Gets the created_date of this ProxyGetCommunicationProfile.  # noqa: E501

          # noqa: E501

        :return: The created_date of this ProxyGetCommunicationProfile.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this ProxyGetCommunicationProfile.

          # noqa: E501

        :param created_date: The created_date of this ProxyGetCommunicationProfile.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def description(self):
        """Gets the description of this ProxyGetCommunicationProfile.  # noqa: E501

          # noqa: E501

        :return: The description of this ProxyGetCommunicationProfile.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProxyGetCommunicationProfile.

          # noqa: E501

        :param description: The description of this ProxyGetCommunicationProfile.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this ProxyGetCommunicationProfile.  # noqa: E501

        Object identifier.  # noqa: E501

        :return: The id of this ProxyGetCommunicationProfile.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProxyGetCommunicationProfile.

        Object identifier.  # noqa: E501

        :param id: The id of this ProxyGetCommunicationProfile.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def profile_name(self):
        """Gets the profile_name of this ProxyGetCommunicationProfile.  # noqa: E501

          # noqa: E501

        :return: The profile_name of this ProxyGetCommunicationProfile.  # noqa: E501
        :rtype: str
        """
        return self._profile_name

    @profile_name.setter
    def profile_name(self, profile_name):
        """Sets the profile_name of this ProxyGetCommunicationProfile.

          # noqa: E501

        :param profile_name: The profile_name of this ProxyGetCommunicationProfile.  # noqa: E501
        :type: str
        """

        self._profile_name = profile_name

    @property
    def updated_by_id(self):
        """Gets the updated_by_id of this ProxyGetCommunicationProfile.  # noqa: E501

          # noqa: E501

        :return: The updated_by_id of this ProxyGetCommunicationProfile.  # noqa: E501
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """Sets the updated_by_id of this ProxyGetCommunicationProfile.

          # noqa: E501

        :param updated_by_id: The updated_by_id of this ProxyGetCommunicationProfile.  # noqa: E501
        :type: str
        """

        self._updated_by_id = updated_by_id

    @property
    def updated_date(self):
        """Gets the updated_date of this ProxyGetCommunicationProfile.  # noqa: E501

          # noqa: E501

        :return: The updated_date of this ProxyGetCommunicationProfile.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this ProxyGetCommunicationProfile.

          # noqa: E501

        :param updated_date: The updated_date of this ProxyGetCommunicationProfile.  # noqa: E501
        :type: datetime
        """

        self._updated_date = updated_date

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
        if issubclass(ProxyGetCommunicationProfile, dict):
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
        if not isinstance(other, ProxyGetCommunicationProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
