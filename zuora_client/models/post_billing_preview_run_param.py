# coding: utf-8




import pprint
import re  # noqa: F401

import six


class PostBillingPreviewRunParam(object):
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
        'assume_renewal': 'str',
        'batch': 'str',
        'charge_type_to_exclude': 'str',
        'including_evergreen_subscription': 'bool',
        'target_date': 'date'
    }

    attribute_map = {
        'assume_renewal': 'assumeRenewal',
        'batch': 'batch',
        'charge_type_to_exclude': 'chargeTypeToExclude',
        'including_evergreen_subscription': 'includingEvergreenSubscription',
        'target_date': 'targetDate'
    }

    def __init__(self, assume_renewal=None, batch=None, charge_type_to_exclude=None, including_evergreen_subscription=None, target_date=None):  # noqa: E501
        """PostBillingPreviewRunParam - a model defined in Swagger"""  # noqa: E501

        self._assume_renewal = None
        self._batch = None
        self._charge_type_to_exclude = None
        self._including_evergreen_subscription = None
        self._target_date = None
        self.discriminator = None

        if assume_renewal is not None:
            self.assume_renewal = assume_renewal
        if batch is not None:
            self.batch = batch
        if charge_type_to_exclude is not None:
            self.charge_type_to_exclude = charge_type_to_exclude
        if including_evergreen_subscription is not None:
            self.including_evergreen_subscription = including_evergreen_subscription
        self.target_date = target_date

    @property
    def assume_renewal(self):
        """Gets the assume_renewal of this PostBillingPreviewRunParam.  # noqa: E501

        Indicates whether to generate a preview of future invoice items and credit memo items with the assumption that the subscriptions are renewed.  Set one of the following values in this field to decide how the assumption is applied in the billing preview.    * **All:** The assumption is applied to all the subscriptions. Zuora generates preview invoice item data and credit memo item data from the first day of the customer's next billing period to the target date.      * **None:** (Default) The assumption is not applied to the subscriptions. Zuora generates preview invoice item data and credit memo item data based on the current term end date and the target date.        * If the target date is later than the current term end date, Zuora generates preview invoice item data and credit memo item data from the first day of the customer's next billing period to the current term end date.      * If the target date is earlier than the current term end date, Zuora generates preview invoice item data and credit memeo item data from the first day of the customer's next billing period to the target date.    * **Autorenew:** The assumption is applied to the subscriptions that have auto-renew enabled. Zuora generates preview invoice item data and credit memo item data from the first day of the customer's next billing period to the target date.    **Note:**    - This field can only be used if the subscription renewal term is not set to 0.           - The credit memo item data is only available if you have Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).       # noqa: E501

        :return: The assume_renewal of this PostBillingPreviewRunParam.  # noqa: E501
        :rtype: str
        """
        return self._assume_renewal

    @assume_renewal.setter
    def assume_renewal(self, assume_renewal):
        """Sets the assume_renewal of this PostBillingPreviewRunParam.

        Indicates whether to generate a preview of future invoice items and credit memo items with the assumption that the subscriptions are renewed.  Set one of the following values in this field to decide how the assumption is applied in the billing preview.    * **All:** The assumption is applied to all the subscriptions. Zuora generates preview invoice item data and credit memo item data from the first day of the customer's next billing period to the target date.      * **None:** (Default) The assumption is not applied to the subscriptions. Zuora generates preview invoice item data and credit memo item data based on the current term end date and the target date.        * If the target date is later than the current term end date, Zuora generates preview invoice item data and credit memo item data from the first day of the customer's next billing period to the current term end date.      * If the target date is earlier than the current term end date, Zuora generates preview invoice item data and credit memeo item data from the first day of the customer's next billing period to the target date.    * **Autorenew:** The assumption is applied to the subscriptions that have auto-renew enabled. Zuora generates preview invoice item data and credit memo item data from the first day of the customer's next billing period to the target date.    **Note:**    - This field can only be used if the subscription renewal term is not set to 0.           - The credit memo item data is only available if you have Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).       # noqa: E501

        :param assume_renewal: The assume_renewal of this PostBillingPreviewRunParam.  # noqa: E501
        :type: str
        """

        self._assume_renewal = assume_renewal

    @property
    def batch(self):
        """Gets the batch of this PostBillingPreviewRunParam.  # noqa: E501

        The customer batch to include in the billing preview run. If not specified, all customer batches are included.   # noqa: E501

        :return: The batch of this PostBillingPreviewRunParam.  # noqa: E501
        :rtype: str
        """
        return self._batch

    @batch.setter
    def batch(self, batch):
        """Sets the batch of this PostBillingPreviewRunParam.

        The customer batch to include in the billing preview run. If not specified, all customer batches are included.   # noqa: E501

        :param batch: The batch of this PostBillingPreviewRunParam.  # noqa: E501
        :type: str
        """
        if batch is not None and len(batch) > 255:
            raise ValueError("Invalid value for `batch`, length must be less than or equal to `255`")  # noqa: E501

        self._batch = batch

    @property
    def charge_type_to_exclude(self):
        """Gets the charge_type_to_exclude of this PostBillingPreviewRunParam.  # noqa: E501

        The charge types to exclude from the forecast run.  **Possible values:** OneTime, Recurring, Usage, and any comma-separated combination of these values.   # noqa: E501

        :return: The charge_type_to_exclude of this PostBillingPreviewRunParam.  # noqa: E501
        :rtype: str
        """
        return self._charge_type_to_exclude

    @charge_type_to_exclude.setter
    def charge_type_to_exclude(self, charge_type_to_exclude):
        """Sets the charge_type_to_exclude of this PostBillingPreviewRunParam.

        The charge types to exclude from the forecast run.  **Possible values:** OneTime, Recurring, Usage, and any comma-separated combination of these values.   # noqa: E501

        :param charge_type_to_exclude: The charge_type_to_exclude of this PostBillingPreviewRunParam.  # noqa: E501
        :type: str
        """

        self._charge_type_to_exclude = charge_type_to_exclude

    @property
    def including_evergreen_subscription(self):
        """Gets the including_evergreen_subscription of this PostBillingPreviewRunParam.  # noqa: E501

        Indicates if evergreen subscriptions are included in the billing preview run. By default, evergreen subscriptions are not included.   # noqa: E501

        :return: The including_evergreen_subscription of this PostBillingPreviewRunParam.  # noqa: E501
        :rtype: bool
        """
        return self._including_evergreen_subscription

    @including_evergreen_subscription.setter
    def including_evergreen_subscription(self, including_evergreen_subscription):
        """Sets the including_evergreen_subscription of this PostBillingPreviewRunParam.

        Indicates if evergreen subscriptions are included in the billing preview run. By default, evergreen subscriptions are not included.   # noqa: E501

        :param including_evergreen_subscription: The including_evergreen_subscription of this PostBillingPreviewRunParam.  # noqa: E501
        :type: bool
        """

        self._including_evergreen_subscription = including_evergreen_subscription

    @property
    def target_date(self):
        """Gets the target_date of this PostBillingPreviewRunParam.  # noqa: E501

        The target date for the billing preview run. The billing preview run generates preview invoice item data and credit memo item data from the first day of the customer's next billing period to the TargetDate.   If the TargetDate is later than the subscription current term end date, the preview invoice item data and credit memo item data is generated from the first day of the customer's next billing period to the current term end date. If you want to generate preview invoice item data and credit memo item data past the end of the subscription current term, specify the AssumeRenewal field in the request.  **Note:** The credit memo item data is only available if you have Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   # noqa: E501

        :return: The target_date of this PostBillingPreviewRunParam.  # noqa: E501
        :rtype: date
        """
        return self._target_date

    @target_date.setter
    def target_date(self, target_date):
        """Sets the target_date of this PostBillingPreviewRunParam.

        The target date for the billing preview run. The billing preview run generates preview invoice item data and credit memo item data from the first day of the customer's next billing period to the TargetDate.   If the TargetDate is later than the subscription current term end date, the preview invoice item data and credit memo item data is generated from the first day of the customer's next billing period to the current term end date. If you want to generate preview invoice item data and credit memo item data past the end of the subscription current term, specify the AssumeRenewal field in the request.  **Note:** The credit memo item data is only available if you have Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   # noqa: E501

        :param target_date: The target_date of this PostBillingPreviewRunParam.  # noqa: E501
        :type: date
        """
        if target_date is None:
            raise ValueError("Invalid value for `target_date`, must not be `None`")  # noqa: E501

        self._target_date = target_date

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
        if issubclass(PostBillingPreviewRunParam, dict):
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
        if not isinstance(other, PostBillingPreviewRunParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other