# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.subscription_product_feature_object_custom_fields import SubscriptionProductFeatureObjectCustomFields  # noqa: F401,E501


class SubscriptionProductFeature(object):
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
        'created_by_id': 'str',
        'created_date': 'datetime',
        'description': 'str',
        'feature_code': 'str',
        'feature_id': 'str',
        'name': 'str',
        'rate_plan_id': 'str',
        'updated_by_id': 'str',
        'updated_date': 'datetime'
    }

    attribute_map = {
        'created_by_id': 'CreatedById',
        'created_date': 'CreatedDate',
        'description': 'Description',
        'feature_code': 'FeatureCode',
        'feature_id': 'FeatureId',
        'name': 'Name',
        'rate_plan_id': 'RatePlanId',
        'updated_by_id': 'UpdatedById',
        'updated_date': 'UpdatedDate'
    }

    def __init__(self, created_by_id=None, created_date=None, description=None, feature_code=None, feature_id=None, name=None, rate_plan_id=None, updated_by_id=None, updated_date=None):  # noqa: E501
        """SubscriptionProductFeature - a model defined in Swagger"""  # noqa: E501

        self._created_by_id = None
        self._created_date = None
        self._description = None
        self._feature_code = None
        self._feature_id = None
        self._name = None
        self._rate_plan_id = None
        self._updated_by_id = None
        self._updated_date = None
        self.discriminator = None

        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_date is not None:
            self.created_date = created_date
        if description is not None:
            self.description = description
        if feature_code is not None:
            self.feature_code = feature_code
        self.feature_id = feature_id
        if name is not None:
            self.name = name
        if rate_plan_id is not None:
            self.rate_plan_id = rate_plan_id
        if updated_by_id is not None:
            self.updated_by_id = updated_by_id
        if updated_date is not None:
            self.updated_date = updated_date

    @property
    def created_by_id(self):
        """Gets the created_by_id of this SubscriptionProductFeature.  # noqa: E501

          # noqa: E501

        :return: The created_by_id of this SubscriptionProductFeature.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this SubscriptionProductFeature.

          # noqa: E501

        :param created_by_id: The created_by_id of this SubscriptionProductFeature.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def created_date(self):
        """Gets the created_date of this SubscriptionProductFeature.  # noqa: E501

         Date and time when the product feature was added to the subscription.   **Character limit**: 29   **Values**:   # noqa: E501

        :return: The created_date of this SubscriptionProductFeature.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this SubscriptionProductFeature.

         Date and time when the product feature was added to the subscription.   **Character limit**: 29   **Values**:   # noqa: E501

        :param created_date: The created_date of this SubscriptionProductFeature.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def description(self):
        """Gets the description of this SubscriptionProductFeature.  # noqa: E501

         Description of the subscription product feature.   **Character limit**: 500   **Values**:   # noqa: E501

        :return: The description of this SubscriptionProductFeature.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SubscriptionProductFeature.

         Description of the subscription product feature.   **Character limit**: 500   **Values**:   # noqa: E501

        :param description: The description of this SubscriptionProductFeature.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def feature_code(self):
        """Gets the feature_code of this SubscriptionProductFeature.  # noqa: E501

         Unique code of the feature.   **Character limit**: 255   **Values**:   # noqa: E501

        :return: The feature_code of this SubscriptionProductFeature.  # noqa: E501
        :rtype: str
        """
        return self._feature_code

    @feature_code.setter
    def feature_code(self, feature_code):
        """Sets the feature_code of this SubscriptionProductFeature.

         Unique code of the feature.   **Character limit**: 255   **Values**:   # noqa: E501

        :param feature_code: The feature_code of this SubscriptionProductFeature.  # noqa: E501
        :type: str
        """

        self._feature_code = feature_code

    @property
    def feature_id(self):
        """Gets the feature_id of this SubscriptionProductFeature.  # noqa: E501

         Internal Zuora ID of the feature.   **Character limit**: 32   **Values**:   # noqa: E501

        :return: The feature_id of this SubscriptionProductFeature.  # noqa: E501
        :rtype: str
        """
        return self._feature_id

    @feature_id.setter
    def feature_id(self, feature_id):
        """Sets the feature_id of this SubscriptionProductFeature.

         Internal Zuora ID of the feature.   **Character limit**: 32   **Values**:   # noqa: E501

        :param feature_id: The feature_id of this SubscriptionProductFeature.  # noqa: E501
        :type: str
        """
        if feature_id is None:
            raise ValueError("Invalid value for `feature_id`, must not be `None`")  # noqa: E501

        self._feature_id = feature_id

    @property
    def name(self):
        """Gets the name of this SubscriptionProductFeature.  # noqa: E501

         Name of the feature.   **Character limit**: 255   **Values**:   # noqa: E501

        :return: The name of this SubscriptionProductFeature.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubscriptionProductFeature.

         Name of the feature.   **Character limit**: 255   **Values**:   # noqa: E501

        :param name: The name of this SubscriptionProductFeature.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def rate_plan_id(self):
        """Gets the rate_plan_id of this SubscriptionProductFeature.  # noqa: E501

         Id of the product rate plan to which the feature belongs.   **Character limit**: 32   **Values**:   # noqa: E501

        :return: The rate_plan_id of this SubscriptionProductFeature.  # noqa: E501
        :rtype: str
        """
        return self._rate_plan_id

    @rate_plan_id.setter
    def rate_plan_id(self, rate_plan_id):
        """Sets the rate_plan_id of this SubscriptionProductFeature.

         Id of the product rate plan to which the feature belongs.   **Character limit**: 32   **Values**:   # noqa: E501

        :param rate_plan_id: The rate_plan_id of this SubscriptionProductFeature.  # noqa: E501
        :type: str
        """

        self._rate_plan_id = rate_plan_id

    @property
    def updated_by_id(self):
        """Gets the updated_by_id of this SubscriptionProductFeature.  # noqa: E501

         Internal Zuora ID of the user who last updated the subscription product feature.   **Character limit**: 32   **Values**:   # noqa: E501

        :return: The updated_by_id of this SubscriptionProductFeature.  # noqa: E501
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """Sets the updated_by_id of this SubscriptionProductFeature.

         Internal Zuora ID of the user who last updated the subscription product feature.   **Character limit**: 32   **Values**:   # noqa: E501

        :param updated_by_id: The updated_by_id of this SubscriptionProductFeature.  # noqa: E501
        :type: str
        """

        self._updated_by_id = updated_by_id

    @property
    def updated_date(self):
        """Gets the updated_date of this SubscriptionProductFeature.  # noqa: E501

         Date and time when the subscription product feature was last updated.   **Character limit**: 29   **Values**:   # noqa: E501

        :return: The updated_date of this SubscriptionProductFeature.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this SubscriptionProductFeature.

         Date and time when the subscription product feature was last updated.   **Character limit**: 29   **Values**:   # noqa: E501

        :param updated_date: The updated_date of this SubscriptionProductFeature.  # noqa: E501
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
        if issubclass(SubscriptionProductFeature, dict):
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
        if not isinstance(other, SubscriptionProductFeature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
