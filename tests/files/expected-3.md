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
| allFilms | FilmsConnection |  |
| allPeople | PeopleConnection |  |
| allPlanets | PlanetsConnection |  |
| allSpecies | SpeciesConnection |  |
| allStarships | StarshipsConnection |  |
| allVehicles | VehiclesConnection |  |
| film | Film |  |
| node | Node | Fetches an object given its ID |
| person | Person |  |
| planet | Planet |  |
| species | Species |  |
| starship | Starship |  |
| vehicle | Vehicle |  |


### Queries arguments


#### allFilms

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| after | String |  |
| first | Int |  |
| before | String |  |
| last | Int |  |




#### allPeople

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| after | String |  |
| first | Int |  |
| before | String |  |
| last | Int |  |




#### allPlanets

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| after | String |  |
| first | Int |  |
| before | String |  |
| last | Int |  |




#### allSpecies

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| after | String |  |
| first | Int |  |
| before | String |  |
| last | Int |  |




#### allStarships

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| after | String |  |
| first | Int |  |
| before | String |  |
| last | Int |  |




#### allVehicles

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| after | String |  |
| first | Int |  |
| before | String |  |
| last | Int |  |




#### film

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| id | ID |  |
| filmID | ID |  |




#### node

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| id | ID! | The ID of an object |




#### person

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| id | ID |  |
| personID | ID |  |




#### planet

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| id | ID |  |
| planetID | ID |  |




#### species

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| id | ID |  |
| speciesID | ID |  |




#### starship

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| id | ID |  |
| starshipID | ID |  |




#### vehicle

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| id | ID |  |
| vehicleID | ID |  |








## Objects

### About objects
Objects in GraphQL represent the resources you can access. An object can 
contain a list of fields, which are specifically typed.


### Film 
A single film.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| title | String | The title of this film. |
| episodeID | Int | The episode number of this film. |
| openingCrawl | String | The opening paragraphs at the beginning of this film. |
| director | String | The name of the director of this film. |
| producers | [String] | The name(s) of the producer(s) of this film. |
| releaseDate | String | The ISO 8601 date format of film release at original creator country. |
| speciesConnection | FilmSpeciesConnection |  |
| starshipConnection | FilmStarshipsConnection |  |
| vehicleConnection | FilmVehiclesConnection |  |
| characterConnection | FilmCharactersConnection |  |
| planetConnection | FilmPlanetsConnection |  |
| created | String | The ISO 8601 date format of the time that this resource was created. |
| edited | String | The ISO 8601 date format of the time that this resource was edited. |
| id | ID! | The ID of an object |



### FilmCharactersConnection 
A connection to a list of items.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | Information to aid in pagination. |
| edges | [FilmCharactersEdge] | A list of edges. |
| totalCount | Int | A count of the total number of objects in this connection, ignoring pagination.This allows a client to fetch the first five objects by passing "5" as theargument to "first", then fetch the total count so it could display "5 of 83",for example. |
| characters | [Person] | A list of all of the objects returned in the connection. This is a conveniencefield provided for quickly exploring the API; rather than querying for"{ edges { node } }" when no edge data is needed, this field can be be usedinstead. Note that when clients like Relay need to fetch the "cursor" field onthe edge to enable efficient pagination, this shortcut cannot be used, and thefull "{ edges { node } }" version should be used instead. |



### FilmCharactersEdge 
An edge in a connection.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Person | The item at the end of the edge |
| cursor | String! | A cursor for use in pagination |



### FilmPlanetsConnection 
A connection to a list of items.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | Information to aid in pagination. |
| edges | [FilmPlanetsEdge] | A list of edges. |
| totalCount | Int | A count of the total number of objects in this connection, ignoring pagination.This allows a client to fetch the first five objects by passing "5" as theargument to "first", then fetch the total count so it could display "5 of 83",for example. |
| planets | [Planet] | A list of all of the objects returned in the connection. This is a conveniencefield provided for quickly exploring the API; rather than querying for"{ edges { node } }" when no edge data is needed, this field can be be usedinstead. Note that when clients like Relay need to fetch the "cursor" field onthe edge to enable efficient pagination, this shortcut cannot be used, and thefull "{ edges { node } }" version should be used instead. |



### FilmPlanetsEdge 
An edge in a connection.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Planet | The item at the end of the edge |
| cursor | String! | A cursor for use in pagination |



