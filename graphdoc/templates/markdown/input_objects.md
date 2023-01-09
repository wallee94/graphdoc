## Input objects

### About input objects
Input objects can be described as "composable objects" because they include 
a set of input fields that define the object.

{% for io in reference.input_objects %}
### {{ io.name }}
{{ io.description|default('', True)|replace("\n", "")|replace("\r", "")|safe }}

### Input fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
{% for name, field in io.fields.items() %}| {{ name }} | {{ field.type|string }} | {{ field.description|default('', True)|replace("\n", "")|replace("\r", "")|safe }} |
{% endfor %}
{% endfor %}
