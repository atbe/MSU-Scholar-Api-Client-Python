# WSUPMProject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**html_renderings** | [**list[WSHtmlRendering]**](WSHtmlRendering.md) |  | [optional] 
**titles** | [**list[WSLocalizedString]**](WSLocalizedString.md) |  | [optional] 
**types** | [**list[WSClassification]**](WSClassification.md) |  | [optional] 
**nature_types** | [**list[WSClassification]**](WSClassification.md) |  | [optional] 
**statuses** | [**list[WSUPMProjectStatus]**](WSUPMProjectStatus.md) |  | [optional] 
**short_titles** | [**list[WSLocalizedString]**](WSLocalizedString.md) |  | [optional] 
**acronym** | **str** |  | [optional] 
**descriptions** | [**list[WSClassifiedLocalizedValue]**](WSClassifiedLocalizedValue.md) |  | [optional] 
**classified_sources** | [**list[WSClassifiedValue]**](WSClassifiedValue.md) |  | [optional] 
**participants** | [**list[WSClassifiedParticipantAssociation]**](WSClassifiedParticipantAssociation.md) |  | [optional] 
**organisations** | [**list[WSOrganisationRef]**](WSOrganisationRef.md) |  | [optional] 
**external_organisations** | [**list[WSExternalOrganisationRef]**](WSExternalOrganisationRef.md) |  | [optional] 
**managing_organisational_unit** | [**WSOrganisationRef**](WSOrganisationRef.md) |  | [optional] 
**collaborative** | **bool** |  | [optional] [default to False]
**collaborators** | [**list[WSCollaboratorAssociation]**](WSCollaboratorAssociation.md) |  | [optional] 
**total_academic_ownership_percentage** | **float** |  | [optional] 
**period** | [**WSDateRange**](WSDateRange.md) |  | [optional] 
**curtailed** | **bool** |  | [optional] [default to False]
**curtail_date** | **datetime** |  | [optional] 
**curtail_reason** | **str** |  | [optional] 
**documents** | [**list[WSDocument]**](WSDocument.md) |  | [optional] 
**links** | [**list[WSLink]**](WSLink.md) |  | [optional] 
**related_applications** | [**list[WSApplicationRef]**](WSApplicationRef.md) |  | [optional] 
**related_awards** | [**list[WSAwardRef]**](WSAwardRef.md) |  | [optional] 
**related_projects** | [**list[WSUPMProjectAssociation]**](WSUPMProjectAssociation.md) |  | [optional] 
**related_press_media** | [**list[WSPressMediaRef]**](WSPressMediaRef.md) | Only available when the Press / Media module is enabled | [optional] 
**related_impacts** | [**list[WSImpactRef]**](WSImpactRef.md) | Only available when the Impact module is enabled | [optional] 
**related_activities** | [**list[WSActivityRef]**](WSActivityRef.md) | Only available when the Activity module is enabled | [optional] 
**related_prizes** | [**list[WSPrizeRef]**](WSPrizeRef.md) | Only available when the Prize module is enabled | [optional] 
**related_data_sets** | [**list[WSDataSetRef]**](WSDataSetRef.md) | Only available when the DataSet module is enabled | [optional] 
**related_research_outputs** | [**list[WSResearchOutputRef]**](WSResearchOutputRef.md) |  | [optional] 
**related_student_thesis** | [**list[WSStudentThesisRef]**](WSStudentThesisRef.md) | Only available when the Student Thesis module is enabled | [optional] 
**keyword_groups** | [**list[WSKeywordGroup]**](WSKeywordGroup.md) |  | [optional] 
**field_of_research_associations** | [**list[WSERA2015FieldOfResearchAssociation]**](WSERA2015FieldOfResearchAssociation.md) | Only available when the ERA module is enabled | [optional] 
**visibilities** | [**list[WSVisibility]**](WSVisibility.md) |  | [optional] 
**confidential** | **bool** |  | [optional] [default to False]
**workflows** | [**list[WSWorkflow]**](WSWorkflow.md) |  | [optional] 
**externalable_info** | [**WSExternalableInformation**](WSExternalableInformation.md) |  | [optional] 
**info** | [**WSContentInformation**](WSContentInformation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


