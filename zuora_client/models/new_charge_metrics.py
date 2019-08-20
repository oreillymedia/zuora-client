# coding: utf-8




import pprint
import re  # noqa: F401

import six


class NewChargeMetrics(object):
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
        'charge_number': 'str',
        'dmrr': 'float',
        'dtcv': 'float',
        'mrr': 'float',
        'original_id': 'str',
        'original_rate_plan_id': 'str',
        'product_rate_plan_charge_id': 'str',
        'product_rate_plan_id': 'str',
        'tcv': 'float'
    }

    attribute_map = {
        'charge_number': 'ChargeNumber',
        'dmrr': 'DMRR',
        'dtcv': 'DTCV',
        'mrr': 'MRR',
        'original_id': 'OriginalId',
        'original_rate_plan_id': 'OriginalRatePlanId',
        'product_rate_plan_charge_id': 'ProductRatePlanChargeId',
        'product_rate_plan_id': 'ProductRatePlanId',
        'tcv': 'TCV'
    }

    def __init__(self, charge_number=None, dmrr=None, dtcv=None, mrr=None, original_id=None, original_rate_plan_id=None, product_rate_plan_charge_id=None, product_rate_plan_id=None, tcv=None):  # noqa: E501
        """NewChargeMetrics - a model defined in Swagger"""  # noqa: E501

        self._charge_number = None
        self._dmrr = None
        self._dtcv = None
        self._mrr = None
        self._original_id = None
        self._original_rate_plan_id = None
        self._product_rate_plan_charge_id = None
        self._product_rate_plan_id = None
        self._tcv = None
        self.discriminator = None

        if charge_number is not None:
            self.charge_number = charge_number
        if dmrr is not None:
            self.dmrr = dmrr
        if dtcv is not None:
            self.dtcv = dtcv
        if mrr is not None:
            self.mrr = mrr
        if original_id is not None:
            self.original_id = original_id
        if original_rate_plan_id is not None:
            self.original_rate_plan_id = original_rate_plan_id
        if product_rate_plan_charge_id is not None:
            self.product_rate_plan_charge_id = product_rate_plan_charge_id
        if product_rate_plan_id is not None:
            self.product_rate_plan_id = product_rate_plan_id
        if tcv is not None:
            self.tcv = tcv

    @property
    def charge_number(self):
        """Gets the charge_number of this NewChargeMetrics.  # noqa: E501

          # noqa: E501

        :return: The charge_number of this NewChargeMetrics.  # noqa: E501
        :rtype: str
        """
        return self._charge_number

    @charge_number.setter
    def charge_number(self, charge_number):
        """Sets the charge_number of this NewChargeMetrics.

          # noqa: E501

        :param charge_number: The charge_number of this NewChargeMetrics.  # noqa: E501
        :type: str
        """

        self._charge_number = charge_number

    @property
    def dmrr(self):
        """Gets the dmrr of this NewChargeMetrics.  # noqa: E501

          # noqa: E501

        :return: The dmrr of this NewChargeMetrics.  # noqa: E501
        :rtype: float
        """
        return self._dmrr

    @dmrr.setter
    def dmrr(self, dmrr):
        """Sets the dmrr of this NewChargeMetrics.

          # noqa: E501

        :param dmrr: The dmrr of this NewChargeMetrics.  # noqa: E501
        :type: float
        """

        self._dmrr = dmrr

    @property
    def dtcv(self):
        """Gets the dtcv of this NewChargeMetrics.  # noqa: E501

          # noqa: E501

        :return: The dtcv of this NewChargeMetrics.  # noqa: E501
        :rtype: float
        """
        return self._dtcv

    @dtcv.setter
    def dtcv(self, dtcv):
        """Sets the dtcv of this NewChargeMetrics.

          # noqa: E501

        :param dtcv: The dtcv of this NewChargeMetrics.  # noqa: E501
        :type: float
        """

        self._dtcv = dtcv

    @property
    def mrr(self):
        """Gets the mrr of this NewChargeMetrics.  # noqa: E501

          # noqa: E501

        :return: The mrr of this NewChargeMetrics.  # noqa: E501
        :rtype: float
        """
        return self._mrr

    @mrr.setter
    def mrr(self, mrr):
        """Sets the mrr of this NewChargeMetrics.

          # noqa: E501

        :param mrr: The mrr of this NewChargeMetrics.  # noqa: E501
        :type: float
        """

        self._mrr = mrr

    @property
    def original_id(self):
        """Gets the original_id of this NewChargeMetrics.  # noqa: E501

          # noqa: E501

        :return: The original_id of this NewChargeMetrics.  # noqa: E501
        :rtype: str
        """
        return self._original_id

    @original_id.setter
    def original_id(self, original_id):
        """Sets the original_id of this NewChargeMetrics.

          # noqa: E501

        :param original_id: The original_id of this NewChargeMetrics.  # noqa: E501
        :type: str
        """

        self._original_id = original_id

    @property
    def original_rate_plan_id(self):
        """Gets the original_rate_plan_id of this NewChargeMetrics.  # noqa: E501

          # noqa: E501

        :return: The original_rate_plan_id of this NewChargeMetrics.  # noqa: E501
        :rtype: str
        """
        return self._original_rate_plan_id

    @original_rate_plan_id.setter
    def original_rate_plan_id(self, original_rate_plan_id):
        """Sets the original_rate_plan_id of this NewChargeMetrics.

          # noqa: E501

        :param original_rate_plan_id: The original_rate_plan_id of this NewChargeMetrics.  # noqa: E501
        :type: str
        """

        self._original_rate_plan_id = original_rate_plan_id

    @property
    def product_rate_plan_charge_id(self):
        """Gets the product_rate_plan_charge_id of this NewChargeMetrics.  # noqa: E501

          # noqa: E501

        :return: The product_rate_plan_charge_id of this NewChargeMetrics.  # noqa: E501
        :rtype: str
        """
        return self._product_rate_plan_charge_id

    @product_rate_plan_charge_id.setter
    def product_rate_plan_charge_id(self, product_rate_plan_charge_id):
        """Sets the product_rate_plan_charge_id of this NewChargeMetrics.

          # noqa: E501

        :param product_rate_plan_charge_id: The product_rate_plan_charge_id of this NewChargeMetrics.  # noqa: E501
        :type: str
        """

        self._product_rate_plan_charge_id = product_rate_plan_charge_id

    @property
    def product_rate_plan_id(self):
        """Gets the product_rate_plan_id of this NewChargeMetrics.  # noqa: E501

          # noqa: E501

        :return: The product_rate_plan_id of this NewChargeMetrics.  # noqa: E501
        :rtype: str
        """
        return self._product_rate_plan_id

    @product_rate_plan_id.setter
    def product_rate_plan_id(self, product_rate_plan_id):
        """Sets the product_rate_plan_id of this NewChargeMetrics.

          # noqa: E501

        :param product_rate_plan_id: The product_rate_plan_id of this NewChargeMetrics.  # noqa: E501
        :type: str
        """

        self._product_rate_plan_id = product_rate_plan_id

    @property
    def tcv(self):
        """Gets the tcv of this NewChargeMetrics.  # noqa: E501

          # noqa: E501

        :return: The tcv of this NewChargeMetrics.  # noqa: E501
        :rtype: float
        """
        return self._tcv

    @tcv.setter
    def tcv(self, tcv):
        """Sets the tcv of this NewChargeMetrics.

          # noqa: E501

        :param tcv: The tcv of this NewChargeMetrics.  # noqa: E501
        :type: float
        """

        self._tcv = tcv

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
        if issubclass(NewChargeMetrics, dict):
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
        if not isinstance(other, NewChargeMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other