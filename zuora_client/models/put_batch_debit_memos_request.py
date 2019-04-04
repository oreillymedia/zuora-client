# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.batch_debit_memo_type import BatchDebitMemoType  # noqa: F401,E501


class PUTBatchDebitMemosRequest(object):
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
        'debit_memos': 'list[BatchDebitMemoType]'
    }

    attribute_map = {
        'debit_memos': 'debitMemos'
    }

    def __init__(self, debit_memos=None):  # noqa: E501
        """PUTBatchDebitMemosRequest - a model defined in Swagger"""  # noqa: E501

        self._debit_memos = None
        self.discriminator = None

        if debit_memos is not None:
            self.debit_memos = debit_memos

    @property
    def debit_memos(self):
        """Gets the debit_memos of this PUTBatchDebitMemosRequest.  # noqa: E501

        Container for debit memo update details.   # noqa: E501

        :return: The debit_memos of this PUTBatchDebitMemosRequest.  # noqa: E501
        :rtype: list[BatchDebitMemoType]
        """
        return self._debit_memos

    @debit_memos.setter
    def debit_memos(self, debit_memos):
        """Sets the debit_memos of this PUTBatchDebitMemosRequest.

        Container for debit memo update details.   # noqa: E501

        :param debit_memos: The debit_memos of this PUTBatchDebitMemosRequest.  # noqa: E501
        :type: list[BatchDebitMemoType]
        """

        self._debit_memos = debit_memos

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
        if issubclass(PUTBatchDebitMemosRequest, dict):
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
        if not isinstance(other, PUTBatchDebitMemosRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
