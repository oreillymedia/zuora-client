# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.revenue_event_object_custom_fields import RevenueEventObjectCustomFields  # noqa: F401,E501


class PUTRSTermType(object):
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
        'distribution_type': 'str',
        'event_type': 'str',
        'event_type_system_id': 'str',
        'notes': 'str',
        'recognition_end': 'date',
        'recognition_start': 'date'
    }

    attribute_map = {
        'distribution_type': 'distributionType',
        'event_type': 'eventType',
        'event_type_system_id': 'eventTypeSystemId',
        'notes': 'notes',
        'recognition_end': 'recognitionEnd',
        'recognition_start': 'recognitionStart'
    }

    def __init__(self, distribution_type=None, event_type=None, event_type_system_id=None, notes=None, recognition_end=None, recognition_start=None):  # noqa: E501
        """PUTRSTermType - a model defined in Swagger"""  # noqa: E501

        self._distribution_type = None
        self._event_type = None
        self._event_type_system_id = None
        self._notes = None
        self._recognition_end = None
        self._recognition_start = None
        self.discriminator = None

        if distribution_type is not None:
            self.distribution_type = distribution_type
        if event_type is not None:
            self.event_type = event_type
        if event_type_system_id is not None:
            self.event_type_system_id = event_type_system_id
        if notes is not None:
            self.notes = notes
        self.recognition_end = recognition_end
        self.recognition_start = recognition_start

    @property
    def distribution_type(self):
        """Gets the distribution_type of this PUTRSTermType.  # noqa: E501

        How you want to distribute the revenue.    * Daily Distribution: Distributes revenue evenly across each day between the recognitionStart and recognitionEnd dates. * Monthly Distribution (Back Load): Back loads the revenue so you distribute the monthly amount in the partial month in the end only. * Monthly Distribution (Front Load): Front loads the revenue so you distribute the monthly amount in the partial month in the beginning only. * Monthly Distribution (Proration by Days): Splits the revenue amount between the two partial months.  **Note:** To use any of the Monthly Distribution options, you must have the \"Monthly recognition over time\" model enabled in **Settings > Finance > Manage Revenue Recognition Models** in the Zuora UI.   # noqa: E501

        :return: The distribution_type of this PUTRSTermType.  # noqa: E501
        :rtype: str
        """
        return self._distribution_type

    @distribution_type.setter
    def distribution_type(self, distribution_type):
        """Sets the distribution_type of this PUTRSTermType.

        How you want to distribute the revenue.    * Daily Distribution: Distributes revenue evenly across each day between the recognitionStart and recognitionEnd dates. * Monthly Distribution (Back Load): Back loads the revenue so you distribute the monthly amount in the partial month in the end only. * Monthly Distribution (Front Load): Front loads the revenue so you distribute the monthly amount in the partial month in the beginning only. * Monthly Distribution (Proration by Days): Splits the revenue amount between the two partial months.  **Note:** To use any of the Monthly Distribution options, you must have the \"Monthly recognition over time\" model enabled in **Settings > Finance > Manage Revenue Recognition Models** in the Zuora UI.   # noqa: E501

        :param distribution_type: The distribution_type of this PUTRSTermType.  # noqa: E501
        :type: str
        """
        allowed_values = ["Daily Distribution", "Monthly Distribution (Back Load)", "Monthly Distribution (Front Load)", "Monthly Distribution (Proration by Days)"]  # noqa: E501
        if distribution_type not in allowed_values:
            raise ValueError(
                "Invalid value for `distribution_type` ({0}), must be one of {1}"  # noqa: E501
                .format(distribution_type, allowed_values)
            )

        self._distribution_type = distribution_type

    @property
    def event_type(self):
        """Gets the event_type of this PUTRSTermType.  # noqa: E501

        Label of the revenue event type. Revenue event type labels can be duplicated. You can configure your revenue event type labels by navigating to **Settings > Finance > Configure Revenue Event Types** in the Zuora UI.  Note that `Credit Memo Posted` and `Debit Memo Posted` are only available if you enable the Invoice Settlement feature.   # noqa: E501

        :return: The event_type of this PUTRSTermType.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this PUTRSTermType.

        Label of the revenue event type. Revenue event type labels can be duplicated. You can configure your revenue event type labels by navigating to **Settings > Finance > Configure Revenue Event Types** in the Zuora UI.  Note that `Credit Memo Posted` and `Debit Memo Posted` are only available if you enable the Invoice Settlement feature.   # noqa: E501

        :param event_type: The event_type of this PUTRSTermType.  # noqa: E501
        :type: str
        """
        allowed_values = ["Invoice Posted", "Invoice Item Adjustment Created", "Invoice Canceled", "Invoice Item Adjustment Canceled", "Revenue Distributed", "Credit Memo Posted", "Debit Memo Posted"]  # noqa: E501
        if event_type not in allowed_values:
            raise ValueError(
                "Invalid value for `event_type` ({0}), must be one of {1}"  # noqa: E501
                .format(event_type, allowed_values)
            )

        self._event_type = event_type

    @property
    def event_type_system_id(self):
        """Gets the event_type_system_id of this PUTRSTermType.  # noqa: E501

        System ID of the revenue event type. Each eventType has a unique system ID. You can configure your revenue event type system IDs by navigating to **Settings > Finance > Configure Revenue Event Types** in the Zuora UI.   # noqa: E501

        :return: The event_type_system_id of this PUTRSTermType.  # noqa: E501
        :rtype: str
        """
        return self._event_type_system_id

    @event_type_system_id.setter
    def event_type_system_id(self, event_type_system_id):
        """Sets the event_type_system_id of this PUTRSTermType.

        System ID of the revenue event type. Each eventType has a unique system ID. You can configure your revenue event type system IDs by navigating to **Settings > Finance > Configure Revenue Event Types** in the Zuora UI.   # noqa: E501

        :param event_type_system_id: The event_type_system_id of this PUTRSTermType.  # noqa: E501
        :type: str
        """

        self._event_type_system_id = event_type_system_id

    @property
    def notes(self):
        """Gets the notes of this PUTRSTermType.  # noqa: E501

        Additional information about this record.   # noqa: E501

        :return: The notes of this PUTRSTermType.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this PUTRSTermType.

        Additional information about this record.   # noqa: E501

        :param notes: The notes of this PUTRSTermType.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def recognition_end(self):
        """Gets the recognition_end of this PUTRSTermType.  # noqa: E501

        The end date of a recognition period in `yyyy-mm-dd` format.   The maximum difference between the `recognitionStart` and `recognitionEnd` date fields is equal to 250 multiplied by the length of an accounting period.   # noqa: E501

        :return: The recognition_end of this PUTRSTermType.  # noqa: E501
        :rtype: date
        """
        return self._recognition_end

    @recognition_end.setter
    def recognition_end(self, recognition_end):
        """Sets the recognition_end of this PUTRSTermType.

        The end date of a recognition period in `yyyy-mm-dd` format.   The maximum difference between the `recognitionStart` and `recognitionEnd` date fields is equal to 250 multiplied by the length of an accounting period.   # noqa: E501

        :param recognition_end: The recognition_end of this PUTRSTermType.  # noqa: E501
        :type: date
        """
        if recognition_end is None:
            raise ValueError("Invalid value for `recognition_end`, must not be `None`")  # noqa: E501

        self._recognition_end = recognition_end

    @property
    def recognition_start(self):
        """Gets the recognition_start of this PUTRSTermType.  # noqa: E501

        The start date of a recognition period in `yyyy-mm-dd` format.  If there is a closed accounting period between the `recognitionStart` and `recognitionEnd` dates, the revenue that would be placed in the closed accounting period is instead placed in the next open accounting period.   # noqa: E501

        :return: The recognition_start of this PUTRSTermType.  # noqa: E501
        :rtype: date
        """
        return self._recognition_start

    @recognition_start.setter
    def recognition_start(self, recognition_start):
        """Sets the recognition_start of this PUTRSTermType.

        The start date of a recognition period in `yyyy-mm-dd` format.  If there is a closed accounting period between the `recognitionStart` and `recognitionEnd` dates, the revenue that would be placed in the closed accounting period is instead placed in the next open accounting period.   # noqa: E501

        :param recognition_start: The recognition_start of this PUTRSTermType.  # noqa: E501
        :type: date
        """
        if recognition_start is None:
            raise ValueError("Invalid value for `recognition_start`, must not be `None`")  # noqa: E501

        self._recognition_start = recognition_start

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
        if issubclass(PUTRSTermType, dict):
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
        if not isinstance(other, PUTRSTermType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
