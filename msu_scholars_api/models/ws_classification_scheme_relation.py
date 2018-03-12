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


class WSClassificationSchemeRelation(object):
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
        'classification': 'WSClassification',
        'title': 'list[WSLocalizedString]',
        'classification_scheme': 'WSClassificationSchemeRef'
    }

    attribute_map = {
        'pure_id': 'pureId',
        'external_id': 'externalId',
        'external_id_source': 'externalIdSource',
        'externally_managed': 'externallyManaged',
        'classification': 'classification',
        'title': 'title',
        'classification_scheme': 'classificationScheme'
    }

    def __init__(self, pure_id=None, external_id=None, external_id_source=None, externally_managed=False, classification=None, title=None, classification_scheme=None):
        """
        WSClassificationSchemeRelation - a model defined in Swagger
        """

        self._pure_id = None
        self._external_id = None
        self._external_id_source = None
        self._externally_managed = None
        self._classification = None
        self._title = None
        self._classification_scheme = None

        if pure_id is not None:
          self.pure_id = pure_id
        if external_id is not None:
          self.external_id = external_id
        if external_id_source is not None:
          self.external_id_source = external_id_source
        if externally_managed is not None:
          self.externally_managed = externally_managed
        if classification is not None:
          self.classification = classification
        if title is not None:
          self.title = title
        if classification_scheme is not None:
          self.classification_scheme = classification_scheme

    @property
    def pure_id(self):
        """
        Gets the pure_id of this WSClassificationSchemeRelation.

        :return: The pure_id of this WSClassificationSchemeRelation.
        :rtype: int
        """
        return self._pure_id

    @pure_id.setter
    def pure_id(self, pure_id):
        """
        Sets the pure_id of this WSClassificationSchemeRelation.

        :param pure_id: The pure_id of this WSClassificationSchemeRelation.
        :type: int
        """

        self._pure_id = pure_id

    @property
    def external_id(self):
        """
        Gets the external_id of this WSClassificationSchemeRelation.

        :return: The external_id of this WSClassificationSchemeRelation.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """
        Sets the external_id of this WSClassificationSchemeRelation.

        :param external_id: The external_id of this WSClassificationSchemeRelation.
        :type: str
        """

        self._external_id = external_id

    @property
    def external_id_source(self):
        """
        Gets the external_id_source of this WSClassificationSchemeRelation.

        :return: The external_id_source of this WSClassificationSchemeRelation.
        :rtype: str
        """
        return self._external_id_source

    @external_id_source.setter
    def external_id_source(self, external_id_source):
        """
        Sets the external_id_source of this WSClassificationSchemeRelation.

        :param external_id_source: The external_id_source of this WSClassificationSchemeRelation.
        :type: str
        """

        self._external_id_source = external_id_source

    @property
    def externally_managed(self):
        """
        Gets the externally_managed of this WSClassificationSchemeRelation.

        :return: The externally_managed of this WSClassificationSchemeRelation.
        :rtype: bool
        """
        return self._externally_managed

    @externally_managed.setter
    def externally_managed(self, externally_managed):
        """
        Sets the externally_managed of this WSClassificationSchemeRelation.

        :param externally_managed: The externally_managed of this WSClassificationSchemeRelation.
        :type: bool
        """

        self._externally_managed = externally_managed

    @property
    def classification(self):
        """
        Gets the classification of this WSClassificationSchemeRelation.

        :return: The classification of this WSClassificationSchemeRelation.
        :rtype: WSClassification
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """
        Sets the classification of this WSClassificationSchemeRelation.

        :param classification: The classification of this WSClassificationSchemeRelation.
        :type: WSClassification
        """

        self._classification = classification

    @property
    def title(self):
        """
        Gets the title of this WSClassificationSchemeRelation.

        :return: The title of this WSClassificationSchemeRelation.
        :rtype: list[WSLocalizedString]
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this WSClassificationSchemeRelation.

        :param title: The title of this WSClassificationSchemeRelation.
        :type: list[WSLocalizedString]
        """

        self._title = title

    @property
    def classification_scheme(self):
        """
        Gets the classification_scheme of this WSClassificationSchemeRelation.

        :return: The classification_scheme of this WSClassificationSchemeRelation.
        :rtype: WSClassificationSchemeRef
        """
        return self._classification_scheme

    @classification_scheme.setter
    def classification_scheme(self, classification_scheme):
        """
        Sets the classification_scheme of this WSClassificationSchemeRelation.

        :param classification_scheme: The classification_scheme of this WSClassificationSchemeRelation.
        :type: WSClassificationSchemeRef
        """

        self._classification_scheme = classification_scheme

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
        if not isinstance(other, WSClassificationSchemeRelation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
