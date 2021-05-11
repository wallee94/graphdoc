from ariadne import load_schema_from_path
from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route

import graphdoc

schema = load_schema_from_path("../schema.graphql")


def schema_docs(request):
    html = graphdoc.to_doc(schema, './templates')
    return HTMLResponse(html)


app = Starlette(routes=[
    Route('/', schema_docs)
])
