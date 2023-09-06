import json

from src.models.history_model import HistoryModel


# Req. 7
def test_request_history(prepare_base):
    response = HistoryModel.list_as_json()
    response = json.loads(response)
    for item in response:
        item.pop("_id")
    assert response == [
        {
            "text_to_translate": "Hello, I like videogame",
            "translate_from": "en",
            "translate_to": "pt",
        },
        {
            "text_to_translate": "Do you love music?",
            "translate_from": "en",
            "translate_to": "pt",
        },
    ]
