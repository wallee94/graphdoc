## Scalars

### About scalars
Scalars are primitive values: Int, Float, String, Boolean, or ID. When calling 
the GraphQL API, you must specify nested subfields until you return only scalars.

{% for scalar in reference.scalars %}
### {{ scalar.name }}
{{ scalar.description|default('', True)|markdown|safe }}
{% endfor %}
