## Interfaces

### About interfaces
Interfaces serve as parent objects from which other objects can inherit.

{% for interface in reference.interfaces %}
### {{ interface.name }}
{{ interface.description|default('', True)|replace("\n", "")|replace("\r", "")|safe }}

{% if interface.implemented_by %}
{% for implementation in interface.implemented_by %}
- {{ implementation.name }}
{% endfor %}
{% endif %}

### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
{% for name, field in interface.fields.items() %}| {{ name }} | {{ field.type|string }} |  {{ field.description|default('', True)|replace("\n", "")|replace("\r", "")|safe }} |   
{% endfor %}

### Fields' arguments

{% for name, field in interface.fields.items() %}
{% if field.args %}
#### {{ name }}

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
{% for arg_name, arg in field.args.items() %}|  {{ arg_name }} | {{ arg.type|string }} | {{ arg.description|default('', True)|replace("\n", "")|replace("\r", "")|safe }} |
{% endfor %}
{% endif %}
{% endfor %}
{% endfor %}

