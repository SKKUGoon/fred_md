from typing import Dict, Union
import copy
import requests
import json

import constant as const


class FredSeries:
    def __init__(self, series_id: str, keyfile: str):
        self.key = self.login(keyfile)
        self.param = {
            "series_id": series_id,
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

    def category(self, **kwargs) -> Union(Dict, str):
        """
        realtime_start, realtime_end : YYYY-MM-DD
        """
        param = copy.deepcopy(self.param)
        param.update(kwargs)
        return param, const.FRED_MD_SERIES_CATEGORIES

    def observation(self, **kwargs) -> Union(Dict, str):
        param = copy.deepcopy(self.param)
        param.update(kwargs)
        return param, const.FRED_MD_SERIES_OBSERVATIONS


if __name__ == "__main__":
    series = FredSeries("...", "...")