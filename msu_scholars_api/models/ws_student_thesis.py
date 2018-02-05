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


class WSStudentThesis(object):
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
        'types': 'list[WSClassification]',
        'languages': 'list[WSClassification]',
        'title': 'str',
        'sub_title': 'str',
        'translated_titles': 'list[WSLocalizedString]',
        'translated_sub_titles': 'list[WSLocalizedString]',
        'abstracts': 'list[WSLocalizedString]',
        'person_associations': 'list[WSClassifiedAuthorAssociation]',
        'organisations': 'list[WSOrganisationRef]',
        'external_organisations': 'list[WSExternalOrganisationRef]',
        'managing_organisational_unit': 'WSOrganisationRef',
        'supervisors': 'list[WSClassifiedInternalExternalPersonAssociation]',
        'award_date': 'WSCompoundDate',
        'awarding_institutions': 'list[WSInternalExternalOrganisationAssociation]',
        'sponsors': 'list[WSExternalOrganisationRef]',
        'keyword_groups': 'list[WSKeywordGroup]',
        'documents': 'list[WSStudentThesisDocument]',
        'links': 'list[WSLink]',
        'bibliographical_notes': 'list[WSLocalizedString]',
        'related_research_outputs': 'list[WSResearchOutputRef]',
        'related_activities': 'list[WSActivityRef]',
        'related_press_media': 'list[WSPressMediaRef]',
        'related_impacts': 'list[WSImpactRef]',
        'related_projects': 'list[WSUPMProjectRef]',
        'related_data_sets': 'list[WSDataSetRef]',
        'related_prizes': 'list[WSPrizeRef]',
        'workflows': 'list[WSWorkflow]',
        'confidential': 'bool',
        'visibilities': 'list[WSVisibility]',
        'info': 'WSContentInformation',
        'externalable_info': 'WSExternalableInformation'
    }

    attribute_map = {
        'uuid': 'uuid',
        'html_renderings': 'htmlRenderings',
        'types': 'types',
        'languages': 'languages',
        'title': 'title',
        'sub_title': 'subTitle',
        'translated_titles': 'translatedTitles',
        'translated_sub_titles': 'translatedSubTitles',
        'abstracts': 'abstracts',
        'person_associations': 'personAssociations',
        'organisations': 'organisations',
        'external_organisations': 'externalOrganisations',
        'managing_organisational_unit': 'managingOrganisationalUnit',
        'supervisors': 'supervisors',
        'award_date': 'awardDate',
        'awarding_institutions': 'awardingInstitutions',
        'sponsors': 'sponsors',
        'keyword_groups': 'keywordGroups',
        'documents': 'documents',
        'links': 'links',
        'bibliographical_notes': 'bibliographicalNotes',
        'related_research_outputs': 'relatedResearchOutputs',
        'related_activities': 'relatedActivities',
        'related_press_media': 'relatedPressMedia',
        'related_impacts': 'relatedImpacts',
        'related_projects': 'relatedProjects',
        'related_data_sets': 'relatedDataSets',
        'related_prizes': 'relatedPrizes',
        'workflows': 'workflows',
        'confidential': 'confidential',
        'visibilities': 'visibilities',
        'info': 'info',
        'externalable_info': 'externalableInfo'
    }

    def __init__(self, uuid=None, html_renderings=None, types=None, languages=None, title=None, sub_title=None, translated_titles=None, translated_sub_titles=None, abstracts=None, person_associations=None, organisations=None, external_organisations=None, managing_organisational_unit=None, supervisors=None, award_date=None, awarding_institutions=None, sponsors=None, keyword_groups=None, documents=None, links=None, bibliographical_notes=None, related_research_outputs=None, related_activities=None, related_press_media=None, related_impacts=None, related_projects=None, related_data_sets=None, related_prizes=None, workflows=None, confidential=False, visibilities=None, info=None, externalable_info=None):
        """
        WSStudentThesis - a model defined in Swagger
        """

        self._uuid = None
        self._html_renderings = None
        self._types = None
        self._languages = None
        self._title = None
        self._sub_title = None
        self._translated_titles = None
        self._translated_sub_titles = None
        self._abstracts = None
        self._person_associations = None
        self._organisations = None
        self._external_organisations = None
        self._managing_organisational_unit = None
        self._supervisors = None
        self._award_date = None
        self._awarding_institutions = None
        self._sponsors = None
        self._keyword_groups = None
        self._documents = None
        self._links = None
        self._bibliographical_notes = None
        self._related_research_outputs = None
        self._related_activities = None
        self._related_press_media = None
        self._related_impacts = None
        self._related_projects = None
        self._related_data_sets = None
        self._related_prizes = None
        self._workflows = None
        self._confidential = None
        self._visibilities = None
        self._info = None
        self._externalable_info = None

        if uuid is not None:
          self.uuid = uuid
        if html_renderings is not None:
          self.html_renderings = html_renderings
        if types is not None:
          self.types = types
        if languages is not None:
          self.languages = languages
        if title is not None:
          self.title = title
        if sub_title is not None:
          self.sub_title = sub_title
        if translated_titles is not None:
          self.translated_titles = translated_titles
        if translated_sub_titles is not None:
          self.translated_sub_titles = translated_sub_titles
        if abstracts is not None:
          self.abstracts = abstracts
        if person_associations is not None:
          self.person_associations = person_associations
        if organisations is not None:
          self.organisations = organisations
        if external_organisations is not None:
          self.external_organisations = external_organisations
        if managing_organisational_unit is not None:
          self.managing_organisational_unit = managing_organisational_unit
        if supervisors is not None:
          self.supervisors = supervisors
        if award_date is not None:
          self.award_date = award_date
        if awarding_institutions is not None:
          self.awarding_institutions = awarding_institutions
        if sponsors is not None:
          self.sponsors = sponsors
        if keyword_groups is not None:
          self.keyword_groups = keyword_groups
        if documents is not None:
          self.documents = documents
        if links is not None:
          self.links = links
        if bibliographical_notes is not None:
          self.bibliographical_notes = bibliographical_notes
        if related_research_outputs is not None:
          self.related_research_outputs = related_research_outputs
        if related_activities is not None:
          self.related_activities = related_activities
        if related_press_media is not None:
          self.related_press_media = related_press_media
        if related_impacts is not None:
          self.related_impacts = related_impacts
        if related_projects is not None:
          self.related_projects = related_projects
        if related_data_sets is not None:
          self.related_data_sets = related_data_sets
        if related_prizes is not None:
          self.related_prizes = related_prizes
        if workflows is not None:
          self.workflows = workflows
        if confidential is not None:
          self.confidential = confidential
        if visibilities is not None:
          self.visibilities = visibilities
        if info is not None:
          self.info = info
        if externalable_info is not None:
          self.externalable_info = externalable_info

    @property
    def uuid(self):
        """
        Gets the uuid of this WSStudentThesis.

        :return: The uuid of this WSStudentThesis.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this WSStudentThesis.

        :param uuid: The uuid of this WSStudentThesis.
        :type: str
        """

        self._uuid = uuid

    @property
    def html_renderings(self):
        """
        Gets the html_renderings of this WSStudentThesis.

        :return: The html_renderings of this WSStudentThesis.
        :rtype: list[WSHtmlRendering]
        """
        return self._html_renderings

    @html_renderings.setter
    def html_renderings(self, html_renderings):
        """
        Sets the html_renderings of this WSStudentThesis.

        :param html_renderings: The html_renderings of this WSStudentThesis.
        :type: list[WSHtmlRendering]
        """

        self._html_renderings = html_renderings

    @property
    def types(self):
        """
        Gets the types of this WSStudentThesis.

        :return: The types of this WSStudentThesis.
        :rtype: list[WSClassification]
        """
        return self._types

    @types.setter
    def types(self, types):
        """
        Sets the types of this WSStudentThesis.

        :param types: The types of this WSStudentThesis.
        :type: list[WSClassification]
        """

        self._types = types

    @property
    def languages(self):
        """
        Gets the languages of this WSStudentThesis.

        :return: The languages of this WSStudentThesis.
        :rtype: list[WSClassification]
        """
        return self._languages

    @languages.setter
    def languages(self, languages):
        """
        Sets the languages of this WSStudentThesis.

        :param languages: The languages of this WSStudentThesis.
        :type: list[WSClassification]
        """

        self._languages = languages

    @property
    def title(self):
        """
        Gets the title of this WSStudentThesis.

        :return: The title of this WSStudentThesis.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this WSStudentThesis.

        :param title: The title of this WSStudentThesis.
        :type: str
        """

        self._title = title

    @property
    def sub_title(self):
        """
        Gets the sub_title of this WSStudentThesis.

        :return: The sub_title of this WSStudentThesis.
        :rtype: str
        """
        return self._sub_title

    @sub_title.setter
    def sub_title(self, sub_title):
        """
        Sets the sub_title of this WSStudentThesis.

        :param sub_title: The sub_title of this WSStudentThesis.
        :type: str
        """

        self._sub_title = sub_title

    @property
    def translated_titles(self):
        """
        Gets the translated_titles of this WSStudentThesis.

        :return: The translated_titles of this WSStudentThesis.
        :rtype: list[WSLocalizedString]
        """
        return self._translated_titles

    @translated_titles.setter
    def translated_titles(self, translated_titles):
        """
        Sets the translated_titles of this WSStudentThesis.

        :param translated_titles: The translated_titles of this WSStudentThesis.
        :type: list[WSLocalizedString]
        """

        self._translated_titles = translated_titles

    @property
    def translated_sub_titles(self):
        """
        Gets the translated_sub_titles of this WSStudentThesis.

        :return: The translated_sub_titles of this WSStudentThesis.
        :rtype: list[WSLocalizedString]
        """
        return self._translated_sub_titles

    @translated_sub_titles.setter
    def translated_sub_titles(self, translated_sub_titles):
        """
        Sets the translated_sub_titles of this WSStudentThesis.

        :param translated_sub_titles: The translated_sub_titles of this WSStudentThesis.
        :type: list[WSLocalizedString]
        """

        self._translated_sub_titles = translated_sub_titles

    @property
    def abstracts(self):
        """
        Gets the abstracts of this WSStudentThesis.

        :return: The abstracts of this WSStudentThesis.
        :rtype: list[WSLocalizedString]
        """
        return self._abstracts

    @abstracts.setter
    def abstracts(self, abstracts):
        """
        Sets the abstracts of this WSStudentThesis.

        :param abstracts: The abstracts of this WSStudentThesis.
        :type: list[WSLocalizedString]
        """

        self._abstracts = abstracts

    @property
    def person_associations(self):
        """
        Gets the person_associations of this WSStudentThesis.

        :return: The person_associations of this WSStudentThesis.
        :rtype: list[WSClassifiedAuthorAssociation]
        """
        return self._person_associations

    @person_associations.setter
    def person_associations(self, person_associations):
        """
        Sets the person_associations of this WSStudentThesis.

        :param person_associations: The person_associations of this WSStudentThesis.
        :type: list[WSClassifiedAuthorAssociation]
        """

        self._person_associations = person_associations

    @property
    def organisations(self):
        """
        Gets the organisations of this WSStudentThesis.

        :return: The organisations of this WSStudentThesis.
        :rtype: list[WSOrganisationRef]
        """
        return self._organisations

    @organisations.setter
    def organisations(self, organisations):
        """
        Sets the organisations of this WSStudentThesis.

        :param organisations: The organisations of this WSStudentThesis.
        :type: list[WSOrganisationRef]
        """

        self._organisations = organisations

    @property
    def external_organisations(self):
        """
        Gets the external_organisations of this WSStudentThesis.

        :return: The external_organisations of this WSStudentThesis.
        :rtype: list[WSExternalOrganisationRef]
        """
        return self._external_organisations

    @external_organisations.setter
    def external_organisations(self, external_organisations):
        """
        Sets the external_organisations of this WSStudentThesis.

        :param external_organisations: The external_organisations of this WSStudentThesis.
        :type: list[WSExternalOrganisationRef]
        """

        self._external_organisations = external_organisations

    @property
    def managing_organisational_unit(self):
        """
        Gets the managing_organisational_unit of this WSStudentThesis.

        :return: The managing_organisational_unit of this WSStudentThesis.
        :rtype: WSOrganisationRef
        """
        return self._managing_organisational_unit

    @managing_organisational_unit.setter
    def managing_organisational_unit(self, managing_organisational_unit):
        """
        Sets the managing_organisational_unit of this WSStudentThesis.

        :param managing_organisational_unit: The managing_organisational_unit of this WSStudentThesis.
        :type: WSOrganisationRef
        """

        self._managing_organisational_unit = managing_organisational_unit

    @property
    def supervisors(self):
        """
        Gets the supervisors of this WSStudentThesis.

        :return: The supervisors of this WSStudentThesis.
        :rtype: list[WSClassifiedInternalExternalPersonAssociation]
        """
        return self._supervisors

    @supervisors.setter
    def supervisors(self, supervisors):
        """
        Sets the supervisors of this WSStudentThesis.

        :param supervisors: The supervisors of this WSStudentThesis.
        :type: list[WSClassifiedInternalExternalPersonAssociation]
        """

        self._supervisors = supervisors

    @property
    def award_date(self):
        """
        Gets the award_date of this WSStudentThesis.

        :return: The award_date of this WSStudentThesis.
        :rtype: WSCompoundDate
        """
        return self._award_date

    @award_date.setter
    def award_date(self, award_date):
        """
        Sets the award_date of this WSStudentThesis.

        :param award_date: The award_date of this WSStudentThesis.
        :type: WSCompoundDate
        """

        self._award_date = award_date

    @property
    def awarding_institutions(self):
        """
        Gets the awarding_institutions of this WSStudentThesis.

        :return: The awarding_institutions of this WSStudentThesis.
        :rtype: list[WSInternalExternalOrganisationAssociation]
        """
        return self._awarding_institutions

    @awarding_institutions.setter
    def awarding_institutions(self, awarding_institutions):
        """
        Sets the awarding_institutions of this WSStudentThesis.

        :param awarding_institutions: The awarding_institutions of this WSStudentThesis.
        :type: list[WSInternalExternalOrganisationAssociation]
        """

        self._awarding_institutions = awarding_institutions

    @property
    def sponsors(self):
        """
        Gets the sponsors of this WSStudentThesis.

        :return: The sponsors of this WSStudentThesis.
        :rtype: list[WSExternalOrganisationRef]
        """
        return self._sponsors

    @sponsors.setter
    def sponsors(self, sponsors):
        """
        Sets the sponsors of this WSStudentThesis.

        :param sponsors: The sponsors of this WSStudentThesis.
        :type: list[WSExternalOrganisationRef]
        """

        self._sponsors = sponsors

    @property
    def keyword_groups(self):
        """
        Gets the keyword_groups of this WSStudentThesis.

        :return: The keyword_groups of this WSStudentThesis.
        :rtype: list[WSKeywordGroup]
        """
        return self._keyword_groups

    @keyword_groups.setter
    def keyword_groups(self, keyword_groups):
        """
        Sets the keyword_groups of this WSStudentThesis.

        :param keyword_groups: The keyword_groups of this WSStudentThesis.
        :type: list[WSKeywordGroup]
        """

        self._keyword_groups = keyword_groups

    @property
    def documents(self):
        """
        Gets the documents of this WSStudentThesis.

        :return: The documents of this WSStudentThesis.
        :rtype: list[WSStudentThesisDocument]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """
        Sets the documents of this WSStudentThesis.

        :param documents: The documents of this WSStudentThesis.
        :type: list[WSStudentThesisDocument]
        """

        self._documents = documents

    @property
    def links(self):
        """
        Gets the links of this WSStudentThesis.

        :return: The links of this WSStudentThesis.
        :rtype: list[WSLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this WSStudentThesis.

        :param links: The links of this WSStudentThesis.
        :type: list[WSLink]
        """

        self._links = links

    @property
    def bibliographical_notes(self):
        """
        Gets the bibliographical_notes of this WSStudentThesis.

        :return: The bibliographical_notes of this WSStudentThesis.
        :rtype: list[WSLocalizedString]
        """
        return self._bibliographical_notes

    @bibliographical_notes.setter
    def bibliographical_notes(self, bibliographical_notes):
        """
        Sets the bibliographical_notes of this WSStudentThesis.

        :param bibliographical_notes: The bibliographical_notes of this WSStudentThesis.
        :type: list[WSLocalizedString]
        """

        self._bibliographical_notes = bibliographical_notes

    @property
    def related_research_outputs(self):
        """
        Gets the related_research_outputs of this WSStudentThesis.

        :return: The related_research_outputs of this WSStudentThesis.
        :rtype: list[WSResearchOutputRef]
        """
        return self._related_research_outputs

    @related_research_outputs.setter
    def related_research_outputs(self, related_research_outputs):
        """
        Sets the related_research_outputs of this WSStudentThesis.

        :param related_research_outputs: The related_research_outputs of this WSStudentThesis.
        :type: list[WSResearchOutputRef]
        """

        self._related_research_outputs = related_research_outputs

    @property
    def related_activities(self):
        """
        Gets the related_activities of this WSStudentThesis.
        Only available when the Activity module is enabled

        :return: The related_activities of this WSStudentThesis.
        :rtype: list[WSActivityRef]
        """
        return self._related_activities

    @related_activities.setter
    def related_activities(self, related_activities):
        """
        Sets the related_activities of this WSStudentThesis.
        Only available when the Activity module is enabled

        :param related_activities: The related_activities of this WSStudentThesis.
        :type: list[WSActivityRef]
        """

        self._related_activities = related_activities

    @property
    def related_press_media(self):
        """
        Gets the related_press_media of this WSStudentThesis.
        Only available when the Press / Media module is enabled

        :return: The related_press_media of this WSStudentThesis.
        :rtype: list[WSPressMediaRef]
        """
        return self._related_press_media

    @related_press_media.setter
    def related_press_media(self, related_press_media):
        """
        Sets the related_press_media of this WSStudentThesis.
        Only available when the Press / Media module is enabled

        :param related_press_media: The related_press_media of this WSStudentThesis.
        :type: list[WSPressMediaRef]
        """

        self._related_press_media = related_press_media

    @property
    def related_impacts(self):
        """
        Gets the related_impacts of this WSStudentThesis.
        Only available when the Impact module is enabled

        :return: The related_impacts of this WSStudentThesis.
        :rtype: list[WSImpactRef]
        """
        return self._related_impacts

    @related_impacts.setter
    def related_impacts(self, related_impacts):
        """
        Sets the related_impacts of this WSStudentThesis.
        Only available when the Impact module is enabled

        :param related_impacts: The related_impacts of this WSStudentThesis.
        :type: list[WSImpactRef]
        """

        self._related_impacts = related_impacts

    @property
    def related_projects(self):
        """
        Gets the related_projects of this WSStudentThesis.
        Only available when the Unified Project Model module is enabled

        :return: The related_projects of this WSStudentThesis.
        :rtype: list[WSUPMProjectRef]
        """
        return self._related_projects

    @related_projects.setter
    def related_projects(self, related_projects):
        """
        Sets the related_projects of this WSStudentThesis.
        Only available when the Unified Project Model module is enabled

        :param related_projects: The related_projects of this WSStudentThesis.
        :type: list[WSUPMProjectRef]
        """

        self._related_projects = related_projects

    @property
    def related_data_sets(self):
        """
        Gets the related_data_sets of this WSStudentThesis.
        Only available when the DataSet module is enabled

        :return: The related_data_sets of this WSStudentThesis.
        :rtype: list[WSDataSetRef]
        """
        return self._related_data_sets

    @related_data_sets.setter
    def related_data_sets(self, related_data_sets):
        """
        Sets the related_data_sets of this WSStudentThesis.
        Only available when the DataSet module is enabled

        :param related_data_sets: The related_data_sets of this WSStudentThesis.
        :type: list[WSDataSetRef]
        """

        self._related_data_sets = related_data_sets

    @property
    def related_prizes(self):
        """
        Gets the related_prizes of this WSStudentThesis.
        Only available when the Prize module is enabled

        :return: The related_prizes of this WSStudentThesis.
        :rtype: list[WSPrizeRef]
        """
        return self._related_prizes

    @related_prizes.setter
    def related_prizes(self, related_prizes):
        """
        Sets the related_prizes of this WSStudentThesis.
        Only available when the Prize module is enabled

        :param related_prizes: The related_prizes of this WSStudentThesis.
        :type: list[WSPrizeRef]
        """

        self._related_prizes = related_prizes

    @property
    def workflows(self):
        """
        Gets the workflows of this WSStudentThesis.

        :return: The workflows of this WSStudentThesis.
        :rtype: list[WSWorkflow]
        """
        return self._workflows

    @workflows.setter
    def workflows(self, workflows):
        """
        Sets the workflows of this WSStudentThesis.

        :param workflows: The workflows of this WSStudentThesis.
        :type: list[WSWorkflow]
        """

        self._workflows = workflows

    @property
    def confidential(self):
        """
        Gets the confidential of this WSStudentThesis.

        :return: The confidential of this WSStudentThesis.
        :rtype: bool
        """
        return self._confidential

    @confidential.setter
    def confidential(self, confidential):
        """
        Sets the confidential of this WSStudentThesis.

        :param confidential: The confidential of this WSStudentThesis.
        :type: bool
        """

        self._confidential = confidential

    @property
    def visibilities(self):
        """
        Gets the visibilities of this WSStudentThesis.

        :return: The visibilities of this WSStudentThesis.
        :rtype: list[WSVisibility]
        """
        return self._visibilities

    @visibilities.setter
    def visibilities(self, visibilities):
        """
        Sets the visibilities of this WSStudentThesis.

        :param visibilities: The visibilities of this WSStudentThesis.
        :type: list[WSVisibility]
        """

        self._visibilities = visibilities

    @property
    def info(self):
        """
        Gets the info of this WSStudentThesis.

        :return: The info of this WSStudentThesis.
        :rtype: WSContentInformation
        """
        return self._info

    @info.setter
    def info(self, info):
        """
        Sets the info of this WSStudentThesis.

        :param info: The info of this WSStudentThesis.
        :type: WSContentInformation
        """

        self._info = info

    @property
    def externalable_info(self):
        """
        Gets the externalable_info of this WSStudentThesis.

        :return: The externalable_info of this WSStudentThesis.
        :rtype: WSExternalableInformation
        """
        return self._externalable_info

    @externalable_info.setter
    def externalable_info(self, externalable_info):
        """
        Sets the externalable_info of this WSStudentThesis.

        :param externalable_info: The externalable_info of this WSStudentThesis.
        :type: WSExternalableInformation
        """

        self._externalable_info = externalable_info

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
        if not isinstance(other, WSStudentThesis):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other