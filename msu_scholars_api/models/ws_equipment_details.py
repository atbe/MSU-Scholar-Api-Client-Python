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


class WSEquipmentDetails(object):
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
        'names': 'list[WSLocalizedString]',
        'classified_sources': 'list[WSClassifiedValue]',
        'acquisition_date': 'datetime',
        'decommission_date': 'datetime',
        'value': 'float',
        'manufacturers': 'list[WSInternalExternalOrganisationAssociation]'
    }

    attribute_map = {
        'pure_id': 'pureId',
        'external_id': 'externalId',
        'external_id_source': 'externalIdSource',
        'externally_managed': 'externallyManaged',
        'names': 'names',
        'classified_sources': 'classifiedSources',
        'acquisition_date': 'acquisitionDate',
        'decommission_date': 'decommissionDate',
        'value': 'value',
        'manufacturers': 'manufacturers'
    }

    def __init__(self, pure_id=None, external_id=None, external_id_source=None, externally_managed=False, names=None, classified_sources=None, acquisition_date=None, decommission_date=None, value=None, manufacturers=None):
        """
        WSEquipmentDetails - a model defined in Swagger
        """

        self._pure_id = None
        self._external_id = None
        self._external_id_source = None
        self._externally_managed = None
        self._names = None
        self._classified_sources = None
        self._acquisition_date = None
        self._decommission_date = None
        self._value = None
        self._manufacturers = None

        if pure_id is not None:
          self.pure_id = pure_id
        if external_id is not None:
          self.external_id = external_id
        if external_id_source is not None:
          self.external_id_source = external_id_source
        if externally_managed is not None:
          self.externally_managed = externally_managed
        if names is not None:
          self.names = names
        if classified_sources is not None:
          self.classified_sources = classified_sources
        if acquisition_date is not None:
          self.acquisition_date = acquisition_date
        if decommission_date is not None:
          self.decommission_date = decommission_date
        if value is not None:
          self.value = value
        if manufacturers is not None:
          self.manufacturers = manufacturers

    @property
    def pure_id(self):
        """
        Gets the pure_id of this WSEquipmentDetails.

        :return: The pure_id of this WSEquipmentDetails.
        :rtype: int
        """
        return self._pure_id

    @pure_id.setter
    def pure_id(self, pure_id):
        """
        Sets the pure_id of this WSEquipmentDetails.

        :param pure_id: The pure_id of this WSEquipmentDetails.
        :type: int
        """

        self._pure_id = pure_id

    @property
    def external_id(self):
        """
        Gets the external_id of this WSEquipmentDetails.

        :return: The external_id of this WSEquipmentDetails.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """
        Sets the external_id of this WSEquipmentDetails.

        :param external_id: The external_id of this WSEquipmentDetails.
        :type: str
        """

        self._external_id = external_id

    @property
    def external_id_source(self):
        """
        Gets the external_id_source of this WSEquipmentDetails.

        :return: The external_id_source of this WSEquipmentDetails.
        :rtype: str
        """
        return self._external_id_source

    @external_id_source.setter
    def external_id_source(self, external_id_source):
        """
        Sets the external_id_source of this WSEquipmentDetails.

        :param external_id_source: The external_id_source of this WSEquipmentDetails.
        :type: str
        """

        self._external_id_source = external_id_source

    @property
    def externally_managed(self):
        """
        Gets the externally_managed of this WSEquipmentDetails.

        :return: The externally_managed of this WSEquipmentDetails.
        :rtype: bool
        """
        return self._externally_managed

    @externally_managed.setter
    def externally_managed(self, externally_managed):
        """
        Sets the externally_managed of this WSEquipmentDetails.

        :param externally_managed: The externally_managed of this WSEquipmentDetails.
        :type: bool
        """

        self._externally_managed = externally_managed

    @property
    def names(self):
        """
        Gets the names of this WSEquipmentDetails.

        :return: The names of this WSEquipmentDetails.
        :rtype: list[WSLocalizedString]
        """
        return self._names

    @names.setter
    def names(self, names):
        """
        Sets the names of this WSEquipmentDetails.

        :param names: The names of this WSEquipmentDetails.
        :type: list[WSLocalizedString]
        """

        self._names = names

    @property
    def classified_sources(self):
        """
        Gets the classified_sources of this WSEquipmentDetails.

        :return: The classified_sources of this WSEquipmentDetails.
        :rtype: list[WSClassifiedValue]
        """
        return self._classified_sources

    @classified_sources.setter
    def classified_sources(self, classified_sources):
        """
        Sets the classified_sources of this WSEquipmentDetails.

        :param classified_sources: The classified_sources of this WSEquipmentDetails.
        :type: list[WSClassifiedValue]
        """

        self._classified_sources = classified_sources

    @property
    def acquisition_date(self):
        """
        Gets the acquisition_date of this WSEquipmentDetails.

        :return: The acquisition_date of this WSEquipmentDetails.
        :rtype: datetime
        """
        return self._acquisition_date

    @acquisition_date.setter
    def acquisition_date(self, acquisition_date):
        """
        Sets the acquisition_date of this WSEquipmentDetails.

        :param acquisition_date: The acquisition_date of this WSEquipmentDetails.
        :type: datetime
        """

        self._acquisition_date = acquisition_date

    @property
    def decommission_date(self):
        """
        Gets the decommission_date of this WSEquipmentDetails.

        :return: The decommission_date of this WSEquipmentDetails.
        :rtype: datetime
        """
        return self._decommission_date

    @decommission_date.setter
    def decommission_date(self, decommission_date):
        """
        Sets the decommission_date of this WSEquipmentDetails.

        :param decommission_date: The decommission_date of this WSEquipmentDetails.
        :type: datetime
        """

        self._decommission_date = decommission_date

    @property
    def value(self):
        """
        Gets the value of this WSEquipmentDetails.

        :return: The value of this WSEquipmentDetails.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this WSEquipmentDetails.

        :param value: The value of this WSEquipmentDetails.
        :type: float
        """

        self._value = value

    @property
    def manufacturers(self):
        """
        Gets the manufacturers of this WSEquipmentDetails.

        :return: The manufacturers of this WSEquipmentDetails.
        :rtype: list[WSInternalExternalOrganisationAssociation]
        """
        return self._manufacturers

    @manufacturers.setter
    def manufacturers(self, manufacturers):
        """
        Sets the manufacturers of this WSEquipmentDetails.

        :param manufacturers: The manufacturers of this WSEquipmentDetails.
        :type: list[WSInternalExternalOrganisationAssociation]
        """

        self._manufacturers = manufacturers

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
        if not isinstance(other, WSEquipmentDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other