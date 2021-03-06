# coding: utf-8




import pprint
import re  # noqa: F401

import six


class ProxyGetImport(object):
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
        'id': 'str',
        'import_type': 'str',
        'imported_count': 'int',
        'md5': 'str',
        'name': 'str',
        'original_resource_url': 'str',
        'result_resource_url': 'str',
        'status': 'str',
        'status_reason': 'str',
        'total_count': 'int',
        'updated_by_id': 'str',
        'updated_date': 'datetime'
    }

    attribute_map = {
        'created_by_id': 'CreatedById',
        'created_date': 'CreatedDate',
        'id': 'Id',
        'import_type': 'ImportType',
        'imported_count': 'ImportedCount',
        'md5': 'Md5',
        'name': 'Name',
        'original_resource_url': 'OriginalResourceUrl',
        'result_resource_url': 'ResultResourceUrl',
        'status': 'Status',
        'status_reason': 'StatusReason',
        'total_count': 'TotalCount',
        'updated_by_id': 'UpdatedById',
        'updated_date': 'UpdatedDate'
    }

    def __init__(self, created_by_id=None, created_date=None, id=None, import_type=None, imported_count=None, md5=None, name=None, original_resource_url=None, result_resource_url=None, status=None, status_reason=None, total_count=None, updated_by_id=None, updated_date=None):  # noqa: E501
        """ProxyGetImport - a model defined in Swagger"""  # noqa: E501

        self._created_by_id = None
        self._created_date = None
        self._id = None
        self._import_type = None
        self._imported_count = None
        self._md5 = None
        self._name = None
        self._original_resource_url = None
        self._result_resource_url = None
        self._status = None
        self._status_reason = None
        self._total_count = None
        self._updated_by_id = None
        self._updated_date = None
        self.discriminator = None

        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_date is not None:
            self.created_date = created_date
        if id is not None:
            self.id = id
        if import_type is not None:
            self.import_type = import_type
        if imported_count is not None:
            self.imported_count = imported_count
        if md5 is not None:
            self.md5 = md5
        if name is not None:
            self.name = name
        if original_resource_url is not None:
            self.original_resource_url = original_resource_url
        if result_resource_url is not None:
            self.result_resource_url = result_resource_url
        if status is not None:
            self.status = status
        if status_reason is not None:
            self.status_reason = status_reason
        if total_count is not None:
            self.total_count = total_count
        if updated_by_id is not None:
            self.updated_by_id = updated_by_id
        if updated_date is not None:
            self.updated_date = updated_date

    @property
    def created_by_id(self):
        """Gets the created_by_id of this ProxyGetImport.  # noqa: E501

         The user ID of the person who created the import.  **Character limit**: 32  **Values**: automatically generated   # noqa: E501

        :return: The created_by_id of this ProxyGetImport.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this ProxyGetImport.

         The user ID of the person who created the import.  **Character limit**: 32  **Values**: automatically generated   # noqa: E501

        :param created_by_id: The created_by_id of this ProxyGetImport.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def created_date(self):
        """Gets the created_date of this ProxyGetImport.  # noqa: E501

         The date when the import was created.  **Character limit**: 29  **Values**: automatically generated   # noqa: E501

        :return: The created_date of this ProxyGetImport.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this ProxyGetImport.

         The date when the import was created.  **Character limit**: 29  **Values**: automatically generated   # noqa: E501

        :param created_date: The created_date of this ProxyGetImport.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def id(self):
        """Gets the id of this ProxyGetImport.  # noqa: E501

        Object identifier.  # noqa: E501

        :return: The id of this ProxyGetImport.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProxyGetImport.

        Object identifier.  # noqa: E501

        :param id: The id of this ProxyGetImport.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def import_type(self):
        """Gets the import_type of this ProxyGetImport.  # noqa: E501

         The type of item imported.  **Character limit**: 7  **Values**: Usage   # noqa: E501

        :return: The import_type of this ProxyGetImport.  # noqa: E501
        :rtype: str
        """
        return self._import_type

    @import_type.setter
    def import_type(self, import_type):
        """Sets the import_type of this ProxyGetImport.

         The type of item imported.  **Character limit**: 7  **Values**: Usage   # noqa: E501

        :param import_type: The import_type of this ProxyGetImport.  # noqa: E501
        :type: str
        """

        self._import_type = import_type

    @property
    def imported_count(self):
        """Gets the imported_count of this ProxyGetImport.  # noqa: E501

        The number of records successfully imported.  **Values**: automatically generated   # noqa: E501

        :return: The imported_count of this ProxyGetImport.  # noqa: E501
        :rtype: int
        """
        return self._imported_count

    @imported_count.setter
    def imported_count(self, imported_count):
        """Sets the imported_count of this ProxyGetImport.

        The number of records successfully imported.  **Values**: automatically generated   # noqa: E501

        :param imported_count: The imported_count of this ProxyGetImport.  # noqa: E501
        :type: int
        """

        self._imported_count = imported_count

    @property
    def md5(self):
        """Gets the md5 of this ProxyGetImport.  # noqa: E501

         A check to validate the import file's integrity.  **Character limit:** 32  **System-generated:** no  **Values**: a string of 32 characters or fewer   # noqa: E501

        :return: The md5 of this ProxyGetImport.  # noqa: E501
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this ProxyGetImport.

         A check to validate the import file's integrity.  **Character limit:** 32  **System-generated:** no  **Values**: a string of 32 characters or fewer   # noqa: E501

        :param md5: The md5 of this ProxyGetImport.  # noqa: E501
        :type: str
        """

        self._md5 = md5

    @property
    def name(self):
        """Gets the name of this ProxyGetImport.  # noqa: E501

         A descriptive name for the import.  **Character limit:** 100  **Values:** one of the following:  - a string of 100 characters or fewer - if NULL default is: `import <ImportType_value>`   # noqa: E501

        :return: The name of this ProxyGetImport.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProxyGetImport.

         A descriptive name for the import.  **Character limit:** 100  **Values:** one of the following:  - a string of 100 characters or fewer - if NULL default is: `import <ImportType_value>`   # noqa: E501

        :param name: The name of this ProxyGetImport.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def original_resource_url(self):
        """Gets the original_resource_url of this ProxyGetImport.  # noqa: E501

         The URL for your import file, which contains your records for upload. When you upload the file, Zuora assigns it to this address.  **Values:** automatic dynamically-generated URL   # noqa: E501

        :return: The original_resource_url of this ProxyGetImport.  # noqa: E501
        :rtype: str
        """
        return self._original_resource_url

    @original_resource_url.setter
    def original_resource_url(self, original_resource_url):
        """Sets the original_resource_url of this ProxyGetImport.

         The URL for your import file, which contains your records for upload. When you upload the file, Zuora assigns it to this address.  **Values:** automatic dynamically-generated URL   # noqa: E501

        :param original_resource_url: The original_resource_url of this ProxyGetImport.  # noqa: E501
        :type: str
        """

        self._original_resource_url = original_resource_url

    @property
    def result_resource_url(self):
        """Gets the result_resource_url of this ProxyGetImport.  # noqa: E501

         The URL for the import result file, which is a zipped CSV file.  **Values**: automatic dynamically-generated URL   # noqa: E501

        :return: The result_resource_url of this ProxyGetImport.  # noqa: E501
        :rtype: str
        """
        return self._result_resource_url

    @result_resource_url.setter
    def result_resource_url(self, result_resource_url):
        """Sets the result_resource_url of this ProxyGetImport.

         The URL for the import result file, which is a zipped CSV file.  **Values**: automatic dynamically-generated URL   # noqa: E501

        :param result_resource_url: The result_resource_url of this ProxyGetImport.  # noqa: E501
        :type: str
        """

        self._result_resource_url = result_resource_url

    @property
    def status(self):
        """Gets the status of this ProxyGetImport.  # noqa: E501

        The status of the import process.  **Values**: automatically generated using one of the following values:  - Pending - Processing - Completed - Failed   # noqa: E501

        :return: The status of this ProxyGetImport.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProxyGetImport.

        The status of the import process.  **Values**: automatically generated using one of the following values:  - Pending - Processing - Completed - Failed   # noqa: E501

        :param status: The status of this ProxyGetImport.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def status_reason(self):
        """Gets the status_reason of this ProxyGetImport.  # noqa: E501

         The reason for the system-generated status. Use this information if the import fails.  **Character limit**: 2000  **Values**: automatically generated error message   # noqa: E501

        :return: The status_reason of this ProxyGetImport.  # noqa: E501
        :rtype: str
        """
        return self._status_reason

    @status_reason.setter
    def status_reason(self, status_reason):
        """Sets the status_reason of this ProxyGetImport.

         The reason for the system-generated status. Use this information if the import fails.  **Character limit**: 2000  **Values**: automatically generated error message   # noqa: E501

        :param status_reason: The status_reason of this ProxyGetImport.  # noqa: E501
        :type: str
        """

        self._status_reason = status_reason

    @property
    def total_count(self):
        """Gets the total_count of this ProxyGetImport.  # noqa: E501

         The number of records in the import file.  **Character limit**:  **Values**: automatically generated   # noqa: E501

        :return: The total_count of this ProxyGetImport.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ProxyGetImport.

         The number of records in the import file.  **Character limit**:  **Values**: automatically generated   # noqa: E501

        :param total_count: The total_count of this ProxyGetImport.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

    @property
    def updated_by_id(self):
        """Gets the updated_by_id of this ProxyGetImport.  # noqa: E501

         The ID of the user who last updated the import.  **Character limit**: 32  **Values**: automatically generated   # noqa: E501

        :return: The updated_by_id of this ProxyGetImport.  # noqa: E501
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """Sets the updated_by_id of this ProxyGetImport.

         The ID of the user who last updated the import.  **Character limit**: 32  **Values**: automatically generated   # noqa: E501

        :param updated_by_id: The updated_by_id of this ProxyGetImport.  # noqa: E501
        :type: str
        """

        self._updated_by_id = updated_by_id

    @property
    def updated_date(self):
        """Gets the updated_date of this ProxyGetImport.  # noqa: E501

         The date when the import was last updated. **Character limit**: 29 **Values**: automatically generated   # noqa: E501

        :return: The updated_date of this ProxyGetImport.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this ProxyGetImport.

         The date when the import was last updated. **Character limit**: 29 **Values**: automatically generated   # noqa: E501

        :param updated_date: The updated_date of this ProxyGetImport.  # noqa: E501
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
        if issubclass(ProxyGetImport, dict):
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
        if not isinstance(other, ProxyGetImport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
