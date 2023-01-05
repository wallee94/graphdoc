## Objects

### About objects
Objects in GraphQL represent the resources you can access. An object can 
contain a list of fields, which are specifically typed.

{% for object in reference.objects %}
### {{ object.name }} 
{{ object.description|default('', True)|markdown|safe }}

{% if object.fields %}
#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
{% for name, field in object.fields.items() %}| {{ name }} | {{ field.type|string }} | {{ field.description|default('', True)|markdown|safe }} |
{% endfor %}
{% endif %}
{% endfor %}
