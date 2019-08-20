# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.contact_object_custom_fields import ContactObjectCustomFields  # noqa: F401,E501


class ProxyCreateContact(object):
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
        'account_id': 'str',
        'address1': 'str',
        'address2': 'str',
        'city': 'str',
        'country': 'str',
        'county': 'str',
        'description': 'str',
        'fax': 'str',
        'first_name': 'str',
        'home_phone': 'str',
        'last_name': 'str',
        'mobile_phone': 'str',
        'nick_name': 'str',
        'other_phone': 'str',
        'other_phone_type': 'str',
        'personal_email': 'str',
        'postal_code': 'str',
        'state': 'str',
        'tax_region': 'str',
        'work_email': 'str',
        'work_phone': 'str'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'address1': 'Address1',
        'address2': 'Address2',
        'city': 'City',
        'country': 'Country',
        'county': 'County',
        'description': 'Description',
        'fax': 'Fax',
        'first_name': 'FirstName',
        'home_phone': 'HomePhone',
        'last_name': 'LastName',
        'mobile_phone': 'MobilePhone',
        'nick_name': 'NickName',
        'other_phone': 'OtherPhone',
        'other_phone_type': 'OtherPhoneType',
        'personal_email': 'PersonalEmail',
        'postal_code': 'PostalCode',
        'state': 'State',
        'tax_region': 'TaxRegion',
        'work_email': 'WorkEmail',
        'work_phone': 'WorkPhone'
    }

    def __init__(self, account_id=None, address1=None, address2=None, city=None, country=None, county=None, description=None, fax=None, first_name=None, home_phone=None, last_name=None, mobile_phone=None, nick_name=None, other_phone=None, other_phone_type=None, personal_email=None, postal_code=None, state=None, tax_region=None, work_email=None, work_phone=None):  # noqa: E501
        """ProxyCreateContact - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._address1 = None
        self._address2 = None
        self._city = None
        self._country = None
        self._county = None
        self._description = None
        self._fax = None
        self._first_name = None
        self._home_phone = None
        self._last_name = None
        self._mobile_phone = None
        self._nick_name = None
        self._other_phone = None
        self._other_phone_type = None
        self._personal_email = None
        self._postal_code = None
        self._state = None
        self._tax_region = None
        self._work_email = None
        self._work_phone = None
        self.discriminator = None

        self.account_id = account_id
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
        if description is not None:
            self.description = description
        if fax is not None:
            self.fax = fax
        self.first_name = first_name
        if home_phone is not None:
            self.home_phone = home_phone
        self.last_name = last_name
        if mobile_phone is not None:
            self.mobile_phone = mobile_phone
        if nick_name is not None:
            self.nick_name = nick_name
        if other_phone is not None:
            self.other_phone = other_phone
        if other_phone_type is not None:
            self.other_phone_type = other_phone_type
        if personal_email is not None:
            self.personal_email = personal_email
        if postal_code is not None:
            self.postal_code = postal_code
        if state is not None:
            self.state = state
        if tax_region is not None:
            self.tax_region = tax_region
        if work_email is not None:
            self.work_email = work_email
        if work_phone is not None:
            self.work_phone = work_phone

    @property
    def account_id(self):
        """Gets the account_id of this ProxyCreateContact.  # noqa: E501

         The Zuora account ID associated with this contact. This field is not required when you use the Subscribe call. This field is required for all other calls. **Character limit: **32 **Values: **a valid account ID   # noqa: E501

        :return: The account_id of this ProxyCreateContact.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ProxyCreateContact.

         The Zuora account ID associated with this contact. This field is not required when you use the Subscribe call. This field is required for all other calls. **Character limit: **32 **Values: **a valid account ID   # noqa: E501

        :param account_id: The account_id of this ProxyCreateContact.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def address1(self):
        """Gets the address1 of this ProxyCreateContact.  # noqa: E501

         The first line of the contact's address, which is often a street address or business name. **Character limit**: 255 **Values**: a string of 255 characters or fewer   # noqa: E501

        :return: The address1 of this ProxyCreateContact.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this ProxyCreateContact.

         The first line of the contact's address, which is often a street address or business name. **Character limit**: 255 **Values**: a string of 255 characters or fewer   # noqa: E501

        :param address1: The address1 of this ProxyCreateContact.  # noqa: E501
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this ProxyCreateContact.  # noqa: E501

         The second line of the contact's address. **Character limit**: 255 **Values**: a string of 255 characters or fewer   # noqa: E501

        :return: The address2 of this ProxyCreateContact.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this ProxyCreateContact.

         The second line of the contact's address. **Character limit**: 255 **Values**: a string of 255 characters or fewer   # noqa: E501

        :param address2: The address2 of this ProxyCreateContact.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def city(self):
        """Gets the city of this ProxyCreateContact.  # noqa: E501

         The city of the contact's address. **Character limit**: 40 **Values: **a string of 40 characters or fewer   # noqa: E501

        :return: The city of this ProxyCreateContact.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this ProxyCreateContact.

         The city of the contact's address. **Character limit**: 40 **Values: **a string of 40 characters or fewer   # noqa: E501

        :param city: The city of this ProxyCreateContact.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this ProxyCreateContact.  # noqa: E501

         The country of the contact's address.   # noqa: E501

        :return: The country of this ProxyCreateContact.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ProxyCreateContact.

         The country of the contact's address.   # noqa: E501

        :param country: The country of this ProxyCreateContact.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def county(self):
        """Gets the county of this ProxyCreateContact.  # noqa: E501

         The county. May optionally be used by Zuora Tax to calculate county tax. **Character limit**: 32 **Values**: a string of 32 characters or fewer   # noqa: E501

        :return: The county of this ProxyCreateContact.  # noqa: E501
        :rtype: str
        """
        return self._county

    @county.setter
    def county(self, county):
        """Sets the county of this ProxyCreateContact.

         The county. May optionally be used by Zuora Tax to calculate county tax. **Character limit**: 32 **Values**: a string of 32 characters or fewer   # noqa: E501

        :param county: The county of this ProxyCreateContact.  # noqa: E501
        :type: str
        """

        self._county = county

    @property
    def description(self):
        """Gets the description of this ProxyCreateContact.  # noqa: E501

         A description for the contact. **Character limit**: 100 **Values**: a string of 100 characters or fewer   # noqa: E501

        :return: The description of this ProxyCreateContact.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProxyCreateContact.

         A description for the contact. **Character limit**: 100 **Values**: a string of 100 characters or fewer   # noqa: E501

        :param description: The description of this ProxyCreateContact.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def fax(self):
        """Gets the fax of this ProxyCreateContact.  # noqa: E501

         The contact's fax number. **Character limit**: 40 **Values**: a string of 40 characters or fewer   # noqa: E501

        :return: The fax of this ProxyCreateContact.  # noqa: E501
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this ProxyCreateContact.

         The contact's fax number. **Character limit**: 40 **Values**: a string of 40 characters or fewer   # noqa: E501

        :param fax: The fax of this ProxyCreateContact.  # noqa: E501
        :type: str
        """

        self._fax = fax

    @property
    def first_name(self):
        """Gets the first_name of this ProxyCreateContact.  # noqa: E501

         The contact's first name. **Character limit**: 100 **Values**: a string of the contact's first name   # noqa: E501

        :return: The first_name of this ProxyCreateContact.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this ProxyCreateContact.

         The contact's first name. **Character limit**: 100 **Values**: a string of the contact's first name   # noqa: E501

        :param first_name: The first_name of this ProxyCreateContact.  # noqa: E501
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def home_phone(self):
        """Gets the home_phone of this ProxyCreateContact.  # noqa: E501

         The contact's home phone number. **Character limit**: 40 **Values**: a string of 40 characters or fewer   # noqa: E501

        :return: The home_phone of this ProxyCreateContact.  # noqa: E501
        :rtype: str
        """
        return self._home_phone

    @home_phone.setter
    def home_phone(self, home_phone):
        """Sets the home_phone of this ProxyCreateContact.

         The contact's home phone number. **Character limit**: 40 **Values**: a string of 40 characters or fewer   # noqa: E501

        :param home_phone: The home_phone of this ProxyCreateContact.  # noqa: E501
        :type: str
        """

        self._home_phone = home_phone

    @property
    def last_name(self):
        """Gets the last_name of this ProxyCreateContact.  # noqa: E501

         The contact's last name. **Character limit**: 100 **Values**: a string of 100 characters or fewer   # noqa: E501

        :return: The last_name of this ProxyCreateContact.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this ProxyCreateContact.

         The contact's last name. **Character limit**: 100 **Values**: a string of 100 characters or fewer   # noqa: E501

        :param last_name: The last_name of this ProxyCreateContact.  # noqa: E501
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def mobile_phone(self):
        """Gets the mobile_phone of this ProxyCreateContact.  # noqa: E501

         The contact's mobile phone number. **Character limit**: 40 **Values**: a string of 40 characters or fewer   # noqa: E501

        :return: The mobile_phone of this ProxyCreateContact.  # noqa: E501
        :rtype: str
        """
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        """Sets the mobile_phone of this ProxyCreateContact.

         The contact's mobile phone number. **Character limit**: 40 **Values**: a string of 40 characters or fewer   # noqa: E501

        :param mobile_phone: The mobile_phone of this ProxyCreateContact.  # noqa: E501
        :type: str
        """

        self._mobile_phone = mobile_phone

    @property
    def nick_name(self):
        """Gets the nick_name of this ProxyCreateContact.  # noqa: E501

         A nickname for the contact. **Character limit**: 100 **Values**: a string of 100 characters or fewer   # noqa: E501

        :return: The nick_name of this ProxyCreateContact.  # noqa: E501
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        """Sets the nick_name of this ProxyCreateContact.

         A nickname for the contact. **Character limit**: 100 **Values**: a string of 100 characters or fewer   # noqa: E501

        :param nick_name: The nick_name of this ProxyCreateContact.  # noqa: E501
        :type: str
        """

        self._nick_name = nick_name

    @property
    def other_phone(self):
        """Gets the other_phone of this ProxyCreateContact.  # noqa: E501

         An additional phone number for the contact. **Character limit**: 40 **Values**: a string of 40 characters or fewer   # noqa: E501

        :return: The other_phone of this ProxyCreateContact.  # noqa: E501
        :rtype: str
        """
        return self._other_phone

    @other_phone.setter
    def other_phone(self, other_phone):
        """Sets the other_phone of this ProxyCreateContact.

         An additional phone number for the contact. **Character limit**: 40 **Values**: a string of 40 characters or fewer   # noqa: E501

        :param other_phone: The other_phone of this ProxyCreateContact.  # noqa: E501
        :type: str
        """

        self._other_phone = other_phone

    @property
    def other_phone_type(self):
        """Gets the other_phone_type of this ProxyCreateContact.  # noqa: E501

        The type of the `OtherPhone`. **Character limit**: 20 **Values**: `Work`, `Mobile`, `Home`, `Other`   # noqa: E501

        :return: The other_phone_type of this ProxyCreateContact.  # noqa: E501
        :rtype: str
        """
        return self._other_phone_type

    @other_phone_type.setter
    def other_phone_type(self, other_phone_type):
        """Sets the other_phone_type of this ProxyCreateContact.

        The type of the `OtherPhone`. **Character limit**: 20 **Values**: `Work`, `Mobile`, `Home`, `Other`   # noqa: E501

        :param other_phone_type: The other_phone_type of this ProxyCreateContact.  # noqa: E501
        :type: str
        """

        self._other_phone_type = other_phone_type

    @property
    def personal_email(self):
        """Gets the personal_email of this ProxyCreateContact.  # noqa: E501

         The contact's personal email address. **Character limit**: 80 **Values**: a string of 80 characters or fewer   # noqa: E501

        :return: The personal_email of this ProxyCreateContact.  # noqa: E501
        :rtype: str
        """
        return self._personal_email

    @personal_email.setter
    def personal_email(self, personal_email):
        """Sets the personal_email of this ProxyCreateContact.

         The contact's personal email address. **Character limit**: 80 **Values**: a string of 80 characters or fewer   # noqa: E501

        :param personal_email: The personal_email of this ProxyCreateContact.  # noqa: E501
        :type: str
        """

        self._personal_email = personal_email

    @property
    def postal_code(self):
        """Gets the postal_code of this ProxyCreateContact.  # noqa: E501

         The zip code for the contact's address. **Character limit:** 20 **Values: **a string of 20 characters or fewer   # noqa: E501

        :return: The postal_code of this ProxyCreateContact.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this ProxyCreateContact.

         The zip code for the contact's address. **Character limit:** 20 **Values: **a string of 20 characters or fewer   # noqa: E501

        :param postal_code: The postal_code of this ProxyCreateContact.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def state(self):
        """Gets the state of this ProxyCreateContact.  # noqa: E501

         The state or province of the contact's address.   # noqa: E501

        :return: The state of this ProxyCreateContact.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ProxyCreateContact.

         The state or province of the contact's address.   # noqa: E501

        :param state: The state of this ProxyCreateContact.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def tax_region(self):
        """Gets the tax_region of this ProxyCreateContact.  # noqa: E501

        If using Zuora Tax rules   # noqa: E501

        :return: The tax_region of this ProxyCreateContact.  # noqa: E501
        :rtype: str
        """
        return self._tax_region

    @tax_region.setter
    def tax_region(self, tax_region):
        """Sets the tax_region of this ProxyCreateContact.

        If using Zuora Tax rules   # noqa: E501

        :param tax_region: The tax_region of this ProxyCreateContact.  # noqa: E501
        :type: str
        """

        self._tax_region = tax_region

    @property
    def work_email(self):
        """Gets the work_email of this ProxyCreateContact.  # noqa: E501

         The contact's business email address. **Character limit**: 80 **Values**: a string of 80 characters or fewer   # noqa: E501

        :return: The work_email of this ProxyCreateContact.  # noqa: E501
        :rtype: str
        """
        return self._work_email

    @work_email.setter
    def work_email(self, work_email):
        """Sets the work_email of this ProxyCreateContact.

         The contact's business email address. **Character limit**: 80 **Values**: a string of 80 characters or fewer   # noqa: E501

        :param work_email: The work_email of this ProxyCreateContact.  # noqa: E501
        :type: str
        """

        self._work_email = work_email

    @property
    def work_phone(self):
        """Gets the work_phone of this ProxyCreateContact.  # noqa: E501

         The contact's business phone number. **Character limit**: 40 **notes**: -- **Values**: a string of 40 characters or fewer   # noqa: E501

        :return: The work_phone of this ProxyCreateContact.  # noqa: E501
        :rtype: str
        """
        return self._work_phone

    @work_phone.setter
    def work_phone(self, work_phone):
        """Sets the work_phone of this ProxyCreateContact.

         The contact's business phone number. **Character limit**: 40 **notes**: -- **Values**: a string of 40 characters or fewer   # noqa: E501

        :param work_phone: The work_phone of this ProxyCreateContact.  # noqa: E501
        :type: str
        """

        self._work_phone = work_phone

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
        if issubclass(ProxyCreateContact, dict):
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
        if not isinstance(other, ProxyCreateContact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
