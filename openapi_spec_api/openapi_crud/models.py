from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import TextField, ManyToManyField, UUIDField, ForeignKey, URLField, EmailField


class BaseModel(models.Model):
    uuid = UUIDField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OpenAPI(models.Model):
    """
    openapi 	string 	REQUIRED. This string MUST be the version number of the OpenAPI Specification that the OpenAPI document uses. The openapi field SHOULD be used by tooling to interpret the OpenAPI document. This is not related to the API info.version string.
    info 	Info Object 	REQUIRED. Provides metadata about the API. The metadata MAY be used by tooling as required.
    jsonSchemaDialect 	string 	The default value for the $schema keyword within Schema Objects contained within this OAS document. This MUST be in the form of a URI.
    servers 	[Server Object] 	An array of Server Objects, which provide connectivity information to a target server. If the servers property is not provided, or is an empty array, the default value would be a Server Object with a url value of /.
    paths 	Paths Object 	The available paths and operations for the API.
    webhooks 	Map[string, Path Item Object | Reference Object] ] 	The incoming webhooks that MAY be received as part of this API and that the API consumer MAY choose to implement. Closely related to the callbacks feature, this section describes requests initiated other than by an API call, for example by an out of band registration. The key name is a unique string to refer to each webhook, while the (optionally referenced) Path Item Object describes a request that may be initiated by the API provider and the expected responses. An example is available.
    components 	Components Object 	An element to hold various schemas for the document.
    security 	[Security Requirement Object] 	A declaration of which security mechanisms can be used across the API. The list of values includes alternative security requirement objects that can be used. Only one of the security requirement objects need to be satisfied to authorize a request. Individual operations can override this definition. To make security optional, an empty security requirement ({}) can be included in the array.
    tags 	[Tag Object] 	A list of tags used by the document with additional metadata. The order of the tags can be used to reflect on their order by the parsing tools. Not all tags that are used by the Operation Object must be declared. The tags that are not declared MAY be organized randomly or based on the tools' logic. Each tag name in the list MUST be unique.
    externalDocs 	External Documentation Object 	Additional external documentation.
    """
    openapi = TextField()
    info = TextField()
    json_schema_dialect = TextField()
    servers = ManyToManyField("Server")
    paths = ForeignKey("Paths", on_delete=models.CASCADE)
    webhooks = ManyToManyField("Webhook")
    components = ForeignKey("Components", on_delete=models.CASCADE)
    security = ForeignKey("SecurityRequirement", on_delete=models.CASCADE)
    tags = ForeignKey("Tag", on_delete=models.CASCADE)
    external_docs = ForeignKey("ExternalDocumentation", on_delete=models.CASCADE)


class Webhook(models.Model):
    """
    """

    name = TextField()
    path = ForeignKey("Paths", on_delete=models.CASCADE)
    reference = ForeignKey("Reference", on_delete=models.CASCADE)


class Info(models.Model):
    """
    """

    pass
    """
    title 	string 	REQUIRED. The title of the API.
    summary 	string 	A short summary of the API.
    description 	string 	A description of the API. CommonMark syntax MAY be used for rich text representation.
    termsOfService 	string 	A URL to the Terms of Service for the API. This MUST be in the form of a URL.
    contact 	Contact Object 	The contact information for the exposed API.
    license 	License Object 	The license information for the exposed API.
    version 	string 	REQUIRED. The version of the OpenAPI document (which is distinct from the OpenAPI Specification version or the API implementation version).
    """

    title = TextField()
    summary = TextField()
    description = TextField()
    terms_of_service = TextField()
    contact = ForeignKey("Contact", on_delete=models.CASCADE)
    license = ForeignKey("License", on_delete=models.CASCADE)


class Contact(models.Model):
    """
    """

    pass
    """
    name 	string 	The identifying name of the contact person/organization.
    url 	string 	The URL pointing to the contact information. This MUST be in the form of a URL.
    email 	string 	The email address of the contact person/organization. This MUST be in the form of an email address.
    """

    name = TextField()
    url = URLField()
    email = EmailField()


