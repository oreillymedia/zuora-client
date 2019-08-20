# coding: utf-8




import pprint
import re  # noqa: F401

import six


class GETAmendmentType(object):
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
        'base_rate_plan_id': 'str',
        'base_subscription_id': 'str',
        'code': 'str',
        'contract_effective_date': 'date',
        'current_term': 'int',
        'current_term_period_type': 'str',
        'customer_acceptance_date': 'date',
        'description': 'str',
        'destination_account_id': 'str',
        'destination_invoice_owner_id': 'str',
        'effective_date': 'date',
        'id': 'str',
        'name': 'str',
        'new_rate_plan_id': 'str',
        'new_subscription_id': 'str',
        'renewal_setting': 'str',
        'renewal_term': 'int',
        'renewal_term_period_type': 'str',
        'resume_date': 'date',
        'service_activation_date': 'date',
        'specific_update_date': 'date',
        'status': 'str',
        'success': 'bool',
        'suspend_date': 'date',
        'term_start_date': 'date',
        'term_type': 'str',
        'type': 'str'
    }

    attribute_map = {
        'auto_renew': 'autoRenew',
        'base_rate_plan_id': 'baseRatePlanId',
        'base_subscription_id': 'baseSubscriptionId',
        'code': 'code',
        'contract_effective_date': 'contractEffectiveDate',
        'current_term': 'currentTerm',
        'current_term_period_type': 'currentTermPeriodType',
        'customer_acceptance_date': 'customerAcceptanceDate',
        'description': 'description',
        'destination_account_id': 'destinationAccountId',
        'destination_invoice_owner_id': 'destinationInvoiceOwnerId',
        'effective_date': 'effectiveDate',
        'id': 'id',
        'name': 'name',
        'new_rate_plan_id': 'newRatePlanId',
        'new_subscription_id': 'newSubscriptionId',
        'renewal_setting': 'renewalSetting',
        'renewal_term': 'renewalTerm',
        'renewal_term_period_type': 'renewalTermPeriodType',
        'resume_date': 'resumeDate',
        'service_activation_date': 'serviceActivationDate',
        'specific_update_date': 'specificUpdateDate',
        'status': 'status',
        'success': 'success',
        'suspend_date': 'suspendDate',
        'term_start_date': 'termStartDate',
        'term_type': 'termType',
        'type': 'type'
    }

    def __init__(self, auto_renew=None, base_rate_plan_id=None, base_subscription_id=None, code=None, contract_effective_date=None, current_term=None, current_term_period_type=None, customer_acceptance_date=None, description=None, destination_account_id=None, destination_invoice_owner_id=None, effective_date=None, id=None, name=None, new_rate_plan_id=None, new_subscription_id=None, renewal_setting=None, renewal_term=None, renewal_term_period_type=None, resume_date=None, service_activation_date=None, specific_update_date=None, status=None, success=None, suspend_date=None, term_start_date=None, term_type=None, type=None):  # noqa: E501
        """GETAmendmentType - a model defined in Swagger"""  # noqa: E501

        self._auto_renew = None
        self._base_rate_plan_id = None
        self._base_subscription_id = None
        self._code = None
        self._contract_effective_date = None
        self._current_term = None
        self._current_term_period_type = None
        self._customer_acceptance_date = None
        self._description = None
        self._destination_account_id = None
        self._destination_invoice_owner_id = None
        self._effective_date = None
        self._id = None
        self._name = None
        self._new_rate_plan_id = None
        self._new_subscription_id = None
        self._renewal_setting = None
        self._renewal_term = None
        self._renewal_term_period_type = None
        self._resume_date = None
        self._service_activation_date = None
        self._specific_update_date = None
        self._status = None
        self._success = None
        self._suspend_date = None
        self._term_start_date = None
        self._term_type = None
        self._type = None
        self.discriminator = None

        if auto_renew is not None:
            self.auto_renew = auto_renew
        if base_rate_plan_id is not None:
            self.base_rate_plan_id = base_rate_plan_id
        if base_subscription_id is not None:
            self.base_subscription_id = base_subscription_id
        if code is not None:
            self.code = code
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
        if destination_account_id is not None:
            self.destination_account_id = destination_account_id
        if destination_invoice_owner_id is not None:
            self.destination_invoice_owner_id = destination_invoice_owner_id
        if effective_date is not None:
            self.effective_date = effective_date
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if new_rate_plan_id is not None:
            self.new_rate_plan_id = new_rate_plan_id
        if new_subscription_id is not None:
            self.new_subscription_id = new_subscription_id
        if renewal_setting is not None:
            self.renewal_setting = renewal_setting
        if renewal_term is not None:
            self.renewal_term = renewal_term
        if renewal_term_period_type is not None:
            self.renewal_term_period_type = renewal_term_period_type
        if resume_date is not None:
            self.resume_date = resume_date
        if service_activation_date is not None:
            self.service_activation_date = service_activation_date
        if specific_update_date is not None:
            self.specific_update_date = specific_update_date
        if status is not None:
            self.status = status
        if success is not None:
            self.success = success
        if suspend_date is not None:
            self.suspend_date = suspend_date
        if term_start_date is not None:
            self.term_start_date = term_start_date
        if term_type is not None:
            self.term_type = term_type
        if type is not None:
            self.type = type

    @property
    def auto_renew(self):
        """Gets the auto_renew of this GETAmendmentType.  # noqa: E501

        Determines whether the subscription is automatically renewed, or whether it expires at the end of the term and needs to be manually renewed.    # noqa: E501

        :return: The auto_renew of this GETAmendmentType.  # noqa: E501
        :rtype: bool
        """
        return self._auto_renew

    @auto_renew.setter
    def auto_renew(self, auto_renew):
        """Sets the auto_renew of this GETAmendmentType.

        Determines whether the subscription is automatically renewed, or whether it expires at the end of the term and needs to be manually renewed.    # noqa: E501

        :param auto_renew: The auto_renew of this GETAmendmentType.  # noqa: E501
        :type: bool
        """

        self._auto_renew = auto_renew

    @property
    def base_rate_plan_id(self):
        """Gets the base_rate_plan_id of this GETAmendmentType.  # noqa: E501

        The rate plan ID on which changes are made. Only the Update or Remove amendment returns a base rate plan ID.   # noqa: E501

        :return: The base_rate_plan_id of this GETAmendmentType.  # noqa: E501
        :rtype: str
        """
        return self._base_rate_plan_id

    @base_rate_plan_id.setter
    def base_rate_plan_id(self, base_rate_plan_id):
        """Sets the base_rate_plan_id of this GETAmendmentType.

        The rate plan ID on which changes are made. Only the Update or Remove amendment returns a base rate plan ID.   # noqa: E501

        :param base_rate_plan_id: The base_rate_plan_id of this GETAmendmentType.  # noqa: E501
        :type: str
        """

        self._base_rate_plan_id = base_rate_plan_id

    @property
    def base_subscription_id(self):
        """Gets the base_subscription_id of this GETAmendmentType.  # noqa: E501

        The ID of the subscription based on which the amendment is created.   # noqa: E501

        :return: The base_subscription_id of this GETAmendmentType.  # noqa: E501
        :rtype: str
        """
        return self._base_subscription_id

    @base_subscription_id.setter
    def base_subscription_id(self, base_subscription_id):
        """Sets the base_subscription_id of this GETAmendmentType.

        The ID of the subscription based on which the amendment is created.   # noqa: E501

        :param base_subscription_id: The base_subscription_id of this GETAmendmentType.  # noqa: E501
        :type: str
        """

        self._base_subscription_id = base_subscription_id

    @property
    def code(self):
        """Gets the code of this GETAmendmentType.  # noqa: E501

        The amendment code.   # noqa: E501

        :return: The code of this GETAmendmentType.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this GETAmendmentType.

        The amendment code.   # noqa: E501

        :param code: The code of this GETAmendmentType.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def contract_effective_date(self):
        """Gets the contract_effective_date of this GETAmendmentType.  # noqa: E501

        The date when the amendment becomes effective for billing purposes, as `yyyy-mm-dd`.   # noqa: E501

        :return: The contract_effective_date of this GETAmendmentType.  # noqa: E501
        :rtype: date
        """
        return self._contract_effective_date

    @contract_effective_date.setter
    def contract_effective_date(self, contract_effective_date):
        """Sets the contract_effective_date of this GETAmendmentType.

        The date when the amendment becomes effective for billing purposes, as `yyyy-mm-dd`.   # noqa: E501

        :param contract_effective_date: The contract_effective_date of this GETAmendmentType.  # noqa: E501
        :type: date
        """

        self._contract_effective_date = contract_effective_date

    @property
    def current_term(self):
        """Gets the current_term of this GETAmendmentType.  # noqa: E501

        The length of the period for the current subscription term.    # noqa: E501

        :return: The current_term of this GETAmendmentType.  # noqa: E501
        :rtype: int
        """
        return self._current_term

    @current_term.setter
    def current_term(self, current_term):
        """Sets the current_term of this GETAmendmentType.

        The length of the period for the current subscription term.    # noqa: E501

        :param current_term: The current_term of this GETAmendmentType.  # noqa: E501
        :type: int
        """

        self._current_term = current_term

    @property
    def current_term_period_type(self):
        """Gets the current_term_period_type of this GETAmendmentType.  # noqa: E501

        The period type for the current subscription term. Possible values are:  - Month - Year - Day - Week   # noqa: E501

        :return: The current_term_period_type of this GETAmendmentType.  # noqa: E501
        :rtype: str
        """
        return self._current_term_period_type

    @current_term_period_type.setter
    def current_term_period_type(self, current_term_period_type):
        """Sets the current_term_period_type of this GETAmendmentType.

        The period type for the current subscription term. Possible values are:  - Month - Year - Day - Week   # noqa: E501

        :param current_term_period_type: The current_term_period_type of this GETAmendmentType.  # noqa: E501
        :type: str
        """

        self._current_term_period_type = current_term_period_type

    @property
    def customer_acceptance_date(self):
        """Gets the customer_acceptance_date of this GETAmendmentType.  # noqa: E501

        The date when the customer accepts the amendment changes to the subscription, as `yyyy-mm-dd`.   # noqa: E501

        :return: The customer_acceptance_date of this GETAmendmentType.  # noqa: E501
        :rtype: date
        """
        return self._customer_acceptance_date

    @customer_acceptance_date.setter
    def customer_acceptance_date(self, customer_acceptance_date):
        """Sets the customer_acceptance_date of this GETAmendmentType.

        The date when the customer accepts the amendment changes to the subscription, as `yyyy-mm-dd`.   # noqa: E501

        :param customer_acceptance_date: The customer_acceptance_date of this GETAmendmentType.  # noqa: E501
        :type: date
        """

        self._customer_acceptance_date = customer_acceptance_date

    @property
    def description(self):
        """Gets the description of this GETAmendmentType.  # noqa: E501

        Description of the amendment.   # noqa: E501

        :return: The description of this GETAmendmentType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GETAmendmentType.

        Description of the amendment.   # noqa: E501

        :param description: The description of this GETAmendmentType.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def destination_account_id(self):
        """Gets the destination_account_id of this GETAmendmentType.  # noqa: E501

        The ID of the account that the subscription is being transferred to.   # noqa: E501

        :return: The destination_account_id of this GETAmendmentType.  # noqa: E501
        :rtype: str
        """
        return self._destination_account_id

    @destination_account_id.setter
    def destination_account_id(self, destination_account_id):
        """Sets the destination_account_id of this GETAmendmentType.

        The ID of the account that the subscription is being transferred to.   # noqa: E501

        :param destination_account_id: The destination_account_id of this GETAmendmentType.  # noqa: E501
        :type: str
        """

        self._destination_account_id = destination_account_id

    @property
    def destination_invoice_owner_id(self):
        """Gets the destination_invoice_owner_id of this GETAmendmentType.  # noqa: E501

        The ID of the invoice that the subscription is being transferred to.   # noqa: E501

        :return: The destination_invoice_owner_id of this GETAmendmentType.  # noqa: E501
        :rtype: str
        """
        return self._destination_invoice_owner_id

    @destination_invoice_owner_id.setter
    def destination_invoice_owner_id(self, destination_invoice_owner_id):
        """Sets the destination_invoice_owner_id of this GETAmendmentType.

        The ID of the invoice that the subscription is being transferred to.   # noqa: E501

        :param destination_invoice_owner_id: The destination_invoice_owner_id of this GETAmendmentType.  # noqa: E501
        :type: str
        """

        self._destination_invoice_owner_id = destination_invoice_owner_id

    @property
    def effective_date(self):
        """Gets the effective_date of this GETAmendmentType.  # noqa: E501

        The date when the amendment changes take effective.    # noqa: E501

        :return: The effective_date of this GETAmendmentType.  # noqa: E501
        :rtype: date
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this GETAmendmentType.

        The date when the amendment changes take effective.    # noqa: E501

        :param effective_date: The effective_date of this GETAmendmentType.  # noqa: E501
        :type: date
        """

        self._effective_date = effective_date

    @property
    def id(self):
        """Gets the id of this GETAmendmentType.  # noqa: E501

        The amendment ID.   # noqa: E501

        :return: The id of this GETAmendmentType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GETAmendmentType.

        The amendment ID.   # noqa: E501

        :param id: The id of this GETAmendmentType.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GETAmendmentType.  # noqa: E501

        The name of the amendment.   # noqa: E501

        :return: The name of this GETAmendmentType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GETAmendmentType.

        The name of the amendment.   # noqa: E501

        :param name: The name of this GETAmendmentType.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def new_rate_plan_id(self):
        """Gets the new_rate_plan_id of this GETAmendmentType.  # noqa: E501

        The ID of the rate plan charge on which amendment is made. Only the Add or Update amendment returns a new rate plan ID.   # noqa: E501

        :return: The new_rate_plan_id of this GETAmendmentType.  # noqa: E501
        :rtype: str
        """
        return self._new_rate_plan_id

    @new_rate_plan_id.setter
    def new_rate_plan_id(self, new_rate_plan_id):
        """Sets the new_rate_plan_id of this GETAmendmentType.

        The ID of the rate plan charge on which amendment is made. Only the Add or Update amendment returns a new rate plan ID.   # noqa: E501

        :param new_rate_plan_id: The new_rate_plan_id of this GETAmendmentType.  # noqa: E501
        :type: str
        """

        self._new_rate_plan_id = new_rate_plan_id

    @property
    def new_subscription_id(self):
        """Gets the new_subscription_id of this GETAmendmentType.  # noqa: E501

        The ID of the subscription that the amendment changes.   # noqa: E501

        :return: The new_subscription_id of this GETAmendmentType.  # noqa: E501
        :rtype: str
        """
        return self._new_subscription_id

    @new_subscription_id.setter
    def new_subscription_id(self, new_subscription_id):
        """Sets the new_subscription_id of this GETAmendmentType.

        The ID of the subscription that the amendment changes.   # noqa: E501

        :param new_subscription_id: The new_subscription_id of this GETAmendmentType.  # noqa: E501
        :type: str
        """

        self._new_subscription_id = new_subscription_id

    @property
    def renewal_setting(self):
        """Gets the renewal_setting of this GETAmendmentType.  # noqa: E501

        Specifies whether a termed subscription will remain termed or change to evergreen when it is renewed. Possible values are:  - RENEW_WITH_SPECIFIC_TERM - RENEW_TO_EVERGREEN   # noqa: E501

        :return: The renewal_setting of this GETAmendmentType.  # noqa: E501
        :rtype: str
        """
        return self._renewal_setting

    @renewal_setting.setter
    def renewal_setting(self, renewal_setting):
        """Sets the renewal_setting of this GETAmendmentType.

        Specifies whether a termed subscription will remain termed or change to evergreen when it is renewed. Possible values are:  - RENEW_WITH_SPECIFIC_TERM - RENEW_TO_EVERGREEN   # noqa: E501

        :param renewal_setting: The renewal_setting of this GETAmendmentType.  # noqa: E501
        :type: str
        """

        self._renewal_setting = renewal_setting

    @property
    def renewal_term(self):
        """Gets the renewal_term of this GETAmendmentType.  # noqa: E501

        The term of renewal for the amended subscription.   # noqa: E501

        :return: The renewal_term of this GETAmendmentType.  # noqa: E501
        :rtype: int
        """
        return self._renewal_term

    @renewal_term.setter
    def renewal_term(self, renewal_term):
        """Sets the renewal_term of this GETAmendmentType.

        The term of renewal for the amended subscription.   # noqa: E501

        :param renewal_term: The renewal_term of this GETAmendmentType.  # noqa: E501
        :type: int
        """

        self._renewal_term = renewal_term

    @property
    def renewal_term_period_type(self):
        """Gets the renewal_term_period_type of this GETAmendmentType.  # noqa: E501

        The period type for the subscription renewal term. Possible values are:  - Month - Year - Day - Week   # noqa: E501

        :return: The renewal_term_period_type of this GETAmendmentType.  # noqa: E501
        :rtype: str
        """
        return self._renewal_term_period_type

    @renewal_term_period_type.setter
    def renewal_term_period_type(self, renewal_term_period_type):
        """Sets the renewal_term_period_type of this GETAmendmentType.

        The period type for the subscription renewal term. Possible values are:  - Month - Year - Day - Week   # noqa: E501

        :param renewal_term_period_type: The renewal_term_period_type of this GETAmendmentType.  # noqa: E501
        :type: str
        """

        self._renewal_term_period_type = renewal_term_period_type

    @property
    def resume_date(self):
        """Gets the resume_date of this GETAmendmentType.  # noqa: E501

        The date when the subscription resumption takes effect, as `yyyy-mm-dd`.  **Note:** This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   # noqa: E501

        :return: The resume_date of this GETAmendmentType.  # noqa: E501
        :rtype: date
        """
        return self._resume_date

    @resume_date.setter
    def resume_date(self, resume_date):
        """Sets the resume_date of this GETAmendmentType.

        The date when the subscription resumption takes effect, as `yyyy-mm-dd`.  **Note:** This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   # noqa: E501

        :param resume_date: The resume_date of this GETAmendmentType.  # noqa: E501
        :type: date
        """

        self._resume_date = resume_date

    @property
    def service_activation_date(self):
        """Gets the service_activation_date of this GETAmendmentType.  # noqa: E501

        The date when service is activated, as `yyyy-mm-dd`.   # noqa: E501

        :return: The service_activation_date of this GETAmendmentType.  # noqa: E501
        :rtype: date
        """
        return self._service_activation_date

    @service_activation_date.setter
    def service_activation_date(self, service_activation_date):
        """Sets the service_activation_date of this GETAmendmentType.

        The date when service is activated, as `yyyy-mm-dd`.   # noqa: E501

        :param service_activation_date: The service_activation_date of this GETAmendmentType.  # noqa: E501
        :type: date
        """

        self._service_activation_date = service_activation_date

    @property
    def specific_update_date(self):
        """Gets the specific_update_date of this GETAmendmentType.  # noqa: E501

        The date when the Update Product amendment takes effect.  Only for the Update Product amendments if there is already a future-dated Update Product amendment on the subscription.   # noqa: E501

        :return: The specific_update_date of this GETAmendmentType.  # noqa: E501
        :rtype: date
        """
        return self._specific_update_date

    @specific_update_date.setter
    def specific_update_date(self, specific_update_date):
        """Sets the specific_update_date of this GETAmendmentType.

        The date when the Update Product amendment takes effect.  Only for the Update Product amendments if there is already a future-dated Update Product amendment on the subscription.   # noqa: E501

        :param specific_update_date: The specific_update_date of this GETAmendmentType.  # noqa: E501
        :type: date
        """

        self._specific_update_date = specific_update_date

    @property
    def status(self):
        """Gets the status of this GETAmendmentType.  # noqa: E501

        The status of the amendment. Possible values are:  - Draft  - Pending Activation - Pending Acceptance - Completed   # noqa: E501

        :return: The status of this GETAmendmentType.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GETAmendmentType.

        The status of the amendment. Possible values are:  - Draft  - Pending Activation - Pending Acceptance - Completed   # noqa: E501

        :param status: The status of this GETAmendmentType.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def success(self):
        """Gets the success of this GETAmendmentType.  # noqa: E501

        Returns `true` if the request was processed successfully.   # noqa: E501

        :return: The success of this GETAmendmentType.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this GETAmendmentType.

        Returns `true` if the request was processed successfully.   # noqa: E501

        :param success: The success of this GETAmendmentType.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def suspend_date(self):
        """Gets the suspend_date of this GETAmendmentType.  # noqa: E501

        The date when the subscription suspension takes effect, as `yyyy-mm-dd`.  **Note:** This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   # noqa: E501

        :return: The suspend_date of this GETAmendmentType.  # noqa: E501
        :rtype: date
        """
        return self._suspend_date

    @suspend_date.setter
    def suspend_date(self, suspend_date):
        """Sets the suspend_date of this GETAmendmentType.

        The date when the subscription suspension takes effect, as `yyyy-mm-dd`.  **Note:** This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   # noqa: E501

        :param suspend_date: The suspend_date of this GETAmendmentType.  # noqa: E501
        :type: date
        """

        self._suspend_date = suspend_date

    @property
    def term_start_date(self):
        """Gets the term_start_date of this GETAmendmentType.  # noqa: E501

        The date when the new terms and conditions take effect.   # noqa: E501

        :return: The term_start_date of this GETAmendmentType.  # noqa: E501
        :rtype: date
        """
        return self._term_start_date

    @term_start_date.setter
    def term_start_date(self, term_start_date):
        """Sets the term_start_date of this GETAmendmentType.

        The date when the new terms and conditions take effect.   # noqa: E501

        :param term_start_date: The term_start_date of this GETAmendmentType.  # noqa: E501
        :type: date
        """

        self._term_start_date = term_start_date

    @property
    def term_type(self):
        """Gets the term_type of this GETAmendmentType.  # noqa: E501

        Indicates if the subscription is `TERMED` or `EVERGREEN`.   # noqa: E501

        :return: The term_type of this GETAmendmentType.  # noqa: E501
        :rtype: str
        """
        return self._term_type

    @term_type.setter
    def term_type(self, term_type):
        """Sets the term_type of this GETAmendmentType.

        Indicates if the subscription is `TERMED` or `EVERGREEN`.   # noqa: E501

        :param term_type: The term_type of this GETAmendmentType.  # noqa: E501
        :type: str
        """

        self._term_type = term_type

    @property
    def type(self):
        """Gets the type of this GETAmendmentType.  # noqa: E501

        Type of the amendment. Possible values are:  - Cancellation - NewProduct - OwnerTransfer - RemoveProduct - Renewal - UpdateProduct - TermsAndConditions   # noqa: E501

        :return: The type of this GETAmendmentType.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GETAmendmentType.

        Type of the amendment. Possible values are:  - Cancellation - NewProduct - OwnerTransfer - RemoveProduct - Renewal - UpdateProduct - TermsAndConditions   # noqa: E501

        :param type: The type of this GETAmendmentType.  # noqa: E501
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
        if issubclass(GETAmendmentType, dict):
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
        if not isinstance(other, GETAmendmentType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
