# GraphQL API Documentation

## About GraphQL

[GraphQL](https://graphql.github.io) data query language is:
  - A [specification](http://spec.graphql.org/June2018/). The spec determines the validity of the schema on the API server. The schema determines the validity of client calls.
  - Strongly typed. The schema defines an API's type system and all object relationships.
  - Introspective. A client can query the schema for details about the schema.
  - Hierarchical. The shape of a GraphQL call mirrors the shape of the JSON data it returns. Nested fields let you query for and receive only the data you specify in a single round trip.
  - An application layer. GraphQL is not a storage model or a database query language. The graph refers to graph structures defined in the schema, where nodes define objects and edges define relationships between objects. The API traverses and returns application data based on the schema definitions, independent of how the data is stored.


## Queries 

### About queries
Every GraphQL schema has a root type for both queries and mutations. 
The query type defines GraphQL operations that retrieve data from the server.

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| allFilms | FilmsConnection | <p></p>
 |
| allPeople | PeopleConnection | <p></p>
 |
| allPlanets | PlanetsConnection | <p></p>
 |
| allSpecies | SpeciesConnection | <p></p>
 |
| allStarships | StarshipsConnection | <p></p>
 |
| allVehicles | VehiclesConnection | <p></p>
 |
| film | Film | <p></p>
 |
| node | Node | <p>Fetches an object given its ID</p>
 |
| person | Person | <p></p>
 |
| planet | Planet | <p></p>
 |
| species | Species | <p></p>
 |
| starship | Starship | <p></p>
 |
| vehicle | Vehicle | <p></p>
 |


### Queries arguments


#### allFilms

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| after | String | <p></p>
 |
| first | Int | <p></p>
 |
| before | String | <p></p>
 |
| last | Int | <p></p>
 |




#### allPeople

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| after | String | <p></p>
 |
| first | Int | <p></p>
 |
| before | String | <p></p>
 |
| last | Int | <p></p>
 |




#### allPlanets

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| after | String | <p></p>
 |
| first | Int | <p></p>
 |
| before | String | <p></p>
 |
| last | Int | <p></p>
 |




#### allSpecies

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| after | String | <p></p>
 |
| first | Int | <p></p>
 |
| before | String | <p></p>
 |
| last | Int | <p></p>
 |




#### allStarships

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| after | String | <p></p>
 |
| first | Int | <p></p>
 |
| before | String | <p></p>
 |
| last | Int | <p></p>
 |




#### allVehicles

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| after | String | <p></p>
 |
| first | Int | <p></p>
 |
| before | String | <p></p>
 |
| last | Int | <p></p>
 |




#### film

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| id | ID | <p></p>
 |
| filmID | ID | <p></p>
 |




#### node

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| id | ID! | <p>The ID of an object</p>
 |




#### person

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| id | ID | <p></p>
 |
| personID | ID | <p></p>
 |




#### planet

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| id | ID | <p></p>
 |
| planetID | ID | <p></p>
 |




#### species

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| id | ID | <p></p>
 |
| speciesID | ID | <p></p>
 |




#### starship

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| id | ID | <p></p>
 |
| starshipID | ID | <p></p>
 |




#### vehicle

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| id | ID | <p></p>
 |
| vehicleID | ID | <p></p>
 |








## Objects

### About objects
Objects in GraphQL represent the resources you can access. An object can 
contain a list of fields, which are specifically typed.


### Film 
<p>A single film.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| title | String | <p>The title of this film.</p>
 |
| episodeID | Int | <p>The episode number of this film.</p>
 |
| openingCrawl | String | <p>The opening paragraphs at the beginning of this film.</p>
 |
| director | String | <p>The name of the director of this film.</p>
 |
| producers | [String] | <p>The name(s) of the producer(s) of this film.</p>
 |
| releaseDate | String | <p>The ISO 8601 date format of film release at original creator country.</p>
 |
| speciesConnection | FilmSpeciesConnection | <p></p>
 |
| starshipConnection | FilmStarshipsConnection | <p></p>
 |
| vehicleConnection | FilmVehiclesConnection | <p></p>
 |
| characterConnection | FilmCharactersConnection | <p></p>
 |
| planetConnection | FilmPlanetsConnection | <p></p>
 |
| created | String | <p>The ISO 8601 date format of the time that this resource was created.</p>
 |
| edited | String | <p>The ISO 8601 date format of the time that this resource was edited.</p>
 |
| id | ID! | <p>The ID of an object</p>
 |



### FilmCharactersConnection 
<p>A connection to a list of items.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | <p>Information to aid in pagination.</p>
 |
| edges | [FilmCharactersEdge] | <p>A list of edges.</p>
 |
| totalCount | Int | <p>A count of the total number of objects in this connection, ignoring pagination.
This allows a client to fetch the first five objects by passing "5" as the
argument to "first", then fetch the total count so it could display "5 of 83",
for example.</p>
 |
| characters | [Person] | <p>A list of all of the objects returned in the connection. This is a convenience
field provided for quickly exploring the API; rather than querying for
"{ edges { node } }" when no edge data is needed, this field can be be used
instead. Note that when clients like Relay need to fetch the "cursor" field on
the edge to enable efficient pagination, this shortcut cannot be used, and the
full "{ edges { node } }" version should be used instead.</p>
 |



### FilmCharactersEdge 
<p>An edge in a connection.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Person | <p>The item at the end of the edge</p>
 |
| cursor | String! | <p>A cursor for use in pagination</p>
 |



### FilmPlanetsConnection 
<p>A connection to a list of items.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | <p>Information to aid in pagination.</p>
 |
| edges | [FilmPlanetsEdge] | <p>A list of edges.</p>
 |
| totalCount | Int | <p>A count of the total number of objects in this connection, ignoring pagination.
This allows a client to fetch the first five objects by passing "5" as the
argument to "first", then fetch the total count so it could display "5 of 83",
for example.</p>
 |
| planets | [Planet] | <p>A list of all of the objects returned in the connection. This is a convenience
field provided for quickly exploring the API; rather than querying for
"{ edges { node } }" when no edge data is needed, this field can be be used
instead. Note that when clients like Relay need to fetch the "cursor" field on
the edge to enable efficient pagination, this shortcut cannot be used, and the
full "{ edges { node } }" version should be used instead.</p>
 |



### FilmPlanetsEdge 
<p>An edge in a connection.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Planet | <p>The item at the end of the edge</p>
 |
| cursor | String! | <p>A cursor for use in pagination</p>
 |



### FilmSpeciesConnection 
<p>A connection to a list of items.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | <p>Information to aid in pagination.</p>
 |
| edges | [FilmSpeciesEdge] | <p>A list of edges.</p>
 |
| totalCount | Int | <p>A count of the total number of objects in this connection, ignoring pagination.
This allows a client to fetch the first five objects by passing "5" as the
argument to "first", then fetch the total count so it could display "5 of 83",
for example.</p>
 |
| species | [Species] | <p>A list of all of the objects returned in the connection. This is a convenience
field provided for quickly exploring the API; rather than querying for
"{ edges { node } }" when no edge data is needed, this field can be be used
instead. Note that when clients like Relay need to fetch the "cursor" field on
the edge to enable efficient pagination, this shortcut cannot be used, and the
full "{ edges { node } }" version should be used instead.</p>
 |



### FilmSpeciesEdge 
<p>An edge in a connection.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Species | <p>The item at the end of the edge</p>
 |
| cursor | String! | <p>A cursor for use in pagination</p>
 |



### FilmStarshipsConnection 
<p>A connection to a list of items.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | <p>Information to aid in pagination.</p>
 |
| edges | [FilmStarshipsEdge] | <p>A list of edges.</p>
 |
| totalCount | Int | <p>A count of the total number of objects in this connection, ignoring pagination.
This allows a client to fetch the first five objects by passing "5" as the
argument to "first", then fetch the total count so it could display "5 of 83",
for example.</p>
 |
| starships | [Starship] | <p>A list of all of the objects returned in the connection. This is a convenience
field provided for quickly exploring the API; rather than querying for
"{ edges { node } }" when no edge data is needed, this field can be be used
instead. Note that when clients like Relay need to fetch the "cursor" field on
the edge to enable efficient pagination, this shortcut cannot be used, and the
full "{ edges { node } }" version should be used instead.</p>
 |



### FilmStarshipsEdge 
<p>An edge in a connection.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Starship | <p>The item at the end of the edge</p>
 |
| cursor | String! | <p>A cursor for use in pagination</p>
 |



### FilmVehiclesConnection 
<p>A connection to a list of items.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | <p>Information to aid in pagination.</p>
 |
| edges | [FilmVehiclesEdge] | <p>A list of edges.</p>
 |
| totalCount | Int | <p>A count of the total number of objects in this connection, ignoring pagination.
This allows a client to fetch the first five objects by passing "5" as the
argument to "first", then fetch the total count so it could display "5 of 83",
for example.</p>
 |
| vehicles | [Vehicle] | <p>A list of all of the objects returned in the connection. This is a convenience
field provided for quickly exploring the API; rather than querying for
"{ edges { node } }" when no edge data is needed, this field can be be used
instead. Note that when clients like Relay need to fetch the "cursor" field on
the edge to enable efficient pagination, this shortcut cannot be used, and the
full "{ edges { node } }" version should be used instead.</p>
 |



### FilmVehiclesEdge 
<p>An edge in a connection.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Vehicle | <p>The item at the end of the edge</p>
 |
| cursor | String! | <p>A cursor for use in pagination</p>
 |



### FilmsConnection 
<p>A connection to a list of items.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | <p>Information to aid in pagination.</p>
 |
| edges | [FilmsEdge] | <p>A list of edges.</p>
 |
| totalCount | Int | <p>A count of the total number of objects in this connection, ignoring pagination.
This allows a client to fetch the first five objects by passing "5" as the
argument to "first", then fetch the total count so it could display "5 of 83",
for example.</p>
 |
| films | [Film] | <p>A list of all of the objects returned in the connection. This is a convenience
field provided for quickly exploring the API; rather than querying for
"{ edges { node } }" when no edge data is needed, this field can be be used
instead. Note that when clients like Relay need to fetch the "cursor" field on
the edge to enable efficient pagination, this shortcut cannot be used, and the
full "{ edges { node } }" version should be used instead.</p>
 |



### FilmsEdge 
<p>An edge in a connection.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Film | <p>The item at the end of the edge</p>
 |
| cursor | String! | <p>A cursor for use in pagination</p>
 |



### PageInfo 
<p>Information about pagination in a connection.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| hasNextPage | Boolean! | <p>When paginating forwards, are there more items?</p>
 |
| hasPreviousPage | Boolean! | <p>When paginating backwards, are there more items?</p>
 |
| startCursor | String | <p>When paginating backwards, the cursor to continue.</p>
 |
| endCursor | String | <p>When paginating forwards, the cursor to continue.</p>
 |



### PeopleConnection 
<p>A connection to a list of items.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | <p>Information to aid in pagination.</p>
 |
| edges | [PeopleEdge] | <p>A list of edges.</p>
 |
| totalCount | Int | <p>A count of the total number of objects in this connection, ignoring pagination.
This allows a client to fetch the first five objects by passing "5" as the
argument to "first", then fetch the total count so it could display "5 of 83",
for example.</p>
 |
| people | [Person] | <p>A list of all of the objects returned in the connection. This is a convenience
field provided for quickly exploring the API; rather than querying for
"{ edges { node } }" when no edge data is needed, this field can be be used
instead. Note that when clients like Relay need to fetch the "cursor" field on
the edge to enable efficient pagination, this shortcut cannot be used, and the
full "{ edges { node } }" version should be used instead.</p>
 |



### PeopleEdge 
<p>An edge in a connection.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Person | <p>The item at the end of the edge</p>
 |
| cursor | String! | <p>A cursor for use in pagination</p>
 |



### Person 
<p>An individual person or character within the Star Wars universe.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| name | String | <p>The name of this person.</p>
 |
| birthYear | String | <p>The birth year of the person, using the in-universe standard of BBY or ABY -
Before the Battle of Yavin or After the Battle of Yavin. The Battle of Yavin is
a battle that occurs at the end of Star Wars episode IV: A New Hope.</p>
 |
| eyeColor | String | <p>The eye color of this person. Will be "unknown" if not known or "n/a" if the
person does not have an eye.</p>
 |
| gender | String | <p>The gender of this person. Either "Male", "Female" or "unknown",
"n/a" if the person does not have a gender.</p>
 |
| hairColor | String | <p>The hair color of this person. Will be "unknown" if not known or "n/a" if the
person does not have hair.</p>
 |
| height | Int | <p>The height of the person in centimeters.</p>
 |
| mass | Float | <p>The mass of the person in kilograms.</p>
 |
| skinColor | String | <p>The skin color of this person.</p>
 |
| homeworld | Planet | <p>A planet that this person was born on or inhabits.</p>
 |
| filmConnection | PersonFilmsConnection | <p></p>
 |
| species | Species | <p>The species that this person belongs to, or null if unknown.</p>
 |
| starshipConnection | PersonStarshipsConnection | <p></p>
 |
| vehicleConnection | PersonVehiclesConnection | <p></p>
 |
| created | String | <p>The ISO 8601 date format of the time that this resource was created.</p>
 |
| edited | String | <p>The ISO 8601 date format of the time that this resource was edited.</p>
 |
| id | ID! | <p>The ID of an object</p>
 |



### PersonFilmsConnection 
<p>A connection to a list of items.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | <p>Information to aid in pagination.</p>
 |
| edges | [PersonFilmsEdge] | <p>A list of edges.</p>
 |
| totalCount | Int | <p>A count of the total number of objects in this connection, ignoring pagination.
This allows a client to fetch the first five objects by passing "5" as the
argument to "first", then fetch the total count so it could display "5 of 83",
for example.</p>
 |
| films | [Film] | <p>A list of all of the objects returned in the connection. This is a convenience
field provided for quickly exploring the API; rather than querying for
"{ edges { node } }" when no edge data is needed, this field can be be used
instead. Note that when clients like Relay need to fetch the "cursor" field on
the edge to enable efficient pagination, this shortcut cannot be used, and the
full "{ edges { node } }" version should be used instead.</p>
 |



### PersonFilmsEdge 
<p>An edge in a connection.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Film | <p>The item at the end of the edge</p>
 |
| cursor | String! | <p>A cursor for use in pagination</p>
 |



### PersonStarshipsConnection 
<p>A connection to a list of items.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | <p>Information to aid in pagination.</p>
 |
| edges | [PersonStarshipsEdge] | <p>A list of edges.</p>
 |
| totalCount | Int | <p>A count of the total number of objects in this connection, ignoring pagination.
This allows a client to fetch the first five objects by passing "5" as the
argument to "first", then fetch the total count so it could display "5 of 83",
for example.</p>
 |
| starships | [Starship] | <p>A list of all of the objects returned in the connection. This is a convenience
field provided for quickly exploring the API; rather than querying for
"{ edges { node } }" when no edge data is needed, this field can be be used
instead. Note that when clients like Relay need to fetch the "cursor" field on
the edge to enable efficient pagination, this shortcut cannot be used, and the
full "{ edges { node } }" version should be used instead.</p>
 |



### PersonStarshipsEdge 
<p>An edge in a connection.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Starship | <p>The item at the end of the edge</p>
 |
| cursor | String! | <p>A cursor for use in pagination</p>
 |



### PersonVehiclesConnection 
<p>A connection to a list of items.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | <p>Information to aid in pagination.</p>
 |
| edges | [PersonVehiclesEdge] | <p>A list of edges.</p>
 |
| totalCount | Int | <p>A count of the total number of objects in this connection, ignoring pagination.
This allows a client to fetch the first five objects by passing "5" as the
argument to "first", then fetch the total count so it could display "5 of 83",
for example.</p>
 |
| vehicles | [Vehicle] | <p>A list of all of the objects returned in the connection. This is a convenience
field provided for quickly exploring the API; rather than querying for
"{ edges { node } }" when no edge data is needed, this field can be be used
instead. Note that when clients like Relay need to fetch the "cursor" field on
the edge to enable efficient pagination, this shortcut cannot be used, and the
full "{ edges { node } }" version should be used instead.</p>
 |



### PersonVehiclesEdge 
<p>An edge in a connection.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Vehicle | <p>The item at the end of the edge</p>
 |
| cursor | String! | <p>A cursor for use in pagination</p>
 |



### Photo 
<p></p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| height | Int | <p></p>
 |
| width | Int | <p></p>
 |



### Planet 
<p>A large mass, planet or planetoid in the Star Wars Universe, at the time of
0 ABY.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| name | String | <p>The name of this planet.</p>
 |
| diameter | Int | <p>The diameter of this planet in kilometers.</p>
 |
| rotationPeriod | Int | <p>The number of standard hours it takes for this planet to complete a single
rotation on its axis.</p>
 |
| orbitalPeriod | Int | <p>The number of standard days it takes for this planet to complete a single orbit
of its local star.</p>
 |
| gravity | String | <p>A number denoting the gravity of this planet, where "1" is normal or 1 standard
G. "2" is twice or 2 standard Gs. "0.5" is half or 0.5 standard Gs.</p>
 |
| population | Float | <p>The average population of sentient beings inhabiting this planet.</p>
 |
| climates | [String] | <p>The climates of this planet.</p>
 |
| terrains | [String] | <p>The terrains of this planet.</p>
 |
| surfaceWater | Float | <p>The percentage of the planet surface that is naturally occuring water or bodies
of water.</p>
 |
| residentConnection | PlanetResidentsConnection | <p></p>
 |
| filmConnection | PlanetFilmsConnection | <p></p>
 |
| created | String | <p>The ISO 8601 date format of the time that this resource was created.</p>
 |
| edited | String | <p>The ISO 8601 date format of the time that this resource was edited.</p>
 |
| id | ID! | <p>The ID of an object</p>
 |



### PlanetFilmsConnection 
<p>A connection to a list of items.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | <p>Information to aid in pagination.</p>
 |
| edges | [PlanetFilmsEdge] | <p>A list of edges.</p>
 |
| totalCount | Int | <p>A count of the total number of objects in this connection, ignoring pagination.
This allows a client to fetch the first five objects by passing "5" as the
argument to "first", then fetch the total count so it could display "5 of 83",
for example.</p>
 |
| films | [Film] | <p>A list of all of the objects returned in the connection. This is a convenience
field provided for quickly exploring the API; rather than querying for
"{ edges { node } }" when no edge data is needed, this field can be be used
instead. Note that when clients like Relay need to fetch the "cursor" field on
the edge to enable efficient pagination, this shortcut cannot be used, and the
full "{ edges { node } }" version should be used instead.</p>
 |



### PlanetFilmsEdge 
<p>An edge in a connection.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Film | <p>The item at the end of the edge</p>
 |
| cursor | String! | <p>A cursor for use in pagination</p>
 |



### PlanetResidentsConnection 
<p>A connection to a list of items.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | <p>Information to aid in pagination.</p>
 |
| edges | [PlanetResidentsEdge] | <p>A list of edges.</p>
 |
| totalCount | Int | <p>A count of the total number of objects in this connection, ignoring pagination.
This allows a client to fetch the first five objects by passing "5" as the
argument to "first", then fetch the total count so it could display "5 of 83",
for example.</p>
 |
| residents | [Person] | <p>A list of all of the objects returned in the connection. This is a convenience
field provided for quickly exploring the API; rather than querying for
"{ edges { node } }" when no edge data is needed, this field can be be used
instead. Note that when clients like Relay need to fetch the "cursor" field on
the edge to enable efficient pagination, this shortcut cannot be used, and the
full "{ edges { node } }" version should be used instead.</p>
 |



### PlanetResidentsEdge 
<p>An edge in a connection.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Person | <p>The item at the end of the edge</p>
 |
| cursor | String! | <p>A cursor for use in pagination</p>
 |



### PlanetsConnection 
<p>A connection to a list of items.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | <p>Information to aid in pagination.</p>
 |
| edges | [PlanetsEdge] | <p>A list of edges.</p>
 |
| totalCount | Int | <p>A count of the total number of objects in this connection, ignoring pagination.
This allows a client to fetch the first five objects by passing "5" as the
argument to "first", then fetch the total count so it could display "5 of 83",
for example.</p>
 |
| planets | [Planet] | <p>A list of all of the objects returned in the connection. This is a convenience
field provided for quickly exploring the API; rather than querying for
"{ edges { node } }" when no edge data is needed, this field can be be used
instead. Note that when clients like Relay need to fetch the "cursor" field on
the edge to enable efficient pagination, this shortcut cannot be used, and the
full "{ edges { node } }" version should be used instead.</p>
 |



### PlanetsEdge 
<p>An edge in a connection.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Planet | <p>The item at the end of the edge</p>
 |
| cursor | String! | <p>A cursor for use in pagination</p>
 |



### SearchQuery 
<p></p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| firstSearchResult | SearchResult | <p></p>
 |



### Species 
<p>A type of person or character within the Star Wars Universe.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| name | String | <p>The name of this species.</p>
 |
| classification | String | <p>The classification of this species, such as "mammal" or "reptile".</p>
 |
| designation | String | <p>The designation of this species, such as "sentient".</p>
 |
| averageHeight | Float | <p>The average height of this species in centimeters.</p>
 |
| averageLifespan | Int | <p>The average lifespan of this species in years, null if unknown.</p>
 |
| eyeColors | [String] | <p>Common eye colors for this species, null if this species does not typically
have eyes.</p>
 |
| hairColors | [String] | <p>Common hair colors for this species, null if this species does not typically
have hair.</p>
 |
| skinColors | [String] | <p>Common skin colors for this species, null if this species does not typically
have skin.</p>
 |
| language | String | <p>The language commonly spoken by this species.</p>
 |
| homeworld | Planet | <p>A planet that this species originates from.</p>
 |
| personConnection | SpeciesPeopleConnection | <p></p>
 |
| filmConnection | SpeciesFilmsConnection | <p></p>
 |
| created | String | <p>The ISO 8601 date format of the time that this resource was created.</p>
 |
| edited | String | <p>The ISO 8601 date format of the time that this resource was edited.</p>
 |
| id | ID! | <p>The ID of an object</p>
 |



### SpeciesConnection 
<p>A connection to a list of items.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | <p>Information to aid in pagination.</p>
 |
| edges | [SpeciesEdge] | <p>A list of edges.</p>
 |
| totalCount | Int | <p>A count of the total number of objects in this connection, ignoring pagination.
This allows a client to fetch the first five objects by passing "5" as the
argument to "first", then fetch the total count so it could display "5 of 83",
for example.</p>
 |
| species | [Species] | <p>A list of all of the objects returned in the connection. This is a convenience
field provided for quickly exploring the API; rather than querying for
"{ edges { node } }" when no edge data is needed, this field can be be used
instead. Note that when clients like Relay need to fetch the "cursor" field on
the edge to enable efficient pagination, this shortcut cannot be used, and the
full "{ edges { node } }" version should be used instead.</p>
 |



### SpeciesEdge 
<p>An edge in a connection.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Species | <p>The item at the end of the edge</p>
 |
| cursor | String! | <p>A cursor for use in pagination</p>
 |



### SpeciesFilmsConnection 
<p>A connection to a list of items.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | <p>Information to aid in pagination.</p>
 |
| edges | [SpeciesFilmsEdge] | <p>A list of edges.</p>
 |
| totalCount | Int | <p>A count of the total number of objects in this connection, ignoring pagination.
This allows a client to fetch the first five objects by passing "5" as the
argument to "first", then fetch the total count so it could display "5 of 83",
for example.</p>
 |
| films | [Film] | <p>A list of all of the objects returned in the connection. This is a convenience
field provided for quickly exploring the API; rather than querying for
"{ edges { node } }" when no edge data is needed, this field can be be used
instead. Note that when clients like Relay need to fetch the "cursor" field on
the edge to enable efficient pagination, this shortcut cannot be used, and the
full "{ edges { node } }" version should be used instead.</p>
 |



### SpeciesFilmsEdge 
<p>An edge in a connection.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Film | <p>The item at the end of the edge</p>
 |
| cursor | String! | <p>A cursor for use in pagination</p>
 |



### SpeciesPeopleConnection 
<p>A connection to a list of items.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | <p>Information to aid in pagination.</p>
 |
| edges | [SpeciesPeopleEdge] | <p>A list of edges.</p>
 |
| totalCount | Int | <p>A count of the total number of objects in this connection, ignoring pagination.
This allows a client to fetch the first five objects by passing "5" as the
argument to "first", then fetch the total count so it could display "5 of 83",
for example.</p>
 |
| people | [Person] | <p>A list of all of the objects returned in the connection. This is a convenience
field provided for quickly exploring the API; rather than querying for
"{ edges { node } }" when no edge data is needed, this field can be be used
instead. Note that when clients like Relay need to fetch the "cursor" field on
the edge to enable efficient pagination, this shortcut cannot be used, and the
full "{ edges { node } }" version should be used instead.</p>
 |



### SpeciesPeopleEdge 
<p>An edge in a connection.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Person | <p>The item at the end of the edge</p>
 |
| cursor | String! | <p>A cursor for use in pagination</p>
 |



### Starship 
<p>A single transport craft that has hyperdrive capability.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| name | String | <p>The name of this starship. The common name, such as "Death Star".</p>
 |
| model | String | <p>The model or official name of this starship. Such as "T-65 X-wing" or "DS-1
Orbital Battle Station".</p>
 |
| starshipClass | String | <p>The class of this starship, such as "Starfighter" or "Deep Space Mobile
Battlestation"</p>
 |
| manufacturers | [String] | <p>The manufacturers of this starship.</p>
 |
| costInCredits | Float | <p>The cost of this starship new, in galactic credits.</p>
 |
| length | Float | <p>The length of this starship in meters.</p>
 |
| crew | String | <p>The number of personnel needed to run or pilot this starship.</p>
 |
| passengers | String | <p>The number of non-essential people this starship can transport.</p>
 |
| maxAtmospheringSpeed | Int | <p>The maximum speed of this starship in atmosphere. null if this starship is
incapable of atmosphering flight.</p>
 |
| hyperdriveRating | Float | <p>The class of this starships hyperdrive.</p>
 |
| MGLT | Int | <p>The Maximum number of Megalights this starship can travel in a standard hour.
A "Megalight" is a standard unit of distance and has never been defined before
within the Star Wars universe. This figure is only really useful for measuring
the difference in speed of starships. We can assume it is similar to AU, the
distance between our Sun (Sol) and Earth.</p>
 |
| cargoCapacity | Float | <p>The maximum number of kilograms that this starship can transport.</p>
 |
| consumables | String | <p>The maximum length of time that this starship can provide consumables for its
entire crew without having to resupply.</p>
 |
| pilotConnection | StarshipPilotsConnection | <p></p>
 |
| filmConnection | StarshipFilmsConnection | <p></p>
 |
| created | String | <p>The ISO 8601 date format of the time that this resource was created.</p>
 |
| edited | String | <p>The ISO 8601 date format of the time that this resource was edited.</p>
 |
| id | ID! | <p>The ID of an object</p>
 |



### StarshipFilmsConnection 
<p>A connection to a list of items.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | <p>Information to aid in pagination.</p>
 |
| edges | [StarshipFilmsEdge] | <p>A list of edges.</p>
 |
| totalCount | Int | <p>A count of the total number of objects in this connection, ignoring pagination.
This allows a client to fetch the first five objects by passing "5" as the
argument to "first", then fetch the total count so it could display "5 of 83",
for example.</p>
 |
| films | [Film] | <p>A list of all of the objects returned in the connection. This is a convenience
field provided for quickly exploring the API; rather than querying for
"{ edges { node } }" when no edge data is needed, this field can be be used
instead. Note that when clients like Relay need to fetch the "cursor" field on
the edge to enable efficient pagination, this shortcut cannot be used, and the
full "{ edges { node } }" version should be used instead.</p>
 |



### StarshipFilmsEdge 
<p>An edge in a connection.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Film | <p>The item at the end of the edge</p>
 |
| cursor | String! | <p>A cursor for use in pagination</p>
 |



### StarshipPilotsConnection 
<p>A connection to a list of items.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | <p>Information to aid in pagination.</p>
 |
| edges | [StarshipPilotsEdge] | <p>A list of edges.</p>
 |
| totalCount | Int | <p>A count of the total number of objects in this connection, ignoring pagination.
This allows a client to fetch the first five objects by passing "5" as the
argument to "first", then fetch the total count so it could display "5 of 83",
for example.</p>
 |
| pilots | [Person] | <p>A list of all of the objects returned in the connection. This is a convenience
field provided for quickly exploring the API; rather than querying for
"{ edges { node } }" when no edge data is needed, this field can be be used
instead. Note that when clients like Relay need to fetch the "cursor" field on
the edge to enable efficient pagination, this shortcut cannot be used, and the
full "{ edges { node } }" version should be used instead.</p>
 |



### StarshipPilotsEdge 
<p>An edge in a connection.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Person | <p>The item at the end of the edge</p>
 |
| cursor | String! | <p>A cursor for use in pagination</p>
 |



### StarshipsConnection 
<p>A connection to a list of items.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | <p>Information to aid in pagination.</p>
 |
| edges | [StarshipsEdge] | <p>A list of edges.</p>
 |
| totalCount | Int | <p>A count of the total number of objects in this connection, ignoring pagination.
This allows a client to fetch the first five objects by passing "5" as the
argument to "first", then fetch the total count so it could display "5 of 83",
for example.</p>
 |
| starships | [Starship] | <p>A list of all of the objects returned in the connection. This is a convenience
field provided for quickly exploring the API; rather than querying for
"{ edges { node } }" when no edge data is needed, this field can be be used
instead. Note that when clients like Relay need to fetch the "cursor" field on
the edge to enable efficient pagination, this shortcut cannot be used, and the
full "{ edges { node } }" version should be used instead.</p>
 |



### StarshipsEdge 
<p>An edge in a connection.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Starship | <p>The item at the end of the edge</p>
 |
| cursor | String! | <p>A cursor for use in pagination</p>
 |



### Vehicle 
<p>A single transport craft that does not have hyperdrive capability</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| name | String | <p>The name of this vehicle. The common name, such as "Sand Crawler" or "Speeder
bike".</p>
 |
| model | String | <p>The model or official name of this vehicle. Such as "All-Terrain Attack
Transport".</p>
 |
| vehicleClass | String | <p>The class of this vehicle, such as "Wheeled" or "Repulsorcraft".</p>
 |
| manufacturers | [String] | <p>The manufacturers of this vehicle.</p>
 |
| costInCredits | Float | <p>The cost of this vehicle new, in Galactic Credits.</p>
 |
| length | Float | <p>The length of this vehicle in meters.</p>
 |
| crew | String | <p>The number of personnel needed to run or pilot this vehicle.</p>
 |
| passengers | String | <p>The number of non-essential people this vehicle can transport.</p>
 |
| maxAtmospheringSpeed | Int | <p>The maximum speed of this vehicle in atmosphere.</p>
 |
| cargoCapacity | Float | <p>The maximum number of kilograms that this vehicle can transport.</p>
 |
| consumables | String | <p>The maximum length of time that this vehicle can provide consumables for its
entire crew without having to resupply.</p>
 |
| pilotConnection | VehiclePilotsConnection | <p></p>
 |
| filmConnection | VehicleFilmsConnection | <p></p>
 |
| created | String | <p>The ISO 8601 date format of the time that this resource was created.</p>
 |
| edited | String | <p>The ISO 8601 date format of the time that this resource was edited.</p>
 |
| id | ID! | <p>The ID of an object</p>
 |



### VehicleFilmsConnection 
<p>A connection to a list of items.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | <p>Information to aid in pagination.</p>
 |
| edges | [VehicleFilmsEdge] | <p>A list of edges.</p>
 |
| totalCount | Int | <p>A count of the total number of objects in this connection, ignoring pagination.
This allows a client to fetch the first five objects by passing "5" as the
argument to "first", then fetch the total count so it could display "5 of 83",
for example.</p>
 |
| films | [Film] | <p>A list of all of the objects returned in the connection. This is a convenience
field provided for quickly exploring the API; rather than querying for
"{ edges { node } }" when no edge data is needed, this field can be be used
instead. Note that when clients like Relay need to fetch the "cursor" field on
the edge to enable efficient pagination, this shortcut cannot be used, and the
full "{ edges { node } }" version should be used instead.</p>
 |



### VehicleFilmsEdge 
<p>An edge in a connection.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Film | <p>The item at the end of the edge</p>
 |
| cursor | String! | <p>A cursor for use in pagination</p>
 |



### VehiclePilotsConnection 
<p>A connection to a list of items.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | <p>Information to aid in pagination.</p>
 |
| edges | [VehiclePilotsEdge] | <p>A list of edges.</p>
 |
| totalCount | Int | <p>A count of the total number of objects in this connection, ignoring pagination.
This allows a client to fetch the first five objects by passing "5" as the
argument to "first", then fetch the total count so it could display "5 of 83",
for example.</p>
 |
| pilots | [Person] | <p>A list of all of the objects returned in the connection. This is a convenience
field provided for quickly exploring the API; rather than querying for
"{ edges { node } }" when no edge data is needed, this field can be be used
instead. Note that when clients like Relay need to fetch the "cursor" field on
the edge to enable efficient pagination, this shortcut cannot be used, and the
full "{ edges { node } }" version should be used instead.</p>
 |



### VehiclePilotsEdge 
<p>An edge in a connection.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Person | <p>The item at the end of the edge</p>
 |
| cursor | String! | <p>A cursor for use in pagination</p>
 |



### VehiclesConnection 
<p>A connection to a list of items.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | <p>Information to aid in pagination.</p>
 |
| edges | [VehiclesEdge] | <p>A list of edges.</p>
 |
| totalCount | Int | <p>A count of the total number of objects in this connection, ignoring pagination.
This allows a client to fetch the first five objects by passing "5" as the
argument to "first", then fetch the total count so it could display "5 of 83",
for example.</p>
 |
| vehicles | [Vehicle] | <p>A list of all of the objects returned in the connection. This is a convenience
field provided for quickly exploring the API; rather than querying for
"{ edges { node } }" when no edge data is needed, this field can be be used
instead. Note that when clients like Relay need to fetch the "cursor" field on
the edge to enable efficient pagination, this shortcut cannot be used, and the
full "{ edges { node } }" version should be used instead.</p>
 |



### VehiclesEdge 
<p>An edge in a connection.</p>



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Vehicle | <p>The item at the end of the edge</p>
 |
| cursor | String! | <p>A cursor for use in pagination</p>
 |






## Interfaces

### About interfaces
Interfaces serve as parent objects from which other objects can inherit.


### Node
<p>An object with an ID</p>




- Film

- Person

- Planet

- Species

- Starship

- Vehicle



### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| id | ID! |  <p>The id of the object.</p>
 |   


### Fields' arguments








## Enums

### About enums
Enums represent possible sets of values for a field.


### Direction
<p></p>


#### Values

| ** Value ** | **Description** | 
|-------------|--------------------|
| NORTH | <p></p>
 | 
| EAST | <p></p>
 | 
| SOUTH | <p></p>
 | 
| WEST | <p></p>
 | 

  



## Unions

### About unions
A union is a type of object representing many objects.


### SearchResult   
<p></p>


#### Possible types
        
- Photo
        
- Person





## Input objects

### About input objects
Input objects can be described as "composable objects" because they include 
a set of input fields that define the object.


### Point2D
<p></p>


### Input fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| x | Float | <p></p>
 |
| y | Float | <p></p>
 |





## Scalars

### About scalars
Scalars are primitive values: Int, Float, String, Boolean, or ID. When calling 
the GraphQL API, you must specify nested subfields until you return only scalars.


### Boolean
<p>The <code>Boolean</code> scalar type represents <code>true</code> or <code>false</code>.</p>


### Float
<p>The <code>Float</code> scalar type represents signed double-precision fractional values as specified by <a href="https://en.wikipedia.org/wiki/IEEE_floating_point">IEEE 754</a>.</p>


### ID
<p>The <code>ID</code> scalar type represents a unique identifier, often used to refetch an object or as key for a cache. The ID type appears in a JSON response as a String; however, it is not intended to be human-readable. When expected as an input type, any string (such as <code>"4"</code>) or integer (such as <code>4</code>) input value will be accepted as an ID.</p>


### Int
<p>The <code>Int</code> scalar type represents non-fractional signed whole numeric values. Int can represent values between -(2^31) and 2^31 - 1.</p>


### String
<p>The <code>String</code> scalar type represents textual data, represented as UTF-8 character sequences. The String type is most often used by GraphQL to represent free-form human-readable text.</p>


### Time
<p></p>


### Url
<p></p>