class License(models.Model):
    """
    name 	string 	REQUIRED. The license name used for the API.
    identifier 	string 	An SPDX license expression for the API. The identifier field is mutually exclusive of the url field.
    url 	string 	A URL to the license used for the API. This MUST be in the form of a URL. The url field is mutually exclusive of the identifier field.
    """

    name = TextField()
    identifier = TextField()
    url = URLField()


class Server(models.Model):
    """
    """

    pass
    """
    url 	string 	REQUIRED. A URL to the target host. This URL supports Server Variables and MAY be relative, to indicate that the host location is relative to the location where the OpenAPI document is being served. Variable substitutions will be made when a variable is named in {brackets}.
    description 	string 	An optional string describing the host designated by the URL. CommonMark syntax MAY be used for rich text representation.
    variables 	Map[string, Server Variable Object] 	A map between a variable name and its value. The value is used for substitution in the server's URL template.
    """

    url = TextField()
    description = TextField()
    variables = ManyToManyField("ServerVariableMap")


class ServerVariableMap(models.Model):
    """
    A map between a variable name and its value. The value is used for substitution in the server's URL template.
    """

    name = TextField()
    server_variable = ForeignKey("ServerVariable", on_delete=models.CASCADE)


class ServerVariable(models.Model):
    """
    enum 	[string] 	An enumeration of string values to be used if the substitution options are from a limited set. The array MUST NOT be empty.
    default 	string 	REQUIRED. The default value to use for substitution, which SHALL be sent if an alternate value is not supplied. Note this behavior is different than the Schema Object's treatment of default values, because in those cases parameter values are optional. If the enum is defined, the value MUST exist in the enum's values.
    description 	string 	An optional description for the server variable. CommonMark syntax MAY be used for rich text representation.
    """

    enum = ArrayField(base_field=TextField())
    default = TextField()
    description = TextField()


class Components(models.Model):
    """
    """

    pass
    """
    schemas 	Map[string, Schema Object] 	An object to hold reusable Schema Objects.
    responses 	Map[string, Response Object | Reference Object] 	An object to hold reusable Response Objects.
    parameters 	Map[string, Parameter Object | Reference Object] 	An object to hold reusable Parameter Objects.
    examples 	Map[string, Example Object | Reference Object] 	An object to hold reusable Example Objects.
    requestBodies 	Map[string, Request Body Object | Reference Object] 	An object to hold reusable Request Body Objects.
    headers 	Map[string, Header Object | Reference Object] 	An object to hold reusable Header Objects.
    securitySchemes 	Map[string, Security Scheme Object | Reference Object] 	An object to hold reusable Security Scheme Objects.
    links 	Map[string, Link Object | Reference Object] 	An object to hold reusable Link Objects.
    callbacks 	Map[string, Callback Object | Reference Object] 	An object to hold reusable Callback Objects.
    pathItems 	Map[string, Path Item Object | Reference Object] 	An object to hold reusable Path Item Object.
    """

    pass


class SchemaMap(models.Model):
    """

    """

    name = TextField()
    schema = ForeignKey("Schema", on_delete=models.CASCADE)
    reference = ForeignKey("Reference", on_delete=models.CASCADE)


class ResponseMap(models.Model):
    """

    """

    pass
    name = TextField()
    response = ForeignKey("Response", on_delete=models.CASCADE)


class ParameterMap(models.Model):
    """

    """

    pass
    name = TextField()
    parameter = ForeignKey("Parameter", on_delete=models.CASCADE)
    reference = ForeignKey("Reference", on_delete=models.CASCADE)


class ExampleMap(models.Model):
    """

    """

    pass
    name = TextField()
    example = ForeignKey("Example", on_delete=models.CASCADE)
    reference = ForeignKey("Reference", on_delete=models.CASCADE)


class RequestBodyMap(models.Model):
    """

    """

    pass
    name = TextField()
    request_body = ForeignKey("RequestBody", on_delete=models.CASCADE)
    reference = ForeignKey("Reference", on_delete=models.CASCADE)


class HeaderMap(models.Model):
    """

    """

    pass
    name = TextField()
    header = ForeignKey("Header", on_delete=models.CASCADE)
    reference = ForeignKey("Reference", on_delete=models.CASCADE)


