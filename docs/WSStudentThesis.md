# WSStudentThesis

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**html_renderings** | [**list[WSHtmlRendering]**](WSHtmlRendering.md) |  | [optional] 
**types** | [**list[WSClassification]**](WSClassification.md) |  | [optional] 
**languages** | [**list[WSClassification]**](WSClassification.md) |  | [optional] 
**title** | **str** |  | [optional] 
**sub_title** | **str** |  | [optional] 
**translated_titles** | [**list[WSLocalizedString]**](WSLocalizedString.md) |  | [optional] 
**translated_sub_titles** | [**list[WSLocalizedString]**](WSLocalizedString.md) |  | [optional] 
**abstract** | **list[str]** |  | [optional] 
**person_associations** | [**list[WSClassifiedAuthorAssociation]**](WSClassifiedAuthorAssociation.md) |  | [optional] 
**organisations** | [**list[WSOrganisationRef]**](WSOrganisationRef.md) |  | [optional] 
**external_organisations** | [**list[WSExternalOrganisationRef]**](WSExternalOrganisationRef.md) |  | [optional] 
**managing_organisational_unit** | [**WSOrganisationRef**](WSOrganisationRef.md) |  | [optional] 
**supervisors** | [**list[WSClassifiedInternalExternalPersonAssociation]**](WSClassifiedInternalExternalPersonAssociation.md) |  | [optional] 
**award_date** | [**WSCompoundDate**](WSCompoundDate.md) |  | [optional] 
**awarding_institutions** | [**list[WSInternalExternalOrganisationAssociation]**](WSInternalExternalOrganisationAssociation.md) |  | [optional] 
**sponsors** | [**list[WSExternalOrganisationRef]**](WSExternalOrganisationRef.md) |  | [optional] 
**keyword_groups** | [**list[WSKeywordGroup]**](WSKeywordGroup.md) |  | [optional] 
**documents** | [**list[WSStudentThesisDocument]**](WSStudentThesisDocument.md) |  | [optional] 
**links** | [**list[WSLink]**](WSLink.md) |  | [optional] 
**bibliographical_notes** | [**list[WSLocalizedString]**](WSLocalizedString.md) |  | [optional] 
**related_research_outputs** | [**list[WSResearchOutputRef]**](WSResearchOutputRef.md) |  | [optional] 
**related_activities** | [**list[WSActivityRef]**](WSActivityRef.md) | Only available when the Activity module is enabled | [optional] 
**related_press_media** | [**list[WSPressMediaRef]**](WSPressMediaRef.md) | Only available when the Press / Media module is enabled | [optional] 
**related_impacts** | [**list[WSImpactRef]**](WSImpactRef.md) | Only available when the Impact module is enabled | [optional] 
**related_projects** | [**list[WSUPMProjectRef]**](WSUPMProjectRef.md) | Only available when the Unified Project Model module is enabled | [optional] 
**related_data_sets** | [**list[WSDataSetRef]**](WSDataSetRef.md) | Only available when the DataSet module is enabled | [optional] 
**related_prizes** | [**list[WSPrizeRef]**](WSPrizeRef.md) | Only available when the Prize module is enabled | [optional] 
**workflows** | [**list[WSWorkflow]**](WSWorkflow.md) |  | [optional] 
**confidential** | **bool** |  | [optional] [default to False]
**visibilities** | [**list[WSVisibility]**](WSVisibility.md) |  | [optional] 
**info** | [**WSContentInformation**](WSContentInformation.md) |  | [optional] 
**externalable_info** | [**WSExternalableInformation**](WSExternalableInformation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