### FilmSpeciesConnection 
A connection to a list of items.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | Information to aid in pagination. |
| edges | [FilmSpeciesEdge] | A list of edges. |
| totalCount | Int | A count of the total number of objects in this connection, ignoring pagination.This allows a client to fetch the first five objects by passing "5" as theargument to "first", then fetch the total count so it could display "5 of 83",for example. |
| species | [Species] | A list of all of the objects returned in the connection. This is a conveniencefield provided for quickly exploring the API; rather than querying for"{ edges { node } }" when no edge data is needed, this field can be be usedinstead. Note that when clients like Relay need to fetch the "cursor" field onthe edge to enable efficient pagination, this shortcut cannot be used, and thefull "{ edges { node } }" version should be used instead. |



### FilmSpeciesEdge 
An edge in a connection.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Species | The item at the end of the edge |
| cursor | String! | A cursor for use in pagination |



### FilmStarshipsConnection 
A connection to a list of items.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | Information to aid in pagination. |
| edges | [FilmStarshipsEdge] | A list of edges. |
| totalCount | Int | A count of the total number of objects in this connection, ignoring pagination.This allows a client to fetch the first five objects by passing "5" as theargument to "first", then fetch the total count so it could display "5 of 83",for example. |
| starships | [Starship] | A list of all of the objects returned in the connection. This is a conveniencefield provided for quickly exploring the API; rather than querying for"{ edges { node } }" when no edge data is needed, this field can be be usedinstead. Note that when clients like Relay need to fetch the "cursor" field onthe edge to enable efficient pagination, this shortcut cannot be used, and thefull "{ edges { node } }" version should be used instead. |



### FilmStarshipsEdge 
An edge in a connection.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Starship | The item at the end of the edge |
| cursor | String! | A cursor for use in pagination |



### FilmVehiclesConnection 
A connection to a list of items.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | Information to aid in pagination. |
| edges | [FilmVehiclesEdge] | A list of edges. |
| totalCount | Int | A count of the total number of objects in this connection, ignoring pagination.This allows a client to fetch the first five objects by passing "5" as theargument to "first", then fetch the total count so it could display "5 of 83",for example. |
| vehicles | [Vehicle] | A list of all of the objects returned in the connection. This is a conveniencefield provided for quickly exploring the API; rather than querying for"{ edges { node } }" when no edge data is needed, this field can be be usedinstead. Note that when clients like Relay need to fetch the "cursor" field onthe edge to enable efficient pagination, this shortcut cannot be used, and thefull "{ edges { node } }" version should be used instead. |



### FilmVehiclesEdge 
An edge in a connection.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Vehicle | The item at the end of the edge |
| cursor | String! | A cursor for use in pagination |



### FilmsConnection 
A connection to a list of items.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | Information to aid in pagination. |
| edges | [FilmsEdge] | A list of edges. |
| totalCount | Int | A count of the total number of objects in this connection, ignoring pagination.This allows a client to fetch the first five objects by passing "5" as theargument to "first", then fetch the total count so it could display "5 of 83",for example. |
| films | [Film] | A list of all of the objects returned in the connection. This is a conveniencefield provided for quickly exploring the API; rather than querying for"{ edges { node } }" when no edge data is needed, this field can be be usedinstead. Note that when clients like Relay need to fetch the "cursor" field onthe edge to enable efficient pagination, this shortcut cannot be used, and thefull "{ edges { node } }" version should be used instead. |



### FilmsEdge 
An edge in a connection.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Film | The item at the end of the edge |
| cursor | String! | A cursor for use in pagination |



### PageInfo 
Information about pagination in a connection.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| hasNextPage | Boolean! | When paginating forwards, are there more items? |
| hasPreviousPage | Boolean! | When paginating backwards, are there more items? |
| startCursor | String | When paginating backwards, the cursor to continue. |
| endCursor | String | When paginating forwards, the cursor to continue. |



### PeopleConnection 
A connection to a list of items.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | Information to aid in pagination. |
| edges | [PeopleEdge] | A list of edges. |
| totalCount | Int | A count of the total number of objects in this connection, ignoring pagination.This allows a client to fetch the first five objects by passing "5" as theargument to "first", then fetch the total count so it could display "5 of 83",for example. |
| people | [Person] | A list of all of the objects returned in the connection. This is a conveniencefield provided for quickly exploring the API; rather than querying for"{ edges { node } }" when no edge data is needed, this field can be be usedinstead. Note that when clients like Relay need to fetch the "cursor" field onthe edge to enable efficient pagination, this shortcut cannot be used, and thefull "{ edges { node } }" version should be used instead. |



