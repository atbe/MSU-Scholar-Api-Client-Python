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


class WSConcept(object):
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
        'thesauri': 'WSThesauriRef',
        'concept_id': 'str',
        'parent_concepts': 'list[WSConceptRef]',
        'semantic_groups': 'list[WSSemanticGroupRef]',
        'name': 'list[WSLocalizedString]',
        'terms': 'list[WSLocalizedString]',
        'idf': 'float',
        'info': 'WSContentInformation'
    }

    attribute_map = {
        'uuid': 'uuid',
        'html_renderings': 'htmlRenderings',
        'thesauri': 'thesauri',
        'concept_id': 'conceptId',
        'parent_concepts': 'parentConcepts',
        'semantic_groups': 'semanticGroups',
        'name': 'name',
        'terms': 'terms',
        'idf': 'idf',
        'info': 'info'
    }

    def __init__(self, uuid=None, html_renderings=None, thesauri=None, concept_id=None, parent_concepts=None, semantic_groups=None, name=None, terms=None, idf=None, info=None):
        """
        WSConcept - a model defined in Swagger
        """

        self._uuid = None
        self._html_renderings = None
        self._thesauri = None
        self._concept_id = None
        self._parent_concepts = None
        self._semantic_groups = None
        self._name = None
        self._terms = None
        self._idf = None
        self._info = None

        if uuid is not None:
          self.uuid = uuid
        if html_renderings is not None:
          self.html_renderings = html_renderings
        if thesauri is not None:
          self.thesauri = thesauri
        if concept_id is not None:
          self.concept_id = concept_id
        if parent_concepts is not None:
          self.parent_concepts = parent_concepts
        if semantic_groups is not None:
          self.semantic_groups = semantic_groups
        if name is not None:
          self.name = name
        if terms is not None:
          self.terms = terms
        if idf is not None:
          self.idf = idf
        if info is not None:
          self.info = info

    @property
    def uuid(self):
        """
        Gets the uuid of this WSConcept.

        :return: The uuid of this WSConcept.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this WSConcept.

        :param uuid: The uuid of this WSConcept.
        :type: str
        """

        self._uuid = uuid

    @property
    def html_renderings(self):
        """
        Gets the html_renderings of this WSConcept.

        :return: The html_renderings of this WSConcept.
        :rtype: list[WSHtmlRendering]
        """
        return self._html_renderings

    @html_renderings.setter
    def html_renderings(self, html_renderings):
        """
        Sets the html_renderings of this WSConcept.

        :param html_renderings: The html_renderings of this WSConcept.
        :type: list[WSHtmlRendering]
        """

        self._html_renderings = html_renderings

    @property
    def thesauri(self):
        """
        Gets the thesauri of this WSConcept.

        :return: The thesauri of this WSConcept.
        :rtype: WSThesauriRef
        """
        return self._thesauri

    @thesauri.setter
    def thesauri(self, thesauri):
        """
        Sets the thesauri of this WSConcept.

        :param thesauri: The thesauri of this WSConcept.
        :type: WSThesauriRef
        """

        self._thesauri = thesauri

    @property
    def concept_id(self):
        """
        Gets the concept_id of this WSConcept.

        :return: The concept_id of this WSConcept.
        :rtype: str
        """
        return self._concept_id

    @concept_id.setter
    def concept_id(self, concept_id):
        """
        Sets the concept_id of this WSConcept.

        :param concept_id: The concept_id of this WSConcept.
        :type: str
        """

        self._concept_id = concept_id

    @property
    def parent_concepts(self):
        """
        Gets the parent_concepts of this WSConcept.

        :return: The parent_concepts of this WSConcept.
        :rtype: list[WSConceptRef]
        """
        return self._parent_concepts

    @parent_concepts.setter
    def parent_concepts(self, parent_concepts):
        """
        Sets the parent_concepts of this WSConcept.

        :param parent_concepts: The parent_concepts of this WSConcept.
        :type: list[WSConceptRef]
        """

        self._parent_concepts = parent_concepts

    @property
    def semantic_groups(self):
        """
        Gets the semantic_groups of this WSConcept.

        :return: The semantic_groups of this WSConcept.
        :rtype: list[WSSemanticGroupRef]
        """
        return self._semantic_groups

    @semantic_groups.setter
    def semantic_groups(self, semantic_groups):
        """
        Sets the semantic_groups of this WSConcept.

        :param semantic_groups: The semantic_groups of this WSConcept.
        :type: list[WSSemanticGroupRef]
        """

        self._semantic_groups = semantic_groups

    @property
    def name(self):
        """
        Gets the name of this WSConcept.

        :return: The name of this WSConcept.
        :rtype: list[WSLocalizedString]
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this WSConcept.

        :param name: The name of this WSConcept.
        :type: list[WSLocalizedString]
        """

        self._name = name

    @property
    def terms(self):
        """
        Gets the terms of this WSConcept.

        :return: The terms of this WSConcept.
        :rtype: list[WSLocalizedString]
        """
        return self._terms

    @terms.setter
    def terms(self, terms):
        """
        Sets the terms of this WSConcept.

        :param terms: The terms of this WSConcept.
        :type: list[WSLocalizedString]
        """

        self._terms = terms

    @property
    def idf(self):
        """
        Gets the idf of this WSConcept.

        :return: The idf of this WSConcept.
        :rtype: float
        """
        return self._idf

    @idf.setter
    def idf(self, idf):
        """
        Sets the idf of this WSConcept.

        :param idf: The idf of this WSConcept.
        :type: float
        """

        self._idf = idf

    @property
    def info(self):
        """
        Gets the info of this WSConcept.

        :return: The info of this WSConcept.
        :rtype: WSContentInformation
        """
        return self._info

    @info.setter
    def info(self, info):
        """
        Sets the info of this WSConcept.

        :param info: The info of this WSConcept.
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
        if not isinstance(other, WSConcept):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
