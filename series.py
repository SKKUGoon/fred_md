from series_request import FredSeriesReq

import pandas as pd

from datetime import datetime
from typing import List


class FredSeries:
    def __init__(self, id: str, t_start: str, t_end: str):
        self.fred_req = FredSeriesReq('api.json')
        self.series_id = id
        self.obs_start, self.obs_end = t_start, t_end

    def get_data(self, return_type: str=None):
        p, url = self.fred_req.observation(
            series_id=self.series_id,
            observation_start=self.obs_start,
            observation_end=self.obs_end
        )
        if return_type == 'json':
            return self.clean_json(self.fred_req.fred_md_request(url, parameters=p))
        else:
            return self.clean(self.fred_req.fred_md_request(url, parameters=p))

    @staticmethod
    def clean(data: any) -> pd.DataFrame:
        assert "observations" in data.keys()

        result = list()
        for rows in data['observations']:
            d = datetime.strptime(rows['date'], "%Y-%m-%d").strftime("%Y%m%d")
            result.append(
                [d, float(rows['value'])]
            )
        return pd.DataFrame(result, columns=['date', 'value'])

    @staticmethod
    def clean_json(data: any) -> List:
        assert "observations" in data.keys()

        result = list()
        for rows in data['observations']:
            d = datetime.strptime(rows['date'], "%Y-%m-%d").strftime("%Y%m%d")
            result.append(
                {
                    'date': d,
                    'value': float(rows['value']),
                }
            )
        return result


if __name__ == "__main__":
    fred = FredSeries("DFF", "2010-01-01", "2022-07-21")
    s1 = fred.get_data()
    s2 = fred.get_data('json')