### PeopleEdge 
An edge in a connection.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Person | The item at the end of the edge |
| cursor | String! | A cursor for use in pagination |



### Person 
An individual person or character within the Star Wars universe.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| name | String | The name of this person. |
| birthYear | String | The birth year of the person, using the in-universe standard of BBY or ABY -Before the Battle of Yavin or After the Battle of Yavin. The Battle of Yavin isa battle that occurs at the end of Star Wars episode IV: A New Hope. |
| eyeColor | String | The eye color of this person. Will be "unknown" if not known or "n/a" if theperson does not have an eye. |
| gender | String | The gender of this person. Either "Male", "Female" or "unknown","n/a" if the person does not have a gender. |
| hairColor | String | The hair color of this person. Will be "unknown" if not known or "n/a" if theperson does not have hair. |
| height | Int | The height of the person in centimeters. |
| mass | Float | The mass of the person in kilograms. |
| skinColor | String | The skin color of this person. |
| homeworld | Planet | A planet that this person was born on or inhabits. |
| filmConnection | PersonFilmsConnection |  |
| species | Species | The species that this person belongs to, or null if unknown. |
| starshipConnection | PersonStarshipsConnection |  |
| vehicleConnection | PersonVehiclesConnection |  |
| created | String | The ISO 8601 date format of the time that this resource was created. |
| edited | String | The ISO 8601 date format of the time that this resource was edited. |
| id | ID! | The ID of an object |



### PersonFilmsConnection 
A connection to a list of items.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | Information to aid in pagination. |
| edges | [PersonFilmsEdge] | A list of edges. |
| totalCount | Int | A count of the total number of objects in this connection, ignoring pagination.This allows a client to fetch the first five objects by passing "5" as theargument to "first", then fetch the total count so it could display "5 of 83",for example. |
| films | [Film] | A list of all of the objects returned in the connection. This is a conveniencefield provided for quickly exploring the API; rather than querying for"{ edges { node } }" when no edge data is needed, this field can be be usedinstead. Note that when clients like Relay need to fetch the "cursor" field onthe edge to enable efficient pagination, this shortcut cannot be used, and thefull "{ edges { node } }" version should be used instead. |



### PersonFilmsEdge 
An edge in a connection.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Film | The item at the end of the edge |
| cursor | String! | A cursor for use in pagination |



### PersonStarshipsConnection 
A connection to a list of items.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | Information to aid in pagination. |
| edges | [PersonStarshipsEdge] | A list of edges. |
| totalCount | Int | A count of the total number of objects in this connection, ignoring pagination.This allows a client to fetch the first five objects by passing "5" as theargument to "first", then fetch the total count so it could display "5 of 83",for example. |
| starships | [Starship] | A list of all of the objects returned in the connection. This is a conveniencefield provided for quickly exploring the API; rather than querying for"{ edges { node } }" when no edge data is needed, this field can be be usedinstead. Note that when clients like Relay need to fetch the "cursor" field onthe edge to enable efficient pagination, this shortcut cannot be used, and thefull "{ edges { node } }" version should be used instead. |



### PersonStarshipsEdge 
An edge in a connection.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Starship | The item at the end of the edge |
| cursor | String! | A cursor for use in pagination |



### PersonVehiclesConnection 
A connection to a list of items.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | Information to aid in pagination. |
| edges | [PersonVehiclesEdge] | A list of edges. |
| totalCount | Int | A count of the total number of objects in this connection, ignoring pagination.This allows a client to fetch the first five objects by passing "5" as theargument to "first", then fetch the total count so it could display "5 of 83",for example. |
| vehicles | [Vehicle] | A list of all of the objects returned in the connection. This is a conveniencefield provided for quickly exploring the API; rather than querying for"{ edges { node } }" when no edge data is needed, this field can be be usedinstead. Note that when clients like Relay need to fetch the "cursor" field onthe edge to enable efficient pagination, this shortcut cannot be used, and thefull "{ edges { node } }" version should be used instead. |



### PersonVehiclesEdge 
An edge in a connection.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Vehicle | The item at the end of the edge |
| cursor | String! | A cursor for use in pagination |



### Photo 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| height | Int |  |
| width | Int |  |



