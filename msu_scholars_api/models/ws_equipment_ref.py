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


class WSEquipmentRef(object):
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
        'external_id': 'str',
        'external_id_source': 'str',
        'externally_managed': 'bool',
        'ref': 'WSEquipment'
    }

    attribute_map = {
        'uuid': 'uuid',
        'link': 'link',
        'names': 'names',
        'types': 'types',
        'external_id': 'externalId',
        'external_id_source': 'externalIdSource',
        'externally_managed': 'externallyManaged',
        'ref': 'ref'
    }

    def __init__(self, uuid=None, link=None, names=None, types=None, external_id=None, external_id_source=None, externally_managed=False, ref=None):
        """
        WSEquipmentRef - a model defined in Swagger
        """

        self._uuid = None
        self._link = None
        self._names = None
        self._types = None
        self._external_id = None
        self._external_id_source = None
        self._externally_managed = None
        self._ref = None

        if uuid is not None:
          self.uuid = uuid
        if link is not None:
          self.link = link
        if names is not None:
          self.names = names
        if types is not None:
          self.types = types
        if external_id is not None:
          self.external_id = external_id
        if external_id_source is not None:
          self.external_id_source = external_id_source
        if externally_managed is not None:
          self.externally_managed = externally_managed
        if ref is not None:
          self.ref = ref

    @property
    def uuid(self):
        """
        Gets the uuid of this WSEquipmentRef.

        :return: The uuid of this WSEquipmentRef.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this WSEquipmentRef.

        :param uuid: The uuid of this WSEquipmentRef.
        :type: str
        """

        self._uuid = uuid

    @property
    def link(self):
        """
        Gets the link of this WSEquipmentRef.

        :return: The link of this WSEquipmentRef.
        :rtype: WSNavigationLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """
        Sets the link of this WSEquipmentRef.

        :param link: The link of this WSEquipmentRef.
        :type: WSNavigationLink
        """

        self._link = link

    @property
    def names(self):
        """
        Gets the names of this WSEquipmentRef.

        :return: The names of this WSEquipmentRef.
        :rtype: list[WSLocalizedString]
        """
        return self._names

    @names.setter
    def names(self, names):
        """
        Sets the names of this WSEquipmentRef.

        :param names: The names of this WSEquipmentRef.
        :type: list[WSLocalizedString]
        """

        self._names = names

    @property
    def types(self):
        """
        Gets the types of this WSEquipmentRef.

        :return: The types of this WSEquipmentRef.
        :rtype: list[WSClassification]
        """
        return self._types

    @types.setter
    def types(self, types):
        """
        Sets the types of this WSEquipmentRef.

        :param types: The types of this WSEquipmentRef.
        :type: list[WSClassification]
        """

        self._types = types

    @property
    def external_id(self):
        """
        Gets the external_id of this WSEquipmentRef.

        :return: The external_id of this WSEquipmentRef.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """
        Sets the external_id of this WSEquipmentRef.

        :param external_id: The external_id of this WSEquipmentRef.
        :type: str
        """

        self._external_id = external_id

    @property
    def external_id_source(self):
        """
        Gets the external_id_source of this WSEquipmentRef.

        :return: The external_id_source of this WSEquipmentRef.
        :rtype: str
        """
        return self._external_id_source

    @external_id_source.setter
    def external_id_source(self, external_id_source):
        """
        Sets the external_id_source of this WSEquipmentRef.

        :param external_id_source: The external_id_source of this WSEquipmentRef.
        :type: str
        """

        self._external_id_source = external_id_source

    @property
    def externally_managed(self):
        """
        Gets the externally_managed of this WSEquipmentRef.

        :return: The externally_managed of this WSEquipmentRef.
        :rtype: bool
        """
        return self._externally_managed

    @externally_managed.setter
    def externally_managed(self, externally_managed):
        """
        Sets the externally_managed of this WSEquipmentRef.

        :param externally_managed: The externally_managed of this WSEquipmentRef.
        :type: bool
        """

        self._externally_managed = externally_managed

    @property
    def ref(self):
        """
        Gets the ref of this WSEquipmentRef.

        :return: The ref of this WSEquipmentRef.
        :rtype: WSEquipment
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this WSEquipmentRef.

        :param ref: The ref of this WSEquipmentRef.
        :type: WSEquipment
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
        if not isinstance(other, WSEquipmentRef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
