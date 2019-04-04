# coding: utf-8




import pprint
import re  # noqa: F401

import six


class GETAccountingPeriodTypeFileIds(object):
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
        'accounts_receivable_account_aging_detail_export_file_id': 'str',
        'accounts_receivable_invoice_aging_detail_export_file_id': 'str',
        'ar_roll_forward_detail_export_file_id': 'str',
        'fx_realized_gain_and_loss_detail_export_file_id': 'str',
        'fx_unrealized_gain_and_loss_detail_export_file_id': 'str',
        'revenue_detail_csv_file_id': 'str',
        'revenue_detail_excel_file_id': 'str',
        'unprocessed_charges_file_id': 'str'
    }

    attribute_map = {
        'accounts_receivable_account_aging_detail_export_file_id': 'accountsReceivableAccountAgingDetailExportFileId',
        'accounts_receivable_invoice_aging_detail_export_file_id': 'accountsReceivableInvoiceAgingDetailExportFileId',
        'ar_roll_forward_detail_export_file_id': 'arRollForwardDetailExportFileId',
        'fx_realized_gain_and_loss_detail_export_file_id': 'fxRealizedGainAndLossDetailExportFileId',
        'fx_unrealized_gain_and_loss_detail_export_file_id': 'fxUnrealizedGainAndLossDetailExportFileId',
        'revenue_detail_csv_file_id': 'revenueDetailCsvFileId',
        'revenue_detail_excel_file_id': 'revenueDetailExcelFileId',
        'unprocessed_charges_file_id': 'unprocessedChargesFileId'
    }

    def __init__(self, accounts_receivable_account_aging_detail_export_file_id=None, accounts_receivable_invoice_aging_detail_export_file_id=None, ar_roll_forward_detail_export_file_id=None, fx_realized_gain_and_loss_detail_export_file_id=None, fx_unrealized_gain_and_loss_detail_export_file_id=None, revenue_detail_csv_file_id=None, revenue_detail_excel_file_id=None, unprocessed_charges_file_id=None):  # noqa: E501
        """GETAccountingPeriodTypeFileIds - a model defined in Swagger"""  # noqa: E501

        self._accounts_receivable_account_aging_detail_export_file_id = None
        self._accounts_receivable_invoice_aging_detail_export_file_id = None
        self._ar_roll_forward_detail_export_file_id = None
        self._fx_realized_gain_and_loss_detail_export_file_id = None
        self._fx_unrealized_gain_and_loss_detail_export_file_id = None
        self._revenue_detail_csv_file_id = None
        self._revenue_detail_excel_file_id = None
        self._unprocessed_charges_file_id = None
        self.discriminator = None

        if accounts_receivable_account_aging_detail_export_file_id is not None:
            self.accounts_receivable_account_aging_detail_export_file_id = accounts_receivable_account_aging_detail_export_file_id
        if accounts_receivable_invoice_aging_detail_export_file_id is not None:
            self.accounts_receivable_invoice_aging_detail_export_file_id = accounts_receivable_invoice_aging_detail_export_file_id
        if ar_roll_forward_detail_export_file_id is not None:
            self.ar_roll_forward_detail_export_file_id = ar_roll_forward_detail_export_file_id
        if fx_realized_gain_and_loss_detail_export_file_id is not None:
            self.fx_realized_gain_and_loss_detail_export_file_id = fx_realized_gain_and_loss_detail_export_file_id
        if fx_unrealized_gain_and_loss_detail_export_file_id is not None:
            self.fx_unrealized_gain_and_loss_detail_export_file_id = fx_unrealized_gain_and_loss_detail_export_file_id
        if revenue_detail_csv_file_id is not None:
            self.revenue_detail_csv_file_id = revenue_detail_csv_file_id
        if revenue_detail_excel_file_id is not None:
            self.revenue_detail_excel_file_id = revenue_detail_excel_file_id
        if unprocessed_charges_file_id is not None:
            self.unprocessed_charges_file_id = unprocessed_charges_file_id

    @property
    def accounts_receivable_account_aging_detail_export_file_id(self):
        """Gets the accounts_receivable_account_aging_detail_export_file_id of this GETAccountingPeriodTypeFileIds.  # noqa: E501

        File ID of the Accounts Receivable Aging Account Detail report.   # noqa: E501

        :return: The accounts_receivable_account_aging_detail_export_file_id of this GETAccountingPeriodTypeFileIds.  # noqa: E501
        :rtype: str
        """
        return self._accounts_receivable_account_aging_detail_export_file_id

    @accounts_receivable_account_aging_detail_export_file_id.setter
    def accounts_receivable_account_aging_detail_export_file_id(self, accounts_receivable_account_aging_detail_export_file_id):
        """Sets the accounts_receivable_account_aging_detail_export_file_id of this GETAccountingPeriodTypeFileIds.

        File ID of the Accounts Receivable Aging Account Detail report.   # noqa: E501

        :param accounts_receivable_account_aging_detail_export_file_id: The accounts_receivable_account_aging_detail_export_file_id of this GETAccountingPeriodTypeFileIds.  # noqa: E501
        :type: str
        """

        self._accounts_receivable_account_aging_detail_export_file_id = accounts_receivable_account_aging_detail_export_file_id

    @property
    def accounts_receivable_invoice_aging_detail_export_file_id(self):
        """Gets the accounts_receivable_invoice_aging_detail_export_file_id of this GETAccountingPeriodTypeFileIds.  # noqa: E501

        File ID of the Accounts Receivable Aging Invoice Detail report.   # noqa: E501

        :return: The accounts_receivable_invoice_aging_detail_export_file_id of this GETAccountingPeriodTypeFileIds.  # noqa: E501
        :rtype: str
        """
        return self._accounts_receivable_invoice_aging_detail_export_file_id

    @accounts_receivable_invoice_aging_detail_export_file_id.setter
    def accounts_receivable_invoice_aging_detail_export_file_id(self, accounts_receivable_invoice_aging_detail_export_file_id):
        """Sets the accounts_receivable_invoice_aging_detail_export_file_id of this GETAccountingPeriodTypeFileIds.

        File ID of the Accounts Receivable Aging Invoice Detail report.   # noqa: E501

        :param accounts_receivable_invoice_aging_detail_export_file_id: The accounts_receivable_invoice_aging_detail_export_file_id of this GETAccountingPeriodTypeFileIds.  # noqa: E501
        :type: str
        """

        self._accounts_receivable_invoice_aging_detail_export_file_id = accounts_receivable_invoice_aging_detail_export_file_id

    @property
    def ar_roll_forward_detail_export_file_id(self):
        """Gets the ar_roll_forward_detail_export_file_id of this GETAccountingPeriodTypeFileIds.  # noqa: E501

        File ID of the Accounts Receivable Detail report.   # noqa: E501

        :return: The ar_roll_forward_detail_export_file_id of this GETAccountingPeriodTypeFileIds.  # noqa: E501
        :rtype: str
        """
        return self._ar_roll_forward_detail_export_file_id

    @ar_roll_forward_detail_export_file_id.setter
    def ar_roll_forward_detail_export_file_id(self, ar_roll_forward_detail_export_file_id):
        """Sets the ar_roll_forward_detail_export_file_id of this GETAccountingPeriodTypeFileIds.

        File ID of the Accounts Receivable Detail report.   # noqa: E501

        :param ar_roll_forward_detail_export_file_id: The ar_roll_forward_detail_export_file_id of this GETAccountingPeriodTypeFileIds.  # noqa: E501
        :type: str
        """

        self._ar_roll_forward_detail_export_file_id = ar_roll_forward_detail_export_file_id

    @property
    def fx_realized_gain_and_loss_detail_export_file_id(self):
        """Gets the fx_realized_gain_and_loss_detail_export_file_id of this GETAccountingPeriodTypeFileIds.  # noqa: E501

        File ID of the Realized Gain and Loss Detail report.  Returned only if you have Foreign Currency Conversion enabled.   # noqa: E501

        :return: The fx_realized_gain_and_loss_detail_export_file_id of this GETAccountingPeriodTypeFileIds.  # noqa: E501
        :rtype: str
        """
        return self._fx_realized_gain_and_loss_detail_export_file_id

    @fx_realized_gain_and_loss_detail_export_file_id.setter
    def fx_realized_gain_and_loss_detail_export_file_id(self, fx_realized_gain_and_loss_detail_export_file_id):
        """Sets the fx_realized_gain_and_loss_detail_export_file_id of this GETAccountingPeriodTypeFileIds.

        File ID of the Realized Gain and Loss Detail report.  Returned only if you have Foreign Currency Conversion enabled.   # noqa: E501

        :param fx_realized_gain_and_loss_detail_export_file_id: The fx_realized_gain_and_loss_detail_export_file_id of this GETAccountingPeriodTypeFileIds.  # noqa: E501
        :type: str
        """

        self._fx_realized_gain_and_loss_detail_export_file_id = fx_realized_gain_and_loss_detail_export_file_id

    @property
    def fx_unrealized_gain_and_loss_detail_export_file_id(self):
        """Gets the fx_unrealized_gain_and_loss_detail_export_file_id of this GETAccountingPeriodTypeFileIds.  # noqa: E501

        File ID of the Unrealized Gain and Loss Detail report.  Returned only if you have Foreign Currency Conversion enabled   # noqa: E501

        :return: The fx_unrealized_gain_and_loss_detail_export_file_id of this GETAccountingPeriodTypeFileIds.  # noqa: E501
        :rtype: str
        """
        return self._fx_unrealized_gain_and_loss_detail_export_file_id

    @fx_unrealized_gain_and_loss_detail_export_file_id.setter
    def fx_unrealized_gain_and_loss_detail_export_file_id(self, fx_unrealized_gain_and_loss_detail_export_file_id):
        """Sets the fx_unrealized_gain_and_loss_detail_export_file_id of this GETAccountingPeriodTypeFileIds.

        File ID of the Unrealized Gain and Loss Detail report.  Returned only if you have Foreign Currency Conversion enabled   # noqa: E501

        :param fx_unrealized_gain_and_loss_detail_export_file_id: The fx_unrealized_gain_and_loss_detail_export_file_id of this GETAccountingPeriodTypeFileIds.  # noqa: E501
        :type: str
        """

        self._fx_unrealized_gain_and_loss_detail_export_file_id = fx_unrealized_gain_and_loss_detail_export_file_id

    @property
    def revenue_detail_csv_file_id(self):
        """Gets the revenue_detail_csv_file_id of this GETAccountingPeriodTypeFileIds.  # noqa: E501

        File ID of the Revenue Detail report in CSV format.   # noqa: E501

        :return: The revenue_detail_csv_file_id of this GETAccountingPeriodTypeFileIds.  # noqa: E501
        :rtype: str
        """
        return self._revenue_detail_csv_file_id

    @revenue_detail_csv_file_id.setter
    def revenue_detail_csv_file_id(self, revenue_detail_csv_file_id):
        """Sets the revenue_detail_csv_file_id of this GETAccountingPeriodTypeFileIds.

        File ID of the Revenue Detail report in CSV format.   # noqa: E501

        :param revenue_detail_csv_file_id: The revenue_detail_csv_file_id of this GETAccountingPeriodTypeFileIds.  # noqa: E501
        :type: str
        """

        self._revenue_detail_csv_file_id = revenue_detail_csv_file_id

    @property
    def revenue_detail_excel_file_id(self):
        """Gets the revenue_detail_excel_file_id of this GETAccountingPeriodTypeFileIds.  # noqa: E501

        File ID of the Revenue Detail report in XLSX format.   # noqa: E501

        :return: The revenue_detail_excel_file_id of this GETAccountingPeriodTypeFileIds.  # noqa: E501
        :rtype: str
        """
        return self._revenue_detail_excel_file_id

    @revenue_detail_excel_file_id.setter
    def revenue_detail_excel_file_id(self, revenue_detail_excel_file_id):
        """Sets the revenue_detail_excel_file_id of this GETAccountingPeriodTypeFileIds.

        File ID of the Revenue Detail report in XLSX format.   # noqa: E501

        :param revenue_detail_excel_file_id: The revenue_detail_excel_file_id of this GETAccountingPeriodTypeFileIds.  # noqa: E501
        :type: str
        """

        self._revenue_detail_excel_file_id = revenue_detail_excel_file_id

    @property
    def unprocessed_charges_file_id(self):
        """Gets the unprocessed_charges_file_id of this GETAccountingPeriodTypeFileIds.  # noqa: E501

        File ID of a report containing all unprocessed charges for the accounting period.   # noqa: E501

        :return: The unprocessed_charges_file_id of this GETAccountingPeriodTypeFileIds.  # noqa: E501
        :rtype: str
        """
        return self._unprocessed_charges_file_id

    @unprocessed_charges_file_id.setter
    def unprocessed_charges_file_id(self, unprocessed_charges_file_id):
        """Sets the unprocessed_charges_file_id of this GETAccountingPeriodTypeFileIds.

        File ID of a report containing all unprocessed charges for the accounting period.   # noqa: E501

        :param unprocessed_charges_file_id: The unprocessed_charges_file_id of this GETAccountingPeriodTypeFileIds.  # noqa: E501
        :type: str
        """

        self._unprocessed_charges_file_id = unprocessed_charges_file_id

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
        if issubclass(GETAccountingPeriodTypeFileIds, dict):
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
        if not isinstance(other, GETAccountingPeriodTypeFileIds):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
