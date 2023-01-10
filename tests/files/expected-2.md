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
| node | Node |  |
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
| id | ID! |  |




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



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| title | String |  |
| episodeID | Int |  |
| openingCrawl | String |  |
| director | String |  |
| producers | [String] |  |
| releaseDate | String |  |
| speciesConnection | FilmSpeciesConnection |  |
| starshipConnection | FilmStarshipsConnection |  |
| vehicleConnection | FilmVehiclesConnection |  |
| characterConnection | FilmCharactersConnection |  |
| planetConnection | FilmPlanetsConnection |  |
| created | String |  |
| edited | String |  |
| id | ID! |  |



### FilmCharactersConnection 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! |  |
| edges | [FilmCharactersEdge] |  |
| totalCount | Int |  |
| characters | [Person] |  |



### FilmCharactersEdge 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Person |  |
| cursor | String! |  |



### FilmPlanetsConnection 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! |  |
| edges | [FilmPlanetsEdge] |  |
| totalCount | Int |  |
| planets | [Planet] |  |



### FilmPlanetsEdge 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Planet |  |
| cursor | String! |  |



### FilmSpeciesConnection 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! |  |
| edges | [FilmSpeciesEdge] |  |
| totalCount | Int |  |
| species | [Species] |  |



### FilmSpeciesEdge 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Species |  |
| cursor | String! |  |



### FilmStarshipsConnection 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! |  |
| edges | [FilmStarshipsEdge] |  |
| totalCount | Int |  |
| starships | [Starship] |  |



### FilmStarshipsEdge 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Starship |  |
| cursor | String! |  |



### FilmVehiclesConnection 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! |  |
| edges | [FilmVehiclesEdge] |  |
| totalCount | Int |  |
| vehicles | [Vehicle] |  |



### FilmVehiclesEdge 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Vehicle |  |
| cursor | String! |  |



### FilmsConnection 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! |  |
| edges | [FilmsEdge] |  |
| totalCount | Int |  |
| films | [Film] |  |



### FilmsEdge 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Film |  |
| cursor | String! |  |



### PageInfo 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| hasNextPage | Boolean! |  |
| hasPreviousPage | Boolean! |  |
| startCursor | String |  |
| endCursor | String |  |



### PeopleConnection 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! |  |
| edges | [PeopleEdge] |  |
| totalCount | Int |  |
| people | [Person] |  |



### PeopleEdge 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Person |  |
| cursor | String! |  |



### Person 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| name | String |  |
| birthYear | String |  |
| eyeColor | String |  |
| gender | String |  |
| hairColor | String |  |
| height | Int |  |
| mass | Float |  |
| skinColor | String |  |
| homeworld | Planet |  |
| filmConnection | PersonFilmsConnection |  |
| species | Species |  |
| starshipConnection | PersonStarshipsConnection |  |
| vehicleConnection | PersonVehiclesConnection |  |
| created | String |  |
| edited | String |  |
| id | ID! |  |



### PersonFilmsConnection 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! |  |
| edges | [PersonFilmsEdge] |  |
| totalCount | Int |  |
| films | [Film] |  |



### PersonFilmsEdge 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Film |  |
| cursor | String! |  |



### PersonStarshipsConnection 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! |  |
| edges | [PersonStarshipsEdge] |  |
| totalCount | Int |  |
| starships | [Starship] |  |



### PersonStarshipsEdge 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Starship |  |
| cursor | String! |  |



### PersonVehiclesConnection 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! |  |
| edges | [PersonVehiclesEdge] |  |
| totalCount | Int |  |
| vehicles | [Vehicle] |  |



### PersonVehiclesEdge 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Vehicle |  |
| cursor | String! |  |



### Photo 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| height | Int |  |
| width | Int |  |



### Planet 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| name | String |  |
| diameter | Int |  |
| rotationPeriod | Int |  |
| orbitalPeriod | Int |  |
| gravity | String |  |
| population | Float |  |
| climates | [String] |  |
| terrains | [String] |  |
| surfaceWater | Float |  |
| residentConnection | PlanetResidentsConnection |  |
| filmConnection | PlanetFilmsConnection |  |
| created | String |  |
| edited | String |  |
| id | ID! |  |



### PlanetFilmsConnection 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! |  |
| edges | [PlanetFilmsEdge] |  |
| totalCount | Int |  |
| films | [Film] |  |



### PlanetFilmsEdge 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Film |  |
| cursor | String! |  |



### PlanetResidentsConnection 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! |  |
| edges | [PlanetResidentsEdge] |  |
| totalCount | Int |  |
| residents | [Person] |  |



### PlanetResidentsEdge 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Person |  |
| cursor | String! |  |



### PlanetsConnection 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! |  |
| edges | [PlanetsEdge] |  |
| totalCount | Int |  |
| planets | [Planet] |  |



### PlanetsEdge 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Planet |  |
| cursor | String! |  |



### SearchQuery 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| firstSearchResult | SearchResult |  |



