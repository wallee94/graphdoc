{% filter trim %}
# GraphQL API Documentation

{% include 'about.md' %}

{% if reference.query %}
{% include 'queries.md' %}
{% endif %}

{% if reference.mutation %}
{% include 'mutations.md' %}
{% endif %}

{% if reference.objects %}
{% include 'objects.md' %}
{% endif %}

{% if reference.interfaces %}
{% include 'interfaces.md' %}
{% endif %}
{% if reference.enums %}
{% include 'enums.md' %}
{% endif %}

{% if reference.unions %}
{% include 'unions.md' %}
{% endif %}

{% if reference.input_objects %}
{% include 'input_objects.md' %}
{% endif %}

{% if reference.scalars %}
{% include 'scalars.md' %}
{% endif %}
{% endfilter %}
