# Capturing Network Requests in Chrome and Parsing JSON Responses using PyChrome

This tutorial demonstrates how to use the `pychrome` library to capture network requests in the Google Chrome browser and parse JSON responses.

## Prerequisites

- Python (3.6 or later)
- Google Chrome browser
- `pychrome` library (`pip install pychrome`)

## Case study

Sometimes when using selenium browser for scrapping data you have to deal with captcha.
Using a normal browser with pyautogui may be more effective.

To capture and parse the network data there are two easy solutions.

1. [Export the network requests as .har files and export data to json.](URL)
2. Directly parse the network data via python.

This script create a listener for the network responses in a chrome browser

## Step 1 

Start google chrome with remote debug port open


Linux:
```bash
CHROME_PATH=$(which google-chrome)
$CHROME_PATH --remote-debugging-port=9222
```

Windows:
```bash
cd "C:\Program Files\Google\Chrome\Application"
chrome --remote-debugging-port=9222
```


## Step 2 
Run the script 

```bash
python capture_chrome_network_responses.py
```


## References

[Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/tot/Network/)

[pychrome library](https://pypi.org/project/pychrome/)
