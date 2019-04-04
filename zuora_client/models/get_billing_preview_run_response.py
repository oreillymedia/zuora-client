# coding: utf-8




import pprint
import re  # noqa: F401

import six


class GetBillingPreviewRunResponse(object):
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
        'created_by_id': 'str',
        'created_date': 'str',
        'end_date': 'str',
        'error_message': 'str',
        'including_evergreen_subscription': 'bool',
        'result_file_url': 'str',
        'run_number': 'str',
        'start_date': 'str',
        'status': 'str',
        'succeeded_accounts': 'int',
        'success': 'bool',
        'target_date': 'date',
        'total_accounts': 'int',
        'updated_by_id': 'str',
        'updated_date': 'datetime'
    }

    attribute_map = {
        'assume_renewal': 'assumeRenewal',
        'batch': 'batch',
        'charge_type_to_exclude': 'chargeTypeToExclude',
        'created_by_id': 'createdById',
        'created_date': 'createdDate',
        'end_date': 'endDate',
        'error_message': 'errorMessage',
        'including_evergreen_subscription': 'includingEvergreenSubscription',
        'result_file_url': 'resultFileUrl',
        'run_number': 'runNumber',
        'start_date': 'startDate',
        'status': 'status',
        'succeeded_accounts': 'succeededAccounts',
        'success': 'success',
        'target_date': 'targetDate',
        'total_accounts': 'totalAccounts',
        'updated_by_id': 'updatedById',
        'updated_date': 'updatedDate'
    }

    def __init__(self, assume_renewal=None, batch=None, charge_type_to_exclude=None, created_by_id=None, created_date=None, end_date=None, error_message=None, including_evergreen_subscription=None, result_file_url=None, run_number=None, start_date=None, status=None, succeeded_accounts=None, success=None, target_date=None, total_accounts=None, updated_by_id=None, updated_date=None):  # noqa: E501
        """GetBillingPreviewRunResponse - a model defined in Swagger"""  # noqa: E501

        self._assume_renewal = None
        self._batch = None
        self._charge_type_to_exclude = None
        self._created_by_id = None
        self._created_date = None
        self._end_date = None
        self._error_message = None
        self._including_evergreen_subscription = None
        self._result_file_url = None
        self._run_number = None
        self._start_date = None
        self._status = None
        self._succeeded_accounts = None
        self._success = None
        self._target_date = None
        self._total_accounts = None
        self._updated_by_id = None
        self._updated_date = None
        self.discriminator = None

        if assume_renewal is not None:
            self.assume_renewal = assume_renewal
        if batch is not None:
            self.batch = batch
        if charge_type_to_exclude is not None:
            self.charge_type_to_exclude = charge_type_to_exclude
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_date is not None:
            self.created_date = created_date
        if end_date is not None:
            self.end_date = end_date
        if error_message is not None:
            self.error_message = error_message
        if including_evergreen_subscription is not None:
            self.including_evergreen_subscription = including_evergreen_subscription
        if result_file_url is not None:
            self.result_file_url = result_file_url
        if run_number is not None:
            self.run_number = run_number
        if start_date is not None:
            self.start_date = start_date
        if status is not None:
            self.status = status
        if succeeded_accounts is not None:
            self.succeeded_accounts = succeeded_accounts
        if success is not None:
            self.success = success
        if target_date is not None:
            self.target_date = target_date
        if total_accounts is not None:
            self.total_accounts = total_accounts
        if updated_by_id is not None:
            self.updated_by_id = updated_by_id
        if updated_date is not None:
            self.updated_date = updated_date

    @property
    def assume_renewal(self):
        """Gets the assume_renewal of this GetBillingPreviewRunResponse.  # noqa: E501

          # noqa: E501

        :return: The assume_renewal of this GetBillingPreviewRunResponse.  # noqa: E501
        :rtype: str
        """
        return self._assume_renewal

    @assume_renewal.setter
    def assume_renewal(self, assume_renewal):
        """Sets the assume_renewal of this GetBillingPreviewRunResponse.

          # noqa: E501

        :param assume_renewal: The assume_renewal of this GetBillingPreviewRunResponse.  # noqa: E501
        :type: str
        """

        self._assume_renewal = assume_renewal

    @property
    def batch(self):
        """Gets the batch of this GetBillingPreviewRunResponse.  # noqa: E501

        The customer batch included in the billing preview run.    # noqa: E501

        :return: The batch of this GetBillingPreviewRunResponse.  # noqa: E501
        :rtype: str
        """
        return self._batch

    @batch.setter
    def batch(self, batch):
        """Sets the batch of this GetBillingPreviewRunResponse.

        The customer batch included in the billing preview run.    # noqa: E501

        :param batch: The batch of this GetBillingPreviewRunResponse.  # noqa: E501
        :type: str
        """

        self._batch = batch

    @property
    def charge_type_to_exclude(self):
        """Gets the charge_type_to_exclude of this GetBillingPreviewRunResponse.  # noqa: E501

        The charge types excluded from the forecast run.   # noqa: E501

        :return: The charge_type_to_exclude of this GetBillingPreviewRunResponse.  # noqa: E501
        :rtype: str
        """
        return self._charge_type_to_exclude

    @charge_type_to_exclude.setter
    def charge_type_to_exclude(self, charge_type_to_exclude):
        """Sets the charge_type_to_exclude of this GetBillingPreviewRunResponse.

        The charge types excluded from the forecast run.   # noqa: E501

        :param charge_type_to_exclude: The charge_type_to_exclude of this GetBillingPreviewRunResponse.  # noqa: E501
        :type: str
        """

        self._charge_type_to_exclude = charge_type_to_exclude

    @property
    def created_by_id(self):
        """Gets the created_by_id of this GetBillingPreviewRunResponse.  # noqa: E501

        The ID of the user who created the billing preview run.   # noqa: E501

        :return: The created_by_id of this GetBillingPreviewRunResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this GetBillingPreviewRunResponse.

        The ID of the user who created the billing preview run.   # noqa: E501

        :param created_by_id: The created_by_id of this GetBillingPreviewRunResponse.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def created_date(self):
        """Gets the created_date of this GetBillingPreviewRunResponse.  # noqa: E501

        The date and time when the billing preview run was created.   # noqa: E501

        :return: The created_date of this GetBillingPreviewRunResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this GetBillingPreviewRunResponse.

        The date and time when the billing preview run was created.   # noqa: E501

        :param created_date: The created_date of this GetBillingPreviewRunResponse.  # noqa: E501
        :type: str
        """

        self._created_date = created_date

    @property
    def end_date(self):
        """Gets the end_date of this GetBillingPreviewRunResponse.  # noqa: E501

        The date and time when the billing preview run completes.   # noqa: E501

        :return: The end_date of this GetBillingPreviewRunResponse.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this GetBillingPreviewRunResponse.

        The date and time when the billing preview run completes.   # noqa: E501

        :param end_date: The end_date of this GetBillingPreviewRunResponse.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def error_message(self):
        """Gets the error_message of this GetBillingPreviewRunResponse.  # noqa: E501

        The error message generated by a failed billing preview run.   # noqa: E501

        :return: The error_message of this GetBillingPreviewRunResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this GetBillingPreviewRunResponse.

        The error message generated by a failed billing preview run.   # noqa: E501

        :param error_message: The error_message of this GetBillingPreviewRunResponse.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def including_evergreen_subscription(self):
        """Gets the including_evergreen_subscription of this GetBillingPreviewRunResponse.  # noqa: E501

        Indicates if evergreen subscriptions are included in the billing preview run.   # noqa: E501

        :return: The including_evergreen_subscription of this GetBillingPreviewRunResponse.  # noqa: E501
        :rtype: bool
        """
        return self._including_evergreen_subscription

    @including_evergreen_subscription.setter
    def including_evergreen_subscription(self, including_evergreen_subscription):
        """Sets the including_evergreen_subscription of this GetBillingPreviewRunResponse.

        Indicates if evergreen subscriptions are included in the billing preview run.   # noqa: E501

        :param including_evergreen_subscription: The including_evergreen_subscription of this GetBillingPreviewRunResponse.  # noqa: E501
        :type: bool
        """

        self._including_evergreen_subscription = including_evergreen_subscription

    @property
    def result_file_url(self):
        """Gets the result_file_url of this GetBillingPreviewRunResponse.  # noqa: E501

        The URL of the zipped CSV result file generated by the billing preview run. This file contains the preview invoice item data and credit memo item data for the specified customers.  **Note:** The credit memo item data is only available if you have Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   # noqa: E501

        :return: The result_file_url of this GetBillingPreviewRunResponse.  # noqa: E501
        :rtype: str
        """
        return self._result_file_url

    @result_file_url.setter
    def result_file_url(self, result_file_url):
        """Sets the result_file_url of this GetBillingPreviewRunResponse.

        The URL of the zipped CSV result file generated by the billing preview run. This file contains the preview invoice item data and credit memo item data for the specified customers.  **Note:** The credit memo item data is only available if you have Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   # noqa: E501

        :param result_file_url: The result_file_url of this GetBillingPreviewRunResponse.  # noqa: E501
        :type: str
        """

        self._result_file_url = result_file_url

    @property
    def run_number(self):
        """Gets the run_number of this GetBillingPreviewRunResponse.  # noqa: E501

        The run number of the billing preview run.   # noqa: E501

        :return: The run_number of this GetBillingPreviewRunResponse.  # noqa: E501
        :rtype: str
        """
        return self._run_number

    @run_number.setter
    def run_number(self, run_number):
        """Sets the run_number of this GetBillingPreviewRunResponse.

        The run number of the billing preview run.   # noqa: E501

        :param run_number: The run_number of this GetBillingPreviewRunResponse.  # noqa: E501
        :type: str
        """

        self._run_number = run_number

    @property
    def start_date(self):
        """Gets the start_date of this GetBillingPreviewRunResponse.  # noqa: E501

        The date and time when the billing preview run starts.   # noqa: E501

        :return: The start_date of this GetBillingPreviewRunResponse.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this GetBillingPreviewRunResponse.

        The date and time when the billing preview run starts.   # noqa: E501

        :param start_date: The start_date of this GetBillingPreviewRunResponse.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def status(self):
        """Gets the status of this GetBillingPreviewRunResponse.  # noqa: E501

        The status of the >billing preview run.  **Possible values:**   * 0: Pending * 1: Processing * 2: Completed * 3: Error * 4: Canceled   # noqa: E501

        :return: The status of this GetBillingPreviewRunResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetBillingPreviewRunResponse.

        The status of the >billing preview run.  **Possible values:**   * 0: Pending * 1: Processing * 2: Completed * 3: Error * 4: Canceled   # noqa: E501

        :param status: The status of this GetBillingPreviewRunResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def succeeded_accounts(self):
        """Gets the succeeded_accounts of this GetBillingPreviewRunResponse.  # noqa: E501

        The number of accounts for which preview invoice item data and credit memo item data was successfully generated during the billing preview run.  **Note:** The credit memo item data is only available if you have Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   # noqa: E501

        :return: The succeeded_accounts of this GetBillingPreviewRunResponse.  # noqa: E501
        :rtype: int
        """
        return self._succeeded_accounts

    @succeeded_accounts.setter
    def succeeded_accounts(self, succeeded_accounts):
        """Sets the succeeded_accounts of this GetBillingPreviewRunResponse.

        The number of accounts for which preview invoice item data and credit memo item data was successfully generated during the billing preview run.  **Note:** The credit memo item data is only available if you have Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   # noqa: E501

        :param succeeded_accounts: The succeeded_accounts of this GetBillingPreviewRunResponse.  # noqa: E501
        :type: int
        """

        self._succeeded_accounts = succeeded_accounts

    @property
    def success(self):
        """Gets the success of this GetBillingPreviewRunResponse.  # noqa: E501

        Returns `true` if the request was processed successfully.  # noqa: E501

        :return: The success of this GetBillingPreviewRunResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this GetBillingPreviewRunResponse.

        Returns `true` if the request was processed successfully.  # noqa: E501

        :param success: The success of this GetBillingPreviewRunResponse.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def target_date(self):
        """Gets the target_date of this GetBillingPreviewRunResponse.  # noqa: E501

        The target date for the billing preview run.             # noqa: E501

        :return: The target_date of this GetBillingPreviewRunResponse.  # noqa: E501
        :rtype: date
        """
        return self._target_date

    @target_date.setter
    def target_date(self, target_date):
        """Sets the target_date of this GetBillingPreviewRunResponse.

        The target date for the billing preview run.             # noqa: E501

        :param target_date: The target_date of this GetBillingPreviewRunResponse.  # noqa: E501
        :type: date
        """

        self._target_date = target_date

    @property
    def total_accounts(self):
        """Gets the total_accounts of this GetBillingPreviewRunResponse.  # noqa: E501

        The total number of accounts in the billing preview run.   # noqa: E501

        :return: The total_accounts of this GetBillingPreviewRunResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_accounts

    @total_accounts.setter
    def total_accounts(self, total_accounts):
        """Sets the total_accounts of this GetBillingPreviewRunResponse.

        The total number of accounts in the billing preview run.   # noqa: E501

        :param total_accounts: The total_accounts of this GetBillingPreviewRunResponse.  # noqa: E501
        :type: int
        """

        self._total_accounts = total_accounts

    @property
    def updated_by_id(self):
        """Gets the updated_by_id of this GetBillingPreviewRunResponse.  # noqa: E501

        The ID of the user who last updated the billing preview run.   # noqa: E501

        :return: The updated_by_id of this GetBillingPreviewRunResponse.  # noqa: E501
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """Sets the updated_by_id of this GetBillingPreviewRunResponse.

        The ID of the user who last updated the billing preview run.   # noqa: E501

        :param updated_by_id: The updated_by_id of this GetBillingPreviewRunResponse.  # noqa: E501
        :type: str
        """

        self._updated_by_id = updated_by_id

    @property
    def updated_date(self):
        """Gets the updated_date of this GetBillingPreviewRunResponse.  # noqa: E501

        The date and time when the billing preview run was last updated.   # noqa: E501

        :return: The updated_date of this GetBillingPreviewRunResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this GetBillingPreviewRunResponse.

        The date and time when the billing preview run was last updated.   # noqa: E501

        :param updated_date: The updated_date of this GetBillingPreviewRunResponse.  # noqa: E501
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
        if issubclass(GetBillingPreviewRunResponse, dict):
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
        if not isinstance(other, GetBillingPreviewRunResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
