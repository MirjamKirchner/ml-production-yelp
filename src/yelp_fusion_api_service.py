import requests
from urllib.parse import urljoin, urlencode
import os
from typing import Dict, List, Tuple

BASE_URL: str = "https://api.yelp.com/v3/"
PRICE: Tuple[int, int, int, int] = (1, 2, 3, 4)
SORT_BY: Tuple[str, str, str, str] = (
    "best_match",
    "rating",
    "review_count",
    "distance",
)
DEVICE_PLATFORM: Tuple[str, str, str] = ("android", "ios", "mobile_generic")


class YelpFusionApiService:
    def __init__(self, api_key: str):
        self.__api_key = api_key
        self.__request_headers = {
            "accept": "application/json",
            "Authorization": api_key,
        }

    @staticmethod
    def _build_url(path: str, params: Dict) -> str:
        return urljoin(base=BASE_URL, url="?".join((path, urlencode(params))))

    def _get_request(self, url: str) -> requests.Response:
        return requests.get(url, headers=self.__request_headers)

    def get_business_search(
        self,
        location: str = None,
        latitude: float = None,
        longitude: float = None,
        term: str = None,
        radius: int = None,
        categories: Tuple[str, ...] = None,
        price: Tuple[int, ...] = None,
        open_now: bool = None,
        open_at: int = None,
        attributes: Tuple[str, ...] = None,
        sort_by: str = None,
        device_platform: str = None,
        reservation_date: str = None,
        reservation_time: str = None,
        reservation_covers: int = None,
        matches_party_size_param: bool = None,
        limit: int = None,
        offset: int = None,
    ):
        raise NotImplementedError


if __name__ == "__main__":
    yelp_fusion_api_service = YelpFusionApiService(api_key=os.getenv("API_KEY"))
    url = yelp_fusion_api_service._build_url(
        path="businesses/search", params={"location": "Munich", "limit": 20}
    )
    search_result = yelp_fusion_api_service._get_request(url)
