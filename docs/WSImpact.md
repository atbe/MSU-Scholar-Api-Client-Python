# WSImpact

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**html_renderings** | [**list[WSHtmlRendering]**](WSHtmlRendering.md) |  | [optional] 
**titles** | [**list[WSLocalizedString]**](WSLocalizedString.md) |  | [optional] 
**types** | [**list[WSClassification]**](WSClassification.md) |  | [optional] 
**statuses** | [**list[WSClassification]**](WSClassification.md) |  | [optional] 
**period** | [**WSCompoundDateRange**](WSCompoundDateRange.md) |  | [optional] 
**descriptions** | [**list[WSClassifiedLocalizedValue]**](WSClassifiedLocalizedValue.md) |  | [optional] 
**categories** | [**list[WSClassification]**](WSClassification.md) |  | [optional] 
**levels** | [**list[WSClassification]**](WSClassification.md) |  | [optional] 
**classified_sources** | [**list[WSClassifiedValue]**](WSClassifiedValue.md) |  | [optional] 
**participants** | [**list[WSImpactClassifiedParticipantAssociation]**](WSImpactClassifiedParticipantAssociation.md) |  | [optional] 
**organisations** | [**list[WSOrganisationRef]**](WSOrganisationRef.md) |  | [optional] 
**external_organisations** | [**list[WSExternalOrganisationRef]**](WSExternalOrganisationRef.md) |  | [optional] 
**evidence_list** | [**list[WSImpactEvidence]**](WSImpactEvidence.md) |  | [optional] 
**managing_organisational_unit** | [**WSOrganisationRef**](WSOrganisationRef.md) |  | [optional] 
**documents** | [**list[WSDocument]**](WSDocument.md) |  | [optional] 
**links** | [**list[WSLink]**](WSLink.md) |  | [optional] 
**related_impacts** | [**list[WSImpactRef]**](WSImpactRef.md) |  | [optional] 
**related_press_media** | [**list[WSPressMediaRef]**](WSPressMediaRef.md) | Only available when the Press / Media module is enabled | [optional] 
**related_research_outputs** | [**list[WSResearchOutputRef]**](WSResearchOutputRef.md) |  | [optional] 
**related_activities** | [**list[WSActivityRef]**](WSActivityRef.md) | Only available when the Activity module is enabled | [optional] 
**related_projects** | [**list[WSUPMProjectRef]**](WSUPMProjectRef.md) | Only available when the Unified Project Model module is enabled | [optional] 
**related_prizes** | [**list[WSPrizeRef]**](WSPrizeRef.md) | Only available when the Prize module is enabled | [optional] 
**related_student_theses** | [**list[WSStudentThesisRef]**](WSStudentThesisRef.md) | Only available when the Student Thesis module is enabled | [optional] 
**related_data_sets** | [**list[WSDataSetRef]**](WSDataSetRef.md) | Only available when the Dataset module is enabled | [optional] 
**visibilities** | [**list[WSVisibility]**](WSVisibility.md) |  | [optional] 
**confidential** | **bool** |  | [optional] [default to False]
**keyword_groups** | [**list[WSKeywordGroup]**](WSKeywordGroup.md) |  | [optional] 
**workflows** | [**list[WSWorkflow]**](WSWorkflow.md) |  | [optional] 
**info** | [**WSContentInformation**](WSContentInformation.md) |  | [optional] 
**externalable_info** | [**WSExternalableInformation**](WSExternalableInformation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


