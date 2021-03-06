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


class WSEquipment(object):
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
        'html_renderings': 'list[WSHtmlRendering]',
        'titles': 'list[WSLocalizedString]',
        'types': 'list[WSClassification]',
        'descriptions': 'list[WSLocalizedString]',
        'acquisition_date': 'datetime',
        'responsible_person': 'WSPersonRef',
        'managing_organisational_unit': 'WSOrganisationRef',
        'keyword_groups': 'list[WSKeywordGroup]',
        'visibilities': 'list[WSVisibility]',
        'externalable_info': 'WSExternalableInformation',
        'info': 'WSContentInformation'
    }

    attribute_map = {
        'uuid': 'uuid',
        'html_renderings': 'htmlRenderings',
        'titles': 'titles',
        'types': 'types',
        'descriptions': 'descriptions',
        'acquisition_date': 'acquisitionDate',
        'responsible_person': 'responsiblePerson',
        'managing_organisational_unit': 'managingOrganisationalUnit',
        'keyword_groups': 'keywordGroups',
        'visibilities': 'visibilities',
        'externalable_info': 'externalableInfo',
        'info': 'info'
    }

    def __init__(self, uuid=None, html_renderings=None, titles=None, types=None, descriptions=None, acquisition_date=None, responsible_person=None, managing_organisational_unit=None, keyword_groups=None, visibilities=None, externalable_info=None, info=None):
        """
        WSEquipment - a model defined in Swagger
        """

        self._uuid = None
        self._html_renderings = None
        self._titles = None
        self._types = None
        self._descriptions = None
        self._acquisition_date = None
        self._responsible_person = None
        self._managing_organisational_unit = None
        self._keyword_groups = None
        self._visibilities = None
        self._externalable_info = None
        self._info = None

        if uuid is not None:
          self.uuid = uuid
        if html_renderings is not None:
          self.html_renderings = html_renderings
        if titles is not None:
          self.titles = titles
        if types is not None:
          self.types = types
        if descriptions is not None:
          self.descriptions = descriptions
        if acquisition_date is not None:
          self.acquisition_date = acquisition_date
        if responsible_person is not None:
          self.responsible_person = responsible_person
        if managing_organisational_unit is not None:
          self.managing_organisational_unit = managing_organisational_unit
        if keyword_groups is not None:
          self.keyword_groups = keyword_groups
        if visibilities is not None:
          self.visibilities = visibilities
        if externalable_info is not None:
          self.externalable_info = externalable_info
        if info is not None:
          self.info = info

    @property
    def uuid(self):
        """
        Gets the uuid of this WSEquipment.

        :return: The uuid of this WSEquipment.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this WSEquipment.

        :param uuid: The uuid of this WSEquipment.
        :type: str
        """

        self._uuid = uuid

    @property
    def html_renderings(self):
        """
        Gets the html_renderings of this WSEquipment.

        :return: The html_renderings of this WSEquipment.
        :rtype: list[WSHtmlRendering]
        """
        return self._html_renderings

    @html_renderings.setter
    def html_renderings(self, html_renderings):
        """
        Sets the html_renderings of this WSEquipment.

        :param html_renderings: The html_renderings of this WSEquipment.
        :type: list[WSHtmlRendering]
        """

        self._html_renderings = html_renderings

    @property
    def titles(self):
        """
        Gets the titles of this WSEquipment.

        :return: The titles of this WSEquipment.
        :rtype: list[WSLocalizedString]
        """
        return self._titles

    @titles.setter
    def titles(self, titles):
        """
        Sets the titles of this WSEquipment.

        :param titles: The titles of this WSEquipment.
        :type: list[WSLocalizedString]
        """

        self._titles = titles

    @property
    def types(self):
        """
        Gets the types of this WSEquipment.

        :return: The types of this WSEquipment.
        :rtype: list[WSClassification]
        """
        return self._types

    @types.setter
    def types(self, types):
        """
        Sets the types of this WSEquipment.

        :param types: The types of this WSEquipment.
        :type: list[WSClassification]
        """

        self._types = types

    @property
    def descriptions(self):
        """
        Gets the descriptions of this WSEquipment.

        :return: The descriptions of this WSEquipment.
        :rtype: list[WSLocalizedString]
        """
        return self._descriptions

    @descriptions.setter
    def descriptions(self, descriptions):
        """
        Sets the descriptions of this WSEquipment.

        :param descriptions: The descriptions of this WSEquipment.
        :type: list[WSLocalizedString]
        """

        self._descriptions = descriptions

    @property
    def acquisition_date(self):
        """
        Gets the acquisition_date of this WSEquipment.

        :return: The acquisition_date of this WSEquipment.
        :rtype: datetime
        """
        return self._acquisition_date

    @acquisition_date.setter
    def acquisition_date(self, acquisition_date):
        """
        Sets the acquisition_date of this WSEquipment.

        :param acquisition_date: The acquisition_date of this WSEquipment.
        :type: datetime
        """

        self._acquisition_date = acquisition_date

    @property
    def responsible_person(self):
        """
        Gets the responsible_person of this WSEquipment.

        :return: The responsible_person of this WSEquipment.
        :rtype: WSPersonRef
        """
        return self._responsible_person

    @responsible_person.setter
    def responsible_person(self, responsible_person):
        """
        Sets the responsible_person of this WSEquipment.

        :param responsible_person: The responsible_person of this WSEquipment.
        :type: WSPersonRef
        """

        self._responsible_person = responsible_person

    @property
    def managing_organisational_unit(self):
        """
        Gets the managing_organisational_unit of this WSEquipment.

        :return: The managing_organisational_unit of this WSEquipment.
        :rtype: WSOrganisationRef
        """
        return self._managing_organisational_unit

    @managing_organisational_unit.setter
    def managing_organisational_unit(self, managing_organisational_unit):
        """
        Sets the managing_organisational_unit of this WSEquipment.

        :param managing_organisational_unit: The managing_organisational_unit of this WSEquipment.
        :type: WSOrganisationRef
        """

        self._managing_organisational_unit = managing_organisational_unit

    @property
    def keyword_groups(self):
        """
        Gets the keyword_groups of this WSEquipment.

        :return: The keyword_groups of this WSEquipment.
        :rtype: list[WSKeywordGroup]
        """
        return self._keyword_groups

    @keyword_groups.setter
    def keyword_groups(self, keyword_groups):
        """
        Sets the keyword_groups of this WSEquipment.

        :param keyword_groups: The keyword_groups of this WSEquipment.
        :type: list[WSKeywordGroup]
        """

        self._keyword_groups = keyword_groups

    @property
    def visibilities(self):
        """
        Gets the visibilities of this WSEquipment.

        :return: The visibilities of this WSEquipment.
        :rtype: list[WSVisibility]
        """
        return self._visibilities

    @visibilities.setter
    def visibilities(self, visibilities):
        """
        Sets the visibilities of this WSEquipment.

        :param visibilities: The visibilities of this WSEquipment.
        :type: list[WSVisibility]
        """

        self._visibilities = visibilities

    @property
    def externalable_info(self):
        """
        Gets the externalable_info of this WSEquipment.

        :return: The externalable_info of this WSEquipment.
        :rtype: WSExternalableInformation
        """
        return self._externalable_info

    @externalable_info.setter
    def externalable_info(self, externalable_info):
        """
        Sets the externalable_info of this WSEquipment.

        :param externalable_info: The externalable_info of this WSEquipment.
        :type: WSExternalableInformation
        """

        self._externalable_info = externalable_info

    @property
    def info(self):
        """
        Gets the info of this WSEquipment.

        :return: The info of this WSEquipment.
        :rtype: WSContentInformation
        """
        return self._info

    @info.setter
    def info(self, info):
        """
        Sets the info of this WSEquipment.

        :param info: The info of this WSEquipment.
        :type: WSContentInformation
        """

        self._info = info

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
        if not isinstance(other, WSEquipment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
