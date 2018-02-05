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


class WSStudentThesisDocument(object):
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
        'title': 'str',
        'document_types': 'list[WSClassification]',
        'url': 'str',
        'document_licenses': 'list[WSClassification]',
        'visible_on_portal_date': 'datetime',
        'visibilities': 'list[WSVisibility]',
        'creator': 'str',
        'created': 'datetime',
        'document_version_types': 'list[WSClassification]',
        'embargo_reasons': 'list[WSClassification]',
        'rights_statement': 'str',
        'embargo_date': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'document_types': 'documentTypes',
        'url': 'url',
        'document_licenses': 'documentLicenses',
        'visible_on_portal_date': 'visibleOnPortalDate',
        'visibilities': 'visibilities',
        'creator': 'creator',
        'created': 'created',
        'document_version_types': 'documentVersionTypes',
        'embargo_reasons': 'embargoReasons',
        'rights_statement': 'rightsStatement',
        'embargo_date': 'embargoDate'
    }

    def __init__(self, id=None, title=None, document_types=None, url=None, document_licenses=None, visible_on_portal_date=None, visibilities=None, creator=None, created=None, document_version_types=None, embargo_reasons=None, rights_statement=None, embargo_date=None):
        """
        WSStudentThesisDocument - a model defined in Swagger
        """

        self._id = None
        self._title = None
        self._document_types = None
        self._url = None
        self._document_licenses = None
        self._visible_on_portal_date = None
        self._visibilities = None
        self._creator = None
        self._created = None
        self._document_version_types = None
        self._embargo_reasons = None
        self._rights_statement = None
        self._embargo_date = None

        if id is not None:
          self.id = id
        if title is not None:
          self.title = title
        if document_types is not None:
          self.document_types = document_types
        if url is not None:
          self.url = url
        if document_licenses is not None:
          self.document_licenses = document_licenses
        if visible_on_portal_date is not None:
          self.visible_on_portal_date = visible_on_portal_date
        if visibilities is not None:
          self.visibilities = visibilities
        if creator is not None:
          self.creator = creator
        if created is not None:
          self.created = created
        if document_version_types is not None:
          self.document_version_types = document_version_types
        if embargo_reasons is not None:
          self.embargo_reasons = embargo_reasons
        if rights_statement is not None:
          self.rights_statement = rights_statement
        if embargo_date is not None:
          self.embargo_date = embargo_date

    @property
    def id(self):
        """
        Gets the id of this WSStudentThesisDocument.

        :return: The id of this WSStudentThesisDocument.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WSStudentThesisDocument.

        :param id: The id of this WSStudentThesisDocument.
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """
        Gets the title of this WSStudentThesisDocument.

        :return: The title of this WSStudentThesisDocument.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this WSStudentThesisDocument.

        :param title: The title of this WSStudentThesisDocument.
        :type: str
        """

        self._title = title

    @property
    def document_types(self):
        """
        Gets the document_types of this WSStudentThesisDocument.

        :return: The document_types of this WSStudentThesisDocument.
        :rtype: list[WSClassification]
        """
        return self._document_types

    @document_types.setter
    def document_types(self, document_types):
        """
        Sets the document_types of this WSStudentThesisDocument.

        :param document_types: The document_types of this WSStudentThesisDocument.
        :type: list[WSClassification]
        """

        self._document_types = document_types

    @property
    def url(self):
        """
        Gets the url of this WSStudentThesisDocument.

        :return: The url of this WSStudentThesisDocument.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this WSStudentThesisDocument.

        :param url: The url of this WSStudentThesisDocument.
        :type: str
        """

        self._url = url

    @property
    def document_licenses(self):
        """
        Gets the document_licenses of this WSStudentThesisDocument.

        :return: The document_licenses of this WSStudentThesisDocument.
        :rtype: list[WSClassification]
        """
        return self._document_licenses

    @document_licenses.setter
    def document_licenses(self, document_licenses):
        """
        Sets the document_licenses of this WSStudentThesisDocument.

        :param document_licenses: The document_licenses of this WSStudentThesisDocument.
        :type: list[WSClassification]
        """

        self._document_licenses = document_licenses

    @property
    def visible_on_portal_date(self):
        """
        Gets the visible_on_portal_date of this WSStudentThesisDocument.

        :return: The visible_on_portal_date of this WSStudentThesisDocument.
        :rtype: datetime
        """
        return self._visible_on_portal_date

    @visible_on_portal_date.setter
    def visible_on_portal_date(self, visible_on_portal_date):
        """
        Sets the visible_on_portal_date of this WSStudentThesisDocument.

        :param visible_on_portal_date: The visible_on_portal_date of this WSStudentThesisDocument.
        :type: datetime
        """

        self._visible_on_portal_date = visible_on_portal_date

    @property
    def visibilities(self):
        """
        Gets the visibilities of this WSStudentThesisDocument.

        :return: The visibilities of this WSStudentThesisDocument.
        :rtype: list[WSVisibility]
        """
        return self._visibilities

    @visibilities.setter
    def visibilities(self, visibilities):
        """
        Sets the visibilities of this WSStudentThesisDocument.

        :param visibilities: The visibilities of this WSStudentThesisDocument.
        :type: list[WSVisibility]
        """

        self._visibilities = visibilities

    @property
    def creator(self):
        """
        Gets the creator of this WSStudentThesisDocument.

        :return: The creator of this WSStudentThesisDocument.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """
        Sets the creator of this WSStudentThesisDocument.

        :param creator: The creator of this WSStudentThesisDocument.
        :type: str
        """

        self._creator = creator

    @property
    def created(self):
        """
        Gets the created of this WSStudentThesisDocument.

        :return: The created of this WSStudentThesisDocument.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this WSStudentThesisDocument.

        :param created: The created of this WSStudentThesisDocument.
        :type: datetime
        """

        self._created = created

    @property
    def document_version_types(self):
        """
        Gets the document_version_types of this WSStudentThesisDocument.

        :return: The document_version_types of this WSStudentThesisDocument.
        :rtype: list[WSClassification]
        """
        return self._document_version_types

    @document_version_types.setter
    def document_version_types(self, document_version_types):
        """
        Sets the document_version_types of this WSStudentThesisDocument.

        :param document_version_types: The document_version_types of this WSStudentThesisDocument.
        :type: list[WSClassification]
        """

        self._document_version_types = document_version_types

    @property
    def embargo_reasons(self):
        """
        Gets the embargo_reasons of this WSStudentThesisDocument.

        :return: The embargo_reasons of this WSStudentThesisDocument.
        :rtype: list[WSClassification]
        """
        return self._embargo_reasons

    @embargo_reasons.setter
    def embargo_reasons(self, embargo_reasons):
        """
        Sets the embargo_reasons of this WSStudentThesisDocument.

        :param embargo_reasons: The embargo_reasons of this WSStudentThesisDocument.
        :type: list[WSClassification]
        """

        self._embargo_reasons = embargo_reasons

    @property
    def rights_statement(self):
        """
        Gets the rights_statement of this WSStudentThesisDocument.

        :return: The rights_statement of this WSStudentThesisDocument.
        :rtype: str
        """
        return self._rights_statement

    @rights_statement.setter
    def rights_statement(self, rights_statement):
        """
        Sets the rights_statement of this WSStudentThesisDocument.

        :param rights_statement: The rights_statement of this WSStudentThesisDocument.
        :type: str
        """

        self._rights_statement = rights_statement

    @property
    def embargo_date(self):
        """
        Gets the embargo_date of this WSStudentThesisDocument.

        :return: The embargo_date of this WSStudentThesisDocument.
        :rtype: datetime
        """
        return self._embargo_date

    @embargo_date.setter
    def embargo_date(self, embargo_date):
        """
        Sets the embargo_date of this WSStudentThesisDocument.

        :param embargo_date: The embargo_date of this WSStudentThesisDocument.
        :type: datetime
        """

        self._embargo_date = embargo_date

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
        if not isinstance(other, WSStudentThesisDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
