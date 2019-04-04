# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.amendment_object_custom_fields import AmendmentObjectCustomFields  # noqa: F401,E501


class ProxyModifyAmendment(object):
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
        'contract_effective_date': 'date',
        'current_term': 'int',
        'current_term_period_type': 'str',
        'customer_acceptance_date': 'date',
        'description': 'str',
        'effective_date': 'date',
        'name': 'str',
        'renewal_setting': 'str',
        'renewal_term': 'int',
        'renewal_term_period_type': 'str',
        'service_activation_date': 'date',
        'specific_update_date': 'date',
        'status': 'str',
        'subscription_id': 'str',
        'term_start_date': 'date',
        'term_type': 'str',
        'type': 'str'
    }

    attribute_map = {
        'auto_renew': 'AutoRenew',
        'contract_effective_date': 'ContractEffectiveDate',
        'current_term': 'CurrentTerm',
        'current_term_period_type': 'CurrentTermPeriodType',
        'customer_acceptance_date': 'CustomerAcceptanceDate',
        'description': 'Description',
        'effective_date': 'EffectiveDate',
        'name': 'Name',
        'renewal_setting': 'RenewalSetting',
        'renewal_term': 'RenewalTerm',
        'renewal_term_period_type': 'RenewalTermPeriodType',
        'service_activation_date': 'ServiceActivationDate',
        'specific_update_date': 'SpecificUpdateDate',
        'status': 'Status',
        'subscription_id': 'SubscriptionId',
        'term_start_date': 'TermStartDate',
        'term_type': 'TermType',
        'type': 'Type'
    }

    def __init__(self, auto_renew=None, contract_effective_date=None, current_term=None, current_term_period_type=None, customer_acceptance_date=None, description=None, effective_date=None, name=None, renewal_setting=None, renewal_term=None, renewal_term_period_type=None, service_activation_date=None, specific_update_date=None, status=None, subscription_id=None, term_start_date=None, term_type=None, type=None):  # noqa: E501
        """ProxyModifyAmendment - a model defined in Swagger"""  # noqa: E501

        self._auto_renew = None
        self._contract_effective_date = None
        self._current_term = None
        self._current_term_period_type = None
        self._customer_acceptance_date = None
        self._description = None
        self._effective_date = None
        self._name = None
        self._renewal_setting = None
        self._renewal_term = None
        self._renewal_term_period_type = None
        self._service_activation_date = None
        self._specific_update_date = None
        self._status = None
        self._subscription_id = None
        self._term_start_date = None
        self._term_type = None
        self._type = None
        self.discriminator = None

        if auto_renew is not None:
            self.auto_renew = auto_renew
        if contract_effective_date is not None:
            self.contract_effective_date = contract_effective_date
        if current_term is not None:
            self.current_term = current_term
        if current_term_period_type is not None:
            self.current_term_period_type = current_term_period_type
        if customer_acceptance_date is not None:
            self.customer_acceptance_date = customer_acceptance_date
        if description is not None:
            self.description = description
        if effective_date is not None:
            self.effective_date = effective_date
        if name is not None:
            self.name = name
        if renewal_setting is not None:
            self.renewal_setting = renewal_setting
        if renewal_term is not None:
            self.renewal_term = renewal_term
        if renewal_term_period_type is not None:
            self.renewal_term_period_type = renewal_term_period_type
        if service_activation_date is not None:
            self.service_activation_date = service_activation_date
        if specific_update_date is not None:
            self.specific_update_date = specific_update_date
        if status is not None:
            self.status = status
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if term_start_date is not None:
            self.term_start_date = term_start_date
        if term_type is not None:
            self.term_type = term_type
        if type is not None:
            self.type = type

    @property
    def auto_renew(self):
        """Gets the auto_renew of this ProxyModifyAmendment.  # noqa: E501

         Determines whether the subscription is automatically renewed, or whether it expires at the end of the term and needs to be manually renewed. **Required:** For amendment of type TermsAndConditions when changing the automatic renewal status of a subscription. **Values**: true, false   # noqa: E501

        :return: The auto_renew of this ProxyModifyAmendment.  # noqa: E501
        :rtype: bool
        """
        return self._auto_renew

    @auto_renew.setter
    def auto_renew(self, auto_renew):
        """Sets the auto_renew of this ProxyModifyAmendment.

         Determines whether the subscription is automatically renewed, or whether it expires at the end of the term and needs to be manually renewed. **Required:** For amendment of type TermsAndConditions when changing the automatic renewal status of a subscription. **Values**: true, false   # noqa: E501

        :param auto_renew: The auto_renew of this ProxyModifyAmendment.  # noqa: E501
        :type: bool
        """

        self._auto_renew = auto_renew

    @property
    def contract_effective_date(self):
        """Gets the contract_effective_date of this ProxyModifyAmendment.  # noqa: E501

         The date when the amendment's changes become effective for billing purposes. **Version notes**: --   # noqa: E501

        :return: The contract_effective_date of this ProxyModifyAmendment.  # noqa: E501
        :rtype: date
        """
        return self._contract_effective_date

    @contract_effective_date.setter
    def contract_effective_date(self, contract_effective_date):
        """Sets the contract_effective_date of this ProxyModifyAmendment.

         The date when the amendment's changes become effective for billing purposes. **Version notes**: --   # noqa: E501

        :param contract_effective_date: The contract_effective_date of this ProxyModifyAmendment.  # noqa: E501
        :type: date
        """

        self._contract_effective_date = contract_effective_date

    @property
    def current_term(self):
        """Gets the current_term of this ProxyModifyAmendment.  # noqa: E501

         The length of the period for the current subscription term. This field can be updated when Status is `Draft`. **Required**: Only if the value of the Type field is set to `TermsAndConditions` and TermType is set to `TERMED`. This field is not required if TermType is set to `EVERGREEN`. **Character limit**: **Values**: a valid number   # noqa: E501

        :return: The current_term of this ProxyModifyAmendment.  # noqa: E501
        :rtype: int
        """
        return self._current_term

    @current_term.setter
    def current_term(self, current_term):
        """Sets the current_term of this ProxyModifyAmendment.

         The length of the period for the current subscription term. This field can be updated when Status is `Draft`. **Required**: Only if the value of the Type field is set to `TermsAndConditions` and TermType is set to `TERMED`. This field is not required if TermType is set to `EVERGREEN`. **Character limit**: **Values**: a valid number   # noqa: E501

        :param current_term: The current_term of this ProxyModifyAmendment.  # noqa: E501
        :type: int
        """

        self._current_term = current_term

    @property
    def current_term_period_type(self):
        """Gets the current_term_period_type of this ProxyModifyAmendment.  # noqa: E501

         The period type for the current subscription term. **Values**:  - `Month` (default) - `Year` - `Day` - `Week` **Note**:  - This field can be updated when Status is `Draft`. - This field is used with the CurrentTerm field to specify the current subscription term.   # noqa: E501

        :return: The current_term_period_type of this ProxyModifyAmendment.  # noqa: E501
        :rtype: str
        """
        return self._current_term_period_type

    @current_term_period_type.setter
    def current_term_period_type(self, current_term_period_type):
        """Sets the current_term_period_type of this ProxyModifyAmendment.

         The period type for the current subscription term. **Values**:  - `Month` (default) - `Year` - `Day` - `Week` **Note**:  - This field can be updated when Status is `Draft`. - This field is used with the CurrentTerm field to specify the current subscription term.   # noqa: E501

        :param current_term_period_type: The current_term_period_type of this ProxyModifyAmendment.  # noqa: E501
        :type: str
        """

        self._current_term_period_type = current_term_period_type

    @property
    def customer_acceptance_date(self):
        """Gets the customer_acceptance_date of this ProxyModifyAmendment.  # noqa: E501

         The date when the customer accepts the amendment's changes to the subscription. **Required**: Only if the value of the Status field is set to PendingAcceptance. **Version notes**: --   # noqa: E501

        :return: The customer_acceptance_date of this ProxyModifyAmendment.  # noqa: E501
        :rtype: date
        """
        return self._customer_acceptance_date

    @customer_acceptance_date.setter
    def customer_acceptance_date(self, customer_acceptance_date):
        """Sets the customer_acceptance_date of this ProxyModifyAmendment.

         The date when the customer accepts the amendment's changes to the subscription. **Required**: Only if the value of the Status field is set to PendingAcceptance. **Version notes**: --   # noqa: E501

        :param customer_acceptance_date: The customer_acceptance_date of this ProxyModifyAmendment.  # noqa: E501
        :type: date
        """

        self._customer_acceptance_date = customer_acceptance_date

    @property
    def description(self):
        """Gets the description of this ProxyModifyAmendment.  # noqa: E501

         A description of the amendment. **Character limit**: 500 **Values**: maximum 500 characters   # noqa: E501

        :return: The description of this ProxyModifyAmendment.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProxyModifyAmendment.

         A description of the amendment. **Character limit**: 500 **Values**: maximum 500 characters   # noqa: E501

        :param description: The description of this ProxyModifyAmendment.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def effective_date(self):
        """Gets the effective_date of this ProxyModifyAmendment.  # noqa: E501

         The date when the amendment's changes take effective. This field validates that the amendment's changes are within valid ranges of products and product rate plans. **Required**: For the cancellation amendments. Optional for other types of amendments. **Version notes**: --   # noqa: E501

        :return: The effective_date of this ProxyModifyAmendment.  # noqa: E501
        :rtype: date
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this ProxyModifyAmendment.

         The date when the amendment's changes take effective. This field validates that the amendment's changes are within valid ranges of products and product rate plans. **Required**: For the cancellation amendments. Optional for other types of amendments. **Version notes**: --   # noqa: E501

        :param effective_date: The effective_date of this ProxyModifyAmendment.  # noqa: E501
        :type: date
        """

        self._effective_date = effective_date

    @property
    def name(self):
        """Gets the name of this ProxyModifyAmendment.  # noqa: E501

         The name of the amendment. **Character limit**: 100 **Values**: a string of 100 characters or fewer   # noqa: E501

        :return: The name of this ProxyModifyAmendment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProxyModifyAmendment.

         The name of the amendment. **Character limit**: 100 **Values**: a string of 100 characters or fewer   # noqa: E501

        :param name: The name of this ProxyModifyAmendment.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def renewal_setting(self):
        """Gets the renewal_setting of this ProxyModifyAmendment.  # noqa: E501

         Specifies whether a termed subscription will remain termed or change to evergreen when it is renewed. **Required**: If TermType is Termed **Values**: RENEW_WITH_SPECIFIC_TERM (default), RENEW_TO_EVERGREEN   # noqa: E501

        :return: The renewal_setting of this ProxyModifyAmendment.  # noqa: E501
        :rtype: str
        """
        return self._renewal_setting

    @renewal_setting.setter
    def renewal_setting(self, renewal_setting):
        """Sets the renewal_setting of this ProxyModifyAmendment.

         Specifies whether a termed subscription will remain termed or change to evergreen when it is renewed. **Required**: If TermType is Termed **Values**: RENEW_WITH_SPECIFIC_TERM (default), RENEW_TO_EVERGREEN   # noqa: E501

        :param renewal_setting: The renewal_setting of this ProxyModifyAmendment.  # noqa: E501
        :type: str
        """

        self._renewal_setting = renewal_setting

    @property
    def renewal_term(self):
        """Gets the renewal_term of this ProxyModifyAmendment.  # noqa: E501

         The term of renewal for the amended subscription. This field can be updated when Status is `Draft`. **Required**: Only if the value of the Type field is set to `TermsAndConditions`. **Character limit**: **Values:** a valid number   # noqa: E501

        :return: The renewal_term of this ProxyModifyAmendment.  # noqa: E501
        :rtype: int
        """
        return self._renewal_term

    @renewal_term.setter
    def renewal_term(self, renewal_term):
        """Sets the renewal_term of this ProxyModifyAmendment.

         The term of renewal for the amended subscription. This field can be updated when Status is `Draft`. **Required**: Only if the value of the Type field is set to `TermsAndConditions`. **Character limit**: **Values:** a valid number   # noqa: E501

        :param renewal_term: The renewal_term of this ProxyModifyAmendment.  # noqa: E501
        :type: int
        """

        self._renewal_term = renewal_term

    @property
    def renewal_term_period_type(self):
        """Gets the renewal_term_period_type of this ProxyModifyAmendment.  # noqa: E501

         The period type for the subscription renewal term. This field can be updated when Status is `Draft`. **Required**: Only if the value of the Type field is set to `TermsAndConditions`. This field is used with the RenewalTerm field to specify the subscription renewal term. **Values**:  - `Month` (default) - `Year` - `Day` - `Week`   # noqa: E501

        :return: The renewal_term_period_type of this ProxyModifyAmendment.  # noqa: E501
        :rtype: str
        """
        return self._renewal_term_period_type

    @renewal_term_period_type.setter
    def renewal_term_period_type(self, renewal_term_period_type):
        """Sets the renewal_term_period_type of this ProxyModifyAmendment.

         The period type for the subscription renewal term. This field can be updated when Status is `Draft`. **Required**: Only if the value of the Type field is set to `TermsAndConditions`. This field is used with the RenewalTerm field to specify the subscription renewal term. **Values**:  - `Month` (default) - `Year` - `Day` - `Week`   # noqa: E501

        :param renewal_term_period_type: The renewal_term_period_type of this ProxyModifyAmendment.  # noqa: E501
        :type: str
        """

        self._renewal_term_period_type = renewal_term_period_type

    @property
    def service_activation_date(self):
        """Gets the service_activation_date of this ProxyModifyAmendment.  # noqa: E501

         The date when service is activated. **Required**: Only if the value of the Status field is set to PendingActivation. **Version notes**: --   # noqa: E501

        :return: The service_activation_date of this ProxyModifyAmendment.  # noqa: E501
        :rtype: date
        """
        return self._service_activation_date

    @service_activation_date.setter
    def service_activation_date(self, service_activation_date):
        """Sets the service_activation_date of this ProxyModifyAmendment.

         The date when service is activated. **Required**: Only if the value of the Status field is set to PendingActivation. **Version notes**: --   # noqa: E501

        :param service_activation_date: The service_activation_date of this ProxyModifyAmendment.  # noqa: E501
        :type: date
        """

        self._service_activation_date = service_activation_date

    @property
    def specific_update_date(self):
        """Gets the specific_update_date of this ProxyModifyAmendment.  # noqa: E501

         The date when the UpdateProduct amendment takes effect. This field is only applicable if there is already a future-dated UpdateProduct amendment on the subscription. **Required**: Only for the UpdateProduct amendments if there is already a future-dated UpdateProduct amendment on the subscription.   # noqa: E501

        :return: The specific_update_date of this ProxyModifyAmendment.  # noqa: E501
        :rtype: date
        """
        return self._specific_update_date

    @specific_update_date.setter
    def specific_update_date(self, specific_update_date):
        """Sets the specific_update_date of this ProxyModifyAmendment.

         The date when the UpdateProduct amendment takes effect. This field is only applicable if there is already a future-dated UpdateProduct amendment on the subscription. **Required**: Only for the UpdateProduct amendments if there is already a future-dated UpdateProduct amendment on the subscription.   # noqa: E501

        :param specific_update_date: The specific_update_date of this ProxyModifyAmendment.  # noqa: E501
        :type: date
        """

        self._specific_update_date = specific_update_date

    @property
    def status(self):
        """Gets the status of this ProxyModifyAmendment.  # noqa: E501

         The status of the amendment. Type: string (enum) **Character limit**: 17 **Values**: one of the following:  - Draft (default, if left null) - Pending Activation - Pending Acceptance - Completed   # noqa: E501

        :return: The status of this ProxyModifyAmendment.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProxyModifyAmendment.

         The status of the amendment. Type: string (enum) **Character limit**: 17 **Values**: one of the following:  - Draft (default, if left null) - Pending Activation - Pending Acceptance - Completed   # noqa: E501

        :param status: The status of this ProxyModifyAmendment.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def subscription_id(self):
        """Gets the subscription_id of this ProxyModifyAmendment.  # noqa: E501

         The ID of the subscription that the amendment changes. **Character limit**: 32 **Values**: a valid subscription ID   # noqa: E501

        :return: The subscription_id of this ProxyModifyAmendment.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this ProxyModifyAmendment.

         The ID of the subscription that the amendment changes. **Character limit**: 32 **Values**: a valid subscription ID   # noqa: E501

        :param subscription_id: The subscription_id of this ProxyModifyAmendment.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def term_start_date(self):
        """Gets the term_start_date of this ProxyModifyAmendment.  # noqa: E501

         The date when the new terms and conditions take effect. **Required**: Only if the value of the Type field is set to TermsAndConditions. **Version notes**: --   # noqa: E501

        :return: The term_start_date of this ProxyModifyAmendment.  # noqa: E501
        :rtype: date
        """
        return self._term_start_date

    @term_start_date.setter
    def term_start_date(self, term_start_date):
        """Sets the term_start_date of this ProxyModifyAmendment.

         The date when the new terms and conditions take effect. **Required**: Only if the value of the Type field is set to TermsAndConditions. **Version notes**: --   # noqa: E501

        :param term_start_date: The term_start_date of this ProxyModifyAmendment.  # noqa: E501
        :type: date
        """

        self._term_start_date = term_start_date

    @property
    def term_type(self):
        """Gets the term_type of this ProxyModifyAmendment.  # noqa: E501

         Indicates if the subscription isTERMED or EVERGREEN.  - A TERMED subscription has an expiration date, and must be manually renewed. - An EVERGREEN subscription doesn't have an expiration date, and must be manually ended.  **Required**: Only when as part of an amendment of type TermsAndConditions &#65279;to change the term type of a subscription. Type: string **Character limit**: 9 **Values**: TERMED, EVERGREEN   # noqa: E501

        :return: The term_type of this ProxyModifyAmendment.  # noqa: E501
        :rtype: str
        """
        return self._term_type

    @term_type.setter
    def term_type(self, term_type):
        """Sets the term_type of this ProxyModifyAmendment.

         Indicates if the subscription isTERMED or EVERGREEN.  - A TERMED subscription has an expiration date, and must be manually renewed. - An EVERGREEN subscription doesn't have an expiration date, and must be manually ended.  **Required**: Only when as part of an amendment of type TermsAndConditions &#65279;to change the term type of a subscription. Type: string **Character limit**: 9 **Values**: TERMED, EVERGREEN   # noqa: E501

        :param term_type: The term_type of this ProxyModifyAmendment.  # noqa: E501
        :type: str
        """

        self._term_type = term_type

    @property
    def type(self):
        """Gets the type of this ProxyModifyAmendment.  # noqa: E501

         The type of amendment. **Character limit**: 18 **Values**: one of the following:  - Cancellation - NewProduct - OwnerTransfer - RemoveProduct - Renewal - UpdateProduct - TermsAndConditions - SuspendSubscription (This value is in **Limited Availability**.) - ResumeSubscription (This value is in **Limited Availability**.)   # noqa: E501

        :return: The type of this ProxyModifyAmendment.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProxyModifyAmendment.

         The type of amendment. **Character limit**: 18 **Values**: one of the following:  - Cancellation - NewProduct - OwnerTransfer - RemoveProduct - Renewal - UpdateProduct - TermsAndConditions - SuspendSubscription (This value is in **Limited Availability**.) - ResumeSubscription (This value is in **Limited Availability**.)   # noqa: E501

        :param type: The type of this ProxyModifyAmendment.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(ProxyModifyAmendment, dict):
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
        if not isinstance(other, ProxyModifyAmendment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