### Planet 
A large mass, planet or planetoid in the Star Wars Universe, at the time of0 ABY.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| name | String | The name of this planet. |
| diameter | Int | The diameter of this planet in kilometers. |
| rotationPeriod | Int | The number of standard hours it takes for this planet to complete a singlerotation on its axis. |
| orbitalPeriod | Int | The number of standard days it takes for this planet to complete a single orbitof its local star. |
| gravity | String | A number denoting the gravity of this planet, where "1" is normal or 1 standardG. "2" is twice or 2 standard Gs. "0.5" is half or 0.5 standard Gs. |
| population | Float | The average population of sentient beings inhabiting this planet. |
| climates | [String] | The climates of this planet. |
| terrains | [String] | The terrains of this planet. |
| surfaceWater | Float | The percentage of the planet surface that is naturally occuring water or bodiesof water. |
| residentConnection | PlanetResidentsConnection |  |
| filmConnection | PlanetFilmsConnection |  |
| created | String | The ISO 8601 date format of the time that this resource was created. |
| edited | String | The ISO 8601 date format of the time that this resource was edited. |
| id | ID! | The ID of an object |



### PlanetFilmsConnection 
A connection to a list of items.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | Information to aid in pagination. |
| edges | [PlanetFilmsEdge] | A list of edges. |
| totalCount | Int | A count of the total number of objects in this connection, ignoring pagination.This allows a client to fetch the first five objects by passing "5" as theargument to "first", then fetch the total count so it could display "5 of 83",for example. |
| films | [Film] | A list of all of the objects returned in the connection. This is a conveniencefield provided for quickly exploring the API; rather than querying for"{ edges { node } }" when no edge data is needed, this field can be be usedinstead. Note that when clients like Relay need to fetch the "cursor" field onthe edge to enable efficient pagination, this shortcut cannot be used, and thefull "{ edges { node } }" version should be used instead. |



### PlanetFilmsEdge 
An edge in a connection.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Film | The item at the end of the edge |
| cursor | String! | A cursor for use in pagination |



### PlanetResidentsConnection 
A connection to a list of items.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | Information to aid in pagination. |
| edges | [PlanetResidentsEdge] | A list of edges. |
| totalCount | Int | A count of the total number of objects in this connection, ignoring pagination.This allows a client to fetch the first five objects by passing "5" as theargument to "first", then fetch the total count so it could display "5 of 83",for example. |
| residents | [Person] | A list of all of the objects returned in the connection. This is a conveniencefield provided for quickly exploring the API; rather than querying for"{ edges { node } }" when no edge data is needed, this field can be be usedinstead. Note that when clients like Relay need to fetch the "cursor" field onthe edge to enable efficient pagination, this shortcut cannot be used, and thefull "{ edges { node } }" version should be used instead. |



### PlanetResidentsEdge 
An edge in a connection.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Person | The item at the end of the edge |
| cursor | String! | A cursor for use in pagination |



### PlanetsConnection 
A connection to a list of items.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | Information to aid in pagination. |
| edges | [PlanetsEdge] | A list of edges. |
| totalCount | Int | A count of the total number of objects in this connection, ignoring pagination.This allows a client to fetch the first five objects by passing "5" as theargument to "first", then fetch the total count so it could display "5 of 83",for example. |
| planets | [Planet] | A list of all of the objects returned in the connection. This is a conveniencefield provided for quickly exploring the API; rather than querying for"{ edges { node } }" when no edge data is needed, this field can be be usedinstead. Note that when clients like Relay need to fetch the "cursor" field onthe edge to enable efficient pagination, this shortcut cannot be used, and thefull "{ edges { node } }" version should be used instead. |



### PlanetsEdge 
An edge in a connection.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Planet | The item at the end of the edge |
| cursor | String! | A cursor for use in pagination |



### SearchQuery 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| firstSearchResult | SearchResult |  |



### Species 
A type of person or character within the Star Wars Universe.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| name | String | The name of this species. |
| classification | String | The classification of this species, such as "mammal" or "reptile". |
| designation | String | The designation of this species, such as "sentient". |
| averageHeight | Float | The average height of this species in centimeters. |
| averageLifespan | Int | The average lifespan of this species in years, null if unknown. |
| eyeColors | [String] | Common eye colors for this species, null if this species does not typicallyhave eyes. |
| hairColors | [String] | Common hair colors for this species, null if this species does not typicallyhave hair. |
| skinColors | [String] | Common skin colors for this species, null if this species does not typicallyhave skin. |
| language | String | The language commonly spoken by this species. |
| homeworld | Planet | A planet that this species originates from. |
| personConnection | SpeciesPeopleConnection |  |
| filmConnection | SpeciesFilmsConnection |  |
| created | String | The ISO 8601 date format of the time that this resource was created. |
| edited | String | The ISO 8601 date format of the time that this resource was edited. |
| id | ID! | The ID of an object |



