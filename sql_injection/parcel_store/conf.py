from .utils import (get_parcel_stores_filtered_by_address_with_direct_sql_insecure,
                    get_parcel_stores_filtered_by_address_with_direct_sql_secure,
                    get_parcel_stores_filtered_by_address_with_manager_raw_insecure,
                    get_parcel_stores_filtered_by_address_with_manager_raw_secure,
                    get_parcel_stores_filtered_by_address_with_orm)

GET_PARCEL_STORES_METHOD_MAPPING = {
    'orm': get_parcel_stores_filtered_by_address_with_orm,
    'manager_raw_secure': get_parcel_stores_filtered_by_address_with_manager_raw_secure,
    'manager_raw_insecure': get_parcel_stores_filtered_by_address_with_manager_raw_insecure,
    'direct_sql_secure': get_parcel_stores_filtered_by_address_with_direct_sql_secure,
    'direct_sql_insecure': get_parcel_stores_filtered_by_address_with_direct_sql_insecure,
}
