## Queries 

### About queries
Every GraphQL schema has a root type for both queries and mutations. 
The query type defines GraphQL operations that retrieve data from the server.

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
{% for name, field in reference.query.fields|dictsort %}| {{ name }} | {{ field.type|string }} | {{ field.description|default('', True)|replace("\n", "")|replace("\r", "")|safe }} |
{% endfor %}

### Queries arguments
{% for name, field in reference.query.fields|dictsort %}
{% if field.args %}
#### {{ name }}

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
{% for arg_name, arg in field.args.items() %}| {{ arg_name }} | {{ arg.type|string }} | {{ arg.description|default('', True)|replace("\n", "")|replace("\r", "")|safe }} |
{% endfor %}
{% endif %}
{% endfor %}