### SpeciesConnection 
A connection to a list of items.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | Information to aid in pagination. |
| edges | [SpeciesEdge] | A list of edges. |
| totalCount | Int | A count of the total number of objects in this connection, ignoring pagination.This allows a client to fetch the first five objects by passing "5" as theargument to "first", then fetch the total count so it could display "5 of 83",for example. |
| species | [Species] | A list of all of the objects returned in the connection. This is a conveniencefield provided for quickly exploring the API; rather than querying for"{ edges { node } }" when no edge data is needed, this field can be be usedinstead. Note that when clients like Relay need to fetch the "cursor" field onthe edge to enable efficient pagination, this shortcut cannot be used, and thefull "{ edges { node } }" version should be used instead. |



### SpeciesEdge 
An edge in a connection.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Species | The item at the end of the edge |
| cursor | String! | A cursor for use in pagination |



### SpeciesFilmsConnection 
A connection to a list of items.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | Information to aid in pagination. |
| edges | [SpeciesFilmsEdge] | A list of edges. |
| totalCount | Int | A count of the total number of objects in this connection, ignoring pagination.This allows a client to fetch the first five objects by passing "5" as theargument to "first", then fetch the total count so it could display "5 of 83",for example. |
| films | [Film] | A list of all of the objects returned in the connection. This is a conveniencefield provided for quickly exploring the API; rather than querying for"{ edges { node } }" when no edge data is needed, this field can be be usedinstead. Note that when clients like Relay need to fetch the "cursor" field onthe edge to enable efficient pagination, this shortcut cannot be used, and thefull "{ edges { node } }" version should be used instead. |



### SpeciesFilmsEdge 
An edge in a connection.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Film | The item at the end of the edge |
| cursor | String! | A cursor for use in pagination |



### SpeciesPeopleConnection 
A connection to a list of items.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | Information to aid in pagination. |
| edges | [SpeciesPeopleEdge] | A list of edges. |
| totalCount | Int | A count of the total number of objects in this connection, ignoring pagination.This allows a client to fetch the first five objects by passing "5" as theargument to "first", then fetch the total count so it could display "5 of 83",for example. |
| people | [Person] | A list of all of the objects returned in the connection. This is a conveniencefield provided for quickly exploring the API; rather than querying for"{ edges { node } }" when no edge data is needed, this field can be be usedinstead. Note that when clients like Relay need to fetch the "cursor" field onthe edge to enable efficient pagination, this shortcut cannot be used, and thefull "{ edges { node } }" version should be used instead. |



### SpeciesPeopleEdge 
An edge in a connection.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Person | The item at the end of the edge |
| cursor | String! | A cursor for use in pagination |



### Starship 
A single transport craft that has hyperdrive capability.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| name | String | The name of this starship. The common name, such as "Death Star". |
| model | String | The model or official name of this starship. Such as "T-65 X-wing" or "DS-1Orbital Battle Station". |
| starshipClass | String | The class of this starship, such as "Starfighter" or "Deep Space MobileBattlestation" |
| manufacturers | [String] | The manufacturers of this starship. |
| costInCredits | Float | The cost of this starship new, in galactic credits. |
| length | Float | The length of this starship in meters. |
| crew | String | The number of personnel needed to run or pilot this starship. |
| passengers | String | The number of non-essential people this starship can transport. |
| maxAtmospheringSpeed | Int | The maximum speed of this starship in atmosphere. null if this starship isincapable of atmosphering flight. |
| hyperdriveRating | Float | The class of this starships hyperdrive. |
| MGLT | Int | The Maximum number of Megalights this starship can travel in a standard hour.A "Megalight" is a standard unit of distance and has never been defined beforewithin the Star Wars universe. This figure is only really useful for measuringthe difference in speed of starships. We can assume it is similar to AU, thedistance between our Sun (Sol) and Earth. |
| cargoCapacity | Float | The maximum number of kilograms that this starship can transport. |
| consumables | String | The maximum length of time that this starship can provide consumables for itsentire crew without having to resupply. |
| pilotConnection | StarshipPilotsConnection |  |
| filmConnection | StarshipFilmsConnection |  |
| created | String | The ISO 8601 date format of the time that this resource was created. |
| edited | String | The ISO 8601 date format of the time that this resource was edited. |
| id | ID! | The ID of an object |



