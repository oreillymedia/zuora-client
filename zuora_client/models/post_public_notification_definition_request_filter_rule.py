# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.filter_rule_parameter_definitions import FilterRuleParameterDefinitions  # noqa: F401,E501


class POSTPublicNotificationDefinitionRequestFilterRule(object):
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
        'condition': 'str',
        'description': 'str',
        'parameters': 'FilterRuleParameterDefinitions'
    }

    attribute_map = {
        'condition': 'condition',
        'description': 'description',
        'parameters': 'parameters'
    }

    def __init__(self, condition=None, description=None, parameters=None):  # noqa: E501
        """POSTPublicNotificationDefinitionRequestFilterRule - a model defined in Swagger"""  # noqa: E501

        self._condition = None
        self._description = None
        self._parameters = None
        self.discriminator = None

        self.condition = condition
        if description is not None:
            self.description = description
        self.parameters = parameters

    @property
    def condition(self):
        """Gets the condition of this POSTPublicNotificationDefinitionRequestFilterRule.  # noqa: E501

        The filter rule conditions, written in [JEXL](http://commons.apache.org/proper/commons-jexl/). The rule might contain event context merge fields and data source merge fields. Data source merge fields must be from [the base object of the event or from the joined objects of the base object](https://knowledgecenter.zuora.com/DC_Developers/M_Export_ZOQL#Data_Sources_and_Objects). Notifications with invalid merge fields will fail to evaluate, thus will not be invoked. For example, to filter an invoice posted notification to only invoices with an amount over 1000, you would define the following condition:  ```Invoice.Amount > 1000```  There are conventions and keywords you need to be aware of. For example:  * `Invoice.Amount` refers to the `Amount` field of the Zuora object `Invoice`.  * Unlike Event Triggers, there is no access to variables with the `_old` suffix. Fields with the `_old` suffix are only available on Event Trigger conditions.   # noqa: E501

        :return: The condition of this POSTPublicNotificationDefinitionRequestFilterRule.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this POSTPublicNotificationDefinitionRequestFilterRule.

        The filter rule conditions, written in [JEXL](http://commons.apache.org/proper/commons-jexl/). The rule might contain event context merge fields and data source merge fields. Data source merge fields must be from [the base object of the event or from the joined objects of the base object](https://knowledgecenter.zuora.com/DC_Developers/M_Export_ZOQL#Data_Sources_and_Objects). Notifications with invalid merge fields will fail to evaluate, thus will not be invoked. For example, to filter an invoice posted notification to only invoices with an amount over 1000, you would define the following condition:  ```Invoice.Amount > 1000```  There are conventions and keywords you need to be aware of. For example:  * `Invoice.Amount` refers to the `Amount` field of the Zuora object `Invoice`.  * Unlike Event Triggers, there is no access to variables with the `_old` suffix. Fields with the `_old` suffix are only available on Event Trigger conditions.   # noqa: E501

        :param condition: The condition of this POSTPublicNotificationDefinitionRequestFilterRule.  # noqa: E501
        :type: str
        """
        if condition is None:
            raise ValueError("Invalid value for `condition`, must not be `None`")  # noqa: E501

        self._condition = condition

    @property
    def description(self):
        """Gets the description of this POSTPublicNotificationDefinitionRequestFilterRule.  # noqa: E501

        The description of the filter rule.  # noqa: E501

        :return: The description of this POSTPublicNotificationDefinitionRequestFilterRule.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this POSTPublicNotificationDefinitionRequestFilterRule.

        The description of the filter rule.  # noqa: E501

        :param description: The description of this POSTPublicNotificationDefinitionRequestFilterRule.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501

        self._description = description

    @property
    def parameters(self):
        """Gets the parameters of this POSTPublicNotificationDefinitionRequestFilterRule.  # noqa: E501


        :return: The parameters of this POSTPublicNotificationDefinitionRequestFilterRule.  # noqa: E501
        :rtype: FilterRuleParameterDefinitions
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this POSTPublicNotificationDefinitionRequestFilterRule.


        :param parameters: The parameters of this POSTPublicNotificationDefinitionRequestFilterRule.  # noqa: E501
        :type: FilterRuleParameterDefinitions
        """
        if parameters is None:
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters

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
        if issubclass(POSTPublicNotificationDefinitionRequestFilterRule, dict):
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
        if not isinstance(other, POSTPublicNotificationDefinitionRequestFilterRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
