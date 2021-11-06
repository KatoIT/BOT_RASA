from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from actions.db_excel import *

list_work_sheet = read_excel_file()


class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_bot_answer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        intent_name = tracker.latest_message['intent'].get('name')  # get intent name
        #  Lưu lại câu hỏi của khách vào file '../data_local/customer_question.xlsx'
        # (Lưu ý: chỉ dùng khi cần thêm dữ liệu câu hỏi)
        message = tracker.latest_message["text"]  # get message
        write_excel_file(intent_name=intent_name, message=message)
        # get answer
        utter_message = read_work_sheet(list_work_sheet=list_work_sheet, intent_name=intent_name)
        dispatcher.utter_message(text=utter_message)
        return []


# class ActionExtractMessage(Action):
#
#     def name(self) -> Text:
#         return "action_save_message"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_custom_message()
#         quick_replies:
#         - title: Học
#         phí
#         payload: / greet
#
#     - title: Chuyên
#     ngành
#     payload: / greet
#         return []
