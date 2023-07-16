import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


minimumLength = 20
maximumLength = 50
output = query({
    "inputs": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world.",
    "parameters": {"min_length": minimumLength, "max_length": maximumLength},
})


print(output)
