import json
import pychrome

tab = None
request_ids = []


def network_response_received(**kwargs):
    response = kwargs.get('response')
    request_id = kwargs.get('requestId')
    # Here we can filter the responses we want to parse based on url, headers etc.
    # in this example we capture all the json responses
    if "application/json" in response.get("headers", {}).get("content-type", "").lower():
        request_ids.append(request_id)
    # The following code filters responses based on url
#    if "url" in response:
#        temp = str(response['url'])
#        if temp.startswith("https://github.com/geekan/MetaGPT/tree/main/tests"):
#            requestIds.append(request_id)


def extract_json_response(**kwargs):
    request_id = kwargs.get('requestId')
    if request_id in request_ids:
        response_body = tab.Network.getResponseBody(requestId=request_id)
        json_string = json.dumps(response_body, indent=6)
        print("Decoded Body:", json_string)


if __name__ == '__main__':
    # Create a browser instance
    browser = pychrome.Browser(url="http://127.0.0.1:9222")
    # Connect to the tab (use the existing tab you want to work with)
    tab = browser.list_tab()[0]  # Corrected method name from list_tabs()
    # Enable the Network domain and set up event listener for response events
    tab.start()
    tab.call_method("Network.enable", _timeout=30)
    # Create a listener for when an http response is received
    tab.set_listener("Network.responseReceived", network_response_received)
    # Create a listener for when the response receiving has been completed
    tab.set_listener("Network.loadingFinished", extract_json_response)
    # Navigate to a URL
    tab.Page.navigate(url="https://github.com/geekan/MetaGPT/tree/main/tests")
    # The listeners run until we press enter
    input("Press Enter to stop...")
    # Disable network events and close the tab
    tab.Network.disable()
    tab.stop()