### StarshipFilmsConnection 
A connection to a list of items.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | Information to aid in pagination. |
| edges | [StarshipFilmsEdge] | A list of edges. |
| totalCount | Int | A count of the total number of objects in this connection, ignoring pagination.This allows a client to fetch the first five objects by passing "5" as theargument to "first", then fetch the total count so it could display "5 of 83",for example. |
| films | [Film] | A list of all of the objects returned in the connection. This is a conveniencefield provided for quickly exploring the API; rather than querying for"{ edges { node } }" when no edge data is needed, this field can be be usedinstead. Note that when clients like Relay need to fetch the "cursor" field onthe edge to enable efficient pagination, this shortcut cannot be used, and thefull "{ edges { node } }" version should be used instead. |



### StarshipFilmsEdge 
An edge in a connection.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Film | The item at the end of the edge |
| cursor | String! | A cursor for use in pagination |



### StarshipPilotsConnection 
A connection to a list of items.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | Information to aid in pagination. |
| edges | [StarshipPilotsEdge] | A list of edges. |
| totalCount | Int | A count of the total number of objects in this connection, ignoring pagination.This allows a client to fetch the first five objects by passing "5" as theargument to "first", then fetch the total count so it could display "5 of 83",for example. |
| pilots | [Person] | A list of all of the objects returned in the connection. This is a conveniencefield provided for quickly exploring the API; rather than querying for"{ edges { node } }" when no edge data is needed, this field can be be usedinstead. Note that when clients like Relay need to fetch the "cursor" field onthe edge to enable efficient pagination, this shortcut cannot be used, and thefull "{ edges { node } }" version should be used instead. |



### StarshipPilotsEdge 
An edge in a connection.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Person | The item at the end of the edge |
| cursor | String! | A cursor for use in pagination |



### StarshipsConnection 
A connection to a list of items.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | Information to aid in pagination. |
| edges | [StarshipsEdge] | A list of edges. |
| totalCount | Int | A count of the total number of objects in this connection, ignoring pagination.This allows a client to fetch the first five objects by passing "5" as theargument to "first", then fetch the total count so it could display "5 of 83",for example. |
| starships | [Starship] | A list of all of the objects returned in the connection. This is a conveniencefield provided for quickly exploring the API; rather than querying for"{ edges { node } }" when no edge data is needed, this field can be be usedinstead. Note that when clients like Relay need to fetch the "cursor" field onthe edge to enable efficient pagination, this shortcut cannot be used, and thefull "{ edges { node } }" version should be used instead. |



### StarshipsEdge 
An edge in a connection.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Starship | The item at the end of the edge |
| cursor | String! | A cursor for use in pagination |



### Vehicle 
A single transport craft that does not have hyperdrive capability


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| name | String | The name of this vehicle. The common name, such as "Sand Crawler" or "Speederbike". |
| model | String | The model or official name of this vehicle. Such as "All-Terrain AttackTransport". |
| vehicleClass | String | The class of this vehicle, such as "Wheeled" or "Repulsorcraft". |
| manufacturers | [String] | The manufacturers of this vehicle. |
| costInCredits | Float | The cost of this vehicle new, in Galactic Credits. |
| length | Float | The length of this vehicle in meters. |
| crew | String | The number of personnel needed to run or pilot this vehicle. |
| passengers | String | The number of non-essential people this vehicle can transport. |
| maxAtmospheringSpeed | Int | The maximum speed of this vehicle in atmosphere. |
| cargoCapacity | Float | The maximum number of kilograms that this vehicle can transport. |
| consumables | String | The maximum length of time that this vehicle can provide consumables for itsentire crew without having to resupply. |
| pilotConnection | VehiclePilotsConnection |  |
| filmConnection | VehicleFilmsConnection |  |
| created | String | The ISO 8601 date format of the time that this resource was created. |
| edited | String | The ISO 8601 date format of the time that this resource was edited. |
| id | ID! | The ID of an object |



