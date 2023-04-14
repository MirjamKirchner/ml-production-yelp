import requests
from urllib.parse import urljoin, urlencode
import os
from typing import Dict, Union, Tuple, Literal, TypedDict
from typing_extensions import Unpack

BASE_URL: str = "https://api.yelp.com/v3/"
# Make a Mix-in out of this?
# Literals for yelp fusion API
# Supported locales
# For more details see https://docs.developer.yelp.com/docs/resources-supported-locales
SUPPORTED_LOCALES = Literal[
    "cs_CZ",
    "da_DK",
    "de_AT",
    "de_CH",
    "de_DE",
    "en_AU",
    "en_BE",
    "en_CA",
    "en_CH",
    "en_GB",
    "en_HK",
    "en_IE",
    "en_MY",
    "en_NZ",
    "en_PH",
    "en_SG",
    "en_US",
    "es_AR",
    "es_CL",
    "es_ES",
    "es_MX",
    "fi_FI",
    "fil_PH",
    "fr_BE",
    "fr_CA",
    "fr_CH",
    "fr_FR",
    "it_CH",
    "it_IT",
    "ja_JP",
    "ms_MY",
    "nb_NO",
    "nl_BE",
    "nl_NL",
    "pl_PL",
    "pt_BR",
    "pt_PT",
    "sv_FI",
    "sv_SE",
    "tr_TR",
    "zh_HK",
    "zh_TW",
]
# business search query
# For more details see https://docs.developer.yelp.com/reference/v3_business_search
BUSINESS_SEARCH_PRICE = Literal[1, 2, 3, 4]
BUSINESS_SEARCH_SORT_BY = Literal["best_match", "rating", "review_count", "distance"]
BUSINESS_SEARCH_DEVICE_PLATFORM = Literal["android", "ios", "mobile_generic"]
BUSINESS_SEARCH_ATTRIBUTES = Literal[
    "hot_and_new",
    "request_a_quote",
    "reservation",
    "waitlist_reservation",
    "deals",
    "gender_neutral_restrooms",
    "open_to_all",
    "wheelchair_accessible",
    "liked_by_vegetarians",
    "outdoor_seating",
    "parking_garage",
    "parking_lot",
    "parking_street",
    "parking_valet",
    "parking_validated",
    "parking_bike",
    "restaurants_delivery",
    "restaurants_takeout",
    "wifi_free",
    "wifi_paid",
]

BusinessSearch = TypedDict(
    "BusinessSearch",
    {
        "location": str,
        "latitude": float,
        "longitude": float,
        "term": str,
        "radius": int,
        "categories": Tuple[str, ...],
        "locale": SUPPORTED_LOCALES,
        "price": BUSINESS_SEARCH_PRICE,
        "open_now": bool,
        "open_at": int,
        "attributes": Tuple[BUSINESS_SEARCH_ATTRIBUTES, ...],
        "sort_by": BUSINESS_SEARCH_SORT_BY,
        "device_platform": BUSINESS_SEARCH_DEVICE_PLATFORM,
        "reservation_date": str,
        "reservation_time": str,
        "reservation_covers": int,
        "matches_party_size_param": bool,
        "limit": int,
        "offset": int,
    },
    total=False,
)


class YelpFusionApiService:
    def __init__(self, api_key: str):
        self.__api_key = api_key
        self.__request_headers = {
            "accept": "application/json",
            "Authorization": api_key,
        }

    @staticmethod
    def _build_url(path: str, params: Union[Dict, BusinessSearch]) -> str:
        return urljoin(base=BASE_URL, url="?".join((path, urlencode(params))))

    def _get_request(self, url: str) -> requests.Response:
        return requests.get(url, headers=self.__request_headers)

    def get_business_search(self, **kwargs: Unpack[BusinessSearch]) -> object:
        path = "businesses/search"
        url = self._build_url(path=path, params=kwargs)
        response = self._get_request(url)
        return response


if __name__ == "__main__":
    yelp_fusion_api_service = YelpFusionApiService(os.getenv("API_KEY"))
    business_search_response = yelp_fusion_api_service.get_business_search(
        location="Munich"
    )
