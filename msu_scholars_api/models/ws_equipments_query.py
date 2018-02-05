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


class WSEquipmentsQuery(object):
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
        'search_string': 'str',
        'uuids': 'list[str]',
        'size': 'int',
        'offset': 'int',
        'linking_strategy': 'str',
        'locales': 'list[str]',
        'fallback_locales': 'list[str]',
        'renderings': 'list[str]',
        'fields': 'list[str]',
        'orderings': 'list[str]',
        'return_used_content': 'bool',
        'navigation_link': 'bool',
        'id_classification': 'str',
        'for_persons': 'WSPersonsQuery',
        'for_organisational_units': 'WSOrganisationsQuery'
    }

    attribute_map = {
        'search_string': 'searchString',
        'uuids': 'uuids',
        'size': 'size',
        'offset': 'offset',
        'linking_strategy': 'linkingStrategy',
        'locales': 'locales',
        'fallback_locales': 'fallbackLocales',
        'renderings': 'renderings',
        'fields': 'fields',
        'orderings': 'orderings',
        'return_used_content': 'returnUsedContent',
        'navigation_link': 'navigationLink',
        'id_classification': 'idClassification',
        'for_persons': 'forPersons',
        'for_organisational_units': 'forOrganisationalUnits'
    }

    def __init__(self, search_string=None, uuids=None, size=None, offset=None, linking_strategy=None, locales=None, fallback_locales=None, renderings=None, fields=None, orderings=None, return_used_content=False, navigation_link=False, id_classification=None, for_persons=None, for_organisational_units=None):
        """
        WSEquipmentsQuery - a model defined in Swagger
        """

        self._search_string = None
        self._uuids = None
        self._size = None
        self._offset = None
        self._linking_strategy = None
        self._locales = None
        self._fallback_locales = None
        self._renderings = None
        self._fields = None
        self._orderings = None
        self._return_used_content = None
        self._navigation_link = None
        self._id_classification = None
        self._for_persons = None
        self._for_organisational_units = None

        if search_string is not None:
          self.search_string = search_string
        if uuids is not None:
          self.uuids = uuids
        if size is not None:
          self.size = size
        if offset is not None:
          self.offset = offset
        if linking_strategy is not None:
          self.linking_strategy = linking_strategy
        if locales is not None:
          self.locales = locales
        if fallback_locales is not None:
          self.fallback_locales = fallback_locales
        if renderings is not None:
          self.renderings = renderings
        if fields is not None:
          self.fields = fields
        if orderings is not None:
          self.orderings = orderings
        if return_used_content is not None:
          self.return_used_content = return_used_content
        if navigation_link is not None:
          self.navigation_link = navigation_link
        if id_classification is not None:
          self.id_classification = id_classification
        if for_persons is not None:
          self.for_persons = for_persons
        if for_organisational_units is not None:
          self.for_organisational_units = for_organisational_units

    @property
    def search_string(self):
        """
        Gets the search_string of this WSEquipmentsQuery.

        :return: The search_string of this WSEquipmentsQuery.
        :rtype: str
        """
        return self._search_string

    @search_string.setter
    def search_string(self, search_string):
        """
        Sets the search_string of this WSEquipmentsQuery.

        :param search_string: The search_string of this WSEquipmentsQuery.
        :type: str
        """

        self._search_string = search_string

    @property
    def uuids(self):
        """
        Gets the uuids of this WSEquipmentsQuery.

        :return: The uuids of this WSEquipmentsQuery.
        :rtype: list[str]
        """
        return self._uuids

    @uuids.setter
    def uuids(self, uuids):
        """
        Sets the uuids of this WSEquipmentsQuery.

        :param uuids: The uuids of this WSEquipmentsQuery.
        :type: list[str]
        """

        self._uuids = uuids

    @property
    def size(self):
        """
        Gets the size of this WSEquipmentsQuery.

        :return: The size of this WSEquipmentsQuery.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this WSEquipmentsQuery.

        :param size: The size of this WSEquipmentsQuery.
        :type: int
        """

        self._size = size

    @property
    def offset(self):
        """
        Gets the offset of this WSEquipmentsQuery.

        :return: The offset of this WSEquipmentsQuery.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this WSEquipmentsQuery.

        :param offset: The offset of this WSEquipmentsQuery.
        :type: int
        """

        self._offset = offset

    @property
    def linking_strategy(self):
        """
        Gets the linking_strategy of this WSEquipmentsQuery.

        :return: The linking_strategy of this WSEquipmentsQuery.
        :rtype: str
        """
        return self._linking_strategy

    @linking_strategy.setter
    def linking_strategy(self, linking_strategy):
        """
        Sets the linking_strategy of this WSEquipmentsQuery.

        :param linking_strategy: The linking_strategy of this WSEquipmentsQuery.
        :type: str
        """

        self._linking_strategy = linking_strategy

    @property
    def locales(self):
        """
        Gets the locales of this WSEquipmentsQuery.

        :return: The locales of this WSEquipmentsQuery.
        :rtype: list[str]
        """
        return self._locales

    @locales.setter
    def locales(self, locales):
        """
        Sets the locales of this WSEquipmentsQuery.

        :param locales: The locales of this WSEquipmentsQuery.
        :type: list[str]
        """

        self._locales = locales

    @property
    def fallback_locales(self):
        """
        Gets the fallback_locales of this WSEquipmentsQuery.

        :return: The fallback_locales of this WSEquipmentsQuery.
        :rtype: list[str]
        """
        return self._fallback_locales

    @fallback_locales.setter
    def fallback_locales(self, fallback_locales):
        """
        Sets the fallback_locales of this WSEquipmentsQuery.

        :param fallback_locales: The fallback_locales of this WSEquipmentsQuery.
        :type: list[str]
        """

        self._fallback_locales = fallback_locales

    @property
    def renderings(self):
        """
        Gets the renderings of this WSEquipmentsQuery.

        :return: The renderings of this WSEquipmentsQuery.
        :rtype: list[str]
        """
        return self._renderings

    @renderings.setter
    def renderings(self, renderings):
        """
        Sets the renderings of this WSEquipmentsQuery.

        :param renderings: The renderings of this WSEquipmentsQuery.
        :type: list[str]
        """

        self._renderings = renderings

    @property
    def fields(self):
        """
        Gets the fields of this WSEquipmentsQuery.

        :return: The fields of this WSEquipmentsQuery.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """
        Sets the fields of this WSEquipmentsQuery.

        :param fields: The fields of this WSEquipmentsQuery.
        :type: list[str]
        """

        self._fields = fields

    @property
    def orderings(self):
        """
        Gets the orderings of this WSEquipmentsQuery.

        :return: The orderings of this WSEquipmentsQuery.
        :rtype: list[str]
        """
        return self._orderings

    @orderings.setter
    def orderings(self, orderings):
        """
        Sets the orderings of this WSEquipmentsQuery.

        :param orderings: The orderings of this WSEquipmentsQuery.
        :type: list[str]
        """

        self._orderings = orderings

    @property
    def return_used_content(self):
        """
        Gets the return_used_content of this WSEquipmentsQuery.

        :return: The return_used_content of this WSEquipmentsQuery.
        :rtype: bool
        """
        return self._return_used_content

    @return_used_content.setter
    def return_used_content(self, return_used_content):
        """
        Sets the return_used_content of this WSEquipmentsQuery.

        :param return_used_content: The return_used_content of this WSEquipmentsQuery.
        :type: bool
        """

        self._return_used_content = return_used_content

    @property
    def navigation_link(self):
        """
        Gets the navigation_link of this WSEquipmentsQuery.

        :return: The navigation_link of this WSEquipmentsQuery.
        :rtype: bool
        """
        return self._navigation_link

    @navigation_link.setter
    def navigation_link(self, navigation_link):
        """
        Sets the navigation_link of this WSEquipmentsQuery.

        :param navigation_link: The navigation_link of this WSEquipmentsQuery.
        :type: bool
        """

        self._navigation_link = navigation_link

    @property
    def id_classification(self):
        """
        Gets the id_classification of this WSEquipmentsQuery.

        :return: The id_classification of this WSEquipmentsQuery.
        :rtype: str
        """
        return self._id_classification

    @id_classification.setter
    def id_classification(self, id_classification):
        """
        Sets the id_classification of this WSEquipmentsQuery.

        :param id_classification: The id_classification of this WSEquipmentsQuery.
        :type: str
        """

        self._id_classification = id_classification

    @property
    def for_persons(self):
        """
        Gets the for_persons of this WSEquipmentsQuery.

        :return: The for_persons of this WSEquipmentsQuery.
        :rtype: WSPersonsQuery
        """
        return self._for_persons

    @for_persons.setter
    def for_persons(self, for_persons):
        """
        Sets the for_persons of this WSEquipmentsQuery.

        :param for_persons: The for_persons of this WSEquipmentsQuery.
        :type: WSPersonsQuery
        """

        self._for_persons = for_persons

    @property
    def for_organisational_units(self):
        """
        Gets the for_organisational_units of this WSEquipmentsQuery.

        :return: The for_organisational_units of this WSEquipmentsQuery.
        :rtype: WSOrganisationsQuery
        """
        return self._for_organisational_units

    @for_organisational_units.setter
    def for_organisational_units(self, for_organisational_units):
        """
        Sets the for_organisational_units of this WSEquipmentsQuery.

        :param for_organisational_units: The for_organisational_units of this WSEquipmentsQuery.
        :type: WSOrganisationsQuery
        """

        self._for_organisational_units = for_organisational_units

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
        if not isinstance(other, WSEquipmentsQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other