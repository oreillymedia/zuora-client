# coding: utf-8




import pprint
import re  # noqa: F401

import six


class CreateEntityResponseType(object):
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
        'display_name': 'str',
        'id': 'str',
        'locale': 'str',
        'name': 'str',
        'parent_id': 'str',
        'status': 'str',
        'success': 'bool',
        'tenant_id': 'str',
        'timezone': 'str'
    }

    attribute_map = {
        'display_name': 'displayName',
        'id': 'id',
        'locale': 'locale',
        'name': 'name',
        'parent_id': 'parentId',
        'status': 'status',
        'success': 'success',
        'tenant_id': 'tenantId',
        'timezone': 'timezone'
    }

    def __init__(self, display_name=None, id=None, locale=None, name=None, parent_id=None, status=None, success=None, tenant_id=None, timezone=None):  # noqa: E501
        """CreateEntityResponseType - a model defined in Swagger"""  # noqa: E501

        self._display_name = None
        self._id = None
        self._locale = None
        self._name = None
        self._parent_id = None
        self._status = None
        self._success = None
        self._tenant_id = None
        self._timezone = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        if id is not None:
            self.id = id
        if locale is not None:
            self.locale = locale
        if name is not None:
            self.name = name
        if parent_id is not None:
            self.parent_id = parent_id
        if status is not None:
            self.status = status
        if success is not None:
            self.success = success
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if timezone is not None:
            self.timezone = timezone

    @property
    def display_name(self):
        """Gets the display_name of this CreateEntityResponseType.  # noqa: E501

        The display name of the entity that is shown in the Zuora UI and APIs.  # noqa: E501

        :return: The display_name of this CreateEntityResponseType.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CreateEntityResponseType.

        The display name of the entity that is shown in the Zuora UI and APIs.  # noqa: E501

        :param display_name: The display_name of this CreateEntityResponseType.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this CreateEntityResponseType.  # noqa: E501

        The entity Id.  # noqa: E501

        :return: The id of this CreateEntityResponseType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateEntityResponseType.

        The entity Id.  # noqa: E501

        :param id: The id of this CreateEntityResponseType.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def locale(self):
        """Gets the locale of this CreateEntityResponseType.  # noqa: E501

        The locale that is used in this entity.  # noqa: E501

        :return: The locale of this CreateEntityResponseType.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this CreateEntityResponseType.

        The locale that is used in this entity.  # noqa: E501

        :param locale: The locale of this CreateEntityResponseType.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def name(self):
        """Gets the name of this CreateEntityResponseType.  # noqa: E501

        The name of the entity.  # noqa: E501

        :return: The name of this CreateEntityResponseType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateEntityResponseType.

        The name of the entity.  # noqa: E501

        :param name: The name of this CreateEntityResponseType.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parent_id(self):
        """Gets the parent_id of this CreateEntityResponseType.  # noqa: E501

        The Id of the parent entity.  # noqa: E501

        :return: The parent_id of this CreateEntityResponseType.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this CreateEntityResponseType.

        The Id of the parent entity.  # noqa: E501

        :param parent_id: The parent_id of this CreateEntityResponseType.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def status(self):
        """Gets the status of this CreateEntityResponseType.  # noqa: E501

        The status of the entity.  # noqa: E501

        :return: The status of this CreateEntityResponseType.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateEntityResponseType.

        The status of the entity.  # noqa: E501

        :param status: The status of this CreateEntityResponseType.  # noqa: E501
        :type: str
        """
        allowed_values = ["Provisioned", "Unprovisioned"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def success(self):
        """Gets the success of this CreateEntityResponseType.  # noqa: E501

        Returns `true` if the request is successful.  # noqa: E501

        :return: The success of this CreateEntityResponseType.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this CreateEntityResponseType.

        Returns `true` if the request is successful.  # noqa: E501

        :param success: The success of this CreateEntityResponseType.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def tenant_id(self):
        """Gets the tenant_id of this CreateEntityResponseType.  # noqa: E501

        The Id of the tenant that the entity belongs to.  # noqa: E501

        :return: The tenant_id of this CreateEntityResponseType.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this CreateEntityResponseType.

        The Id of the tenant that the entity belongs to.  # noqa: E501

        :param tenant_id: The tenant_id of this CreateEntityResponseType.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def timezone(self):
        """Gets the timezone of this CreateEntityResponseType.  # noqa: E501

        The time zone that is used in this entity.  # noqa: E501

        :return: The timezone of this CreateEntityResponseType.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this CreateEntityResponseType.

        The time zone that is used in this entity.  # noqa: E501

        :param timezone: The timezone of this CreateEntityResponseType.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

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
        if issubclass(CreateEntityResponseType, dict):
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
        if not isinstance(other, CreateEntityResponseType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
