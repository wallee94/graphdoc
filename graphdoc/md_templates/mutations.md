## Mutations

### About mutations
Every GraphQL schema has a root type for both queries and mutations. 
The mutation type defines GraphQL operations that change data on the server. 
It is analogous to performing HTTP verbs such as POST, PATCH, and DELETE.

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
{% for name, field in reference.mutation.fields|dictsort %}| {{ name }} | {{ field.type|string }} | {{ field.description|default('', True)|markdown|safe }} |
{% endfor %}

### Mutations' arguments
{% for name, field in reference.mutation.fields|dictsort %}
{% if field.args %}
#### {{ name }}
| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
{% for arg_name, arg in field.args.items() %}| {{ arg_name }} | {{ arg.type|string }} | {{ arg.description|default('', True)|markdown|safe }} |
{% endfor %}
{% endif %}
{% endfor %}

### Return fields
{% for name, field in reference.mutation.fields|dictsort %}
{% if field.args %}
#### {{ name }}
| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
{% for return_name, return in field.unwrapped_type.fields.items() %}| {{ return_name }} | {{ return.type|string }} | {{ return.description|default('', True)|markdown|safe }} |
{% endfor %}
{% endif %}
{% endfor %}
