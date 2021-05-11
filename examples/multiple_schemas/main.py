from fastapi import FastAPI, Response

import cities_api
import countries_api
import graphdoc

app = FastAPI()


@app.get("/cities/docs")
async def graphql_cities_docs():
    html = graphdoc.to_doc(cities_api.schema)
    return Response(content=html, media_type="text/html")


@app.get("/countries/docs")
async def graphql_countries_docs():
    html = graphdoc.to_doc(countries_api.schema)
    return Response(content=html, media_type="text/html")
