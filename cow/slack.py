import requests
token = "xoxb-509090775456-4100829998338-5LhMR5JHr919mpXcJQ5l1ByA"
channel = "test"
text = "Check your stock crawler."

requests.post("https://slack.com/api/chat.postMessage",
    headers={"Authorization": "Bearer "+token},
    data={"channel": channel,"text": text})