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


class WSExternalOrganisation(object):
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
        'nature_types': 'list[WSClassification]',
        'parent': 'WSExternalOrganisationRef',
        'acronym': 'str',
        'alternative_names': 'list[str]',
        'classified_sources': 'list[WSClassifiedValue]',
        'address': 'WSAddress',
        'phone_number': 'str',
        'mobile_phone_number': 'str',
        'fax': 'str',
        'email': 'str',
        'bank_account_number': 'str',
        'vat_number': 'str',
        'documents': 'list[WSDocument]',
        'links': 'list[WSLink]',
        'keyword_groups': 'list[WSKeywordGroup]',
        'note': 'str',
        'visibilities': 'list[WSVisibility]',
        'workflows': 'list[WSWorkflow]',
        'externalable_info': 'WSExternalableInformation',
        'info': 'WSContentInformation'
    }

    attribute_map = {
        'uuid': 'uuid',
        'html_renderings': 'htmlRenderings',
        'name': 'name',
        'types': 'types',
        'nature_types': 'natureTypes',
        'parent': 'parent',
        'acronym': 'acronym',
        'alternative_names': 'alternativeNames',
        'classified_sources': 'classifiedSources',
        'address': 'address',
        'phone_number': 'phoneNumber',
        'mobile_phone_number': 'mobilePhoneNumber',
        'fax': 'fax',
        'email': 'email',
        'bank_account_number': 'bankAccountNumber',
        'vat_number': 'vatNumber',
        'documents': 'documents',
        'links': 'links',
        'keyword_groups': 'keywordGroups',
        'note': 'note',
        'visibilities': 'visibilities',
        'workflows': 'workflows',
        'externalable_info': 'externalableInfo',
        'info': 'info'
    }

    def __init__(self, uuid=None, html_renderings=None, name=None, types=None, nature_types=None, parent=None, acronym=None, alternative_names=None, classified_sources=None, address=None, phone_number=None, mobile_phone_number=None, fax=None, email=None, bank_account_number=None, vat_number=None, documents=None, links=None, keyword_groups=None, note=None, visibilities=None, workflows=None, externalable_info=None, info=None):
        """
        WSExternalOrganisation - a model defined in Swagger
        """

        self._uuid = None
        self._html_renderings = None
        self._name = None
        self._types = None
        self._nature_types = None
        self._parent = None
        self._acronym = None
        self._alternative_names = None
        self._classified_sources = None
        self._address = None
        self._phone_number = None
        self._mobile_phone_number = None
        self._fax = None
        self._email = None
        self._bank_account_number = None
        self._vat_number = None
        self._documents = None
        self._links = None
        self._keyword_groups = None
        self._note = None
        self._visibilities = None
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
        if nature_types is not None:
          self.nature_types = nature_types
        if parent is not None:
          self.parent = parent
        if acronym is not None:
          self.acronym = acronym
        if alternative_names is not None:
          self.alternative_names = alternative_names
        if classified_sources is not None:
          self.classified_sources = classified_sources
        if address is not None:
          self.address = address
        if phone_number is not None:
          self.phone_number = phone_number
        if mobile_phone_number is not None:
          self.mobile_phone_number = mobile_phone_number
        if fax is not None:
          self.fax = fax
        if email is not None:
          self.email = email
        if bank_account_number is not None:
          self.bank_account_number = bank_account_number
        if vat_number is not None:
          self.vat_number = vat_number
        if documents is not None:
          self.documents = documents
        if links is not None:
          self.links = links
        if keyword_groups is not None:
          self.keyword_groups = keyword_groups
        if note is not None:
          self.note = note
        if visibilities is not None:
          self.visibilities = visibilities
        if workflows is not None:
          self.workflows = workflows
        if externalable_info is not None:
          self.externalable_info = externalable_info
        if info is not None:
          self.info = info

    @property
    def uuid(self):
        """
        Gets the uuid of this WSExternalOrganisation.

        :return: The uuid of this WSExternalOrganisation.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this WSExternalOrganisation.

        :param uuid: The uuid of this WSExternalOrganisation.
        :type: str
        """

        self._uuid = uuid

    @property
    def html_renderings(self):
        """
        Gets the html_renderings of this WSExternalOrganisation.

        :return: The html_renderings of this WSExternalOrganisation.
        :rtype: list[WSHtmlRendering]
        """
        return self._html_renderings

    @html_renderings.setter
    def html_renderings(self, html_renderings):
        """
        Sets the html_renderings of this WSExternalOrganisation.

        :param html_renderings: The html_renderings of this WSExternalOrganisation.
        :type: list[WSHtmlRendering]
        """

        self._html_renderings = html_renderings

    @property
    def name(self):
        """
        Gets the name of this WSExternalOrganisation.

        :return: The name of this WSExternalOrganisation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this WSExternalOrganisation.

        :param name: The name of this WSExternalOrganisation.
        :type: str
        """

        self._name = name

    @property
    def types(self):
        """
        Gets the types of this WSExternalOrganisation.

        :return: The types of this WSExternalOrganisation.
        :rtype: list[WSClassification]
        """
        return self._types

    @types.setter
    def types(self, types):
        """
        Sets the types of this WSExternalOrganisation.

        :param types: The types of this WSExternalOrganisation.
        :type: list[WSClassification]
        """

        self._types = types

    @property
    def nature_types(self):
        """
        Gets the nature_types of this WSExternalOrganisation.

        :return: The nature_types of this WSExternalOrganisation.
        :rtype: list[WSClassification]
        """
        return self._nature_types

    @nature_types.setter
    def nature_types(self, nature_types):
        """
        Sets the nature_types of this WSExternalOrganisation.

        :param nature_types: The nature_types of this WSExternalOrganisation.
        :type: list[WSClassification]
        """

        self._nature_types = nature_types

    @property
    def parent(self):
        """
        Gets the parent of this WSExternalOrganisation.

        :return: The parent of this WSExternalOrganisation.
        :rtype: WSExternalOrganisationRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this WSExternalOrganisation.

        :param parent: The parent of this WSExternalOrganisation.
        :type: WSExternalOrganisationRef
        """

        self._parent = parent

    @property
    def acronym(self):
        """
        Gets the acronym of this WSExternalOrganisation.

        :return: The acronym of this WSExternalOrganisation.
        :rtype: str
        """
        return self._acronym

    @acronym.setter
    def acronym(self, acronym):
        """
        Sets the acronym of this WSExternalOrganisation.

        :param acronym: The acronym of this WSExternalOrganisation.
        :type: str
        """

        self._acronym = acronym

    @property
    def alternative_names(self):
        """
        Gets the alternative_names of this WSExternalOrganisation.

        :return: The alternative_names of this WSExternalOrganisation.
        :rtype: list[str]
        """
        return self._alternative_names

    @alternative_names.setter
    def alternative_names(self, alternative_names):
        """
        Sets the alternative_names of this WSExternalOrganisation.

        :param alternative_names: The alternative_names of this WSExternalOrganisation.
        :type: list[str]
        """

        self._alternative_names = alternative_names

    @property
    def classified_sources(self):
        """
        Gets the classified_sources of this WSExternalOrganisation.

        :return: The classified_sources of this WSExternalOrganisation.
        :rtype: list[WSClassifiedValue]
        """
        return self._classified_sources

    @classified_sources.setter
    def classified_sources(self, classified_sources):
        """
        Sets the classified_sources of this WSExternalOrganisation.

        :param classified_sources: The classified_sources of this WSExternalOrganisation.
        :type: list[WSClassifiedValue]
        """

        self._classified_sources = classified_sources

    @property
    def address(self):
        """
        Gets the address of this WSExternalOrganisation.

        :return: The address of this WSExternalOrganisation.
        :rtype: WSAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this WSExternalOrganisation.

        :param address: The address of this WSExternalOrganisation.
        :type: WSAddress
        """

        self._address = address

    @property
    def phone_number(self):
        """
        Gets the phone_number of this WSExternalOrganisation.

        :return: The phone_number of this WSExternalOrganisation.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this WSExternalOrganisation.

        :param phone_number: The phone_number of this WSExternalOrganisation.
        :type: str
        """

        self._phone_number = phone_number

    @property
    def mobile_phone_number(self):
        """
        Gets the mobile_phone_number of this WSExternalOrganisation.

        :return: The mobile_phone_number of this WSExternalOrganisation.
        :rtype: str
        """
        return self._mobile_phone_number

    @mobile_phone_number.setter
    def mobile_phone_number(self, mobile_phone_number):
        """
        Sets the mobile_phone_number of this WSExternalOrganisation.

        :param mobile_phone_number: The mobile_phone_number of this WSExternalOrganisation.
        :type: str
        """

        self._mobile_phone_number = mobile_phone_number

    @property
    def fax(self):
        """
        Gets the fax of this WSExternalOrganisation.

        :return: The fax of this WSExternalOrganisation.
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """
        Sets the fax of this WSExternalOrganisation.

        :param fax: The fax of this WSExternalOrganisation.
        :type: str
        """

        self._fax = fax

    @property
    def email(self):
        """
        Gets the email of this WSExternalOrganisation.

        :return: The email of this WSExternalOrganisation.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this WSExternalOrganisation.

        :param email: The email of this WSExternalOrganisation.
        :type: str
        """

        self._email = email

    @property
    def bank_account_number(self):
        """
        Gets the bank_account_number of this WSExternalOrganisation.

        :return: The bank_account_number of this WSExternalOrganisation.
        :rtype: str
        """
        return self._bank_account_number

    @bank_account_number.setter
    def bank_account_number(self, bank_account_number):
        """
        Sets the bank_account_number of this WSExternalOrganisation.

        :param bank_account_number: The bank_account_number of this WSExternalOrganisation.
        :type: str
        """

        self._bank_account_number = bank_account_number

    @property
    def vat_number(self):
        """
        Gets the vat_number of this WSExternalOrganisation.

        :return: The vat_number of this WSExternalOrganisation.
        :rtype: str
        """
        return self._vat_number

    @vat_number.setter
    def vat_number(self, vat_number):
        """
        Sets the vat_number of this WSExternalOrganisation.

        :param vat_number: The vat_number of this WSExternalOrganisation.
        :type: str
        """

        self._vat_number = vat_number

    @property
    def documents(self):
        """
        Gets the documents of this WSExternalOrganisation.

        :return: The documents of this WSExternalOrganisation.
        :rtype: list[WSDocument]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """
        Sets the documents of this WSExternalOrganisation.

        :param documents: The documents of this WSExternalOrganisation.
        :type: list[WSDocument]
        """

        self._documents = documents

    @property
    def links(self):
        """
        Gets the links of this WSExternalOrganisation.

        :return: The links of this WSExternalOrganisation.
        :rtype: list[WSLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this WSExternalOrganisation.

        :param links: The links of this WSExternalOrganisation.
        :type: list[WSLink]
        """

        self._links = links

    @property
    def keyword_groups(self):
        """
        Gets the keyword_groups of this WSExternalOrganisation.

        :return: The keyword_groups of this WSExternalOrganisation.
        :rtype: list[WSKeywordGroup]
        """
        return self._keyword_groups

    @keyword_groups.setter
    def keyword_groups(self, keyword_groups):
        """
        Sets the keyword_groups of this WSExternalOrganisation.

        :param keyword_groups: The keyword_groups of this WSExternalOrganisation.
        :type: list[WSKeywordGroup]
        """

        self._keyword_groups = keyword_groups

    @property
    def note(self):
        """
        Gets the note of this WSExternalOrganisation.

        :return: The note of this WSExternalOrganisation.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """
        Sets the note of this WSExternalOrganisation.

        :param note: The note of this WSExternalOrganisation.
        :type: str
        """

        self._note = note

    @property
    def visibilities(self):
        """
        Gets the visibilities of this WSExternalOrganisation.

        :return: The visibilities of this WSExternalOrganisation.
        :rtype: list[WSVisibility]
        """
        return self._visibilities

    @visibilities.setter
    def visibilities(self, visibilities):
        """
        Sets the visibilities of this WSExternalOrganisation.

        :param visibilities: The visibilities of this WSExternalOrganisation.
        :type: list[WSVisibility]
        """

        self._visibilities = visibilities

    @property
    def workflows(self):
        """
        Gets the workflows of this WSExternalOrganisation.

        :return: The workflows of this WSExternalOrganisation.
        :rtype: list[WSWorkflow]
        """
        return self._workflows

    @workflows.setter
    def workflows(self, workflows):
        """
        Sets the workflows of this WSExternalOrganisation.

        :param workflows: The workflows of this WSExternalOrganisation.
        :type: list[WSWorkflow]
        """

        self._workflows = workflows

    @property
    def externalable_info(self):
        """
        Gets the externalable_info of this WSExternalOrganisation.

        :return: The externalable_info of this WSExternalOrganisation.
        :rtype: WSExternalableInformation
        """
        return self._externalable_info

    @externalable_info.setter
    def externalable_info(self, externalable_info):
        """
        Sets the externalable_info of this WSExternalOrganisation.

        :param externalable_info: The externalable_info of this WSExternalOrganisation.
        :type: WSExternalableInformation
        """

        self._externalable_info = externalable_info

    @property
    def info(self):
        """
        Gets the info of this WSExternalOrganisation.

        :return: The info of this WSExternalOrganisation.
        :rtype: WSContentInformation
        """
        return self._info

    @info.setter
    def info(self, info):
        """
        Sets the info of this WSExternalOrganisation.

        :param info: The info of this WSExternalOrganisation.
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
        if not isinstance(other, WSExternalOrganisation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
