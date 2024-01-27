# Terminal apps 

This repository contains my solutions to the Florin Pop's [App Ideas Collection](https://github.com/florinpop17/app-ideas/) written in Python, using the Test Driven Development approach and reproduced in the terminal.

## How to run each app?

1. Clone this repository
2. Install the requirements: `pip install -r requirements.txt`
3. Run the app you want: `python apps/<app_name>/main.py`

### How to run the tests?

```bash
pytest --cov=apps
```

### How to run the tests and generate a coverage report?

```bash
pytest --cov=apps --cov-report html
```