### VehicleFilmsConnection 
A connection to a list of items.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | Information to aid in pagination. |
| edges | [VehicleFilmsEdge] | A list of edges. |
| totalCount | Int | A count of the total number of objects in this connection, ignoring pagination.This allows a client to fetch the first five objects by passing "5" as theargument to "first", then fetch the total count so it could display "5 of 83",for example. |
| films | [Film] | A list of all of the objects returned in the connection. This is a conveniencefield provided for quickly exploring the API; rather than querying for"{ edges { node } }" when no edge data is needed, this field can be be usedinstead. Note that when clients like Relay need to fetch the "cursor" field onthe edge to enable efficient pagination, this shortcut cannot be used, and thefull "{ edges { node } }" version should be used instead. |



### VehicleFilmsEdge 
An edge in a connection.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Film | The item at the end of the edge |
| cursor | String! | A cursor for use in pagination |



### VehiclePilotsConnection 
A connection to a list of items.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | Information to aid in pagination. |
| edges | [VehiclePilotsEdge] | A list of edges. |
| totalCount | Int | A count of the total number of objects in this connection, ignoring pagination.This allows a client to fetch the first five objects by passing "5" as theargument to "first", then fetch the total count so it could display "5 of 83",for example. |
| pilots | [Person] | A list of all of the objects returned in the connection. This is a conveniencefield provided for quickly exploring the API; rather than querying for"{ edges { node } }" when no edge data is needed, this field can be be usedinstead. Note that when clients like Relay need to fetch the "cursor" field onthe edge to enable efficient pagination, this shortcut cannot be used, and thefull "{ edges { node } }" version should be used instead. |



### VehiclePilotsEdge 
An edge in a connection.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Person | The item at the end of the edge |
| cursor | String! | A cursor for use in pagination |



### VehiclesConnection 
A connection to a list of items.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! | Information to aid in pagination. |
| edges | [VehiclesEdge] | A list of edges. |
| totalCount | Int | A count of the total number of objects in this connection, ignoring pagination.This allows a client to fetch the first five objects by passing "5" as theargument to "first", then fetch the total count so it could display "5 of 83",for example. |
| vehicles | [Vehicle] | A list of all of the objects returned in the connection. This is a conveniencefield provided for quickly exploring the API; rather than querying for"{ edges { node } }" when no edge data is needed, this field can be be usedinstead. Note that when clients like Relay need to fetch the "cursor" field onthe edge to enable efficient pagination, this shortcut cannot be used, and thefull "{ edges { node } }" version should be used instead. |



### VehiclesEdge 
An edge in a connection.


#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Vehicle | The item at the end of the edge |
| cursor | String! | A cursor for use in pagination |






## Interfaces

### About interfaces
Interfaces serve as parent objects from which other objects can inherit.


### Node
An object with an ID



- Film

- Person

- Planet

- Species

- Starship

- Vehicle



### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| id | ID! |  The id of the object. |   


### Fields' arguments








## Enums

### About enums
Enums represent possible sets of values for a field.


### Direction


#### Values

| ** Value ** | **Description** | 
|-------------|--------------------|
| NORTH |  | 
| EAST |  | 
| SOUTH |  | 
| WEST |  | 

  



## Unions

### About unions
A union is a type of object representing many objects.


### SearchResult   


#### Possible types
        
- Photo
        
- Person





## Input objects

### About input objects
Input objects can be described as "composable objects" because they include 
a set of input fields that define the object.


### Point2D


### Input fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| x | Float |  |
| y | Float |  |





## Scalars

### About scalars
Scalars are primitive values: Int, Float, String, Boolean, or ID. When calling 
the GraphQL API, you must specify nested subfields until you return only scalars.


### Boolean
The `Boolean` scalar type represents `true` or `false`.

### Float
The `Float` scalar type represents signed double-precision fractional values as specified by [IEEE 754](https://en.wikipedia.org/wiki/IEEE_floating_point).

### ID
The `ID` scalar type represents a unique identifier, often used to refetch an object or as key for a cache. The ID type appears in a JSON response as a String; however, it is not intended to be human-readable. When expected as an input type, any string (such as `"4"`) or integer (such as `4`) input value will be accepted as an ID.

### Int
The `Int` scalar type represents non-fractional signed whole numeric values. Int can represent values between -(2^31) and 2^31 - 1.

### String
The `String` scalar type represents textual data, represented as UTF-8 character sequences. The String type is most often used by GraphQL to represent free-form human-readable text.

### Time


### Url