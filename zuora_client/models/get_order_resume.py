# coding: utf-8




import pprint
import re  # noqa: F401

import six


class GetOrderResume(object):
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
        'extends_term': 'bool',
        'resume_date': 'date',
        'resume_periods': 'int',
        'resume_periods_type': 'str',
        'resume_policy': 'str',
        'resume_specific_date': 'date'
    }

    attribute_map = {
        'extends_term': 'extendsTerm',
        'resume_date': 'resumeDate',
        'resume_periods': 'resumePeriods',
        'resume_periods_type': 'resumePeriodsType',
        'resume_policy': 'resumePolicy',
        'resume_specific_date': 'resumeSpecificDate'
    }

    def __init__(self, extends_term=None, resume_date=None, resume_periods=None, resume_periods_type=None, resume_policy=None, resume_specific_date=None):  # noqa: E501
        """GetOrderResume - a model defined in Swagger"""  # noqa: E501

        self._extends_term = None
        self._resume_date = None
        self._resume_periods = None
        self._resume_periods_type = None
        self._resume_policy = None
        self._resume_specific_date = None
        self.discriminator = None

        if extends_term is not None:
            self.extends_term = extends_term
        if resume_date is not None:
            self.resume_date = resume_date
        if resume_periods is not None:
            self.resume_periods = resume_periods
        if resume_periods_type is not None:
            self.resume_periods_type = resume_periods_type
        if resume_policy is not None:
            self.resume_policy = resume_policy
        if resume_specific_date is not None:
            self.resume_specific_date = resume_specific_date

    @property
    def extends_term(self):
        """Gets the extends_term of this GetOrderResume.  # noqa: E501

        Specifies whether to extend the subscription term by the length of time the suspension is in effect. Note this field is not applicable in a Resume order action auto-created by the Order Metrics migration.   # noqa: E501

        :return: The extends_term of this GetOrderResume.  # noqa: E501
        :rtype: bool
        """
        return self._extends_term

    @extends_term.setter
    def extends_term(self, extends_term):
        """Sets the extends_term of this GetOrderResume.

        Specifies whether to extend the subscription term by the length of time the suspension is in effect. Note this field is not applicable in a Resume order action auto-created by the Order Metrics migration.   # noqa: E501

        :param extends_term: The extends_term of this GetOrderResume.  # noqa: E501
        :type: bool
        """

        self._extends_term = extends_term

    @property
    def resume_date(self):
        """Gets the resume_date of this GetOrderResume.  # noqa: E501

        The resume date when the resumption takes effect.   # noqa: E501

        :return: The resume_date of this GetOrderResume.  # noqa: E501
        :rtype: date
        """
        return self._resume_date

    @resume_date.setter
    def resume_date(self, resume_date):
        """Sets the resume_date of this GetOrderResume.

        The resume date when the resumption takes effect.   # noqa: E501

        :param resume_date: The resume_date of this GetOrderResume.  # noqa: E501
        :type: date
        """

        self._resume_date = resume_date

    @property
    def resume_periods(self):
        """Gets the resume_periods of this GetOrderResume.  # noqa: E501

        This field is applicable only when the `suspendPolicy` field is set to `FixedPeriodsFromToday` or `FixedPeriodsFromSuspendDate`. It must be used together with the `resumePeriodsType` field. Note this field is not applicable in a Resume order action auto-created by the Order Metrics migration.  The total number of the periods used to specify when a subscription resumption takes effect. The subscription resumption will take place after the specified time frame (`suspendPeriods` multiplied by `suspendPeriodsType`) from today's date.    # noqa: E501

        :return: The resume_periods of this GetOrderResume.  # noqa: E501
        :rtype: int
        """
        return self._resume_periods

    @resume_periods.setter
    def resume_periods(self, resume_periods):
        """Sets the resume_periods of this GetOrderResume.

        This field is applicable only when the `suspendPolicy` field is set to `FixedPeriodsFromToday` or `FixedPeriodsFromSuspendDate`. It must be used together with the `resumePeriodsType` field. Note this field is not applicable in a Resume order action auto-created by the Order Metrics migration.  The total number of the periods used to specify when a subscription resumption takes effect. The subscription resumption will take place after the specified time frame (`suspendPeriods` multiplied by `suspendPeriodsType`) from today's date.    # noqa: E501

        :param resume_periods: The resume_periods of this GetOrderResume.  # noqa: E501
        :type: int
        """

        self._resume_periods = resume_periods

    @property
    def resume_periods_type(self):
        """Gets the resume_periods_type of this GetOrderResume.  # noqa: E501

        This field is applicable only when the `suspendPolicy` field is set to `FixedPeriodsFromToday` or `FixedPeriodsFromSuspendDate`. It must be used together with the `resumePeriods` field. Note this field is not applicable in a Resume order action auto-created by the Order Metrics migration.  The period type used to specify when a subscription resumption takes effect. The subscription suspension will take place after the specified time frame (`suspendPeriods` multiplied by `suspendPeriodsType`) from today's date.    # noqa: E501

        :return: The resume_periods_type of this GetOrderResume.  # noqa: E501
        :rtype: str
        """
        return self._resume_periods_type

    @resume_periods_type.setter
    def resume_periods_type(self, resume_periods_type):
        """Sets the resume_periods_type of this GetOrderResume.

        This field is applicable only when the `suspendPolicy` field is set to `FixedPeriodsFromToday` or `FixedPeriodsFromSuspendDate`. It must be used together with the `resumePeriods` field. Note this field is not applicable in a Resume order action auto-created by the Order Metrics migration.  The period type used to specify when a subscription resumption takes effect. The subscription suspension will take place after the specified time frame (`suspendPeriods` multiplied by `suspendPeriodsType`) from today's date.    # noqa: E501

        :param resume_periods_type: The resume_periods_type of this GetOrderResume.  # noqa: E501
        :type: str
        """
        allowed_values = ["Day", "Week", "Month", "Year"]  # noqa: E501
        if resume_periods_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resume_periods_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resume_periods_type, allowed_values)
            )

        self._resume_periods_type = resume_periods_type

    @property
    def resume_policy(self):
        """Gets the resume_policy of this GetOrderResume.  # noqa: E501

        Resume methods. Specify a way to resume a subscription. See [Resume Date](https://knowledgecenter.zuora.com/BC_Subscription_Management/Subscriptions/Resume_a_Subscription#Resume_Date) for more information. Note this field is not applicable in a Resume order action auto-created by the Order Metrics migration.  If `SuspendDate` is specfied, the resumption will take place on the same day as the suspension.    # noqa: E501

        :return: The resume_policy of this GetOrderResume.  # noqa: E501
        :rtype: str
        """
        return self._resume_policy

    @resume_policy.setter
    def resume_policy(self, resume_policy):
        """Sets the resume_policy of this GetOrderResume.

        Resume methods. Specify a way to resume a subscription. See [Resume Date](https://knowledgecenter.zuora.com/BC_Subscription_Management/Subscriptions/Resume_a_Subscription#Resume_Date) for more information. Note this field is not applicable in a Resume order action auto-created by the Order Metrics migration.  If `SuspendDate` is specfied, the resumption will take place on the same day as the suspension.    # noqa: E501

        :param resume_policy: The resume_policy of this GetOrderResume.  # noqa: E501
        :type: str
        """
        allowed_values = ["Today", "FixedPeriodsFromSuspendDate", "FixedPeriodsFromToday", "SpecificDate", "SuspendDate"]  # noqa: E501
        if resume_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `resume_policy` ({0}), must be one of {1}"  # noqa: E501
                .format(resume_policy, allowed_values)
            )

        self._resume_policy = resume_policy

    @property
    def resume_specific_date(self):
        """Gets the resume_specific_date of this GetOrderResume.  # noqa: E501

        This field is applicable only when the `resumePolicy` field is set to `SpecificDate`. Note this field is not applicable in a Resume order action auto-created by the Order Metrics migration.  A specific date when the subscription resumption takes effect, in YYYY-MM-DD format. The value should not be earlier than the subscription suspension date.   # noqa: E501

        :return: The resume_specific_date of this GetOrderResume.  # noqa: E501
        :rtype: date
        """
        return self._resume_specific_date

    @resume_specific_date.setter
    def resume_specific_date(self, resume_specific_date):
        """Sets the resume_specific_date of this GetOrderResume.

        This field is applicable only when the `resumePolicy` field is set to `SpecificDate`. Note this field is not applicable in a Resume order action auto-created by the Order Metrics migration.  A specific date when the subscription resumption takes effect, in YYYY-MM-DD format. The value should not be earlier than the subscription suspension date.   # noqa: E501

        :param resume_specific_date: The resume_specific_date of this GetOrderResume.  # noqa: E501
        :type: date
        """

        self._resume_specific_date = resume_specific_date

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
        if issubclass(GetOrderResume, dict):
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
        if not isinstance(other, GetOrderResume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
