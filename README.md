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