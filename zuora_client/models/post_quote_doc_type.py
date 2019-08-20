# coding: utf-8




import pprint
import re  # noqa: F401

import six


class POSTQuoteDocType(object):
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
        'apiuser': 'str',
        'document_type': 'str',
        'locale': 'str',
        'password': 'str',
        'quote_id': 'str',
        'sandbox': 'str',
        'server_url': 'str',
        'session_id': 'str',
        'template_id': 'str',
        'token': 'str',
        'use_sfdc_locale': 'str',
        'username': 'str',
        'zquotes_major_version': 'str',
        'zquotes_minor_version': 'str'
    }

    attribute_map = {
        'apiuser': 'apiuser',
        'document_type': 'documentType',
        'locale': 'locale',
        'password': 'password',
        'quote_id': 'quoteId',
        'sandbox': 'sandbox',
        'server_url': 'serverUrl',
        'session_id': 'sessionId',
        'template_id': 'templateId',
        'token': 'token',
        'use_sfdc_locale': 'useSFDCLocale',
        'username': 'username',
        'zquotes_major_version': 'zquotesMajorVersion',
        'zquotes_minor_version': 'zquotesMinorVersion'
    }

    def __init__(self, apiuser=None, document_type=None, locale=None, password=None, quote_id=None, sandbox=None, server_url=None, session_id=None, template_id=None, token=None, use_sfdc_locale=None, username=None, zquotes_major_version=None, zquotes_minor_version=None):  # noqa: E501
        """POSTQuoteDocType - a model defined in Swagger"""  # noqa: E501

        self._apiuser = None
        self._document_type = None
        self._locale = None
        self._password = None
        self._quote_id = None
        self._sandbox = None
        self._server_url = None
        self._session_id = None
        self._template_id = None
        self._token = None
        self._use_sfdc_locale = None
        self._username = None
        self._zquotes_major_version = None
        self._zquotes_minor_version = None
        self.discriminator = None

        if apiuser is not None:
            self.apiuser = apiuser
        self.document_type = document_type
        if locale is not None:
            self.locale = locale
        if password is not None:
            self.password = password
        self.quote_id = quote_id
        if sandbox is not None:
            self.sandbox = sandbox
        self.server_url = server_url
        self.session_id = session_id
        self.template_id = template_id
        if token is not None:
            self.token = token
        if use_sfdc_locale is not None:
            self.use_sfdc_locale = use_sfdc_locale
        if username is not None:
            self.username = username
        if zquotes_major_version is not None:
            self.zquotes_major_version = zquotes_major_version
        if zquotes_minor_version is not None:
            self.zquotes_minor_version = zquotes_minor_version

    @property
    def apiuser(self):
        """Gets the apiuser of this POSTQuoteDocType.  # noqa: E501

        If not using Salesforce locale, this API Zuora user will be used to retrieve the locale from Zuora.   # noqa: E501

        :return: The apiuser of this POSTQuoteDocType.  # noqa: E501
        :rtype: str
        """
        return self._apiuser

    @apiuser.setter
    def apiuser(self, apiuser):
        """Sets the apiuser of this POSTQuoteDocType.

        If not using Salesforce locale, this API Zuora user will be used to retrieve the locale from Zuora.   # noqa: E501

        :param apiuser: The apiuser of this POSTQuoteDocType.  # noqa: E501
        :type: str
        """

        self._apiuser = apiuser

    @property
    def document_type(self):
        """Gets the document_type of this POSTQuoteDocType.  # noqa: E501

        Type of the document to generate: `PDF` or `DOC`.   # noqa: E501

        :return: The document_type of this POSTQuoteDocType.  # noqa: E501
        :rtype: str
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """Sets the document_type of this POSTQuoteDocType.

        Type of the document to generate: `PDF` or `DOC`.   # noqa: E501

        :param document_type: The document_type of this POSTQuoteDocType.  # noqa: E501
        :type: str
        """
        if document_type is None:
            raise ValueError("Invalid value for `document_type`, must not be `None`")  # noqa: E501

        self._document_type = document_type

    @property
    def locale(self):
        """Gets the locale of this POSTQuoteDocType.  # noqa: E501

        Salesforce locale value to use.   # noqa: E501

        :return: The locale of this POSTQuoteDocType.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this POSTQuoteDocType.

        Salesforce locale value to use.   # noqa: E501

        :param locale: The locale of this POSTQuoteDocType.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def password(self):
        """Gets the password of this POSTQuoteDocType.  # noqa: E501

          # noqa: E501

        :return: The password of this POSTQuoteDocType.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this POSTQuoteDocType.

          # noqa: E501

        :param password: The password of this POSTQuoteDocType.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def quote_id(self):
        """Gets the quote_id of this POSTQuoteDocType.  # noqa: E501

        ｜ Id of the quote。  # noqa: E501

        :return: The quote_id of this POSTQuoteDocType.  # noqa: E501
        :rtype: str
        """
        return self._quote_id

    @quote_id.setter
    def quote_id(self, quote_id):
        """Sets the quote_id of this POSTQuoteDocType.

        ｜ Id of the quote。  # noqa: E501

        :param quote_id: The quote_id of this POSTQuoteDocType.  # noqa: E501
        :type: str
        """
        if quote_id is None:
            raise ValueError("Invalid value for `quote_id`, must not be `None`")  # noqa: E501

        self._quote_id = quote_id

    @property
    def sandbox(self):
        """Gets the sandbox of this POSTQuoteDocType.  # noqa: E501

          # noqa: E501

        :return: The sandbox of this POSTQuoteDocType.  # noqa: E501
        :rtype: str
        """
        return self._sandbox

    @sandbox.setter
    def sandbox(self, sandbox):
        """Sets the sandbox of this POSTQuoteDocType.

          # noqa: E501

        :param sandbox: The sandbox of this POSTQuoteDocType.  # noqa: E501
        :type: str
        """

        self._sandbox = sandbox

    @property
    def server_url(self):
        """Gets the server_url of this POSTQuoteDocType.  # noqa: E501

        SOAP URL used to login to Salesforce to get data. You can get the value with the following code in a Visualforce page: `{!$Api.Partner_Server_URL_100}`   # noqa: E501

        :return: The server_url of this POSTQuoteDocType.  # noqa: E501
        :rtype: str
        """
        return self._server_url

    @server_url.setter
    def server_url(self, server_url):
        """Sets the server_url of this POSTQuoteDocType.

        SOAP URL used to login to Salesforce to get data. You can get the value with the following code in a Visualforce page: `{!$Api.Partner_Server_URL_100}`   # noqa: E501

        :param server_url: The server_url of this POSTQuoteDocType.  # noqa: E501
        :type: str
        """
        if server_url is None:
            raise ValueError("Invalid value for `server_url`, must not be `None`")  # noqa: E501

        self._server_url = server_url

    @property
    def session_id(self):
        """Gets the session_id of this POSTQuoteDocType.  # noqa: E501

        Salesforce session id used to log in to Salesforce to get data. You can get the value with the following code in a Visualforce page: *{!$Api.Session_ID}*   # noqa: E501

        :return: The session_id of this POSTQuoteDocType.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this POSTQuoteDocType.

        Salesforce session id used to log in to Salesforce to get data. You can get the value with the following code in a Visualforce page: *{!$Api.Session_ID}*   # noqa: E501

        :param session_id: The session_id of this POSTQuoteDocType.  # noqa: E501
        :type: str
        """
        if session_id is None:
            raise ValueError("Invalid value for `session_id`, must not be `None`")  # noqa: E501

        self._session_id = session_id

    @property
    def template_id(self):
        """Gets the template_id of this POSTQuoteDocType.  # noqa: E501

        Id of the quote template in Zuora.   # noqa: E501

        :return: The template_id of this POSTQuoteDocType.  # noqa: E501
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this POSTQuoteDocType.

        Id of the quote template in Zuora.   # noqa: E501

        :param template_id: The template_id of this POSTQuoteDocType.  # noqa: E501
        :type: str
        """
        if template_id is None:
            raise ValueError("Invalid value for `template_id`, must not be `None`")  # noqa: E501

        self._template_id = template_id

    @property
    def token(self):
        """Gets the token of this POSTQuoteDocType.  # noqa: E501

          # noqa: E501

        :return: The token of this POSTQuoteDocType.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this POSTQuoteDocType.

          # noqa: E501

        :param token: The token of this POSTQuoteDocType.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def use_sfdc_locale(self):
        """Gets the use_sfdc_locale of this POSTQuoteDocType.  # noqa: E501

        If using Salesforce org locale, set this to a value that is not null.   # noqa: E501

        :return: The use_sfdc_locale of this POSTQuoteDocType.  # noqa: E501
        :rtype: str
        """
        return self._use_sfdc_locale

    @use_sfdc_locale.setter
    def use_sfdc_locale(self, use_sfdc_locale):
        """Sets the use_sfdc_locale of this POSTQuoteDocType.

        If using Salesforce org locale, set this to a value that is not null.   # noqa: E501

        :param use_sfdc_locale: The use_sfdc_locale of this POSTQuoteDocType.  # noqa: E501
        :type: str
        """

        self._use_sfdc_locale = use_sfdc_locale

    @property
    def username(self):
        """Gets the username of this POSTQuoteDocType.  # noqa: E501

          # noqa: E501

        :return: The username of this POSTQuoteDocType.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this POSTQuoteDocType.

          # noqa: E501

        :param username: The username of this POSTQuoteDocType.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def zquotes_major_version(self):
        """Gets the zquotes_major_version of this POSTQuoteDocType.  # noqa: E501

        The major version number of Zuora Quotes you are generating the quote document in. You can use a quote template with hierarchy sizes bigger than 3 if this is set to 7 or higher.   # noqa: E501

        :return: The zquotes_major_version of this POSTQuoteDocType.  # noqa: E501
        :rtype: str
        """
        return self._zquotes_major_version

    @zquotes_major_version.setter
    def zquotes_major_version(self, zquotes_major_version):
        """Sets the zquotes_major_version of this POSTQuoteDocType.

        The major version number of Zuora Quotes you are generating the quote document in. You can use a quote template with hierarchy sizes bigger than 3 if this is set to 7 or higher.   # noqa: E501

        :param zquotes_major_version: The zquotes_major_version of this POSTQuoteDocType.  # noqa: E501
        :type: str
        """

        self._zquotes_major_version = zquotes_major_version

    @property
    def zquotes_minor_version(self):
        """Gets the zquotes_minor_version of this POSTQuoteDocType.  # noqa: E501

        The minor version number of Zuora Quotes you are generating the quote document in.   # noqa: E501

        :return: The zquotes_minor_version of this POSTQuoteDocType.  # noqa: E501
        :rtype: str
        """
        return self._zquotes_minor_version

    @zquotes_minor_version.setter
    def zquotes_minor_version(self, zquotes_minor_version):
        """Sets the zquotes_minor_version of this POSTQuoteDocType.

        The minor version number of Zuora Quotes you are generating the quote document in.   # noqa: E501

        :param zquotes_minor_version: The zquotes_minor_version of this POSTQuoteDocType.  # noqa: E501
        :type: str
        """

        self._zquotes_minor_version = zquotes_minor_version

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
        if issubclass(POSTQuoteDocType, dict):
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
        if not isinstance(other, POSTQuoteDocType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
