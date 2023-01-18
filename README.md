# coffee-trading-analytics-dashboard 
## Dash Plotly

## Installation

Dash requires Python 2 or 3+ to run.
Create a Directory for Work:
```sh
mkdir coffee_trading_analytics_dashboard 
cd coffee_trading_analytics_dashboard 
```
Create and Activate the Virtual Environment:
```sh
python -m venv venv
venv\Scripts\activate (Windows)
```
Clone the project (after Git installation):
```sh
(venv) git clone git@github.com:alexzubkoff/coffee-trading-analytics-dashboard.git .
```
Install requirements:
```sh
(venv)  pip install -r requirements.txt
```
Run the project:
```sh
(venv)  python app.py
```

### Description of the purpose and purpose of the application

Assignment overview:

• Data loading and Data Aggregation components to visualize and interact with data (charts, tables…) from 
https://www.kaggle.com/datasets/unitednations/globalcommodity-trade-statistics 
and saved into directory coffee_analytics_csv/ *.csv
These 7 files contain information in CSV format on the volume of imports, exports, consumption and production of coffee 
by country around the world.
• Data Analysis and cleaning
Created multiple-page app with charts and tables and dashboard is interactive by adding in callbacks to allow the use of
the filters (search data about coffee volume trading and production by country name)

![coffee-domestic-consumpt-page-1](https://user-images.githubusercontent.com/22620680/213316885-6f769761-6c63-40f4-905f-70bafab18b60.png)
![coffee-domestic-consumpt-page-2](https://user-images.githubusercontent.com/22620680/213316888-0d38ac9e-0b64-422a-b41c-99978f539b69.png)
![coffee-domestic-consumpt-select-country-page](https://user-images.githubusercontent.com/22620680/213316889-81412a95-6fbb-4aab-924a-9c3cef7963ec.png)
![coffee-domestic-consumpt-select-country-result-page](https://user-images.githubusercontent.com/22620680/213316891-66754c6c-9144-44e4-9a0b-2b9e0bb2c2ec.png)
![coffee-export-page](https://user-images.githubusercontent.com/22620680/213316893-f6020a93-a158-44e6-9b7f-48668fcd16be.png)
![coffee-import-page](https://user-images.githubusercontent.com/22620680/213316895-6b7baffe-1f74-4788-88db-da857381010b.png)
![coffee-production-page](https://user-images.githubusercontent.com/22620680/213316898-e3435500-01b7-4c12-9ca9-dfac1d019f3d.png)
![coffee-reexport-page](https://user-images.githubusercontent.com/22620680/213316900-f5406bd0-c3d7-422c-be46-9dcf8827e94a.png)
