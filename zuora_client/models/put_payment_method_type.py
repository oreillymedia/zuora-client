# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.payment_method_object_custom_fields import PaymentMethodObjectCustomFields  # noqa: F401,E501


class PUTPaymentMethodType(object):
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
        'address_line1': 'str',
        'address_line2': 'str',
        'card_holder_name': 'str',
        'city': 'str',
        'country': 'str',
        'default_payment_method': 'bool',
        'email': 'str',
        'expiration_month': 'str',
        'expiration_year': 'str',
        'num_consecutive_failures': 'int',
        'phone': 'str',
        'security_code': 'str',
        'state': 'str',
        'zip_code': 'str'
    }

    attribute_map = {
        'address_line1': 'addressLine1',
        'address_line2': 'addressLine2',
        'card_holder_name': 'cardHolderName',
        'city': 'city',
        'country': 'country',
        'default_payment_method': 'defaultPaymentMethod',
        'email': 'email',
        'expiration_month': 'expirationMonth',
        'expiration_year': 'expirationYear',
        'num_consecutive_failures': 'numConsecutiveFailures',
        'phone': 'phone',
        'security_code': 'securityCode',
        'state': 'state',
        'zip_code': 'zipCode'
    }

    def __init__(self, address_line1=None, address_line2=None, card_holder_name=None, city=None, country=None, default_payment_method=None, email=None, expiration_month=None, expiration_year=None, num_consecutive_failures=None, phone=None, security_code=None, state=None, zip_code=None):  # noqa: E501
        """PUTPaymentMethodType - a model defined in Swagger"""  # noqa: E501

        self._address_line1 = None
        self._address_line2 = None
        self._card_holder_name = None
        self._city = None
        self._country = None
        self._default_payment_method = None
        self._email = None
        self._expiration_month = None
        self._expiration_year = None
        self._num_consecutive_failures = None
        self._phone = None
        self._security_code = None
        self._state = None
        self._zip_code = None
        self.discriminator = None

        if address_line1 is not None:
            self.address_line1 = address_line1
        if address_line2 is not None:
            self.address_line2 = address_line2
        if card_holder_name is not None:
            self.card_holder_name = card_holder_name
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if default_payment_method is not None:
            self.default_payment_method = default_payment_method
        if email is not None:
            self.email = email
        if expiration_month is not None:
            self.expiration_month = expiration_month
        if expiration_year is not None:
            self.expiration_year = expiration_year
        if num_consecutive_failures is not None:
            self.num_consecutive_failures = num_consecutive_failures
        if phone is not None:
            self.phone = phone
        if security_code is not None:
            self.security_code = security_code
        if state is not None:
            self.state = state
        if zip_code is not None:
            self.zip_code = zip_code

    @property
    def address_line1(self):
        """Gets the address_line1 of this PUTPaymentMethodType.  # noqa: E501

        First address line, 255 characters or less.   # noqa: E501

        :return: The address_line1 of this PUTPaymentMethodType.  # noqa: E501
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """Sets the address_line1 of this PUTPaymentMethodType.

        First address line, 255 characters or less.   # noqa: E501

        :param address_line1: The address_line1 of this PUTPaymentMethodType.  # noqa: E501
        :type: str
        """

        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """Gets the address_line2 of this PUTPaymentMethodType.  # noqa: E501

        Second address line, 255 characters or less.   # noqa: E501

        :return: The address_line2 of this PUTPaymentMethodType.  # noqa: E501
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """Sets the address_line2 of this PUTPaymentMethodType.

        Second address line, 255 characters or less.   # noqa: E501

        :param address_line2: The address_line2 of this PUTPaymentMethodType.  # noqa: E501
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def card_holder_name(self):
        """Gets the card_holder_name of this PUTPaymentMethodType.  # noqa: E501

        The full name as it appears on the card, e.g., \"John J Smith\", 50 characters or less.   # noqa: E501

        :return: The card_holder_name of this PUTPaymentMethodType.  # noqa: E501
        :rtype: str
        """
        return self._card_holder_name

    @card_holder_name.setter
    def card_holder_name(self, card_holder_name):
        """Sets the card_holder_name of this PUTPaymentMethodType.

        The full name as it appears on the card, e.g., \"John J Smith\", 50 characters or less.   # noqa: E501

        :param card_holder_name: The card_holder_name of this PUTPaymentMethodType.  # noqa: E501
        :type: str
        """

        self._card_holder_name = card_holder_name

    @property
    def city(self):
        """Gets the city of this PUTPaymentMethodType.  # noqa: E501

        City, 40 characters or less.   # noqa: E501

        :return: The city of this PUTPaymentMethodType.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this PUTPaymentMethodType.

        City, 40 characters or less.   # noqa: E501

        :param city: The city of this PUTPaymentMethodType.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this PUTPaymentMethodType.  # noqa: E501

        Country; must be a valid country name or abbreviation.   # noqa: E501

        :return: The country of this PUTPaymentMethodType.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this PUTPaymentMethodType.

        Country; must be a valid country name or abbreviation.   # noqa: E501

        :param country: The country of this PUTPaymentMethodType.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def default_payment_method(self):
        """Gets the default_payment_method of this PUTPaymentMethodType.  # noqa: E501

        Specify \"true\" to make this card the default payment method; otherwise, omit this parameter to keep the current default payment method.   # noqa: E501

        :return: The default_payment_method of this PUTPaymentMethodType.  # noqa: E501
        :rtype: bool
        """
        return self._default_payment_method

    @default_payment_method.setter
    def default_payment_method(self, default_payment_method):
        """Sets the default_payment_method of this PUTPaymentMethodType.

        Specify \"true\" to make this card the default payment method; otherwise, omit this parameter to keep the current default payment method.   # noqa: E501

        :param default_payment_method: The default_payment_method of this PUTPaymentMethodType.  # noqa: E501
        :type: bool
        """

        self._default_payment_method = default_payment_method

    @property
    def email(self):
        """Gets the email of this PUTPaymentMethodType.  # noqa: E501

        Card holder's email address, 80 characters or less.   # noqa: E501

        :return: The email of this PUTPaymentMethodType.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PUTPaymentMethodType.

        Card holder's email address, 80 characters or less.   # noqa: E501

        :param email: The email of this PUTPaymentMethodType.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def expiration_month(self):
        """Gets the expiration_month of this PUTPaymentMethodType.  # noqa: E501

        One or two digit(s) expiration month (1-12).   # noqa: E501

        :return: The expiration_month of this PUTPaymentMethodType.  # noqa: E501
        :rtype: str
        """
        return self._expiration_month

    @expiration_month.setter
    def expiration_month(self, expiration_month):
        """Sets the expiration_month of this PUTPaymentMethodType.

        One or two digit(s) expiration month (1-12).   # noqa: E501

        :param expiration_month: The expiration_month of this PUTPaymentMethodType.  # noqa: E501
        :type: str
        """

        self._expiration_month = expiration_month

    @property
    def expiration_year(self):
        """Gets the expiration_year of this PUTPaymentMethodType.  # noqa: E501

        Four-digit expiration year.   # noqa: E501

        :return: The expiration_year of this PUTPaymentMethodType.  # noqa: E501
        :rtype: str
        """
        return self._expiration_year

    @expiration_year.setter
    def expiration_year(self, expiration_year):
        """Sets the expiration_year of this PUTPaymentMethodType.

        Four-digit expiration year.   # noqa: E501

        :param expiration_year: The expiration_year of this PUTPaymentMethodType.  # noqa: E501
        :type: str
        """

        self._expiration_year = expiration_year

    @property
    def num_consecutive_failures(self):
        """Gets the num_consecutive_failures of this PUTPaymentMethodType.  # noqa: E501

        The number of consecutive failed payments for this payment method. It is reset to `0` upon successful payment.    # noqa: E501

        :return: The num_consecutive_failures of this PUTPaymentMethodType.  # noqa: E501
        :rtype: int
        """
        return self._num_consecutive_failures

    @num_consecutive_failures.setter
    def num_consecutive_failures(self, num_consecutive_failures):
        """Sets the num_consecutive_failures of this PUTPaymentMethodType.

        The number of consecutive failed payments for this payment method. It is reset to `0` upon successful payment.    # noqa: E501

        :param num_consecutive_failures: The num_consecutive_failures of this PUTPaymentMethodType.  # noqa: E501
        :type: int
        """
        if num_consecutive_failures is not None and num_consecutive_failures > 100:  # noqa: E501
            raise ValueError("Invalid value for `num_consecutive_failures`, must be a value less than or equal to `100`")  # noqa: E501
        if num_consecutive_failures is not None and num_consecutive_failures < 0:  # noqa: E501
            raise ValueError("Invalid value for `num_consecutive_failures`, must be a value greater than or equal to `0`")  # noqa: E501

        self._num_consecutive_failures = num_consecutive_failures

    @property
    def phone(self):
        """Gets the phone of this PUTPaymentMethodType.  # noqa: E501

        Phone number, 40 characters or less.   # noqa: E501

        :return: The phone of this PUTPaymentMethodType.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this PUTPaymentMethodType.

        Phone number, 40 characters or less.   # noqa: E501

        :param phone: The phone of this PUTPaymentMethodType.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def security_code(self):
        """Gets the security_code of this PUTPaymentMethodType.  # noqa: E501

        The CVV or CVV2 security code for the credit card or debit card. Only required if changing expirationMonth, expirationYear, or cardHolderName. To ensure PCI compliance, this value isn't stored and can't be queried.    # noqa: E501

        :return: The security_code of this PUTPaymentMethodType.  # noqa: E501
        :rtype: str
        """
        return self._security_code

    @security_code.setter
    def security_code(self, security_code):
        """Sets the security_code of this PUTPaymentMethodType.

        The CVV or CVV2 security code for the credit card or debit card. Only required if changing expirationMonth, expirationYear, or cardHolderName. To ensure PCI compliance, this value isn't stored and can't be queried.    # noqa: E501

        :param security_code: The security_code of this PUTPaymentMethodType.  # noqa: E501
        :type: str
        """

        self._security_code = security_code

    @property
    def state(self):
        """Gets the state of this PUTPaymentMethodType.  # noqa: E501

        State; must be a valid state name or 2-character abbreviation.   # noqa: E501

        :return: The state of this PUTPaymentMethodType.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PUTPaymentMethodType.

        State; must be a valid state name or 2-character abbreviation.   # noqa: E501

        :param state: The state of this PUTPaymentMethodType.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def zip_code(self):
        """Gets the zip_code of this PUTPaymentMethodType.  # noqa: E501

        Zip code, 20 characters or less.   # noqa: E501

        :return: The zip_code of this PUTPaymentMethodType.  # noqa: E501
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this PUTPaymentMethodType.

        Zip code, 20 characters or less.   # noqa: E501

        :param zip_code: The zip_code of this PUTPaymentMethodType.  # noqa: E501
        :type: str
        """

        self._zip_code = zip_code

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
        if issubclass(PUTPaymentMethodType, dict):
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
        if not isinstance(other, PUTPaymentMethodType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
