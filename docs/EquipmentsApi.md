# msu_scholars_api.EquipmentsApi

All URIs are relative to *https://scholars.opb.msu.edu/ws/api/510*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_available_orderings**](EquipmentsApi.md#get_available_orderings) | **GET** /equipments-meta/orderings | Lists available orderings
[**get_available_renderings**](EquipmentsApi.md#get_available_renderings) | **GET** /equipments-meta/renderings | Lists available renderings
[**get_equipment**](EquipmentsApi.md#get_equipment) | **GET** /equipments/{id} | Get equipment
[**list_equipment**](EquipmentsApi.md#list_equipment) | **GET** /equipments | Lists all equipment
[**list_equipment_0**](EquipmentsApi.md#list_equipment_0) | **POST** /equipments | Complex operation for equipment
[**list_equipment_fingerprints**](EquipmentsApi.md#list_equipment_fingerprints) | **GET** /equipments/{id}/fingerprints | Lists fingerprints on an equipment


# **get_available_orderings**
> WSOrderingsList get_available_orderings()

Lists available orderings

Lists all orderings available to the equipment endpoint. These values can be used by the order parameter

### Example 
```python
from __future__ import print_function
import time
import msu_scholars_api
from msu_scholars_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
msu_scholars_api.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: apiKey
msu_scholars_api.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = msu_scholars_api.EquipmentsApi()

try: 
    # Lists available orderings
    api_response = api_instance.get_available_orderings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EquipmentsApi->get_available_orderings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WSOrderingsList**](WSOrderingsList.md)

### Authorization

[api-key](../README.md#api-key), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_renderings**
> WSRenderingsList get_available_renderings()

Lists available renderings

Lists all renderings available to the equipment endpoint. These values can be used by the rendering parameter

### Example 
```python
from __future__ import print_function
import time
import msu_scholars_api
from msu_scholars_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
msu_scholars_api.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: apiKey
msu_scholars_api.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = msu_scholars_api.EquipmentsApi()

try: 
    # Lists available renderings
    api_response = api_instance.get_available_renderings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EquipmentsApi->get_available_renderings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WSRenderingsList**](WSRenderingsList.md)

### Authorization

[api-key](../README.md#api-key), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_equipment**
> WSEquipment get_equipment(id, id_classification=id_classification, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, return_used_content=return_used_content, navigation_link=navigation_link)

Get equipment

Get equipment with specific ID (path parameter).

### Example 
```python
from __future__ import print_function
import time
import msu_scholars_api
from msu_scholars_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
msu_scholars_api.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: apiKey
msu_scholars_api.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = msu_scholars_api.EquipmentsApi()
id = 'id_example' # str | Id of the desired equipment
id_classification = 'id_classification_example' # str | Specifies an optional classification used to specify which type of ID should be used in the match. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#idclassification_param\">Read more</a> (optional)
fields = ['fields_example'] # list[str] | Limit the fields included in the response. E.g. 'nameVariants.nameVariant' will only return the name variants. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\">Read more</a> (optional)
locale = ['locale_example'] # list[str] | Enter the desired locale. E.g. 'en_GB' will only return the English text strings. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\">Read more</a> (optional)
fallback_locale = ['fallback_locale_example'] # list[str] | Fallback locale string. Syntax is 'Locale1=>Locale2' to map Locale1 to Locale2. Example: 'da_DK=>en_GB'. Locale1 must be equal to locale provided in the locale string. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\">Read more</a> (optional)
rendering = ['rendering_example'] # list[str] | HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\">Read more</a> (optional)
return_used_content = true # bool | If 'true', the id's of the content used to create HTML renderings are returned as part of the result. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\">Read more</a> (optional)
navigation_link = true # bool | Include navigation links for paging and content. Default: true. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\">Read more</a> (optional)

try: 
    # Get equipment
    api_response = api_instance.get_equipment(id, id_classification=id_classification, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, return_used_content=return_used_content, navigation_link=navigation_link)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EquipmentsApi->get_equipment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the desired equipment | 
 **id_classification** | **str**| Specifies an optional classification used to specify which type of ID should be used in the match. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#idclassification_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fields** | [**list[str]**](str.md)| Limit the fields included in the response. E.g. &#39;nameVariants.nameVariant&#39; will only return the name variants. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **locale** | [**list[str]**](str.md)| Enter the desired locale. E.g. &#39;en_GB&#39; will only return the English text strings. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fallback_locale** | [**list[str]**](str.md)| Fallback locale string. Syntax is &#39;Locale1&#x3D;&gt;Locale2&#39; to map Locale1 to Locale2. Example: &#39;da_DK&#x3D;&gt;en_GB&#39;. Locale1 must be equal to locale provided in the locale string. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **rendering** | [**list[str]**](str.md)| HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **return_used_content** | **bool**| If &#39;true&#39;, the id&#39;s of the content used to create HTML renderings are returned as part of the result. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **navigation_link** | **bool**| Include navigation links for paging and content. Default: true. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 

### Return type

[**WSEquipment**](WSEquipment.md)

### Authorization

[api-key](../README.md#api-key), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_equipment**
> WSEquipmentListResult list_equipment(q=q, order=order, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, linking_strategy=linking_strategy, return_used_content=return_used_content, navigation_link=navigation_link, size=size, offset=offset, page=page, page_size=page_size)

Lists all equipment

Lists all equipment in the PURE installation. If filtering of the returned equipment is required, see the POST version which supports additional filtering.

### Example 
```python
from __future__ import print_function
import time
import msu_scholars_api
from msu_scholars_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
msu_scholars_api.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: apiKey
msu_scholars_api.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = msu_scholars_api.EquipmentsApi()
q = 'q_example' # str | Free text search string using Lucene query syntax. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#q_param\">Read more</a> (optional)
order = ['order_example'] # list[str] | Specify the ordering of content in the result. Default: ID ascending. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#order_param\">Read more</a> (optional)
fields = ['fields_example'] # list[str] | Limit the fields included in the response. E.g. 'nameVariants.nameVariant' will only return the name variants. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\">Read more</a> (optional)
locale = ['locale_example'] # list[str] | Enter the desired locale. E.g. 'en_GB' will only return the English text strings. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\">Read more</a> (optional)
fallback_locale = ['fallback_locale_example'] # list[str] | Fallback locale string. Syntax is 'Locale1=>Locale2' to map Locale1 to Locale2. Example: 'da_DK=>en_GB'. Locale1 must be equal to locale provided in the locale string. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\">Read more</a> (optional)
rendering = ['rendering_example'] # list[str] | HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\">Read more</a> (optional)
linking_strategy = 'linking_strategy_example' # str | Specifies the linking strategy to use used when creating HTML renderings. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#linkingStrategy_param\">Read more</a> (optional)
return_used_content = true # bool | If 'true', the id's of the content used to create HTML renderings are returned as part of the result. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\">Read more</a> (optional)
navigation_link = true # bool | Include navigation links for paging and content. Default: true. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\">Read more</a> (optional)
size = 56 # int | Enter the number of results per window. Default: 10. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#size_offset_param\">Read more</a> (optional)
offset = 56 # int | Enter the offset into the total result set where items should be returned from. Default: 0. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#size_offset_param\">Read more</a> (optional)
page = 56 # int | Enter the desired page number. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#page_size_param\">Read more</a> (optional)
page_size = 56 # int | Enter the desired number of results per page. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#page_size_param\">Read more</a> (optional)

try: 
    # Lists all equipment
    api_response = api_instance.list_equipment(q=q, order=order, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, linking_strategy=linking_strategy, return_used_content=return_used_content, navigation_link=navigation_link, size=size, offset=offset, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EquipmentsApi->list_equipment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Free text search string using Lucene query syntax. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#q_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **order** | [**list[str]**](str.md)| Specify the ordering of content in the result. Default: ID ascending. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#order_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fields** | [**list[str]**](str.md)| Limit the fields included in the response. E.g. &#39;nameVariants.nameVariant&#39; will only return the name variants. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **locale** | [**list[str]**](str.md)| Enter the desired locale. E.g. &#39;en_GB&#39; will only return the English text strings. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fallback_locale** | [**list[str]**](str.md)| Fallback locale string. Syntax is &#39;Locale1&#x3D;&gt;Locale2&#39; to map Locale1 to Locale2. Example: &#39;da_DK&#x3D;&gt;en_GB&#39;. Locale1 must be equal to locale provided in the locale string. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **rendering** | [**list[str]**](str.md)| HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **linking_strategy** | **str**| Specifies the linking strategy to use used when creating HTML renderings. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#linkingStrategy_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **return_used_content** | **bool**| If &#39;true&#39;, the id&#39;s of the content used to create HTML renderings are returned as part of the result. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **navigation_link** | **bool**| Include navigation links for paging and content. Default: true. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **size** | **int**| Enter the number of results per window. Default: 10. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#size_offset_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **offset** | **int**| Enter the offset into the total result set where items should be returned from. Default: 0. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#size_offset_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **page** | **int**| Enter the desired page number. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#page_size_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **page_size** | **int**| Enter the desired number of results per page. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#page_size_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 

### Return type

[**WSEquipmentListResult**](WSEquipmentListResult.md)

### Authorization

[api-key](../README.md#api-key), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_equipment_0**
> WSEquipmentListResult list_equipment_0(body=body)

Complex operation for equipment

Lists equipment in the PURE installation, similar to the GET version, instead of using parameters to alter the response, an XML document is posted with the request. The XML document contains fields for all the parameters available for the GET version, but also additional filtering options. For documentation of the XML format see <a href=\"documentation/Content/Topics/CT_Equipment.htm#post_xml\">Equipment documentation</a>

### Example 
```python
from __future__ import print_function
import time
import msu_scholars_api
from msu_scholars_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
msu_scholars_api.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: apiKey
msu_scholars_api.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = msu_scholars_api.EquipmentsApi()
body = msu_scholars_api.WSEquipmentsQuery() # WSEquipmentsQuery |  (optional)

try: 
    # Complex operation for equipment
    api_response = api_instance.list_equipment_0(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EquipmentsApi->list_equipment_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WSEquipmentsQuery**](WSEquipmentsQuery.md)|  | [optional] 

### Return type

[**WSEquipmentListResult**](WSEquipmentListResult.md)

### Authorization

[api-key](../README.md#api-key), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_equipment_fingerprints**
> WSFingerprintListResult list_equipment_fingerprints(id, id_classification=id_classification, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, return_used_content=return_used_content, navigation_link=navigation_link)

Lists fingerprints on an equipment

Lists all fingerprints associated to the equipment specified by an ID (supplied as path parameter)

### Example 
```python
from __future__ import print_function
import time
import msu_scholars_api
from msu_scholars_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
msu_scholars_api.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: apiKey
msu_scholars_api.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = msu_scholars_api.EquipmentsApi()
id = 'id_example' # str | id
id_classification = 'id_classification_example' # str | Specifies an optional classification used to specify which type of ID should be used in the match. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#idclassification_param\">Read more</a> (optional)
fields = ['fields_example'] # list[str] | Limit the fields included in the response. E.g. 'nameVariants.nameVariant' will only return the name variants. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\">Read more</a> (optional)
locale = ['locale_example'] # list[str] | Enter the desired locale. E.g. 'en_GB' will only return the English text strings. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\">Read more</a> (optional)
fallback_locale = ['fallback_locale_example'] # list[str] | Fallback locale string. Syntax is 'Locale1=>Locale2' to map Locale1 to Locale2. Example: 'da_DK=>en_GB'. Locale1 must be equal to locale provided in the locale string. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\">Read more</a> (optional)
rendering = ['rendering_example'] # list[str] | HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\">Read more</a> (optional)
return_used_content = true # bool | If 'true', the id's of the content used to create HTML renderings are returned as part of the result. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\">Read more</a> (optional)
navigation_link = true # bool | Include navigation links for paging and content. Default: true. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\">Read more</a> (optional)

try: 
    # Lists fingerprints on an equipment
    api_response = api_instance.list_equipment_fingerprints(id, id_classification=id_classification, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, return_used_content=return_used_content, navigation_link=navigation_link)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EquipmentsApi->list_equipment_fingerprints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **id_classification** | **str**| Specifies an optional classification used to specify which type of ID should be used in the match. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#idclassification_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fields** | [**list[str]**](str.md)| Limit the fields included in the response. E.g. &#39;nameVariants.nameVariant&#39; will only return the name variants. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **locale** | [**list[str]**](str.md)| Enter the desired locale. E.g. &#39;en_GB&#39; will only return the English text strings. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fallback_locale** | [**list[str]**](str.md)| Fallback locale string. Syntax is &#39;Locale1&#x3D;&gt;Locale2&#39; to map Locale1 to Locale2. Example: &#39;da_DK&#x3D;&gt;en_GB&#39;. Locale1 must be equal to locale provided in the locale string. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **rendering** | [**list[str]**](str.md)| HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **return_used_content** | **bool**| If &#39;true&#39;, the id&#39;s of the content used to create HTML renderings are returned as part of the result. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **navigation_link** | **bool**| Include navigation links for paging and content. Default: true. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 

### Return type

[**WSFingerprintListResult**](WSFingerprintListResult.md)

### Authorization

[api-key](../README.md#api-key), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

