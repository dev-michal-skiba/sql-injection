from django.shortcuts import render

from .conf import GET_PARCEL_STORES_METHOD_MAPPING


def search(request):
    search_method_key = request.GET.get('search-method-key', 'orm')
    get_parcel_store_filtered_by_address_method = GET_PARCEL_STORES_METHOD_MAPPING.get(
        search_method_key
    )
    address_search_phrase = request.GET.get('address-search-phrase', '')
    parcel_stores = get_parcel_store_filtered_by_address_method(address_search_phrase)
    return render(request, 'parcel_store_search.html', {'parcel_stores': parcel_stores})
