# coding: utf-8

"""
    Pure API 511

    This is the Pure Web Service. Listed below are all available endpoints, along with a short description.<br/><br/>In order to use the Pure Web Service, you must enter an API key. These are generated in the Administrator tab of Pure, and issued with a given set of available endpoints.<br/>To enter your API key and begin your use, press the 'Authorize' button to at the top of this page. <br/>You are then presented with two options for entering the API key: <ol><li>Use the API key in query format.</li><li>Use the API key in a header.</li><br/> For further documentation, see <a href=\"documentation/Default.htm\">API Documentation</a>.<br/><br/>A new version of the API is released with each major version of Pure, and remains available for one year. This version is no longer available in Pure 5.15.<br/>The old web service is deprecated, but still available <a href=\"../../../doc/\">here</a>, and it will no longer be available in Pure 5.13.

    OpenAPI spec version: 511
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class WSAuthorCollaboration(object):
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
        'pure_id': 'int',
        'external_id': 'str',
        'external_id_source': 'str',
        'externally_managed': 'bool',
        'uuid': 'str',
        'html_renderings': 'list[WSHtmlRendering]',
        'names': 'list[WSLocalizedString]',
        'name_variants': 'list[str]',
        'external_organisations': 'list[WSExternalOrganisationRef]',
        'classified_sources': 'list[WSClassifiedValue]',
        'workflows': 'list[WSWorkflow]',
        'info': 'WSContentInformation'
    }

    attribute_map = {
        'pure_id': 'pureId',
        'external_id': 'externalId',
        'external_id_source': 'externalIdSource',
        'externally_managed': 'externallyManaged',
        'uuid': 'uuid',
        'html_renderings': 'htmlRenderings',
        'names': 'names',
        'name_variants': 'nameVariants',
        'external_organisations': 'externalOrganisations',
        'classified_sources': 'classifiedSources',
        'workflows': 'workflows',
        'info': 'info'
    }

    def __init__(self, pure_id=None, external_id=None, external_id_source=None, externally_managed=False, uuid=None, html_renderings=None, names=None, name_variants=None, external_organisations=None, classified_sources=None, workflows=None, info=None):
        """
        WSAuthorCollaboration - a model defined in Swagger
        """

        self._pure_id = None
        self._external_id = None
        self._external_id_source = None
        self._externally_managed = None
        self._uuid = None
        self._html_renderings = None
        self._names = None
        self._name_variants = None
        self._external_organisations = None
        self._classified_sources = None
        self._workflows = None
        self._info = None

        if pure_id is not None:
          self.pure_id = pure_id
        if external_id is not None:
          self.external_id = external_id
        if external_id_source is not None:
          self.external_id_source = external_id_source
        if externally_managed is not None:
          self.externally_managed = externally_managed
        if uuid is not None:
          self.uuid = uuid
        if html_renderings is not None:
          self.html_renderings = html_renderings
        if names is not None:
          self.names = names
        if name_variants is not None:
          self.name_variants = name_variants
        if external_organisations is not None:
          self.external_organisations = external_organisations
        if classified_sources is not None:
          self.classified_sources = classified_sources
        if workflows is not None:
          self.workflows = workflows
        if info is not None:
          self.info = info

    @property
    def pure_id(self):
        """
        Gets the pure_id of this WSAuthorCollaboration.

        :return: The pure_id of this WSAuthorCollaboration.
        :rtype: int
        """
        return self._pure_id

    @pure_id.setter
    def pure_id(self, pure_id):
        """
        Sets the pure_id of this WSAuthorCollaboration.

        :param pure_id: The pure_id of this WSAuthorCollaboration.
        :type: int
        """

        self._pure_id = pure_id

    @property
    def external_id(self):
        """
        Gets the external_id of this WSAuthorCollaboration.

        :return: The external_id of this WSAuthorCollaboration.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """
        Sets the external_id of this WSAuthorCollaboration.

        :param external_id: The external_id of this WSAuthorCollaboration.
        :type: str
        """

        self._external_id = external_id

    @property
    def external_id_source(self):
        """
        Gets the external_id_source of this WSAuthorCollaboration.

        :return: The external_id_source of this WSAuthorCollaboration.
        :rtype: str
        """
        return self._external_id_source

    @external_id_source.setter
    def external_id_source(self, external_id_source):
        """
        Sets the external_id_source of this WSAuthorCollaboration.

        :param external_id_source: The external_id_source of this WSAuthorCollaboration.
        :type: str
        """

        self._external_id_source = external_id_source

    @property
    def externally_managed(self):
        """
        Gets the externally_managed of this WSAuthorCollaboration.

        :return: The externally_managed of this WSAuthorCollaboration.
        :rtype: bool
        """
        return self._externally_managed

    @externally_managed.setter
    def externally_managed(self, externally_managed):
        """
        Sets the externally_managed of this WSAuthorCollaboration.

        :param externally_managed: The externally_managed of this WSAuthorCollaboration.
        :type: bool
        """

        self._externally_managed = externally_managed

    @property
    def uuid(self):
        """
        Gets the uuid of this WSAuthorCollaboration.

        :return: The uuid of this WSAuthorCollaboration.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this WSAuthorCollaboration.

        :param uuid: The uuid of this WSAuthorCollaboration.
        :type: str
        """

        self._uuid = uuid

    @property
    def html_renderings(self):
        """
        Gets the html_renderings of this WSAuthorCollaboration.

        :return: The html_renderings of this WSAuthorCollaboration.
        :rtype: list[WSHtmlRendering]
        """
        return self._html_renderings

    @html_renderings.setter
    def html_renderings(self, html_renderings):
        """
        Sets the html_renderings of this WSAuthorCollaboration.

        :param html_renderings: The html_renderings of this WSAuthorCollaboration.
        :type: list[WSHtmlRendering]
        """

        self._html_renderings = html_renderings

    @property
    def names(self):
        """
        Gets the names of this WSAuthorCollaboration.

        :return: The names of this WSAuthorCollaboration.
        :rtype: list[WSLocalizedString]
        """
        return self._names

    @names.setter
    def names(self, names):
        """
        Sets the names of this WSAuthorCollaboration.

        :param names: The names of this WSAuthorCollaboration.
        :type: list[WSLocalizedString]
        """

        self._names = names

    @property
    def name_variants(self):
        """
        Gets the name_variants of this WSAuthorCollaboration.

        :return: The name_variants of this WSAuthorCollaboration.
        :rtype: list[str]
        """
        return self._name_variants

    @name_variants.setter
    def name_variants(self, name_variants):
        """
        Sets the name_variants of this WSAuthorCollaboration.

        :param name_variants: The name_variants of this WSAuthorCollaboration.
        :type: list[str]
        """

        self._name_variants = name_variants

    @property
    def external_organisations(self):
        """
        Gets the external_organisations of this WSAuthorCollaboration.

        :return: The external_organisations of this WSAuthorCollaboration.
        :rtype: list[WSExternalOrganisationRef]
        """
        return self._external_organisations

    @external_organisations.setter
    def external_organisations(self, external_organisations):
        """
        Sets the external_organisations of this WSAuthorCollaboration.

        :param external_organisations: The external_organisations of this WSAuthorCollaboration.
        :type: list[WSExternalOrganisationRef]
        """

        self._external_organisations = external_organisations

    @property
    def classified_sources(self):
        """
        Gets the classified_sources of this WSAuthorCollaboration.

        :return: The classified_sources of this WSAuthorCollaboration.
        :rtype: list[WSClassifiedValue]
        """
        return self._classified_sources

    @classified_sources.setter
    def classified_sources(self, classified_sources):
        """
        Sets the classified_sources of this WSAuthorCollaboration.

        :param classified_sources: The classified_sources of this WSAuthorCollaboration.
        :type: list[WSClassifiedValue]
        """

        self._classified_sources = classified_sources

    @property
    def workflows(self):
        """
        Gets the workflows of this WSAuthorCollaboration.

        :return: The workflows of this WSAuthorCollaboration.
        :rtype: list[WSWorkflow]
        """
        return self._workflows

    @workflows.setter
    def workflows(self, workflows):
        """
        Sets the workflows of this WSAuthorCollaboration.

        :param workflows: The workflows of this WSAuthorCollaboration.
        :type: list[WSWorkflow]
        """

        self._workflows = workflows

    @property
    def info(self):
        """
        Gets the info of this WSAuthorCollaboration.

        :return: The info of this WSAuthorCollaboration.
        :rtype: WSContentInformation
        """
        return self._info

    @info.setter
    def info(self, info):
        """
        Sets the info of this WSAuthorCollaboration.

        :param info: The info of this WSAuthorCollaboration.
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
        if not isinstance(other, WSAuthorCollaboration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other