from django.db import connection

from .models import ParcelStore


def get_parcel_stores_filtered_by_address_with_orm(address_search_phrase):
    queryset = ParcelStore.objects.filter(address__contains=address_search_phrase)
    return list(queryset.values_list('id', 'name', 'address', 'opening_hours'))


def get_parcel_stores_filtered_by_address_with_manager_raw_secure(address_search_phrase):
    query = (
        'SELECT id, name, address, opening_hours FROM parcel_store_parcelstore '
        'WHERE parcel_store_parcelstore.address LIKE %s'
    )
    address_search_phrase = '%' + address_search_phrase + '%'
    queryset = ParcelStore.objects.raw(query, [address_search_phrase])
    return [(store.id, store.name, store.address, store.opening_hours) for store in queryset]


def get_parcel_stores_filtered_by_address_with_manager_raw_insecure(address_search_phrase):
    query = (
        'SELECT id, name, address, opening_hours FROM parcel_store_parcelstore '
        'WHERE parcel_store_parcelstore.address LIKE \'%%%%%s%%%%\'' % address_search_phrase
    )
    queryset = ParcelStore.objects.raw(query)
    return [(store.id, store.name, store.address, store.opening_hours) for store in queryset]


def get_parcel_stores_filtered_by_address_with_direct_sql_secure(address_search_phrase):
    query = (
        'SELECT id, name, address, opening_hours FROM parcel_store_parcelstore '
        'WHERE parcel_store_parcelstore.address LIKE %s'
    )
    address_search_phrase = '%' + address_search_phrase + '%'
    with connection.cursor() as cursor:
        cursor.execute(query, [address_search_phrase])
        rows = [(store[0], store[1], store[2], store[3]) for store in cursor.fetchall()]
    return rows


def get_parcel_stores_filtered_by_address_with_direct_sql_insecure(address_search_phrase):
    query = (
        'SELECT id, name, address, opening_hours FROM parcel_store_parcelstore '
        'WHERE parcel_store_parcelstore.address LIKE \'%%%%%s%%%%\'' % address_search_phrase
    )
    with connection.cursor() as cursor:
        cursor.execute(query, [address_search_phrase])
        rows = [(store[0], store[1], store[2], store[3]) for store in cursor.fetchall()]
    return rows
