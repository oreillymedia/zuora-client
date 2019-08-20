# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.contact_object_custom_fields import ContactObjectCustomFields  # noqa: F401,E501


class GETAccountTypeSoldToContact(object):
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
        'address1': 'str',
        'address2': 'str',
        'city': 'str',
        'country': 'str',
        'county': 'str',
        'fax': 'str',
        'first_name': 'str',
        'home_phone': 'str',
        'last_name': 'str',
        'mobile_phone': 'str',
        'nickname': 'str',
        'other_phone': 'str',
        'other_phone_type': 'str',
        'personal_email': 'str',
        'state': 'str',
        'tax_region': 'str',
        'work_email': 'str',
        'work_phone': 'str',
        'zip_code': 'str'
    }

    attribute_map = {
        'address1': 'address1',
        'address2': 'address2',
        'city': 'city',
        'country': 'country',
        'county': 'county',
        'fax': 'fax',
        'first_name': 'firstName',
        'home_phone': 'homePhone',
        'last_name': 'lastName',
        'mobile_phone': 'mobilePhone',
        'nickname': 'nickname',
        'other_phone': 'otherPhone',
        'other_phone_type': 'otherPhoneType',
        'personal_email': 'personalEmail',
        'state': 'state',
        'tax_region': 'taxRegion',
        'work_email': 'workEmail',
        'work_phone': 'workPhone',
        'zip_code': 'zipCode'
    }

    def __init__(self, address1=None, address2=None, city=None, country=None, county=None, fax=None, first_name=None, home_phone=None, last_name=None, mobile_phone=None, nickname=None, other_phone=None, other_phone_type=None, personal_email=None, state=None, tax_region=None, work_email=None, work_phone=None, zip_code=None):  # noqa: E501
        """GETAccountTypeSoldToContact - a model defined in Swagger"""  # noqa: E501

        self._address1 = None
        self._address2 = None
        self._city = None
        self._country = None
        self._county = None
        self._fax = None
        self._first_name = None
        self._home_phone = None
        self._last_name = None
        self._mobile_phone = None
        self._nickname = None
        self._other_phone = None
        self._other_phone_type = None
        self._personal_email = None
        self._state = None
        self._tax_region = None
        self._work_email = None
        self._work_phone = None
        self._zip_code = None
        self.discriminator = None

        if address1 is not None:
            self.address1 = address1
        if address2 is not None:
            self.address2 = address2
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if county is not None:
            self.county = county
        if fax is not None:
            self.fax = fax
        if first_name is not None:
            self.first_name = first_name
        if home_phone is not None:
            self.home_phone = home_phone
        if last_name is not None:
            self.last_name = last_name
        if mobile_phone is not None:
            self.mobile_phone = mobile_phone
        if nickname is not None:
            self.nickname = nickname
        if other_phone is not None:
            self.other_phone = other_phone
        if other_phone_type is not None:
            self.other_phone_type = other_phone_type
        if personal_email is not None:
            self.personal_email = personal_email
        if state is not None:
            self.state = state
        if tax_region is not None:
            self.tax_region = tax_region
        if work_email is not None:
            self.work_email = work_email
        if work_phone is not None:
            self.work_phone = work_phone
        if zip_code is not None:
            self.zip_code = zip_code

    @property
    def address1(self):
        """Gets the address1 of this GETAccountTypeSoldToContact.  # noqa: E501

        First address line, 255 characters or less.   # noqa: E501

        :return: The address1 of this GETAccountTypeSoldToContact.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this GETAccountTypeSoldToContact.

        First address line, 255 characters or less.   # noqa: E501

        :param address1: The address1 of this GETAccountTypeSoldToContact.  # noqa: E501
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this GETAccountTypeSoldToContact.  # noqa: E501

        Second address line, 255 characters or less.   # noqa: E501

        :return: The address2 of this GETAccountTypeSoldToContact.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this GETAccountTypeSoldToContact.

        Second address line, 255 characters or less.   # noqa: E501

        :param address2: The address2 of this GETAccountTypeSoldToContact.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def city(self):
        """Gets the city of this GETAccountTypeSoldToContact.  # noqa: E501

        City, 40 characters or less.   # noqa: E501

        :return: The city of this GETAccountTypeSoldToContact.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this GETAccountTypeSoldToContact.

        City, 40 characters or less.   # noqa: E501

        :param city: The city of this GETAccountTypeSoldToContact.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this GETAccountTypeSoldToContact.  # noqa: E501

        Full country name. This field does not contain the ISO-standard abbreviation of the country name.   # noqa: E501

        :return: The country of this GETAccountTypeSoldToContact.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this GETAccountTypeSoldToContact.

        Full country name. This field does not contain the ISO-standard abbreviation of the country name.   # noqa: E501

        :param country: The country of this GETAccountTypeSoldToContact.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def county(self):
        """Gets the county of this GETAccountTypeSoldToContact.  # noqa: E501

        County; 32 characters or less. Zuora tax uses this information to calculate county taxation.            # noqa: E501

        :return: The county of this GETAccountTypeSoldToContact.  # noqa: E501
        :rtype: str
        """
        return self._county

    @county.setter
    def county(self, county):
        """Sets the county of this GETAccountTypeSoldToContact.

        County; 32 characters or less. Zuora tax uses this information to calculate county taxation.            # noqa: E501

        :param county: The county of this GETAccountTypeSoldToContact.  # noqa: E501
        :type: str
        """

        self._county = county

    @property
    def fax(self):
        """Gets the fax of this GETAccountTypeSoldToContact.  # noqa: E501

        Fax phone number, 40 characters or less.   # noqa: E501

        :return: The fax of this GETAccountTypeSoldToContact.  # noqa: E501
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this GETAccountTypeSoldToContact.

        Fax phone number, 40 characters or less.   # noqa: E501

        :param fax: The fax of this GETAccountTypeSoldToContact.  # noqa: E501
        :type: str
        """

        self._fax = fax

    @property
    def first_name(self):
        """Gets the first_name of this GETAccountTypeSoldToContact.  # noqa: E501

        First name, 100 characters or less.   # noqa: E501

        :return: The first_name of this GETAccountTypeSoldToContact.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this GETAccountTypeSoldToContact.

        First name, 100 characters or less.   # noqa: E501

        :param first_name: The first_name of this GETAccountTypeSoldToContact.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def home_phone(self):
        """Gets the home_phone of this GETAccountTypeSoldToContact.  # noqa: E501

        Home phone number, 40 characters or less.   # noqa: E501

        :return: The home_phone of this GETAccountTypeSoldToContact.  # noqa: E501
        :rtype: str
        """
        return self._home_phone

    @home_phone.setter
    def home_phone(self, home_phone):
        """Sets the home_phone of this GETAccountTypeSoldToContact.

        Home phone number, 40 characters or less.   # noqa: E501

        :param home_phone: The home_phone of this GETAccountTypeSoldToContact.  # noqa: E501
        :type: str
        """

        self._home_phone = home_phone

    @property
    def last_name(self):
        """Gets the last_name of this GETAccountTypeSoldToContact.  # noqa: E501

        Last name, 100 characters or less.   # noqa: E501

        :return: The last_name of this GETAccountTypeSoldToContact.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this GETAccountTypeSoldToContact.

        Last name, 100 characters or less.   # noqa: E501

        :param last_name: The last_name of this GETAccountTypeSoldToContact.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def mobile_phone(self):
        """Gets the mobile_phone of this GETAccountTypeSoldToContact.  # noqa: E501

        Mobile phone number, 40 characters or less.   # noqa: E501

        :return: The mobile_phone of this GETAccountTypeSoldToContact.  # noqa: E501
        :rtype: str
        """
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        """Sets the mobile_phone of this GETAccountTypeSoldToContact.

        Mobile phone number, 40 characters or less.   # noqa: E501

        :param mobile_phone: The mobile_phone of this GETAccountTypeSoldToContact.  # noqa: E501
        :type: str
        """

        self._mobile_phone = mobile_phone

    @property
    def nickname(self):
        """Gets the nickname of this GETAccountTypeSoldToContact.  # noqa: E501

        Nickname for this contact.   # noqa: E501

        :return: The nickname of this GETAccountTypeSoldToContact.  # noqa: E501
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """Sets the nickname of this GETAccountTypeSoldToContact.

        Nickname for this contact.   # noqa: E501

        :param nickname: The nickname of this GETAccountTypeSoldToContact.  # noqa: E501
        :type: str
        """

        self._nickname = nickname

    @property
    def other_phone(self):
        """Gets the other_phone of this GETAccountTypeSoldToContact.  # noqa: E501

        Other phone number, 40 characters or less.   # noqa: E501

        :return: The other_phone of this GETAccountTypeSoldToContact.  # noqa: E501
        :rtype: str
        """
        return self._other_phone

    @other_phone.setter
    def other_phone(self, other_phone):
        """Sets the other_phone of this GETAccountTypeSoldToContact.

        Other phone number, 40 characters or less.   # noqa: E501

        :param other_phone: The other_phone of this GETAccountTypeSoldToContact.  # noqa: E501
        :type: str
        """

        self._other_phone = other_phone

    @property
    def other_phone_type(self):
        """Gets the other_phone_type of this GETAccountTypeSoldToContact.  # noqa: E501

        Possible values are: `Work`, `Mobile`, `Home`, `Other`.   # noqa: E501

        :return: The other_phone_type of this GETAccountTypeSoldToContact.  # noqa: E501
        :rtype: str
        """
        return self._other_phone_type

    @other_phone_type.setter
    def other_phone_type(self, other_phone_type):
        """Sets the other_phone_type of this GETAccountTypeSoldToContact.

        Possible values are: `Work`, `Mobile`, `Home`, `Other`.   # noqa: E501

        :param other_phone_type: The other_phone_type of this GETAccountTypeSoldToContact.  # noqa: E501
        :type: str
        """

        self._other_phone_type = other_phone_type

    @property
    def personal_email(self):
        """Gets the personal_email of this GETAccountTypeSoldToContact.  # noqa: E501

        Personal email address, 80 characters or less.   # noqa: E501

        :return: The personal_email of this GETAccountTypeSoldToContact.  # noqa: E501
        :rtype: str
        """
        return self._personal_email

    @personal_email.setter
    def personal_email(self, personal_email):
        """Sets the personal_email of this GETAccountTypeSoldToContact.

        Personal email address, 80 characters or less.   # noqa: E501

        :param personal_email: The personal_email of this GETAccountTypeSoldToContact.  # noqa: E501
        :type: str
        """

        self._personal_email = personal_email

    @property
    def state(self):
        """Gets the state of this GETAccountTypeSoldToContact.  # noqa: E501

        Full state name. This field does not contain the ISO-standard abbreviation of the state name.   # noqa: E501

        :return: The state of this GETAccountTypeSoldToContact.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this GETAccountTypeSoldToContact.

        Full state name. This field does not contain the ISO-standard abbreviation of the state name.   # noqa: E501

        :param state: The state of this GETAccountTypeSoldToContact.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def tax_region(self):
        """Gets the tax_region of this GETAccountTypeSoldToContact.  # noqa: E501

        A region string, defined in your Zuora tax rules.   # noqa: E501

        :return: The tax_region of this GETAccountTypeSoldToContact.  # noqa: E501
        :rtype: str
        """
        return self._tax_region

    @tax_region.setter
    def tax_region(self, tax_region):
        """Sets the tax_region of this GETAccountTypeSoldToContact.

        A region string, defined in your Zuora tax rules.   # noqa: E501

        :param tax_region: The tax_region of this GETAccountTypeSoldToContact.  # noqa: E501
        :type: str
        """

        self._tax_region = tax_region

    @property
    def work_email(self):
        """Gets the work_email of this GETAccountTypeSoldToContact.  # noqa: E501

        Work email address, 80 characters or less.   # noqa: E501

        :return: The work_email of this GETAccountTypeSoldToContact.  # noqa: E501
        :rtype: str
        """
        return self._work_email

    @work_email.setter
    def work_email(self, work_email):
        """Sets the work_email of this GETAccountTypeSoldToContact.

        Work email address, 80 characters or less.   # noqa: E501

        :param work_email: The work_email of this GETAccountTypeSoldToContact.  # noqa: E501
        :type: str
        """

        self._work_email = work_email

    @property
    def work_phone(self):
        """Gets the work_phone of this GETAccountTypeSoldToContact.  # noqa: E501

        Work phone number, 40 characters or less.   # noqa: E501

        :return: The work_phone of this GETAccountTypeSoldToContact.  # noqa: E501
        :rtype: str
        """
        return self._work_phone

    @work_phone.setter
    def work_phone(self, work_phone):
        """Sets the work_phone of this GETAccountTypeSoldToContact.

        Work phone number, 40 characters or less.   # noqa: E501

        :param work_phone: The work_phone of this GETAccountTypeSoldToContact.  # noqa: E501
        :type: str
        """

        self._work_phone = work_phone

    @property
    def zip_code(self):
        """Gets the zip_code of this GETAccountTypeSoldToContact.  # noqa: E501

        Zip code, 20 characters or less.   # noqa: E501

        :return: The zip_code of this GETAccountTypeSoldToContact.  # noqa: E501
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this GETAccountTypeSoldToContact.

        Zip code, 20 characters or less.   # noqa: E501

        :param zip_code: The zip_code of this GETAccountTypeSoldToContact.  # noqa: E501
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
        if issubclass(GETAccountTypeSoldToContact, dict):
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
        if not isinstance(other, GETAccountTypeSoldToContact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
