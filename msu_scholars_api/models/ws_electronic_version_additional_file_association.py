# coding: utf-8

"""
    PURE API 510

    This is the Pure Web Service. Listed below are all available endpoints, along with a short description.<br/>In order to use the Pure Web Service, you must enter an API key. These are generated in the Administrator tab of Pure, and issues with a given set of available endpoints.<br/>To enter your API key and begin your use, press the Authorize button to at the top of the page. You are then presented with two options for entering the API key: the first option is to use the API key in query format, and the second option is to use the API key in a header.<br/> For further documentation, see <a href=\"documentation/Default.htm\">API Documentation</a>.<br/>A new version of the API is released with each major version of Pure, and remains available for one year. This version is no longer available in Pure 5.14<br/>The old web service is deprecated, but still available <a href=\"../../../doc/\">here</a>, and it will no longer be available in Pure 5.13

    OpenAPI spec version: 510
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class WSElectronicVersionAdditionalFileAssociation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'id': 'int',
        'license_types': 'list[WSClassification]',
        'user_defined_license': 'str',
        'visible_on_portal_date': 'datetime',
        'creator': 'str',
        'created': 'datetime',
        'file': 'WSFileRef',
        'title': 'str',
        'access_types': 'list[WSClassification]',
        'embargo_start_date': 'datetime',
        'embargo_end_date': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'license_types': 'licenseTypes',
        'user_defined_license': 'userDefinedLicense',
        'visible_on_portal_date': 'visibleOnPortalDate',
        'creator': 'creator',
        'created': 'created',
        'file': 'file',
        'title': 'title',
        'access_types': 'accessTypes',
        'embargo_start_date': 'embargoStartDate',
        'embargo_end_date': 'embargoEndDate'
    }

    def __init__(self, id=None, license_types=None, user_defined_license=None, visible_on_portal_date=None, creator=None, created=None, file=None, title=None, access_types=None, embargo_start_date=None, embargo_end_date=None):
        """
        WSElectronicVersionAdditionalFileAssociation - a model defined in Swagger
        """

        self._id = None
        self._license_types = None
        self._user_defined_license = None
        self._visible_on_portal_date = None
        self._creator = None
        self._created = None
        self._file = None
        self._title = None
        self._access_types = None
        self._embargo_start_date = None
        self._embargo_end_date = None

        if id is not None:
          self.id = id
        if license_types is not None:
          self.license_types = license_types
        if user_defined_license is not None:
          self.user_defined_license = user_defined_license
        if visible_on_portal_date is not None:
          self.visible_on_portal_date = visible_on_portal_date
        if creator is not None:
          self.creator = creator
        if created is not None:
          self.created = created
        if file is not None:
          self.file = file
        if title is not None:
          self.title = title
        if access_types is not None:
          self.access_types = access_types
        if embargo_start_date is not None:
          self.embargo_start_date = embargo_start_date
        if embargo_end_date is not None:
          self.embargo_end_date = embargo_end_date

    @property
    def id(self):
        """
        Gets the id of this WSElectronicVersionAdditionalFileAssociation.

        :return: The id of this WSElectronicVersionAdditionalFileAssociation.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WSElectronicVersionAdditionalFileAssociation.

        :param id: The id of this WSElectronicVersionAdditionalFileAssociation.
        :type: int
        """

        self._id = id

    @property
    def license_types(self):
        """
        Gets the license_types of this WSElectronicVersionAdditionalFileAssociation.

        :return: The license_types of this WSElectronicVersionAdditionalFileAssociation.
        :rtype: list[WSClassification]
        """
        return self._license_types

    @license_types.setter
    def license_types(self, license_types):
        """
        Sets the license_types of this WSElectronicVersionAdditionalFileAssociation.

        :param license_types: The license_types of this WSElectronicVersionAdditionalFileAssociation.
        :type: list[WSClassification]
        """

        self._license_types = license_types

    @property
    def user_defined_license(self):
        """
        Gets the user_defined_license of this WSElectronicVersionAdditionalFileAssociation.

        :return: The user_defined_license of this WSElectronicVersionAdditionalFileAssociation.
        :rtype: str
        """
        return self._user_defined_license

    @user_defined_license.setter
    def user_defined_license(self, user_defined_license):
        """
        Sets the user_defined_license of this WSElectronicVersionAdditionalFileAssociation.

        :param user_defined_license: The user_defined_license of this WSElectronicVersionAdditionalFileAssociation.
        :type: str
        """

        self._user_defined_license = user_defined_license

    @property
    def visible_on_portal_date(self):
        """
        Gets the visible_on_portal_date of this WSElectronicVersionAdditionalFileAssociation.

        :return: The visible_on_portal_date of this WSElectronicVersionAdditionalFileAssociation.
        :rtype: datetime
        """
        return self._visible_on_portal_date

    @visible_on_portal_date.setter
    def visible_on_portal_date(self, visible_on_portal_date):
        """
        Sets the visible_on_portal_date of this WSElectronicVersionAdditionalFileAssociation.

        :param visible_on_portal_date: The visible_on_portal_date of this WSElectronicVersionAdditionalFileAssociation.
        :type: datetime
        """

        self._visible_on_portal_date = visible_on_portal_date

    @property
    def creator(self):
        """
        Gets the creator of this WSElectronicVersionAdditionalFileAssociation.

        :return: The creator of this WSElectronicVersionAdditionalFileAssociation.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """
        Sets the creator of this WSElectronicVersionAdditionalFileAssociation.

        :param creator: The creator of this WSElectronicVersionAdditionalFileAssociation.
        :type: str
        """

        self._creator = creator

    @property
    def created(self):
        """
        Gets the created of this WSElectronicVersionAdditionalFileAssociation.

        :return: The created of this WSElectronicVersionAdditionalFileAssociation.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this WSElectronicVersionAdditionalFileAssociation.

        :param created: The created of this WSElectronicVersionAdditionalFileAssociation.
        :type: datetime
        """

        self._created = created

    @property
    def file(self):
        """
        Gets the file of this WSElectronicVersionAdditionalFileAssociation.

        :return: The file of this WSElectronicVersionAdditionalFileAssociation.
        :rtype: WSFileRef
        """
        return self._file

    @file.setter
    def file(self, file):
        """
        Sets the file of this WSElectronicVersionAdditionalFileAssociation.

        :param file: The file of this WSElectronicVersionAdditionalFileAssociation.
        :type: WSFileRef
        """

        self._file = file

    @property
    def title(self):
        """
        Gets the title of this WSElectronicVersionAdditionalFileAssociation.

        :return: The title of this WSElectronicVersionAdditionalFileAssociation.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this WSElectronicVersionAdditionalFileAssociation.

        :param title: The title of this WSElectronicVersionAdditionalFileAssociation.
        :type: str
        """

        self._title = title

    @property
    def access_types(self):
        """
        Gets the access_types of this WSElectronicVersionAdditionalFileAssociation.

        :return: The access_types of this WSElectronicVersionAdditionalFileAssociation.
        :rtype: list[WSClassification]
        """
        return self._access_types

    @access_types.setter
    def access_types(self, access_types):
        """
        Sets the access_types of this WSElectronicVersionAdditionalFileAssociation.

        :param access_types: The access_types of this WSElectronicVersionAdditionalFileAssociation.
        :type: list[WSClassification]
        """

        self._access_types = access_types

    @property
    def embargo_start_date(self):
        """
        Gets the embargo_start_date of this WSElectronicVersionAdditionalFileAssociation.

        :return: The embargo_start_date of this WSElectronicVersionAdditionalFileAssociation.
        :rtype: datetime
        """
        return self._embargo_start_date

    @embargo_start_date.setter
    def embargo_start_date(self, embargo_start_date):
        """
        Sets the embargo_start_date of this WSElectronicVersionAdditionalFileAssociation.

        :param embargo_start_date: The embargo_start_date of this WSElectronicVersionAdditionalFileAssociation.
        :type: datetime
        """

        self._embargo_start_date = embargo_start_date

    @property
    def embargo_end_date(self):
        """
        Gets the embargo_end_date of this WSElectronicVersionAdditionalFileAssociation.

        :return: The embargo_end_date of this WSElectronicVersionAdditionalFileAssociation.
        :rtype: datetime
        """
        return self._embargo_end_date

    @embargo_end_date.setter
    def embargo_end_date(self, embargo_end_date):
        """
        Sets the embargo_end_date of this WSElectronicVersionAdditionalFileAssociation.

        :param embargo_end_date: The embargo_end_date of this WSElectronicVersionAdditionalFileAssociation.
        :type: datetime
        """

        self._embargo_end_date = embargo_end_date

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, WSElectronicVersionAdditionalFileAssociation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other