class SecuritySchemeMap(models.Model):
    """

    """

    pass
    name = TextField()
    security_scheme = ForeignKey("SecurityScheme", on_delete=models.CASCADE)
    reference = ForeignKey("Reference", on_delete=models.CASCADE)


class LinkMap(models.Model):
    """

    """

    pass
    name = TextField()
    link = ForeignKey("Link", on_delete=models.CASCADE)
    reference = ForeignKey("Reference", on_delete=models.CASCADE)


class CallbackMap(models.Model):
    """

    """

    pass
    name = TextField()
    callback = ForeignKey("Callback", on_delete=models.CASCADE)
    reference = ForeignKey("Reference", on_delete=models.CASCADE)


class PathItemMap(models.Model):
    """

    """

    name = TextField()
    path_item = ForeignKey("PathItem", on_delete=models.CASCADE)
    reference = ForeignKey("Reference", on_delete=models.CASCADE)


class Paths(models.Model):
    """
    /{path} 	Path Item Object 	A relative path to an individual endpoint. The field name MUST begin with a forward slash (/). The path is appended (no relative URL resolution) to the expanded URL from the Server Object's url field in order to construct the full URL. Path templating is allowed. When matching URLs, concrete (non-templated) paths would be matched before their templated counterparts. Templated paths with the same hierarchy but different templated names MUST NOT exist as they are identical. In case of ambiguous matching, it's up to the tooling to decide which one to use.
    """

    path = TextField()


class PathItem(models.Model):
    """
    $ref 	string 	Allows for a referenced definition of this path item. The referenced structure MUST be in the form of a Path Item Object. In case a Path Item Object field appears both in the defined object and the referenced object, the behavior is undefined. See the rules for resolving Relative References.
    summary 	string 	An optional, string summary, intended to apply to all operations in this path.
    description 	string 	An optional, string description, intended to apply to all operations in this path. CommonMark syntax MAY be used for rich text representation.
    get 	Operation Object 	A definition of a GET operation on this path.
    put 	Operation Object 	A definition of a PUT operation on this path.
    post 	Operation Object 	A definition of a POST operation on this path.
    delete 	Operation Object 	A definition of a DELETE operation on this path.
    options 	Operation Object 	A definition of a OPTIONS operation on this path.
    head 	Operation Object 	A definition of a HEAD operation on this path.
    patch 	Operation Object 	A definition of a PATCH operation on this path.
    trace 	Operation Object 	A definition of a TRACE operation on this path.
    servers 	[Server Object] 	An alternative server array to service all operations in this path.
    parameters 	[Parameter Object | Reference Object] 	A list of parameters that are applicable for all the operations described under this path. These parameters can be overridden at the operation level, but cannot be removed there. The list MUST NOT include duplicated parameters. A unique parameter is defined by a combination of a name and location. The list can use the Reference Object to link to parameters that are defined at the OpenAPI Object's components/parameters.
    """

    pass


class Operation(models.Model):
    """
    """

    pass


class ExternalDocumentation(models.Model):
    """
    """

    pass


class Parameter(models.Model):
    """
    """

    pass


class RequestBody(models.Model):
    """
    """

    pass


class MediaType(models.Model):
    """
    """

    pass


class Encoding(models.Model):
    """
    """

    pass


class Responses(models.Model):
    """
    """

    pass


class Response(models.Model):
    """
    """

    pass


class Callback(models.Model):
    """
    """

    pass


class Example(models.Model):
    """
    """

    pass


class Link(models.Model):
    """
    """

    pass


class Header(models.Model):
    """
    """

    pass


class Tag(models.Model):
    """
    """

    pass


class Reference(models.Model):
    """
    """

    pass


class Schema(models.Model):
    """
    """

    pass


class Discriminator(models.Model):
    """
    """

    pass


class XML(models.Model):
    """
    """

    pass


class SecurityScheme(models.Model):
    """
    """

    pass


class OAuthFlows(models.Model):
    """
    """

    pass


class OAuthFlow(models.Model):
    """
    """

    pass


class SecurityRequirement(models.Model):
    """
    """

    pass
