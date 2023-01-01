## Unions

### About unions
A union is a type of object representing many objects.

{% for union in reference.unions %}
### {{ union.name }}   
{{ union.description|default('', True)|markdown|safe }}

#### Possible types
{% for type in union.types %}        
- {{ type.name }}
{% endfor %}
{% endfor %}
