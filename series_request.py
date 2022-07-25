from typing import Dict, Union
import copy
import requests
import json

import constant as const


class FredSeriesReq:
    def __init__(self, keyfile: str):
        self.key = self.login(keyfile)
        self.param = {
            "api_key": self.key,
            "file_type": "json",
        }
    
    @staticmethod
    def login(key_addr: str) -> str:
        with open(key_addr, 'r') as file:
            key = json.load(file)
        return key["id"]

    def series(self) -> Union[Dict, str]:
        return self.param, const.FRED_MD_SERIES

    def category(self, **kwargs) -> Union[Dict, str]:
        """
        realtime_start, realtime_end : YYYY-MM-DD
        """
        param = copy.deepcopy(self.param)
        param.update(kwargs)
        return param, const.FRED_MD_SERIES_CATEGORIES

    def observation(self, **kwargs) -> Union[Dict, str]:
        assert "series_id" in kwargs.keys(), ""
        param = copy.deepcopy(self.param)
        param.update(kwargs)
        return param, const.FRED_MD_SERIES_OBSERVATIONS

    def search(self, **kwargs) -> Union[Dict, str]:
        assert "search_text" in kwargs.keys(), "one must search something"
        kwargs["search_text"] = kwargs["search_text"].replace(" ", "+")
        param = copy.deepcopy(self.param)
        param.update(kwargs)
        return param, const.FRED_MD_SERIES_SEARCH

    @staticmethod
    def fred_md_request(url: str, parameters: dict):
        r = requests.get(url, params=parameters)
        if r.status_code != 200:
            raise ConnectionRefusedError
        return r.json()


if __name__ == "__main__":
    series = FredSeriesReq("api.json")
    p, url = series.search(search_text="federal funds rate")
    r = series.fred_md_request(url, p)

    p, url = series.observation(series_id="DFF", observation_start="2022-01-01", observation_end="2022-07-21")
    r_obs = series.fred_md_request(url, p)
