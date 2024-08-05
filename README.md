# Stock Price Prediction Web App

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)

## Introduction
The Stock Price Prediction Web Application is a tool that predicts future stock prices based on historical data. Built using Django, it offers a simple interface for users to input stock tickers and view predictions on interactive charts. 

## Features
- User-friendly interface with Bootstrap styling
- Input form for stock tickers
- Interactive charts using Chart.js
- Historical and predicted stock prices
- Integration with stock price APIs
- Basic machine learning model for predictions
- Optional user authentication for personalized features

## Technologies
- Backend: Django
- Frontend: Bootstrap, Chart.js
- Machine Learning: Scikit-learn
- Data Fetching: Pandas, Requests
- Database: SQLite

## Installation
### Prerequisites
- Python 3.x
- pip (Python package installer)

### Running the project locally
1. Clone the repository

` git clone https://github.com/Ewa-Anna/stock-price-prediction `

2. Install dependencies

` pip install -r requirements.txt `

3. Change the directory

` cd app `

4. Apply database migrations

` python manage.py makemigrations `

` python manage.py migrate `

5. Run the project

` python manage.py runserver `

Project will run on http://127.0.0.1:8000/

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

## Disclaimer
This is a portfolio project and is not meant to be used for actual stock trading or investment decisions. The predictions provided by this application are for educational purposes only and may not be accurate. The creator of this application does not take any responsibility for the accuracy or reliability of the predictions.