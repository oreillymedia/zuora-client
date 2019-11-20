# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.get_product_feature_type import GetProductFeatureType  # noqa: F401,E501
from zuora_client.models.product_object_custom_fields import ProductObjectCustomFields  # noqa: F401,E501
from zuora_client.models.product_object_ns_fields import ProductObjectNSFields  # noqa: F401,E501


class GETProductType(object):
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
        'item_type__ns': 'str',
        'sync_date__ns': 'str',
        'category': 'str',
        'description': 'str',
        'effective_end_date': 'date',
        'effective_start_date': 'date',
        'id': 'str',
        'name': 'str',
        'product_features': 'list[GetProductFeatureType]',
        'product_rate_plans': 'list[GETProductRatePlanType]',
        'sku': 'str',
        'tags': 'str',
        'ProductType__c': 'str',
    }

    attribute_map = {
        'integration_id__ns': 'IntegrationId__NS',
        'integration_status__ns': 'IntegrationStatus__NS',
        'item_type__ns': 'ItemType__NS',
        'sync_date__ns': 'SyncDate__NS',
        'category': 'category',
        'description': 'description',
        'effective_end_date': 'effectiveEndDate',
        'effective_start_date': 'effectiveStartDate',
        'id': 'id',
        'name': 'name',
        'product_features': 'productFeatures',
        'product_rate_plans': 'productRatePlans',
        'sku': 'sku',
        'tags': 'tags',
        'ProductType__c': 'ProductType__c',
    }

    def __init__(self, integration_id__ns=None, integration_status__ns=None, item_type__ns=None, sync_date__ns=None, category=None, description=None, effective_end_date=None, effective_start_date=None, id=None, name=None, product_features=None, product_rate_plans=None, sku=None, tags=None, ProductType__c=None):  # noqa: E501
        """GETProductType - a model defined in Swagger"""  # noqa: E501

        self._integration_id__ns = None
        self._integration_status__ns = None
        self._item_type__ns = None
        self._sync_date__ns = None
        self._category = None
        self._description = None
        self._effective_end_date = None
        self._effective_start_date = None
        self._id = None
        self._name = None
        self._product_features = None
        self._product_rate_plans = None
        self._sku = None
        self._tags = None
        self.discriminator = None
        self._ProductType__c = None

        if integration_id__ns is not None:
            self.integration_id__ns = integration_id__ns
        if integration_status__ns is not None:
            self.integration_status__ns = integration_status__ns
        if item_type__ns is not None:
            self.item_type__ns = item_type__ns
        if sync_date__ns is not None:
            self.sync_date__ns = sync_date__ns
        if category is not None:
            self.category = category
        if description is not None:
            self.description = description
        if effective_end_date is not None:
            self.effective_end_date = effective_end_date
        if effective_start_date is not None:
            self.effective_start_date = effective_start_date
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if product_features is not None:
            self.product_features = product_features
        if product_rate_plans is not None:
            self.product_rate_plans = product_rate_plans
        if sku is not None:
            self.sku = sku
        if tags is not None:
            self.tags = tags
        if ProductType__c is not None:
            self.ProductType__c = ProductType__c

    @property
    def ProductType__c(self):
        return self._ProductType__c

    @ProductType__c.setter
    def ProductType__c(self, ProductType__c):
        self._ProductType__c = ProductType__c

    @property
    def integration_id__ns(self):
        """Gets the integration_id__ns of this GETProductType.  # noqa: E501

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_id__ns of this GETProductType.  # noqa: E501
        :rtype: str
        """
        return self._integration_id__ns

    @integration_id__ns.setter
    def integration_id__ns(self, integration_id__ns):
        """Sets the integration_id__ns of this GETProductType.

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_id__ns: The integration_id__ns of this GETProductType.  # noqa: E501
        :type: str
        """
        if integration_id__ns is not None and len(integration_id__ns) > 255:
            raise ValueError("Invalid value for `integration_id__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_id__ns = integration_id__ns

    @property
    def integration_status__ns(self):
        """Gets the integration_status__ns of this GETProductType.  # noqa: E501

        Status of the product's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_status__ns of this GETProductType.  # noqa: E501
        :rtype: str
        """
        return self._integration_status__ns

    @integration_status__ns.setter
    def integration_status__ns(self, integration_status__ns):
        """Sets the integration_status__ns of this GETProductType.

        Status of the product's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_status__ns: The integration_status__ns of this GETProductType.  # noqa: E501
        :type: str
        """
        if integration_status__ns is not None and len(integration_status__ns) > 255:
            raise ValueError("Invalid value for `integration_status__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_status__ns = integration_status__ns

    @property
    def item_type__ns(self):
        """Gets the item_type__ns of this GETProductType.  # noqa: E501

        Type of item that is created in NetSuite for the product. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The item_type__ns of this GETProductType.  # noqa: E501
        :rtype: str
        """
        return self._item_type__ns

    @item_type__ns.setter
    def item_type__ns(self, item_type__ns):
        """Sets the item_type__ns of this GETProductType.

        Type of item that is created in NetSuite for the product. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param item_type__ns: The item_type__ns of this GETProductType.  # noqa: E501
        :type: str
        """
        allowed_values = ["Inventory", "Non Inventory", "Service"]  # noqa: E501
        if item_type__ns not in allowed_values:
            raise ValueError(
                "Invalid value for `item_type__ns` ({0}), must be one of {1}"  # noqa: E501
                .format(item_type__ns, allowed_values)
            )

        self._item_type__ns = item_type__ns

    @property
    def sync_date__ns(self):
        """Gets the sync_date__ns of this GETProductType.  # noqa: E501

        Date when the product was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The sync_date__ns of this GETProductType.  # noqa: E501
        :rtype: str
        """
        return self._sync_date__ns

    @sync_date__ns.setter
    def sync_date__ns(self, sync_date__ns):
        """Sets the sync_date__ns of this GETProductType.

        Date when the product was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param sync_date__ns: The sync_date__ns of this GETProductType.  # noqa: E501
        :type: str
        """
        if sync_date__ns is not None and len(sync_date__ns) > 255:
            raise ValueError("Invalid value for `sync_date__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._sync_date__ns = sync_date__ns

    @property
    def category(self):
        """Gets the category of this GETProductType.  # noqa: E501

        Category of the product. Used by Zuora Quotes Guided Product Selector.  Possible values are:   - Base Products   - Add On Services   - Miscellaneous Products   # noqa: E501

        :return: The category of this GETProductType.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this GETProductType.

        Category of the product. Used by Zuora Quotes Guided Product Selector.  Possible values are:   - Base Products   - Add On Services   - Miscellaneous Products   # noqa: E501

        :param category: The category of this GETProductType.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def description(self):
        """Gets the description of this GETProductType.  # noqa: E501

        Optional product description.   # noqa: E501

        :return: The description of this GETProductType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GETProductType.

        Optional product description.   # noqa: E501

        :param description: The description of this GETProductType.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def effective_end_date(self):
        """Gets the effective_end_date of this GETProductType.  # noqa: E501

        The date when the product expires and cannot be subscribed to anymore, as `yyyy-mm-dd`.   # noqa: E501

        :return: The effective_end_date of this GETProductType.  # noqa: E501
        :rtype: date
        """
        return self._effective_end_date

    @effective_end_date.setter
    def effective_end_date(self, effective_end_date):
        """Sets the effective_end_date of this GETProductType.

        The date when the product expires and cannot be subscribed to anymore, as `yyyy-mm-dd`.   # noqa: E501

        :param effective_end_date: The effective_end_date of this GETProductType.  # noqa: E501
        :type: date
        """

        self._effective_end_date = effective_end_date

    @property
    def effective_start_date(self):
        """Gets the effective_start_date of this GETProductType.  # noqa: E501

        The date when the product becomes available and can be subscribed to, as `yyyy-mm-dd`.   # noqa: E501

        :return: The effective_start_date of this GETProductType.  # noqa: E501
        :rtype: date
        """
        return self._effective_start_date

    @effective_start_date.setter
    def effective_start_date(self, effective_start_date):
        """Sets the effective_start_date of this GETProductType.

        The date when the product becomes available and can be subscribed to, as `yyyy-mm-dd`.   # noqa: E501

        :param effective_start_date: The effective_start_date of this GETProductType.  # noqa: E501
        :type: date
        """

        self._effective_start_date = effective_start_date

    @property
    def id(self):
        """Gets the id of this GETProductType.  # noqa: E501

        Product ID.   # noqa: E501

        :return: The id of this GETProductType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GETProductType.

        Product ID.   # noqa: E501

        :param id: The id of this GETProductType.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GETProductType.  # noqa: E501

        Product name, up to 100 characters.   # noqa: E501

        :return: The name of this GETProductType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GETProductType.

        Product name, up to 100 characters.   # noqa: E501

        :param name: The name of this GETProductType.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def product_features(self):
        """Gets the product_features of this GETProductType.  # noqa: E501

        Container for one or more product features. Only available when the following settings are enabled: - The Entitlements feature in your tenant - The Enable Feature Specification in Product and Subscriptions setting in Settings > Billing   # noqa: E501

        :return: The product_features of this GETProductType.  # noqa: E501
        :rtype: list[GetProductFeatureType]
        """
        return self._product_features

    @product_features.setter
    def product_features(self, product_features):
        """Sets the product_features of this GETProductType.

        Container for one or more product features. Only available when the following settings are enabled: - The Entitlements feature in your tenant - The Enable Feature Specification in Product and Subscriptions setting in Settings > Billing   # noqa: E501

        :param product_features: The product_features of this GETProductType.  # noqa: E501
        :type: list[GetProductFeatureType]
        """

        self._product_features = product_features

    @property
    def product_rate_plans(self):
        """Gets the product_rate_plans of this GETProductType.  # noqa: E501

        URL to retrieve information about all product rate plans of a specific product. For example, `https://rest.zuora.com/v1/rateplan/40289f466463d683016463ef8b7301a0/productRatePlan`. If you want to view the product rate plan details, call [Get product rate plans](https://www.zuora.com/developer/api-reference/#operation/GET_ProductRatePlans) with the returned URL.  This field is in Zuora REST API version control. If you set the `zuora-version` request header to `230.0` or later, the value of this field is a URL. Zuora recommends that you use the latest behavior to retrieve product information.  If you do not set the `zuora-version` request header or you set this header to `229.0` or earlier, the value of this field is an array of product rate plan details. For more information about the array, see the response body of [Get product rate plans](https://www.zuora.com/developer/api-reference/#operation/GET_ProductRatePlans).    # noqa: E501

        :return: The product_rate_plans of this GETProductType.  # noqa: E501
        :rtype: str
        """
        return self._product_rate_plans

    @product_rate_plans.setter
    def product_rate_plans(self, product_rate_plans):
        """Sets the product_rate_plans of this GETProductType.

        URL to retrieve information about all product rate plans of a specific product. For example, `https://rest.zuora.com/v1/rateplan/40289f466463d683016463ef8b7301a0/productRatePlan`. If you want to view the product rate plan details, call [Get product rate plans](https://www.zuora.com/developer/api-reference/#operation/GET_ProductRatePlans) with the returned URL.  This field is in Zuora REST API version control. If you set the `zuora-version` request header to `230.0` or later, the value of this field is a URL. Zuora recommends that you use the latest behavior to retrieve product information.  If you do not set the `zuora-version` request header or you set this header to `229.0` or earlier, the value of this field is an array of product rate plan details. For more information about the array, see the response body of [Get product rate plans](https://www.zuora.com/developer/api-reference/#operation/GET_ProductRatePlans).    # noqa: E501

        :param product_rate_plans: The product_rate_plans of this GETProductType.  # noqa: E501
        :type: str
        """

        self._product_rate_plans = product_rate_plans

    @property
    def sku(self):
        """Gets the sku of this GETProductType.  # noqa: E501

        Unique product SKU, up to 50 characters.   # noqa: E501

        :return: The sku of this GETProductType.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this GETProductType.

        Unique product SKU, up to 50 characters.   # noqa: E501

        :param sku: The sku of this GETProductType.  # noqa: E501
        :type: str
        """

        self._sku = sku

    @property
    def tags(self):
        """Gets the tags of this GETProductType.  # noqa: E501

          # noqa: E501

        :return: The tags of this GETProductType.  # noqa: E501
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this GETProductType.

          # noqa: E501

        :param tags: The tags of this GETProductType.  # noqa: E501
        :type: str
        """

        self._tags = tags

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
        if issubclass(GETProductType, dict):
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
        if not isinstance(other, GETProductType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
