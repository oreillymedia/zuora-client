# coding: utf-8




import pprint
import re  # noqa: F401

import six


class PUTOrderActionTriggerDatesRequestTypeTriggerDates(object):
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
        'name': 'str',
        'trigger_date': 'date'
    }

    attribute_map = {
        'name': 'name',
        'trigger_date': 'triggerDate'
    }

    def __init__(self, name=None, trigger_date=None):  # noqa: E501
        """PUTOrderActionTriggerDatesRequestTypeTriggerDates - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._trigger_date = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if trigger_date is not None:
            self.trigger_date = trigger_date

    @property
    def name(self):
        """Gets the name of this PUTOrderActionTriggerDatesRequestTypeTriggerDates.  # noqa: E501

        Name of the trigger date of the order action.  # noqa: E501

        :return: The name of this PUTOrderActionTriggerDatesRequestTypeTriggerDates.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PUTOrderActionTriggerDatesRequestTypeTriggerDates.

        Name of the trigger date of the order action.  # noqa: E501

        :param name: The name of this PUTOrderActionTriggerDatesRequestTypeTriggerDates.  # noqa: E501
        :type: str
        """
        allowed_values = ["ServiceActivation", "CustomerAcceptance"]  # noqa: E501
        if name not in allowed_values:
            raise ValueError(
                "Invalid value for `name` ({0}), must be one of {1}"  # noqa: E501
                .format(name, allowed_values)
            )

        self._name = name

    @property
    def trigger_date(self):
        """Gets the trigger_date of this PUTOrderActionTriggerDatesRequestTypeTriggerDates.  # noqa: E501

        Trigger date in YYYY-MM-DD format. The date you are to set as the service activation date or the customer acceptance date.   # noqa: E501

        :return: The trigger_date of this PUTOrderActionTriggerDatesRequestTypeTriggerDates.  # noqa: E501
        :rtype: date
        """
        return self._trigger_date

    @trigger_date.setter
    def trigger_date(self, trigger_date):
        """Sets the trigger_date of this PUTOrderActionTriggerDatesRequestTypeTriggerDates.

        Trigger date in YYYY-MM-DD format. The date you are to set as the service activation date or the customer acceptance date.   # noqa: E501

        :param trigger_date: The trigger_date of this PUTOrderActionTriggerDatesRequestTypeTriggerDates.  # noqa: E501
        :type: date
        """

        self._trigger_date = trigger_date

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
        if issubclass(PUTOrderActionTriggerDatesRequestTypeTriggerDates, dict):
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
        if not isinstance(other, PUTOrderActionTriggerDatesRequestTypeTriggerDates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
