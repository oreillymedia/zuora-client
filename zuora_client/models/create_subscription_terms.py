# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.create_order_create_subscription_terms_initial_term import CreateOrderCreateSubscriptionTermsInitialTerm  # noqa: F401,E501
from zuora_client.models.renewal_term import RenewalTerm  # noqa: F401,E501


class CreateSubscriptionTerms(object):
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
        'auto_renew': 'bool',
        'initial_term': 'CreateOrderCreateSubscriptionTermsInitialTerm',
        'renewal_setting': 'str',
        'renewal_terms': 'list[RenewalTerm]'
    }

    attribute_map = {
        'auto_renew': 'autoRenew',
        'initial_term': 'initialTerm',
        'renewal_setting': 'renewalSetting',
        'renewal_terms': 'renewalTerms'
    }

    def __init__(self, auto_renew=None, initial_term=None, renewal_setting=None, renewal_terms=None):  # noqa: E501
        """CreateSubscriptionTerms - a model defined in Swagger"""  # noqa: E501

        self._auto_renew = None
        self._initial_term = None
        self._renewal_setting = None
        self._renewal_terms = None
        self.discriminator = None

        if auto_renew is not None:
            self.auto_renew = auto_renew
        self.initial_term = initial_term
        if renewal_setting is not None:
            self.renewal_setting = renewal_setting
        self.renewal_terms = renewal_terms

    @property
    def auto_renew(self):
        """Gets the auto_renew of this CreateSubscriptionTerms.  # noqa: E501

        Specifies whether the subscription automatically renews at the end of the each term. Only applicable if the type of the first term is `TERMED`.   # noqa: E501

        :return: The auto_renew of this CreateSubscriptionTerms.  # noqa: E501
        :rtype: bool
        """
        return self._auto_renew

    @auto_renew.setter
    def auto_renew(self, auto_renew):
        """Sets the auto_renew of this CreateSubscriptionTerms.

        Specifies whether the subscription automatically renews at the end of the each term. Only applicable if the type of the first term is `TERMED`.   # noqa: E501

        :param auto_renew: The auto_renew of this CreateSubscriptionTerms.  # noqa: E501
        :type: bool
        """

        self._auto_renew = auto_renew

    @property
    def initial_term(self):
        """Gets the initial_term of this CreateSubscriptionTerms.  # noqa: E501


        :return: The initial_term of this CreateSubscriptionTerms.  # noqa: E501
        :rtype: CreateOrderCreateSubscriptionTermsInitialTerm
        """
        return self._initial_term

    @initial_term.setter
    def initial_term(self, initial_term):
        """Sets the initial_term of this CreateSubscriptionTerms.


        :param initial_term: The initial_term of this CreateSubscriptionTerms.  # noqa: E501
        :type: CreateOrderCreateSubscriptionTermsInitialTerm
        """
        if initial_term is None:
            raise ValueError("Invalid value for `initial_term`, must not be `None`")  # noqa: E501

        self._initial_term = initial_term

    @property
    def renewal_setting(self):
        """Gets the renewal_setting of this CreateSubscriptionTerms.  # noqa: E501

        Specifies the type of the terms that follow the first term if the subscription is renewed. Only applicable if the type of the first term is `TERMED`.  * `RENEW_WITH_SPECIFIC_TERM` - Each renewal term has a predefined duration. The first entry in `renewalTerms` specifies the duration of the second term of the subscription, the second entry in `renewalTerms` specifies the duration of the third term of the subscription, and so on. The last entry in `renewalTerms` specifies the ultimate duration of each renewal term. * `RENEW_TO_EVERGREEN` - The second term of the subscription does not have a predefined duration.   # noqa: E501

        :return: The renewal_setting of this CreateSubscriptionTerms.  # noqa: E501
        :rtype: str
        """
        return self._renewal_setting

    @renewal_setting.setter
    def renewal_setting(self, renewal_setting):
        """Sets the renewal_setting of this CreateSubscriptionTerms.

        Specifies the type of the terms that follow the first term if the subscription is renewed. Only applicable if the type of the first term is `TERMED`.  * `RENEW_WITH_SPECIFIC_TERM` - Each renewal term has a predefined duration. The first entry in `renewalTerms` specifies the duration of the second term of the subscription, the second entry in `renewalTerms` specifies the duration of the third term of the subscription, and so on. The last entry in `renewalTerms` specifies the ultimate duration of each renewal term. * `RENEW_TO_EVERGREEN` - The second term of the subscription does not have a predefined duration.   # noqa: E501

        :param renewal_setting: The renewal_setting of this CreateSubscriptionTerms.  # noqa: E501
        :type: str
        """
        allowed_values = ["RENEW_WITH_SPECIFIC_TERM", "RENEW_TO_EVERGREEN"]  # noqa: E501
        if renewal_setting not in allowed_values:
            raise ValueError(
                "Invalid value for `renewal_setting` ({0}), must be one of {1}"  # noqa: E501
                .format(renewal_setting, allowed_values)
            )

        self._renewal_setting = renewal_setting

    @property
    def renewal_terms(self):
        """Gets the renewal_terms of this CreateSubscriptionTerms.  # noqa: E501

        List of renewal terms of the subscription. Only applicable if the type of the first term is `TERMED` and the value of the `renewalSetting` field is `RENEW_WITH_SPECIFIC_TERM`.   # noqa: E501

        :return: The renewal_terms of this CreateSubscriptionTerms.  # noqa: E501
        :rtype: list[RenewalTerm]
        """
        return self._renewal_terms

    @renewal_terms.setter
    def renewal_terms(self, renewal_terms):
        """Sets the renewal_terms of this CreateSubscriptionTerms.

        List of renewal terms of the subscription. Only applicable if the type of the first term is `TERMED` and the value of the `renewalSetting` field is `RENEW_WITH_SPECIFIC_TERM`.   # noqa: E501

        :param renewal_terms: The renewal_terms of this CreateSubscriptionTerms.  # noqa: E501
        :type: list[RenewalTerm]
        """
        if renewal_terms is None:
            raise ValueError("Invalid value for `renewal_terms`, must not be `None`")  # noqa: E501

        self._renewal_terms = renewal_terms

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
        if issubclass(CreateSubscriptionTerms, dict):
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
        if not isinstance(other, CreateSubscriptionTerms):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
