# Example app using custom templates

Graphdoc allows using jinja templates to customize the HTML 
generated.

This is an example app using 
[Starlette](https://www.starlette.io/) and 
[Ariadne](https://ariadnegraphql.org/)

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

Go to http://localhost:8000 to see the generated page using
the custom docs in the `templates` folder

## Using custom templates

The `graphdoc.to_doc` method accepts a second argument with a path
to a templates folder. Templates are loaded using jinja's 
[FileSystemLoader](https://jinja.palletsprojects.com/en/2.11.x/api/#jinja2.FileSystemLoader).

Files in this folder will override the default templates. Take a look
to the default [here](https://github.com/wallee94/graphdoc/tree/main/graphdoc/templates).

In this example, the templates path is `./templates`, and we 
are overriding `about.html`.