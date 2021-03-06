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


class WSPrize(object):
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
        'categories': 'list[WSClassification]',
        'descriptions': 'list[WSClassifiedLocalizedValue]',
        'award_date': 'WSCompoundDate',
        'degree_of_recognitions': 'list[WSClassification]',
        'organisations': 'list[WSOrganisationRef]',
        'external_organisations': 'list[WSExternalOrganisationRef]',
        'granting_organisations': 'list[WSInternalExternalOrganisationAssociation]',
        'event': 'WSEventRef',
        'classified_sources': 'list[WSClassifiedValue]',
        'receivers_of_prize': 'list[WSClassifiedPersonAssociation]',
        'managing_organisational_unit': 'WSOrganisationRef',
        'documents': 'list[WSDocument]',
        'links': 'list[WSLink]',
        'related_prizes': 'list[WSPrizeRef]',
        'related_research_outputs': 'list[WSResearchOutputRef]',
        'related_activities': 'list[WSActivityRef]',
        'related_press_media': 'list[WSPressMediaRef]',
        'related_projects': 'list[WSUPMProjectRef]',
        'related_impacts': 'list[WSImpactRef]',
        'related_data_sets': 'list[WSDataSetRef]',
        'related_student_thesis': 'list[WSStudentThesisRef]',
        'keyword_groups': 'list[WSKeywordGroup]',
        'visibilities': 'list[WSVisibility]',
        'workflows': 'list[WSWorkflow]',
        'externalable_info': 'WSExternalableInformation',
        'info': 'WSContentInformation'
    }

    attribute_map = {
        'uuid': 'uuid',
        'html_renderings': 'htmlRenderings',
        'titles': 'titles',
        'types': 'types',
        'categories': 'categories',
        'descriptions': 'descriptions',
        'award_date': 'awardDate',
        'degree_of_recognitions': 'degreeOfRecognitions',
        'organisations': 'organisations',
        'external_organisations': 'externalOrganisations',
        'granting_organisations': 'grantingOrganisations',
        'event': 'event',
        'classified_sources': 'classifiedSources',
        'receivers_of_prize': 'receiversOfPrize',
        'managing_organisational_unit': 'managingOrganisationalUnit',
        'documents': 'documents',
        'links': 'links',
        'related_prizes': 'relatedPrizes',
        'related_research_outputs': 'relatedResearchOutputs',
        'related_activities': 'relatedActivities',
        'related_press_media': 'relatedPressMedia',
        'related_projects': 'relatedProjects',
        'related_impacts': 'relatedImpacts',
        'related_data_sets': 'relatedDataSets',
        'related_student_thesis': 'relatedStudentThesis',
        'keyword_groups': 'keywordGroups',
        'visibilities': 'visibilities',
        'workflows': 'workflows',
        'externalable_info': 'externalableInfo',
        'info': 'info'
    }

    def __init__(self, uuid=None, html_renderings=None, titles=None, types=None, categories=None, descriptions=None, award_date=None, degree_of_recognitions=None, organisations=None, external_organisations=None, granting_organisations=None, event=None, classified_sources=None, receivers_of_prize=None, managing_organisational_unit=None, documents=None, links=None, related_prizes=None, related_research_outputs=None, related_activities=None, related_press_media=None, related_projects=None, related_impacts=None, related_data_sets=None, related_student_thesis=None, keyword_groups=None, visibilities=None, workflows=None, externalable_info=None, info=None):
        """
        WSPrize - a model defined in Swagger
        """

        self._uuid = None
        self._html_renderings = None
        self._titles = None
        self._types = None
        self._categories = None
        self._descriptions = None
        self._award_date = None
        self._degree_of_recognitions = None
        self._organisations = None
        self._external_organisations = None
        self._granting_organisations = None
        self._event = None
        self._classified_sources = None
        self._receivers_of_prize = None
        self._managing_organisational_unit = None
        self._documents = None
        self._links = None
        self._related_prizes = None
        self._related_research_outputs = None
        self._related_activities = None
        self._related_press_media = None
        self._related_projects = None
        self._related_impacts = None
        self._related_data_sets = None
        self._related_student_thesis = None
        self._keyword_groups = None
        self._visibilities = None
        self._workflows = None
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
        if categories is not None:
          self.categories = categories
        if descriptions is not None:
          self.descriptions = descriptions
        if award_date is not None:
          self.award_date = award_date
        if degree_of_recognitions is not None:
          self.degree_of_recognitions = degree_of_recognitions
        if organisations is not None:
          self.organisations = organisations
        if external_organisations is not None:
          self.external_organisations = external_organisations
        if granting_organisations is not None:
          self.granting_organisations = granting_organisations
        if event is not None:
          self.event = event
        if classified_sources is not None:
          self.classified_sources = classified_sources
        if receivers_of_prize is not None:
          self.receivers_of_prize = receivers_of_prize
        if managing_organisational_unit is not None:
          self.managing_organisational_unit = managing_organisational_unit
        if documents is not None:
          self.documents = documents
        if links is not None:
          self.links = links
        if related_prizes is not None:
          self.related_prizes = related_prizes
        if related_research_outputs is not None:
          self.related_research_outputs = related_research_outputs
        if related_activities is not None:
          self.related_activities = related_activities
        if related_press_media is not None:
          self.related_press_media = related_press_media
        if related_projects is not None:
          self.related_projects = related_projects
        if related_impacts is not None:
          self.related_impacts = related_impacts
        if related_data_sets is not None:
          self.related_data_sets = related_data_sets
        if related_student_thesis is not None:
          self.related_student_thesis = related_student_thesis
        if keyword_groups is not None:
          self.keyword_groups = keyword_groups
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
        Gets the uuid of this WSPrize.

        :return: The uuid of this WSPrize.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this WSPrize.

        :param uuid: The uuid of this WSPrize.
        :type: str
        """

        self._uuid = uuid

    @property
    def html_renderings(self):
        """
        Gets the html_renderings of this WSPrize.

        :return: The html_renderings of this WSPrize.
        :rtype: list[WSHtmlRendering]
        """
        return self._html_renderings

    @html_renderings.setter
    def html_renderings(self, html_renderings):
        """
        Sets the html_renderings of this WSPrize.

        :param html_renderings: The html_renderings of this WSPrize.
        :type: list[WSHtmlRendering]
        """

        self._html_renderings = html_renderings

    @property
    def titles(self):
        """
        Gets the titles of this WSPrize.

        :return: The titles of this WSPrize.
        :rtype: list[WSLocalizedString]
        """
        return self._titles

    @titles.setter
    def titles(self, titles):
        """
        Sets the titles of this WSPrize.

        :param titles: The titles of this WSPrize.
        :type: list[WSLocalizedString]
        """

        self._titles = titles

    @property
    def types(self):
        """
        Gets the types of this WSPrize.

        :return: The types of this WSPrize.
        :rtype: list[WSClassification]
        """
        return self._types

    @types.setter
    def types(self, types):
        """
        Sets the types of this WSPrize.

        :param types: The types of this WSPrize.
        :type: list[WSClassification]
        """

        self._types = types

    @property
    def categories(self):
        """
        Gets the categories of this WSPrize.

        :return: The categories of this WSPrize.
        :rtype: list[WSClassification]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """
        Sets the categories of this WSPrize.

        :param categories: The categories of this WSPrize.
        :type: list[WSClassification]
        """

        self._categories = categories

    @property
    def descriptions(self):
        """
        Gets the descriptions of this WSPrize.

        :return: The descriptions of this WSPrize.
        :rtype: list[WSClassifiedLocalizedValue]
        """
        return self._descriptions

    @descriptions.setter
    def descriptions(self, descriptions):
        """
        Sets the descriptions of this WSPrize.

        :param descriptions: The descriptions of this WSPrize.
        :type: list[WSClassifiedLocalizedValue]
        """

        self._descriptions = descriptions

    @property
    def award_date(self):
        """
        Gets the award_date of this WSPrize.

        :return: The award_date of this WSPrize.
        :rtype: WSCompoundDate
        """
        return self._award_date

    @award_date.setter
    def award_date(self, award_date):
        """
        Sets the award_date of this WSPrize.

        :param award_date: The award_date of this WSPrize.
        :type: WSCompoundDate
        """

        self._award_date = award_date

    @property
    def degree_of_recognitions(self):
        """
        Gets the degree_of_recognitions of this WSPrize.

        :return: The degree_of_recognitions of this WSPrize.
        :rtype: list[WSClassification]
        """
        return self._degree_of_recognitions

    @degree_of_recognitions.setter
    def degree_of_recognitions(self, degree_of_recognitions):
        """
        Sets the degree_of_recognitions of this WSPrize.

        :param degree_of_recognitions: The degree_of_recognitions of this WSPrize.
        :type: list[WSClassification]
        """

        self._degree_of_recognitions = degree_of_recognitions

    @property
    def organisations(self):
        """
        Gets the organisations of this WSPrize.

        :return: The organisations of this WSPrize.
        :rtype: list[WSOrganisationRef]
        """
        return self._organisations

    @organisations.setter
    def organisations(self, organisations):
        """
        Sets the organisations of this WSPrize.

        :param organisations: The organisations of this WSPrize.
        :type: list[WSOrganisationRef]
        """

        self._organisations = organisations

    @property
    def external_organisations(self):
        """
        Gets the external_organisations of this WSPrize.

        :return: The external_organisations of this WSPrize.
        :rtype: list[WSExternalOrganisationRef]
        """
        return self._external_organisations

    @external_organisations.setter
    def external_organisations(self, external_organisations):
        """
        Sets the external_organisations of this WSPrize.

        :param external_organisations: The external_organisations of this WSPrize.
        :type: list[WSExternalOrganisationRef]
        """

        self._external_organisations = external_organisations

    @property
    def granting_organisations(self):
        """
        Gets the granting_organisations of this WSPrize.

        :return: The granting_organisations of this WSPrize.
        :rtype: list[WSInternalExternalOrganisationAssociation]
        """
        return self._granting_organisations

    @granting_organisations.setter
    def granting_organisations(self, granting_organisations):
        """
        Sets the granting_organisations of this WSPrize.

        :param granting_organisations: The granting_organisations of this WSPrize.
        :type: list[WSInternalExternalOrganisationAssociation]
        """

        self._granting_organisations = granting_organisations

    @property
    def event(self):
        """
        Gets the event of this WSPrize.

        :return: The event of this WSPrize.
        :rtype: WSEventRef
        """
        return self._event

    @event.setter
    def event(self, event):
        """
        Sets the event of this WSPrize.

        :param event: The event of this WSPrize.
        :type: WSEventRef
        """

        self._event = event

    @property
    def classified_sources(self):
        """
        Gets the classified_sources of this WSPrize.

        :return: The classified_sources of this WSPrize.
        :rtype: list[WSClassifiedValue]
        """
        return self._classified_sources

    @classified_sources.setter
    def classified_sources(self, classified_sources):
        """
        Sets the classified_sources of this WSPrize.

        :param classified_sources: The classified_sources of this WSPrize.
        :type: list[WSClassifiedValue]
        """

        self._classified_sources = classified_sources

    @property
    def receivers_of_prize(self):
        """
        Gets the receivers_of_prize of this WSPrize.

        :return: The receivers_of_prize of this WSPrize.
        :rtype: list[WSClassifiedPersonAssociation]
        """
        return self._receivers_of_prize

    @receivers_of_prize.setter
    def receivers_of_prize(self, receivers_of_prize):
        """
        Sets the receivers_of_prize of this WSPrize.

        :param receivers_of_prize: The receivers_of_prize of this WSPrize.
        :type: list[WSClassifiedPersonAssociation]
        """

        self._receivers_of_prize = receivers_of_prize

    @property
    def managing_organisational_unit(self):
        """
        Gets the managing_organisational_unit of this WSPrize.

        :return: The managing_organisational_unit of this WSPrize.
        :rtype: WSOrganisationRef
        """
        return self._managing_organisational_unit

    @managing_organisational_unit.setter
    def managing_organisational_unit(self, managing_organisational_unit):
        """
        Sets the managing_organisational_unit of this WSPrize.

        :param managing_organisational_unit: The managing_organisational_unit of this WSPrize.
        :type: WSOrganisationRef
        """

        self._managing_organisational_unit = managing_organisational_unit

    @property
    def documents(self):
        """
        Gets the documents of this WSPrize.

        :return: The documents of this WSPrize.
        :rtype: list[WSDocument]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """
        Sets the documents of this WSPrize.

        :param documents: The documents of this WSPrize.
        :type: list[WSDocument]
        """

        self._documents = documents

    @property
    def links(self):
        """
        Gets the links of this WSPrize.

        :return: The links of this WSPrize.
        :rtype: list[WSLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this WSPrize.

        :param links: The links of this WSPrize.
        :type: list[WSLink]
        """

        self._links = links

    @property
    def related_prizes(self):
        """
        Gets the related_prizes of this WSPrize.

        :return: The related_prizes of this WSPrize.
        :rtype: list[WSPrizeRef]
        """
        return self._related_prizes

    @related_prizes.setter
    def related_prizes(self, related_prizes):
        """
        Sets the related_prizes of this WSPrize.

        :param related_prizes: The related_prizes of this WSPrize.
        :type: list[WSPrizeRef]
        """

        self._related_prizes = related_prizes

    @property
    def related_research_outputs(self):
        """
        Gets the related_research_outputs of this WSPrize.

        :return: The related_research_outputs of this WSPrize.
        :rtype: list[WSResearchOutputRef]
        """
        return self._related_research_outputs

    @related_research_outputs.setter
    def related_research_outputs(self, related_research_outputs):
        """
        Sets the related_research_outputs of this WSPrize.

        :param related_research_outputs: The related_research_outputs of this WSPrize.
        :type: list[WSResearchOutputRef]
        """

        self._related_research_outputs = related_research_outputs

    @property
    def related_activities(self):
        """
        Gets the related_activities of this WSPrize.
        Only available when the Activity module is enabled

        :return: The related_activities of this WSPrize.
        :rtype: list[WSActivityRef]
        """
        return self._related_activities

    @related_activities.setter
    def related_activities(self, related_activities):
        """
        Sets the related_activities of this WSPrize.
        Only available when the Activity module is enabled

        :param related_activities: The related_activities of this WSPrize.
        :type: list[WSActivityRef]
        """

        self._related_activities = related_activities

    @property
    def related_press_media(self):
        """
        Gets the related_press_media of this WSPrize.
        Only available when the Press / Media module is enabled

        :return: The related_press_media of this WSPrize.
        :rtype: list[WSPressMediaRef]
        """
        return self._related_press_media

    @related_press_media.setter
    def related_press_media(self, related_press_media):
        """
        Sets the related_press_media of this WSPrize.
        Only available when the Press / Media module is enabled

        :param related_press_media: The related_press_media of this WSPrize.
        :type: list[WSPressMediaRef]
        """

        self._related_press_media = related_press_media

    @property
    def related_projects(self):
        """
        Gets the related_projects of this WSPrize.
        Only available when the Unified Project Model module is enabled

        :return: The related_projects of this WSPrize.
        :rtype: list[WSUPMProjectRef]
        """
        return self._related_projects

    @related_projects.setter
    def related_projects(self, related_projects):
        """
        Sets the related_projects of this WSPrize.
        Only available when the Unified Project Model module is enabled

        :param related_projects: The related_projects of this WSPrize.
        :type: list[WSUPMProjectRef]
        """

        self._related_projects = related_projects

    @property
    def related_impacts(self):
        """
        Gets the related_impacts of this WSPrize.
        Only available when the Impact module is enabled

        :return: The related_impacts of this WSPrize.
        :rtype: list[WSImpactRef]
        """
        return self._related_impacts

    @related_impacts.setter
    def related_impacts(self, related_impacts):
        """
        Sets the related_impacts of this WSPrize.
        Only available when the Impact module is enabled

        :param related_impacts: The related_impacts of this WSPrize.
        :type: list[WSImpactRef]
        """

        self._related_impacts = related_impacts

    @property
    def related_data_sets(self):
        """
        Gets the related_data_sets of this WSPrize.
        Only available when the DataSet module is enabled

        :return: The related_data_sets of this WSPrize.
        :rtype: list[WSDataSetRef]
        """
        return self._related_data_sets

    @related_data_sets.setter
    def related_data_sets(self, related_data_sets):
        """
        Sets the related_data_sets of this WSPrize.
        Only available when the DataSet module is enabled

        :param related_data_sets: The related_data_sets of this WSPrize.
        :type: list[WSDataSetRef]
        """

        self._related_data_sets = related_data_sets

    @property
    def related_student_thesis(self):
        """
        Gets the related_student_thesis of this WSPrize.
        Only available when the Student Thesis module is enabled

        :return: The related_student_thesis of this WSPrize.
        :rtype: list[WSStudentThesisRef]
        """
        return self._related_student_thesis

    @related_student_thesis.setter
    def related_student_thesis(self, related_student_thesis):
        """
        Sets the related_student_thesis of this WSPrize.
        Only available when the Student Thesis module is enabled

        :param related_student_thesis: The related_student_thesis of this WSPrize.
        :type: list[WSStudentThesisRef]
        """

        self._related_student_thesis = related_student_thesis

    @property
    def keyword_groups(self):
        """
        Gets the keyword_groups of this WSPrize.

        :return: The keyword_groups of this WSPrize.
        :rtype: list[WSKeywordGroup]
        """
        return self._keyword_groups

    @keyword_groups.setter
    def keyword_groups(self, keyword_groups):
        """
        Sets the keyword_groups of this WSPrize.

        :param keyword_groups: The keyword_groups of this WSPrize.
        :type: list[WSKeywordGroup]
        """

        self._keyword_groups = keyword_groups

    @property
    def visibilities(self):
        """
        Gets the visibilities of this WSPrize.

        :return: The visibilities of this WSPrize.
        :rtype: list[WSVisibility]
        """
        return self._visibilities

    @visibilities.setter
    def visibilities(self, visibilities):
        """
        Sets the visibilities of this WSPrize.

        :param visibilities: The visibilities of this WSPrize.
        :type: list[WSVisibility]
        """

        self._visibilities = visibilities

    @property
    def workflows(self):
        """
        Gets the workflows of this WSPrize.

        :return: The workflows of this WSPrize.
        :rtype: list[WSWorkflow]
        """
        return self._workflows

    @workflows.setter
    def workflows(self, workflows):
        """
        Sets the workflows of this WSPrize.

        :param workflows: The workflows of this WSPrize.
        :type: list[WSWorkflow]
        """

        self._workflows = workflows

    @property
    def externalable_info(self):
        """
        Gets the externalable_info of this WSPrize.

        :return: The externalable_info of this WSPrize.
        :rtype: WSExternalableInformation
        """
        return self._externalable_info

    @externalable_info.setter
    def externalable_info(self, externalable_info):
        """
        Sets the externalable_info of this WSPrize.

        :param externalable_info: The externalable_info of this WSPrize.
        :type: WSExternalableInformation
        """

        self._externalable_info = externalable_info

    @property
    def info(self):
        """
        Gets the info of this WSPrize.

        :return: The info of this WSPrize.
        :rtype: WSContentInformation
        """
        return self._info

    @info.setter
    def info(self, info):
        """
        Sets the info of this WSPrize.

        :param info: The info of this WSPrize.
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
        if not isinstance(other, WSPrize):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
