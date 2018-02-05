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


class WSPublisher(object):
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
        'name': 'str',
        'types': 'list[WSClassification]',
        'alternative_names': 'list[str]',
        'keyword_groups': 'list[WSKeywordGroup]',
        'countries': 'list[WSClassification]',
        'workflows': 'list[WSWorkflow]',
        'externalable_info': 'WSExternalableInformation',
        'info': 'WSContentInformation'
    }

    attribute_map = {
        'uuid': 'uuid',
        'html_renderings': 'htmlRenderings',
        'name': 'name',
        'types': 'types',
        'alternative_names': 'alternativeNames',
        'keyword_groups': 'keywordGroups',
        'countries': 'countries',
        'workflows': 'workflows',
        'externalable_info': 'externalableInfo',
        'info': 'info'
    }

    def __init__(self, uuid=None, html_renderings=None, name=None, types=None, alternative_names=None, keyword_groups=None, countries=None, workflows=None, externalable_info=None, info=None):
        """
        WSPublisher - a model defined in Swagger
        """

        self._uuid = None
        self._html_renderings = None
        self._name = None
        self._types = None
        self._alternative_names = None
        self._keyword_groups = None
        self._countries = None
        self._workflows = None
        self._externalable_info = None
        self._info = None

        if uuid is not None:
          self.uuid = uuid
        if html_renderings is not None:
          self.html_renderings = html_renderings
        if name is not None:
          self.name = name
        if types is not None:
          self.types = types
        if alternative_names is not None:
          self.alternative_names = alternative_names
        if keyword_groups is not None:
          self.keyword_groups = keyword_groups
        if countries is not None:
          self.countries = countries
        if workflows is not None:
          self.workflows = workflows
        if externalable_info is not None:
          self.externalable_info = externalable_info
        if info is not None:
          self.info = info

    @property
    def uuid(self):
        """
        Gets the uuid of this WSPublisher.

        :return: The uuid of this WSPublisher.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this WSPublisher.

        :param uuid: The uuid of this WSPublisher.
        :type: str
        """

        self._uuid = uuid

    @property
    def html_renderings(self):
        """
        Gets the html_renderings of this WSPublisher.

        :return: The html_renderings of this WSPublisher.
        :rtype: list[WSHtmlRendering]
        """
        return self._html_renderings

    @html_renderings.setter
    def html_renderings(self, html_renderings):
        """
        Sets the html_renderings of this WSPublisher.

        :param html_renderings: The html_renderings of this WSPublisher.
        :type: list[WSHtmlRendering]
        """

        self._html_renderings = html_renderings

    @property
    def name(self):
        """
        Gets the name of this WSPublisher.

        :return: The name of this WSPublisher.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this WSPublisher.

        :param name: The name of this WSPublisher.
        :type: str
        """

        self._name = name

    @property
    def types(self):
        """
        Gets the types of this WSPublisher.

        :return: The types of this WSPublisher.
        :rtype: list[WSClassification]
        """
        return self._types

    @types.setter
    def types(self, types):
        """
        Sets the types of this WSPublisher.

        :param types: The types of this WSPublisher.
        :type: list[WSClassification]
        """

        self._types = types

    @property
    def alternative_names(self):
        """
        Gets the alternative_names of this WSPublisher.

        :return: The alternative_names of this WSPublisher.
        :rtype: list[str]
        """
        return self._alternative_names

    @alternative_names.setter
    def alternative_names(self, alternative_names):
        """
        Sets the alternative_names of this WSPublisher.

        :param alternative_names: The alternative_names of this WSPublisher.
        :type: list[str]
        """

        self._alternative_names = alternative_names

    @property
    def keyword_groups(self):
        """
        Gets the keyword_groups of this WSPublisher.

        :return: The keyword_groups of this WSPublisher.
        :rtype: list[WSKeywordGroup]
        """
        return self._keyword_groups

    @keyword_groups.setter
    def keyword_groups(self, keyword_groups):
        """
        Sets the keyword_groups of this WSPublisher.

        :param keyword_groups: The keyword_groups of this WSPublisher.
        :type: list[WSKeywordGroup]
        """

        self._keyword_groups = keyword_groups

    @property
    def countries(self):
        """
        Gets the countries of this WSPublisher.

        :return: The countries of this WSPublisher.
        :rtype: list[WSClassification]
        """
        return self._countries

    @countries.setter
    def countries(self, countries):
        """
        Sets the countries of this WSPublisher.

        :param countries: The countries of this WSPublisher.
        :type: list[WSClassification]
        """

        self._countries = countries

    @property
    def workflows(self):
        """
        Gets the workflows of this WSPublisher.

        :return: The workflows of this WSPublisher.
        :rtype: list[WSWorkflow]
        """
        return self._workflows

    @workflows.setter
    def workflows(self, workflows):
        """
        Sets the workflows of this WSPublisher.

        :param workflows: The workflows of this WSPublisher.
        :type: list[WSWorkflow]
        """

        self._workflows = workflows

    @property
    def externalable_info(self):
        """
        Gets the externalable_info of this WSPublisher.

        :return: The externalable_info of this WSPublisher.
        :rtype: WSExternalableInformation
        """
        return self._externalable_info

    @externalable_info.setter
    def externalable_info(self, externalable_info):
        """
        Sets the externalable_info of this WSPublisher.

        :param externalable_info: The externalable_info of this WSPublisher.
        :type: WSExternalableInformation
        """

        self._externalable_info = externalable_info

    @property
    def info(self):
        """
        Gets the info of this WSPublisher.

        :return: The info of this WSPublisher.
        :rtype: WSContentInformation
        """
        return self._info

    @info.setter
    def info(self, info):
        """
        Sets the info of this WSPublisher.

        :param info: The info of this WSPublisher.
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
        if not isinstance(other, WSPublisher):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
