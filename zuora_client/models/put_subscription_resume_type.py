# coding: utf-8




import pprint
import re  # noqa: F401

import six


class PUTSubscriptionResumeType(object):
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
        'apply_credit_balance': 'bool',
        'collect': 'bool',
        'contract_effective_date': 'date',
        'document_date': 'date',
        'extends_term': 'bool',
        'invoice': 'bool',
        'invoice_collect': 'bool',
        'invoice_target_date': 'date',
        'resume_periods': 'str',
        'resume_periods_type': 'str',
        'resume_policy': 'str',
        'resume_specific_date': 'date',
        'run_billing': 'bool',
        'target_date': 'date'
    }

    attribute_map = {
        'apply_credit_balance': 'applyCreditBalance',
        'collect': 'collect',
        'contract_effective_date': 'contractEffectiveDate',
        'document_date': 'documentDate',
        'extends_term': 'extendsTerm',
        'invoice': 'invoice',
        'invoice_collect': 'invoiceCollect',
        'invoice_target_date': 'invoiceTargetDate',
        'resume_periods': 'resumePeriods',
        'resume_periods_type': 'resumePeriodsType',
        'resume_policy': 'resumePolicy',
        'resume_specific_date': 'resumeSpecificDate',
        'run_billing': 'runBilling',
        'target_date': 'targetDate'
    }

    def __init__(self, apply_credit_balance=None, collect=None, contract_effective_date=None, document_date=None, extends_term=None, invoice=None, invoice_collect=None, invoice_target_date=None, resume_periods=None, resume_periods_type=None, resume_policy=None, resume_specific_date=None, run_billing=False, target_date=None):  # noqa: E501
        """PUTSubscriptionResumeType - a model defined in Swagger"""  # noqa: E501

        self._apply_credit_balance = None
        self._collect = None
        self._contract_effective_date = None
        self._document_date = None
        self._extends_term = None
        self._invoice = None
        self._invoice_collect = None
        self._invoice_target_date = None
        self._resume_periods = None
        self._resume_periods_type = None
        self._resume_policy = None
        self._resume_specific_date = None
        self._run_billing = None
        self._target_date = None
        self.discriminator = None

        if apply_credit_balance is not None:
            self.apply_credit_balance = apply_credit_balance
        if collect is not None:
            self.collect = collect
        if contract_effective_date is not None:
            self.contract_effective_date = contract_effective_date
        if document_date is not None:
            self.document_date = document_date
        if extends_term is not None:
            self.extends_term = extends_term
        if invoice is not None:
            self.invoice = invoice
        if invoice_collect is not None:
            self.invoice_collect = invoice_collect
        if invoice_target_date is not None:
            self.invoice_target_date = invoice_target_date
        if resume_periods is not None:
            self.resume_periods = resume_periods
        if resume_periods_type is not None:
            self.resume_periods_type = resume_periods_type
        self.resume_policy = resume_policy
        if resume_specific_date is not None:
            self.resume_specific_date = resume_specific_date
        if run_billing is not None:
            self.run_billing = run_billing
        if target_date is not None:
            self.target_date = target_date

    @property
    def apply_credit_balance(self):
        """Gets the apply_credit_balance of this PUTSubscriptionResumeType.  # noqa: E501

        Applies a credit balance to an invoice.  If the value is `true`, the credit balance is applied to the invoice. If the value is `false`, no action is taken.   To view the credit balance adjustment, retrieve the details of the invoice using the Get Invoices method.  Prerequisite: `invoice` must be `true`.   **Note:**    - If you are using the field `invoiceCollect` rather than the field `invoice`, the `invoiceCollect` value must be `true`.   - This field is deprecated if you have the Invoice Settlement feature enabled.   # noqa: E501

        :return: The apply_credit_balance of this PUTSubscriptionResumeType.  # noqa: E501
        :rtype: bool
        """
        return self._apply_credit_balance

    @apply_credit_balance.setter
    def apply_credit_balance(self, apply_credit_balance):
        """Sets the apply_credit_balance of this PUTSubscriptionResumeType.

        Applies a credit balance to an invoice.  If the value is `true`, the credit balance is applied to the invoice. If the value is `false`, no action is taken.   To view the credit balance adjustment, retrieve the details of the invoice using the Get Invoices method.  Prerequisite: `invoice` must be `true`.   **Note:**    - If you are using the field `invoiceCollect` rather than the field `invoice`, the `invoiceCollect` value must be `true`.   - This field is deprecated if you have the Invoice Settlement feature enabled.   # noqa: E501

        :param apply_credit_balance: The apply_credit_balance of this PUTSubscriptionResumeType.  # noqa: E501
        :type: bool
        """

        self._apply_credit_balance = apply_credit_balance

    @property
    def collect(self):
        """Gets the collect of this PUTSubscriptionResumeType.  # noqa: E501

        Collects an automatic payment for a subscription. The collection generated in this operation is only for this subscription, not for the entire customer account.  If the value is `true`, the automatic payment is collected. If the value is `false`, no action is taken.  The default value is false.  This field is in Zuora REST API version control. Supported minor versions are 196.0 or later. To use this field in the method, you must set the `zuora-version` parameter to the minor version number in the request header.  Prerequisite: `invoice` must be `true`.   # noqa: E501

        :return: The collect of this PUTSubscriptionResumeType.  # noqa: E501
        :rtype: bool
        """
        return self._collect

    @collect.setter
    def collect(self, collect):
        """Sets the collect of this PUTSubscriptionResumeType.

        Collects an automatic payment for a subscription. The collection generated in this operation is only for this subscription, not for the entire customer account.  If the value is `true`, the automatic payment is collected. If the value is `false`, no action is taken.  The default value is false.  This field is in Zuora REST API version control. Supported minor versions are 196.0 or later. To use this field in the method, you must set the `zuora-version` parameter to the minor version number in the request header.  Prerequisite: `invoice` must be `true`.   # noqa: E501

        :param collect: The collect of this PUTSubscriptionResumeType.  # noqa: E501
        :type: bool
        """

        self._collect = collect

    @property
    def contract_effective_date(self):
        """Gets the contract_effective_date of this PUTSubscriptionResumeType.  # noqa: E501

        The date when the customer notifies you that they want to resume their subscription.   # noqa: E501

        :return: The contract_effective_date of this PUTSubscriptionResumeType.  # noqa: E501
        :rtype: date
        """
        return self._contract_effective_date

    @contract_effective_date.setter
    def contract_effective_date(self, contract_effective_date):
        """Sets the contract_effective_date of this PUTSubscriptionResumeType.

        The date when the customer notifies you that they want to resume their subscription.   # noqa: E501

        :param contract_effective_date: The contract_effective_date of this PUTSubscriptionResumeType.  # noqa: E501
        :type: date
        """

        self._contract_effective_date = contract_effective_date

    @property
    def document_date(self):
        """Gets the document_date of this PUTSubscriptionResumeType.  # noqa: E501

        The date of the billing document, in `yyyy-mm-dd` format. It represents the invoice date for invoices, credit memo date for credit memos, and debit memo date for debit memos.  - If this field is specified, the specified date is used as the billing document date.  - If this field is not specified, the date specified in the `targetDate` is used as the billing document date.   # noqa: E501

        :return: The document_date of this PUTSubscriptionResumeType.  # noqa: E501
        :rtype: date
        """
        return self._document_date

    @document_date.setter
    def document_date(self, document_date):
        """Sets the document_date of this PUTSubscriptionResumeType.

        The date of the billing document, in `yyyy-mm-dd` format. It represents the invoice date for invoices, credit memo date for credit memos, and debit memo date for debit memos.  - If this field is specified, the specified date is used as the billing document date.  - If this field is not specified, the date specified in the `targetDate` is used as the billing document date.   # noqa: E501

        :param document_date: The document_date of this PUTSubscriptionResumeType.  # noqa: E501
        :type: date
        """

        self._document_date = document_date

    @property
    def extends_term(self):
        """Gets the extends_term of this PUTSubscriptionResumeType.  # noqa: E501

        Whether to extend the subscription term by the length of time the suspension is in effect.  Values: `true`, `false`.   # noqa: E501

        :return: The extends_term of this PUTSubscriptionResumeType.  # noqa: E501
        :rtype: bool
        """
        return self._extends_term

    @extends_term.setter
    def extends_term(self, extends_term):
        """Sets the extends_term of this PUTSubscriptionResumeType.

        Whether to extend the subscription term by the length of time the suspension is in effect.  Values: `true`, `false`.   # noqa: E501

        :param extends_term: The extends_term of this PUTSubscriptionResumeType.  # noqa: E501
        :type: bool
        """

        self._extends_term = extends_term

    @property
    def invoice(self):
        """Gets the invoice of this PUTSubscriptionResumeType.  # noqa: E501

        **Note:** This field has been replaced by the `runBilling` field. The `invoice` field is only available for backward compatibility.   Creates an invoice for a subscription. The invoice generated in this operation is only for this subscription, not for the entire customer account.   If the value is `true`, an invoice is created. If the value is `false`, no action is taken. The default value is `false`.   This field is in Zuora REST API version control. Supported minor versions are `196.0` and `207.0`. To use this field in the method, you must set the `zuora-version` parameter to the minor version number in the request header.    # noqa: E501

        :return: The invoice of this PUTSubscriptionResumeType.  # noqa: E501
        :rtype: bool
        """
        return self._invoice

    @invoice.setter
    def invoice(self, invoice):
        """Sets the invoice of this PUTSubscriptionResumeType.

        **Note:** This field has been replaced by the `runBilling` field. The `invoice` field is only available for backward compatibility.   Creates an invoice for a subscription. The invoice generated in this operation is only for this subscription, not for the entire customer account.   If the value is `true`, an invoice is created. If the value is `false`, no action is taken. The default value is `false`.   This field is in Zuora REST API version control. Supported minor versions are `196.0` and `207.0`. To use this field in the method, you must set the `zuora-version` parameter to the minor version number in the request header.    # noqa: E501

        :param invoice: The invoice of this PUTSubscriptionResumeType.  # noqa: E501
        :type: bool
        """

        self._invoice = invoice

    @property
    def invoice_collect(self):
        """Gets the invoice_collect of this PUTSubscriptionResumeType.  # noqa: E501

        **Note:** This field has been replaced by the `invoice` field and the `collect` field. `invoiceCollect` is available only for backward compatibility.  If `true`, an invoice is generated and payment collected automatically during the subscription process. If `false` (default), no invoicing or payment takes place.  The invoice generated in this operation is only for this subscription, not for the entire customer account.  This field is in Zuora REST API version control. Supported minor versions are 186.0, 187.0, 188.0, 189.0, and 196.0.   # noqa: E501

        :return: The invoice_collect of this PUTSubscriptionResumeType.  # noqa: E501
        :rtype: bool
        """
        return self._invoice_collect

    @invoice_collect.setter
    def invoice_collect(self, invoice_collect):
        """Sets the invoice_collect of this PUTSubscriptionResumeType.

        **Note:** This field has been replaced by the `invoice` field and the `collect` field. `invoiceCollect` is available only for backward compatibility.  If `true`, an invoice is generated and payment collected automatically during the subscription process. If `false` (default), no invoicing or payment takes place.  The invoice generated in this operation is only for this subscription, not for the entire customer account.  This field is in Zuora REST API version control. Supported minor versions are 186.0, 187.0, 188.0, 189.0, and 196.0.   # noqa: E501

        :param invoice_collect: The invoice_collect of this PUTSubscriptionResumeType.  # noqa: E501
        :type: bool
        """

        self._invoice_collect = invoice_collect

    @property
    def invoice_target_date(self):
        """Gets the invoice_target_date of this PUTSubscriptionResumeType.  # noqa: E501

        **Note:** This field has been replaced by the `targetDate` field. The `invoiceTargetDate` field is only available for backward compatibility.   Date through which to calculate charges if an invoice is generated, as yyyy-mm-dd. Default is current date.   This field is in Zuora REST API version control. Supported minor versions are `207.0` and earlier.     # noqa: E501

        :return: The invoice_target_date of this PUTSubscriptionResumeType.  # noqa: E501
        :rtype: date
        """
        return self._invoice_target_date

    @invoice_target_date.setter
    def invoice_target_date(self, invoice_target_date):
        """Sets the invoice_target_date of this PUTSubscriptionResumeType.

        **Note:** This field has been replaced by the `targetDate` field. The `invoiceTargetDate` field is only available for backward compatibility.   Date through which to calculate charges if an invoice is generated, as yyyy-mm-dd. Default is current date.   This field is in Zuora REST API version control. Supported minor versions are `207.0` and earlier.     # noqa: E501

        :param invoice_target_date: The invoice_target_date of this PUTSubscriptionResumeType.  # noqa: E501
        :type: date
        """

        self._invoice_target_date = invoice_target_date

    @property
    def resume_periods(self):
        """Gets the resume_periods of this PUTSubscriptionResumeType.  # noqa: E501

        The length of the period used to specify when the subscription is resumed. The subscription resumption takes effect after a specified period based on the suspend date or today's date. You must use this field together with the `resumePeriodsType` field to specify the period.  **Note:** This field is only applicable when the `suspendPolicy` field is set to `FixedPeriodsFromToday` or `FixedPeriodsFromSuspendDate`.   # noqa: E501

        :return: The resume_periods of this PUTSubscriptionResumeType.  # noqa: E501
        :rtype: str
        """
        return self._resume_periods

    @resume_periods.setter
    def resume_periods(self, resume_periods):
        """Sets the resume_periods of this PUTSubscriptionResumeType.

        The length of the period used to specify when the subscription is resumed. The subscription resumption takes effect after a specified period based on the suspend date or today's date. You must use this field together with the `resumePeriodsType` field to specify the period.  **Note:** This field is only applicable when the `suspendPolicy` field is set to `FixedPeriodsFromToday` or `FixedPeriodsFromSuspendDate`.   # noqa: E501

        :param resume_periods: The resume_periods of this PUTSubscriptionResumeType.  # noqa: E501
        :type: str
        """

        self._resume_periods = resume_periods

    @property
    def resume_periods_type(self):
        """Gets the resume_periods_type of this PUTSubscriptionResumeType.  # noqa: E501

        The period type used to define when the subscription resumption takes effect. The subscription resumption takes effect after a specified period based on the suspend date or today's date. You must use this field together with the `resumePeriods` field to specify the period.  Values: `Day`, `Week`, `Month`, `Year`  **Note:** This field is only applicable when the `suspendPolicy` field is set to `FixedPeriodsFromToday` or `FixedPeriodsFromSuspendDate`.   # noqa: E501

        :return: The resume_periods_type of this PUTSubscriptionResumeType.  # noqa: E501
        :rtype: str
        """
        return self._resume_periods_type

    @resume_periods_type.setter
    def resume_periods_type(self, resume_periods_type):
        """Sets the resume_periods_type of this PUTSubscriptionResumeType.

        The period type used to define when the subscription resumption takes effect. The subscription resumption takes effect after a specified period based on the suspend date or today's date. You must use this field together with the `resumePeriods` field to specify the period.  Values: `Day`, `Week`, `Month`, `Year`  **Note:** This field is only applicable when the `suspendPolicy` field is set to `FixedPeriodsFromToday` or `FixedPeriodsFromSuspendDate`.   # noqa: E501

        :param resume_periods_type: The resume_periods_type of this PUTSubscriptionResumeType.  # noqa: E501
        :type: str
        """

        self._resume_periods_type = resume_periods_type

    @property
    def resume_policy(self):
        """Gets the resume_policy of this PUTSubscriptionResumeType.  # noqa: E501

        Resume methods. Specify a way to resume a subscription.  Values:  * `Today`: The subscription resumption takes effect on today's date.  * `FixedPeriodsFromSuspendDate`: The subscription resumption takes effect after a specified period based on the suspend date. You must specify the `resumePeriods` and `resumePeriodsType` fields to define the period.  * `SpecificDate`: The subscription resumption takes effect on a specific date. You must define the specific date in the `resumeSpecificDate` field.  * `FixedPeriodsFromToday`: The subscription resumption takes effect after a specified period based on the today's date. You must specify the `resumePeriods` and `resumePeriodsType` fields to define the period.   # noqa: E501

        :return: The resume_policy of this PUTSubscriptionResumeType.  # noqa: E501
        :rtype: str
        """
        return self._resume_policy

    @resume_policy.setter
    def resume_policy(self, resume_policy):
        """Sets the resume_policy of this PUTSubscriptionResumeType.

        Resume methods. Specify a way to resume a subscription.  Values:  * `Today`: The subscription resumption takes effect on today's date.  * `FixedPeriodsFromSuspendDate`: The subscription resumption takes effect after a specified period based on the suspend date. You must specify the `resumePeriods` and `resumePeriodsType` fields to define the period.  * `SpecificDate`: The subscription resumption takes effect on a specific date. You must define the specific date in the `resumeSpecificDate` field.  * `FixedPeriodsFromToday`: The subscription resumption takes effect after a specified period based on the today's date. You must specify the `resumePeriods` and `resumePeriodsType` fields to define the period.   # noqa: E501

        :param resume_policy: The resume_policy of this PUTSubscriptionResumeType.  # noqa: E501
        :type: str
        """
        if resume_policy is None:
            raise ValueError("Invalid value for `resume_policy`, must not be `None`")  # noqa: E501

        self._resume_policy = resume_policy

    @property
    def resume_specific_date(self):
        """Gets the resume_specific_date of this PUTSubscriptionResumeType.  # noqa: E501

        A specific date when the subscription resumption takes effect, in the format yyyy-mm-dd.  **Note:** This field is only applicable only when the `resumePolicy` field is set to `SpecificDate`.  The value should not be earlier than the subscription suspension date.   # noqa: E501

        :return: The resume_specific_date of this PUTSubscriptionResumeType.  # noqa: E501
        :rtype: date
        """
        return self._resume_specific_date

    @resume_specific_date.setter
    def resume_specific_date(self, resume_specific_date):
        """Sets the resume_specific_date of this PUTSubscriptionResumeType.

        A specific date when the subscription resumption takes effect, in the format yyyy-mm-dd.  **Note:** This field is only applicable only when the `resumePolicy` field is set to `SpecificDate`.  The value should not be earlier than the subscription suspension date.   # noqa: E501

        :param resume_specific_date: The resume_specific_date of this PUTSubscriptionResumeType.  # noqa: E501
        :type: date
        """

        self._resume_specific_date = resume_specific_date

    @property
    def run_billing(self):
        """Gets the run_billing of this PUTSubscriptionResumeType.  # noqa: E501

        Creates an invoice for a subscription. If you have the Invoice Settlement feature enabled, a credit memo might also be created based on the [invoice and credit memo generation rule](https://knowledgecenter.zuora.com/CB_Billing/Invoice_Settlement/Credit_and_Debit_Memos/Rules_for_Generating_Invoices_and_Credit_Memos).     The billing documents generated in this operation is only for this subscription, not for the entire customer account.   Possible values:  - `true`: An invoice is created. If you have the Invoice Settlement feature enabled, a credit memo might also be created.   - `false`: No invoice is created.   **Note:** This field is in Zuora REST API version control. Supported minor versions are `211.0` or later. To use this field in the method, you must set the `zuora-version` parameter to the minor version number in the request header.   # noqa: E501

        :return: The run_billing of this PUTSubscriptionResumeType.  # noqa: E501
        :rtype: bool
        """
        return self._run_billing

    @run_billing.setter
    def run_billing(self, run_billing):
        """Sets the run_billing of this PUTSubscriptionResumeType.

        Creates an invoice for a subscription. If you have the Invoice Settlement feature enabled, a credit memo might also be created based on the [invoice and credit memo generation rule](https://knowledgecenter.zuora.com/CB_Billing/Invoice_Settlement/Credit_and_Debit_Memos/Rules_for_Generating_Invoices_and_Credit_Memos).     The billing documents generated in this operation is only for this subscription, not for the entire customer account.   Possible values:  - `true`: An invoice is created. If you have the Invoice Settlement feature enabled, a credit memo might also be created.   - `false`: No invoice is created.   **Note:** This field is in Zuora REST API version control. Supported minor versions are `211.0` or later. To use this field in the method, you must set the `zuora-version` parameter to the minor version number in the request header.   # noqa: E501

        :param run_billing: The run_billing of this PUTSubscriptionResumeType.  # noqa: E501
        :type: bool
        """

        self._run_billing = run_billing

    @property
    def target_date(self):
        """Gets the target_date of this PUTSubscriptionResumeType.  # noqa: E501

        Date through which to calculate charges if an invoice or a credit memo is generated, as yyyy-mm-dd. Default is current date.   **Note:** The credit memo is only available if you have the Invoice Settlement feature enabled.   This field is in Zuora REST API version control. Supported minor versions are `211.0` and later. To use this field in the method, you must set the  `zuora-version` parameter to the minor version number in the request header.   # noqa: E501

        :return: The target_date of this PUTSubscriptionResumeType.  # noqa: E501
        :rtype: date
        """
        return self._target_date

    @target_date.setter
    def target_date(self, target_date):
        """Sets the target_date of this PUTSubscriptionResumeType.

        Date through which to calculate charges if an invoice or a credit memo is generated, as yyyy-mm-dd. Default is current date.   **Note:** The credit memo is only available if you have the Invoice Settlement feature enabled.   This field is in Zuora REST API version control. Supported minor versions are `211.0` and later. To use this field in the method, you must set the  `zuora-version` parameter to the minor version number in the request header.   # noqa: E501

        :param target_date: The target_date of this PUTSubscriptionResumeType.  # noqa: E501
        :type: date
        """

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
        if issubclass(PUTSubscriptionResumeType, dict):
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
        if not isinstance(other, PUTSubscriptionResumeType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
