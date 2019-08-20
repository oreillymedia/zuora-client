# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.debit_memo_object_custom_fields import DebitMemoObjectCustomFields  # noqa: F401,E501
from zuora_client.models.debit_memo_object_ns_fields import DebitMemoObjectNSFields  # noqa: F401,E501


class GETDebitMemoTypewithSuccess(object):
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
        'integration_id__ns': 'str',
        'integration_status__ns': 'str',
        'sync_date__ns': 'str',
        'account_id': 'str',
        'amount': 'float',
        'auto_pay': 'bool',
        'balance': 'float',
        'be_applied_amount': 'float',
        'cancelled_by_id': 'str',
        'cancelled_on': 'datetime',
        'comment': 'str',
        'created_by_id': 'str',
        'created_date': 'datetime',
        'debit_memo_date': 'date',
        'due_date': 'date',
        'id': 'str',
        'latest_pdf_file_id': 'str',
        'number': 'str',
        'posted_by_id': 'str',
        'posted_on': 'datetime',
        'reason_code': 'str',
        'referred_invoice_id': 'str',
        'status': 'str',
        'target_date': 'date',
        'tax_amount': 'float',
        'total_tax_exempt_amount': 'float',
        'transferred_to_accounting': 'str',
        'updated_by_id': 'str',
        'updated_date': 'datetime'
    }

    attribute_map = {
        'integration_id__ns': 'IntegrationId__NS',
        'integration_status__ns': 'IntegrationStatus__NS',
        'sync_date__ns': 'SyncDate__NS',
        'account_id': 'accountId',
        'amount': 'amount',
        'auto_pay': 'autoPay',
        'balance': 'balance',
        'be_applied_amount': 'beAppliedAmount',
        'cancelled_by_id': 'cancelledById',
        'cancelled_on': 'cancelledOn',
        'comment': 'comment',
        'created_by_id': 'createdById',
        'created_date': 'createdDate',
        'debit_memo_date': 'debitMemoDate',
        'due_date': 'dueDate',
        'id': 'id',
        'latest_pdf_file_id': 'latestPDFFileId',
        'number': 'number',
        'posted_by_id': 'postedById',
        'posted_on': 'postedOn',
        'reason_code': 'reasonCode',
        'referred_invoice_id': 'referredInvoiceId',
        'status': 'status',
        'target_date': 'targetDate',
        'tax_amount': 'taxAmount',
        'total_tax_exempt_amount': 'totalTaxExemptAmount',
        'transferred_to_accounting': 'transferredToAccounting',
        'updated_by_id': 'updatedById',
        'updated_date': 'updatedDate'
    }

    def __init__(self, integration_id__ns=None, integration_status__ns=None, sync_date__ns=None, account_id=None, amount=None, auto_pay=None, balance=None, be_applied_amount=None, cancelled_by_id=None, cancelled_on=None, comment=None, created_by_id=None, created_date=None, debit_memo_date=None, due_date=None, id=None, latest_pdf_file_id=None, number=None, posted_by_id=None, posted_on=None, reason_code=None, referred_invoice_id=None, status=None, target_date=None, tax_amount=None, total_tax_exempt_amount=None, transferred_to_accounting=None, updated_by_id=None, updated_date=None):  # noqa: E501
        """GETDebitMemoTypewithSuccess - a model defined in Swagger"""  # noqa: E501

        self._integration_id__ns = None
        self._integration_status__ns = None
        self._sync_date__ns = None
        self._account_id = None
        self._amount = None
        self._auto_pay = None
        self._balance = None
        self._be_applied_amount = None
        self._cancelled_by_id = None
        self._cancelled_on = None
        self._comment = None
        self._created_by_id = None
        self._created_date = None
        self._debit_memo_date = None
        self._due_date = None
        self._id = None
        self._latest_pdf_file_id = None
        self._number = None
        self._posted_by_id = None
        self._posted_on = None
        self._reason_code = None
        self._referred_invoice_id = None
        self._status = None
        self._target_date = None
        self._tax_amount = None
        self._total_tax_exempt_amount = None
        self._transferred_to_accounting = None
        self._updated_by_id = None
        self._updated_date = None
        self.discriminator = None

        if integration_id__ns is not None:
            self.integration_id__ns = integration_id__ns
        if integration_status__ns is not None:
            self.integration_status__ns = integration_status__ns
        if sync_date__ns is not None:
            self.sync_date__ns = sync_date__ns
        if account_id is not None:
            self.account_id = account_id
        if amount is not None:
            self.amount = amount
        if auto_pay is not None:
            self.auto_pay = auto_pay
        if balance is not None:
            self.balance = balance
        if be_applied_amount is not None:
            self.be_applied_amount = be_applied_amount
        if cancelled_by_id is not None:
            self.cancelled_by_id = cancelled_by_id
        if cancelled_on is not None:
            self.cancelled_on = cancelled_on
        if comment is not None:
            self.comment = comment
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_date is not None:
            self.created_date = created_date
        if debit_memo_date is not None:
            self.debit_memo_date = debit_memo_date
        if due_date is not None:
            self.due_date = due_date
        if id is not None:
            self.id = id
        if latest_pdf_file_id is not None:
            self.latest_pdf_file_id = latest_pdf_file_id
        if number is not None:
            self.number = number
        if posted_by_id is not None:
            self.posted_by_id = posted_by_id
        if posted_on is not None:
            self.posted_on = posted_on
        if reason_code is not None:
            self.reason_code = reason_code
        if referred_invoice_id is not None:
            self.referred_invoice_id = referred_invoice_id
        if status is not None:
            self.status = status
        if target_date is not None:
            self.target_date = target_date
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if total_tax_exempt_amount is not None:
            self.total_tax_exempt_amount = total_tax_exempt_amount
        if transferred_to_accounting is not None:
            self.transferred_to_accounting = transferred_to_accounting
        if updated_by_id is not None:
            self.updated_by_id = updated_by_id
        if updated_date is not None:
            self.updated_date = updated_date

    @property
    def integration_id__ns(self):
        """Gets the integration_id__ns of this GETDebitMemoTypewithSuccess.  # noqa: E501

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_id__ns of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._integration_id__ns

    @integration_id__ns.setter
    def integration_id__ns(self, integration_id__ns):
        """Sets the integration_id__ns of this GETDebitMemoTypewithSuccess.

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_id__ns: The integration_id__ns of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :type: str
        """
        if integration_id__ns is not None and len(integration_id__ns) > 255:
            raise ValueError("Invalid value for `integration_id__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_id__ns = integration_id__ns

    @property
    def integration_status__ns(self):
        """Gets the integration_status__ns of this GETDebitMemoTypewithSuccess.  # noqa: E501

        Status of the debit memo's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_status__ns of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._integration_status__ns

    @integration_status__ns.setter
    def integration_status__ns(self, integration_status__ns):
        """Sets the integration_status__ns of this GETDebitMemoTypewithSuccess.

        Status of the debit memo's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_status__ns: The integration_status__ns of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :type: str
        """
        if integration_status__ns is not None and len(integration_status__ns) > 255:
            raise ValueError("Invalid value for `integration_status__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_status__ns = integration_status__ns

    @property
    def sync_date__ns(self):
        """Gets the sync_date__ns of this GETDebitMemoTypewithSuccess.  # noqa: E501

        Date when the debit memo was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The sync_date__ns of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._sync_date__ns

    @sync_date__ns.setter
    def sync_date__ns(self, sync_date__ns):
        """Sets the sync_date__ns of this GETDebitMemoTypewithSuccess.

        Date when the debit memo was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param sync_date__ns: The sync_date__ns of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :type: str
        """
        if sync_date__ns is not None and len(sync_date__ns) > 255:
            raise ValueError("Invalid value for `sync_date__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._sync_date__ns = sync_date__ns

    @property
    def account_id(self):
        """Gets the account_id of this GETDebitMemoTypewithSuccess.  # noqa: E501

        The ID of the customer account associated with the debit memo.   # noqa: E501

        :return: The account_id of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this GETDebitMemoTypewithSuccess.

        The ID of the customer account associated with the debit memo.   # noqa: E501

        :param account_id: The account_id of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def amount(self):
        """Gets the amount of this GETDebitMemoTypewithSuccess.  # noqa: E501

        The total amount of the debit memo.   # noqa: E501

        :return: The amount of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GETDebitMemoTypewithSuccess.

        The total amount of the debit memo.   # noqa: E501

        :param amount: The amount of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def auto_pay(self):
        """Gets the auto_pay of this GETDebitMemoTypewithSuccess.  # noqa: E501

        Whether debit memos are automatically picked up for processing in the corresponding payment run.   By default, debit memos are automatically picked up for processing in the corresponding payment run.         # noqa: E501

        :return: The auto_pay of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :rtype: bool
        """
        return self._auto_pay

    @auto_pay.setter
    def auto_pay(self, auto_pay):
        """Sets the auto_pay of this GETDebitMemoTypewithSuccess.

        Whether debit memos are automatically picked up for processing in the corresponding payment run.   By default, debit memos are automatically picked up for processing in the corresponding payment run.         # noqa: E501

        :param auto_pay: The auto_pay of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :type: bool
        """

        self._auto_pay = auto_pay

    @property
    def balance(self):
        """Gets the balance of this GETDebitMemoTypewithSuccess.  # noqa: E501

        The balance of the debit memo.   # noqa: E501

        :return: The balance of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this GETDebitMemoTypewithSuccess.

        The balance of the debit memo.   # noqa: E501

        :param balance: The balance of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :type: float
        """

        self._balance = balance

    @property
    def be_applied_amount(self):
        """Gets the be_applied_amount of this GETDebitMemoTypewithSuccess.  # noqa: E501

        The applied amount of the debit memo.   # noqa: E501

        :return: The be_applied_amount of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :rtype: float
        """
        return self._be_applied_amount

    @be_applied_amount.setter
    def be_applied_amount(self, be_applied_amount):
        """Sets the be_applied_amount of this GETDebitMemoTypewithSuccess.

        The applied amount of the debit memo.   # noqa: E501

        :param be_applied_amount: The be_applied_amount of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :type: float
        """

        self._be_applied_amount = be_applied_amount

    @property
    def cancelled_by_id(self):
        """Gets the cancelled_by_id of this GETDebitMemoTypewithSuccess.  # noqa: E501

        The ID of the Zuora user who cancelled the debit memo.   # noqa: E501

        :return: The cancelled_by_id of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._cancelled_by_id

    @cancelled_by_id.setter
    def cancelled_by_id(self, cancelled_by_id):
        """Sets the cancelled_by_id of this GETDebitMemoTypewithSuccess.

        The ID of the Zuora user who cancelled the debit memo.   # noqa: E501

        :param cancelled_by_id: The cancelled_by_id of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._cancelled_by_id = cancelled_by_id

    @property
    def cancelled_on(self):
        """Gets the cancelled_on of this GETDebitMemoTypewithSuccess.  # noqa: E501

        The date and time when the debit memo was cancelled, in `yyyy-mm-dd hh:mm:ss` format.   # noqa: E501

        :return: The cancelled_on of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :rtype: datetime
        """
        return self._cancelled_on

    @cancelled_on.setter
    def cancelled_on(self, cancelled_on):
        """Sets the cancelled_on of this GETDebitMemoTypewithSuccess.

        The date and time when the debit memo was cancelled, in `yyyy-mm-dd hh:mm:ss` format.   # noqa: E501

        :param cancelled_on: The cancelled_on of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :type: datetime
        """

        self._cancelled_on = cancelled_on

    @property
    def comment(self):
        """Gets the comment of this GETDebitMemoTypewithSuccess.  # noqa: E501

        Comments about the debit memo.   # noqa: E501

        :return: The comment of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this GETDebitMemoTypewithSuccess.

        Comments about the debit memo.   # noqa: E501

        :param comment: The comment of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def created_by_id(self):
        """Gets the created_by_id of this GETDebitMemoTypewithSuccess.  # noqa: E501

        The ID of the Zuora user who created the debit memo.   # noqa: E501

        :return: The created_by_id of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this GETDebitMemoTypewithSuccess.

        The ID of the Zuora user who created the debit memo.   # noqa: E501

        :param created_by_id: The created_by_id of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def created_date(self):
        """Gets the created_date of this GETDebitMemoTypewithSuccess.  # noqa: E501

        The date and time when the debit memo was created, in `yyyy-mm-dd hh:mm:ss` format. For example, 2017-03-01 15:31:10.   # noqa: E501

        :return: The created_date of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this GETDebitMemoTypewithSuccess.

        The date and time when the debit memo was created, in `yyyy-mm-dd hh:mm:ss` format. For example, 2017-03-01 15:31:10.   # noqa: E501

        :param created_date: The created_date of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def debit_memo_date(self):
        """Gets the debit_memo_date of this GETDebitMemoTypewithSuccess.  # noqa: E501

        The date when the debit memo takes effect, in `yyyy-mm-dd` format. For example, 2017-05-20.   # noqa: E501

        :return: The debit_memo_date of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :rtype: date
        """
        return self._debit_memo_date

    @debit_memo_date.setter
    def debit_memo_date(self, debit_memo_date):
        """Sets the debit_memo_date of this GETDebitMemoTypewithSuccess.

        The date when the debit memo takes effect, in `yyyy-mm-dd` format. For example, 2017-05-20.   # noqa: E501

        :param debit_memo_date: The debit_memo_date of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :type: date
        """

        self._debit_memo_date = debit_memo_date

    @property
    def due_date(self):
        """Gets the due_date of this GETDebitMemoTypewithSuccess.  # noqa: E501

        The date by which the payment for the debit memo is due, in `yyyy-mm-dd` format.   # noqa: E501

        :return: The due_date of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this GETDebitMemoTypewithSuccess.

        The date by which the payment for the debit memo is due, in `yyyy-mm-dd` format.   # noqa: E501

        :param due_date: The due_date of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :type: date
        """

        self._due_date = due_date

    @property
    def id(self):
        """Gets the id of this GETDebitMemoTypewithSuccess.  # noqa: E501

        The unique ID of the debit memo.   # noqa: E501

        :return: The id of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GETDebitMemoTypewithSuccess.

        The unique ID of the debit memo.   # noqa: E501

        :param id: The id of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def latest_pdf_file_id(self):
        """Gets the latest_pdf_file_id of this GETDebitMemoTypewithSuccess.  # noqa: E501

        The ID of the latest PDF file generated for the debit memo.   # noqa: E501

        :return: The latest_pdf_file_id of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._latest_pdf_file_id

    @latest_pdf_file_id.setter
    def latest_pdf_file_id(self, latest_pdf_file_id):
        """Sets the latest_pdf_file_id of this GETDebitMemoTypewithSuccess.

        The ID of the latest PDF file generated for the debit memo.   # noqa: E501

        :param latest_pdf_file_id: The latest_pdf_file_id of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._latest_pdf_file_id = latest_pdf_file_id

    @property
    def number(self):
        """Gets the number of this GETDebitMemoTypewithSuccess.  # noqa: E501

        The unique identification number of the debit memo.   # noqa: E501

        :return: The number of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this GETDebitMemoTypewithSuccess.

        The unique identification number of the debit memo.   # noqa: E501

        :param number: The number of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def posted_by_id(self):
        """Gets the posted_by_id of this GETDebitMemoTypewithSuccess.  # noqa: E501

        The ID of the Zuora user who posted the debit memo.   # noqa: E501

        :return: The posted_by_id of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._posted_by_id

    @posted_by_id.setter
    def posted_by_id(self, posted_by_id):
        """Sets the posted_by_id of this GETDebitMemoTypewithSuccess.

        The ID of the Zuora user who posted the debit memo.   # noqa: E501

        :param posted_by_id: The posted_by_id of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._posted_by_id = posted_by_id

    @property
    def posted_on(self):
        """Gets the posted_on of this GETDebitMemoTypewithSuccess.  # noqa: E501

        The date and time when the debit memo was posted, in `yyyy-mm-dd hh:mm:ss` format.   # noqa: E501

        :return: The posted_on of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :rtype: datetime
        """
        return self._posted_on

    @posted_on.setter
    def posted_on(self, posted_on):
        """Sets the posted_on of this GETDebitMemoTypewithSuccess.

        The date and time when the debit memo was posted, in `yyyy-mm-dd hh:mm:ss` format.   # noqa: E501

        :param posted_on: The posted_on of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :type: datetime
        """

        self._posted_on = posted_on

    @property
    def reason_code(self):
        """Gets the reason_code of this GETDebitMemoTypewithSuccess.  # noqa: E501

        A code identifying the reason for the transaction. The value must be an existing reason code or empty.   # noqa: E501

        :return: The reason_code of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._reason_code

    @reason_code.setter
    def reason_code(self, reason_code):
        """Sets the reason_code of this GETDebitMemoTypewithSuccess.

        A code identifying the reason for the transaction. The value must be an existing reason code or empty.   # noqa: E501

        :param reason_code: The reason_code of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._reason_code = reason_code

    @property
    def referred_invoice_id(self):
        """Gets the referred_invoice_id of this GETDebitMemoTypewithSuccess.  # noqa: E501

        The ID of a referred invoice.   # noqa: E501

        :return: The referred_invoice_id of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._referred_invoice_id

    @referred_invoice_id.setter
    def referred_invoice_id(self, referred_invoice_id):
        """Sets the referred_invoice_id of this GETDebitMemoTypewithSuccess.

        The ID of a referred invoice.   # noqa: E501

        :param referred_invoice_id: The referred_invoice_id of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._referred_invoice_id = referred_invoice_id

    @property
    def status(self):
        """Gets the status of this GETDebitMemoTypewithSuccess.  # noqa: E501

        The status of the debit memo.    # noqa: E501

        :return: The status of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GETDebitMemoTypewithSuccess.

        The status of the debit memo.    # noqa: E501

        :param status: The status of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :type: str
        """
        allowed_values = ["Draft", "Posted", "Canceled", "Error", "PendingForTax", "Generating", "CancelInProgress"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def target_date(self):
        """Gets the target_date of this GETDebitMemoTypewithSuccess.  # noqa: E501

        The target date for the debit memo, in `yyyy-mm-dd` format. For example, 2017-07-20.   # noqa: E501

        :return: The target_date of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :rtype: date
        """
        return self._target_date

    @target_date.setter
    def target_date(self, target_date):
        """Sets the target_date of this GETDebitMemoTypewithSuccess.

        The target date for the debit memo, in `yyyy-mm-dd` format. For example, 2017-07-20.   # noqa: E501

        :param target_date: The target_date of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :type: date
        """

        self._target_date = target_date

    @property
    def tax_amount(self):
        """Gets the tax_amount of this GETDebitMemoTypewithSuccess.  # noqa: E501

        The amount of taxation.   # noqa: E501

        :return: The tax_amount of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this GETDebitMemoTypewithSuccess.

        The amount of taxation.   # noqa: E501

        :param tax_amount: The tax_amount of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :type: float
        """

        self._tax_amount = tax_amount

    @property
    def total_tax_exempt_amount(self):
        """Gets the total_tax_exempt_amount of this GETDebitMemoTypewithSuccess.  # noqa: E501

        The total amount of taxes or VAT for which the customer has an exemption.   # noqa: E501

        :return: The total_tax_exempt_amount of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :rtype: float
        """
        return self._total_tax_exempt_amount

    @total_tax_exempt_amount.setter
    def total_tax_exempt_amount(self, total_tax_exempt_amount):
        """Sets the total_tax_exempt_amount of this GETDebitMemoTypewithSuccess.

        The total amount of taxes or VAT for which the customer has an exemption.   # noqa: E501

        :param total_tax_exempt_amount: The total_tax_exempt_amount of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :type: float
        """

        self._total_tax_exempt_amount = total_tax_exempt_amount

    @property
    def transferred_to_accounting(self):
        """Gets the transferred_to_accounting of this GETDebitMemoTypewithSuccess.  # noqa: E501

        Whether the debit memo was transferred to an external accounting system. Use this field for integration with accounting systems, such as NetSuite.    # noqa: E501

        :return: The transferred_to_accounting of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._transferred_to_accounting

    @transferred_to_accounting.setter
    def transferred_to_accounting(self, transferred_to_accounting):
        """Sets the transferred_to_accounting of this GETDebitMemoTypewithSuccess.

        Whether the debit memo was transferred to an external accounting system. Use this field for integration with accounting systems, such as NetSuite.    # noqa: E501

        :param transferred_to_accounting: The transferred_to_accounting of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :type: str
        """
        allowed_values = ["Processing", "Yes", "No", "Error", "Ignore"]  # noqa: E501
        if transferred_to_accounting not in allowed_values:
            raise ValueError(
                "Invalid value for `transferred_to_accounting` ({0}), must be one of {1}"  # noqa: E501
                .format(transferred_to_accounting, allowed_values)
            )

        self._transferred_to_accounting = transferred_to_accounting

    @property
    def updated_by_id(self):
        """Gets the updated_by_id of this GETDebitMemoTypewithSuccess.  # noqa: E501

        The ID of the Zuora user who last updated the debit memo.   # noqa: E501

        :return: The updated_by_id of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """Sets the updated_by_id of this GETDebitMemoTypewithSuccess.

        The ID of the Zuora user who last updated the debit memo.   # noqa: E501

        :param updated_by_id: The updated_by_id of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :type: str
        """

        self._updated_by_id = updated_by_id

    @property
    def updated_date(self):
        """Gets the updated_date of this GETDebitMemoTypewithSuccess.  # noqa: E501

        The date and time when the debit memo was last updated, in `yyyy-mm-dd hh:mm:ss` format. For example, 2017-03-02 15:31:10.   # noqa: E501

        :return: The updated_date of this GETDebitMemoTypewithSuccess.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this GETDebitMemoTypewithSuccess.

        The date and time when the debit memo was last updated, in `yyyy-mm-dd hh:mm:ss` format. For example, 2017-03-02 15:31:10.   # noqa: E501

        :param updated_date: The updated_date of this GETDebitMemoTypewithSuccess.  # noqa: E501
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
        if issubclass(GETDebitMemoTypewithSuccess, dict):
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
        if not isinstance(other, GETDebitMemoTypewithSuccess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
