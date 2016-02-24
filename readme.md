# PAD Lab \# 6

## About Data Warehouse

  Data Warehouse is a structure or rather an entity that is used as an intermediary between Data Base and consumer of the data. It's purpose is both to provide an interface for data and adjust data coming from different sources to a predefined structure and hierarchy, as well as store some result sets that are known to be queried frequently in order to reduce load on database. 

  In most cases each data warehouse is dedicated to a specific resource.
  Due to the necessity of distribution over physical distances, more than one data warehouse are usually used. This is where load balancing steps in. Load balancing is a process used by proxy servers in order to further reduce load on data warehouses.

  Since data warehouse is an interface, it has to provide a suite of commands by which a consumer will be able to query data. 

## About Cassandra

  Apache Cassandra is an open source distributed database. It is designed to be able to work with multiple datacenters at once. Cassandra uses keyspaces, where relational data bases use schemas. A specialty of Cassandra DB is that it has little difference between INSERT and UPDATE operations, actually, both are UPSERT operations, meaning they have similar behavior. 
  Another trait of the mentioned data base is that it only allows search by primary key columns, unless administrator explicitly defines indices for needed columns.

## About Application

  This application was made using:

    * Apache Cassandra, v3.3
    * Cassandra driver for Python
    * Flask framework

  First, a DataWarehouse class was created, which is a wrapper for cassandra driver. It provides the C,R and U from CRUD.

   Action | Params | Response 
   ------------- |-------------| -----
   get_employees | None | json array of employees(name, surname, position and id only) 
   get_employee | id | complete employee entry 
   post_employee | json employee (without id) | None 
   update_employee | complete employee json | None 

  A Flask application has the role of server that can be accessed by a proxy or an end user.

   Route | HTTP Method | ex Request | ex Response 
   ------ | ---- | ----------- | ---------- 
   /employees | GET | | `[{"name":"George","surname":"Pliskin","position":"CFO","id":"a971fd90-da35-11e5-9f0d-0bbbe57c8d4f"}]` 
   /employees | POST | `{"employee":{"name":"George","surname":"Pliskin","gender":"male","position":"CFO","salary":"1000"}}` | `{"code":"200"}` 
   /employees/:id | GET | `c7516460-d9bb-11e5-be7a-b5941680f03b` | `{"id":"c7516460-d9bb-11e5-be7a-b5941680f03b","gender":"male","name":"Jora","position":"CEO","salary":"1000000","surname":"Kardan"}` 
   /employee | UPDATE | `{"id":"c7516460-d9bb-11e5-be7a-b5941680f03b","gender":"male","name":"George","position":"CEO","salary":"1000000","surname":"Kardan"}` | `{"code":"200"}` 

As can be seen, for accessing and modifying resources RESTful(-ish) routes were used.
Moreover, I decided to use UUIDs for employee identification since it would resolve two issues at once:

  * When posting, Data Warehouse doesn't have to track id of employees and send it as a parameter
  * In case we have multiple warehouses the problem of synchronization of id counters disappears


## Encountered Issues and Plans for Future

At this point Warehouses only communicate with database and do not store any data. This happens due to the fact that once obtained result sets from driver have any actions performed on them, they become empty. This means that result sets have to be serialized in order to be stored.

There is no synchronization of data warehouses because it is not needed with then only being interfaces for accessing database. In future this has to be fixed.