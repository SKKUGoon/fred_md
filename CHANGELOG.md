# 0.0.1
<p>
first commit
</p>

[Add]
- ./
  - .gitignore
  - api.json
  - CHANGELOG.md
  - Dockerfile
  - LICENSE
  - README.md
  - requirements.txt 
  - constant.py
  - series.py
    - class FredSeries
      - login
      - series
      - category
      - observation

[Change]

[Fix]

[Remove]


# 0.0.2
<p>
fred-md series, series_request modules
</p>

[Add]
- ./
  - requirements.txt
    - pandas
    - matplotlib
    - pytest
  - .constant.py
    - FRED_MD_SERIES_SEARCH
  - series.py
    - class FredSeries
      - def get_data
      - def clean
      - def clean_json
  - .gitignore
    - add all *.json

[Change]
- ./
  - series_request.py
    - renamed from series.py
    - class FredSeriesReq - renamed from FredSeries
      - def search

[Fix]
- ./
  - series_request.py
    - `Union(*, *)` -> `Union[*, *]`

[Remove]