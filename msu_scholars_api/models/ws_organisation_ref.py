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


class WSOrganisationRef(object):
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
        'uuid': 'str',
        'link': 'WSNavigationLink',
        'names': 'list[WSLocalizedString]',
        'types': 'list[WSClassification]',
        'ref': 'WSOrganisation'
    }

    attribute_map = {
        'uuid': 'uuid',
        'link': 'link',
        'names': 'names',
        'types': 'types',
        'ref': 'ref'
    }

    def __init__(self, uuid=None, link=None, names=None, types=None, ref=None):
        """
        WSOrganisationRef - a model defined in Swagger
        """

        self._uuid = None
        self._link = None
        self._names = None
        self._types = None
        self._ref = None

        if uuid is not None:
          self.uuid = uuid
        if link is not None:
          self.link = link
        if names is not None:
          self.names = names
        if types is not None:
          self.types = types
        if ref is not None:
          self.ref = ref

    @property
    def uuid(self):
        """
        Gets the uuid of this WSOrganisationRef.

        :return: The uuid of this WSOrganisationRef.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this WSOrganisationRef.

        :param uuid: The uuid of this WSOrganisationRef.
        :type: str
        """

        self._uuid = uuid

    @property
    def link(self):
        """
        Gets the link of this WSOrganisationRef.

        :return: The link of this WSOrganisationRef.
        :rtype: WSNavigationLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """
        Sets the link of this WSOrganisationRef.

        :param link: The link of this WSOrganisationRef.
        :type: WSNavigationLink
        """

        self._link = link

    @property
    def names(self):
        """
        Gets the names of this WSOrganisationRef.

        :return: The names of this WSOrganisationRef.
        :rtype: list[WSLocalizedString]
        """
        return self._names

    @names.setter
    def names(self, names):
        """
        Sets the names of this WSOrganisationRef.

        :param names: The names of this WSOrganisationRef.
        :type: list[WSLocalizedString]
        """

        self._names = names

    @property
    def types(self):
        """
        Gets the types of this WSOrganisationRef.

        :return: The types of this WSOrganisationRef.
        :rtype: list[WSClassification]
        """
        return self._types

    @types.setter
    def types(self, types):
        """
        Sets the types of this WSOrganisationRef.

        :param types: The types of this WSOrganisationRef.
        :type: list[WSClassification]
        """

        self._types = types

    @property
    def ref(self):
        """
        Gets the ref of this WSOrganisationRef.

        :return: The ref of this WSOrganisationRef.
        :rtype: WSOrganisation
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this WSOrganisationRef.

        :param ref: The ref of this WSOrganisationRef.
        :type: WSOrganisation
        """

        self._ref = ref

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
        if not isinstance(other, WSOrganisationRef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other