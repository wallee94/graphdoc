# Documenting multiple API

The `graphdoc.to_doc` method takes any schema, so you can create documentation
for multiple APIs in the same project.

This is an example using Graphene 2 and FastAPI

## Setup

To run it locally, install the dependencies in your
environment

```shell
pip install -r requirements.txt
```

An run the server using uvicorn

```shell
uvicorn main:app --reload
```

Go to http://localhost:8000/cities/docs and http://localhost:8000/countries/docs
to see both docs pages
