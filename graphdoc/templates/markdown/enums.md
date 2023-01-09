## Enums

### About enums
Enums represent possible sets of values for a field.

{% for enum in reference.enums %}
### {{ enum.name }}
{{ enum.description|default('', True)|markdown|safe }}

#### Values

| ** Value ** | **Description** | 
|-------------|--------------------|
{% for value, obj in enum.values.items() %}| {{ value }} | {{ obj.description|default('', True)|markdown|safe }} | 
{% endfor %}
{% endfor %}  