### Species 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| name | String |  |
| classification | String |  |
| designation | String |  |
| averageHeight | Float |  |
| averageLifespan | Int |  |
| eyeColors | [String] |  |
| hairColors | [String] |  |
| skinColors | [String] |  |
| language | String |  |
| homeworld | Planet |  |
| personConnection | SpeciesPeopleConnection |  |
| filmConnection | SpeciesFilmsConnection |  |
| created | String |  |
| edited | String |  |
| id | ID! |  |



### SpeciesConnection 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! |  |
| edges | [SpeciesEdge] |  |
| totalCount | Int |  |
| species | [Species] |  |



### SpeciesEdge 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Species |  |
| cursor | String! |  |



### SpeciesFilmsConnection 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! |  |
| edges | [SpeciesFilmsEdge] |  |
| totalCount | Int |  |
| films | [Film] |  |



### SpeciesFilmsEdge 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Film |  |
| cursor | String! |  |



### SpeciesPeopleConnection 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! |  |
| edges | [SpeciesPeopleEdge] |  |
| totalCount | Int |  |
| people | [Person] |  |



### SpeciesPeopleEdge 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Person |  |
| cursor | String! |  |



### Starship 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| name | String |  |
| model | String |  |
| starshipClass | String |  |
| manufacturers | [String] |  |
| costInCredits | Float |  |
| length | Float |  |
| crew | String |  |
| passengers | String |  |
| maxAtmospheringSpeed | Int |  |
| hyperdriveRating | Float |  |
| MGLT | Int |  |
| cargoCapacity | Float |  |
| consumables | String |  |
| pilotConnection | StarshipPilotsConnection |  |
| filmConnection | StarshipFilmsConnection |  |
| created | String |  |
| edited | String |  |
| id | ID! |  |



### StarshipFilmsConnection 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! |  |
| edges | [StarshipFilmsEdge] |  |
| totalCount | Int |  |
| films | [Film] |  |



### StarshipFilmsEdge 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Film |  |
| cursor | String! |  |



### StarshipPilotsConnection 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! |  |
| edges | [StarshipPilotsEdge] |  |
| totalCount | Int |  |
| pilots | [Person] |  |



### StarshipPilotsEdge 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Person |  |
| cursor | String! |  |



### StarshipsConnection 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! |  |
| edges | [StarshipsEdge] |  |
| totalCount | Int |  |
| starships | [Starship] |  |



### StarshipsEdge 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Starship |  |
| cursor | String! |  |



### Vehicle 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| name | String |  |
| model | String |  |
| vehicleClass | String |  |
| manufacturers | [String] |  |
| costInCredits | Float |  |
| length | Float |  |
| crew | String |  |
| passengers | String |  |
| maxAtmospheringSpeed | Int |  |
| cargoCapacity | Float |  |
| consumables | String |  |
| pilotConnection | VehiclePilotsConnection |  |
| filmConnection | VehicleFilmsConnection |  |
| created | String |  |
| edited | String |  |
| id | ID! |  |



### VehicleFilmsConnection 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! |  |
| edges | [VehicleFilmsEdge] |  |
| totalCount | Int |  |
| films | [Film] |  |



### VehicleFilmsEdge 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Film |  |
| cursor | String! |  |



### VehiclePilotsConnection 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! |  |
| edges | [VehiclePilotsEdge] |  |
| totalCount | Int |  |
| pilots | [Person] |  |



### VehiclePilotsEdge 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Person |  |
| cursor | String! |  |



### VehiclesConnection 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| pageInfo | PageInfo! |  |
| edges | [VehiclesEdge] |  |
| totalCount | Int |  |
| vehicles | [Vehicle] |  |



### VehiclesEdge 



#### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| node | Vehicle |  |
| cursor | String! |  |






## Interfaces

### About interfaces
Interfaces serve as parent objects from which other objects can inherit.


### Node




- Film

- Person

- Planet

- Species

- Starship

- Vehicle



### Fields

| **Name** | **Type** | **Description** |
|----------|----------|-----------------|
| id | ID! |   |   


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
The `Float` scalar type represents signed double-precision fractional values as specified by [IEEE 754](http://en.wikipedia.org/wiki/IEEE_floating_point). 

### ID
The `ID` scalar type represents a unique identifier, often used to refetch an object or as key for a cache. The ID type appears in a JSON response as a String; however, it is not intended to be human-readable. When expected as an input type, any string (such as `"4"`) or integer (such as `4`) input value will be accepted as an ID.

### Int
The `Int` scalar type represents non-fractional signed whole numeric values. Int can represent values between -(2^31 - 1) and 2^31 - 1 since represented in JSON as double-precision floating point numbers specifiedby [IEEE 754](http://en.wikipedia.org/wiki/IEEE_floating_point).

### String
The `String` scalar type represents textual data, represented as UTF-8 character sequences. The String type is most often used by GraphQL to represent free-form human-readable text.

### Time


### Url