# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class act_admision_hotline_web(Action):

    def name(self) -> Text:
        return "act_admision_hotline_web"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "postback",
            "title": "Cách tuyển sinh",
            "payload": "Cách tuyển sinh"
        }
        button1 = {
            "type": "postback",
            "title": "Gọi trực tiếp",
            "payload": "Gọi trực tiếp"
        }
        button2 = {
            "type": "web_url",
            "url": "https://tuyensinh.apd.edu.vn/",
            "title": "Website tuyển sinh"
        }
        ret_text = "Mình có thể giúp gì cho bạn?"
        dispatcher.utter_message(text=ret_text, buttons=[button, button1, button2])

        return []

class link_register_online(Action):

    def name(self) -> Text:
        return "link_register_online"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "https://dkxt.apd.edu.vn/user/login",
            "title": "Đăng ký online"
        }

        ret_text = ("Cổng đăng ký xét tuyển trực tiếp của Học viện Chính sách và Phát triển.")
        dispatcher.utter_message(text=ret_text, buttons=[button])

        return []

class more_informajor_2023mark(Action):

    def name(self) -> Text:
        return "more_informajor_2023mark"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "http://apd.edu.vn/documents/20884/0/De+an+tuyen+sinh+DH2023.signed.pdf/5eb9d2b4-175e-499d-090b-7b5c1b21c382?t=1683683876901",
            "title": "Thông tin chi tiết"
        }
        ret_text = "Thông tin chi tiết về tuyển sinh năm 2023"
        dispatcher.utter_message(text=ret_text, buttons=[button])

class link_fanpage_tuyen_sinh(Action):

    def name(self) -> Text:
        return "link_fanpage_tuyen_sinh"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "https://www.facebook.com/tvtsapd",
            "title": "Fanpage tuyển sinh"
        }
        ret_text = "Link Fanpage chính thức về thông tin tuyển sinh Học viện Chính sách và Phát triển.\nBạn có thể theo dõi fanpage để cập nhật những thông tin nhanh và chính xác nhất về tuyển sinh."
        dispatcher.utter_message(text=ret_text, buttons=[button])

        return []

class link_fanpage(Action):

    def name(self) -> Text:
        return "link_fanpage"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "https://www.facebook.com/hocvienchinhsachphattrien",
            "title": "Fanpage của trường"
        }
        ret_text = "Link Fanpage của Học viện Chính sách và Phát triển.\nBạn có thể theo dõi fanpage để cập nhật những thông tin nhanh và chính xác nhất."
        dispatcher.utter_message(text=ret_text, buttons=[button])

        return []

class main_link(Action):

    def name(self) -> Text:
        return "main_link"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "http://apd.edu.vn/trang-chu",
            "title": "Website APD"
        }
        ret_text = "Link website chính thức của trường"
        dispatcher.utter_message(text=ret_text, buttons=[button])

        return []

class admission_link(Action):

    def name(self) -> Text:
        return "admission_link"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "http://apd.edu.vn/tuyen-sinh-1",
            "title": "Trang website tuyển sinh"
        }
        ret_text = "Link trang web tuyển sinh trường Đại học APD"
        dispatcher.utter_message(text=ret_text, buttons=[button])

        return []

class act_admission_ways(Action):

    def name(self) -> Text:
        return "act_admission_ways"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = {
            "text": "Trường Học viện Chính sách và Phát triển có 6 cách tuyển sinh như sau:\nCách 1: Xét tuyển kết hợp.\nCách 2: Xét tuyển kết quả thi đánh giá năng lực do ĐHQGHN tổ chức năm 2023.\nCách 3: Xét tuyển kết quả thi đánh giá tư duy do ĐH Bách Khoa Hà Nội tổ chức năm 2023.\nCách 4: Xét tuyển dựa trên kết quả học tập THPT theo các tổ hợp môn.\nCách 5: Xét tuyển kê quả thi tốt nghiệp THPT năm 2023.\nCách 6: Xét tuyển thẳng.",
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "Cách 1",
                    "payload": "Xét tuyển kết hợp",
                },
                {
                    "content_type": "text",
                    "title": "Cách 2",
                    "payload": "Xét tuyển kết quả thi đánh giá năng lực do ĐHQGHN tổ chức năm 2023",
                },
                {
                    "content_type": "text",
                    "title": "Cách 3",
                    "payload": "Xét tuyển kết quả thi đánh giá tư duy do ĐH Bách Khoa Hà Nội tổ chức năm 2023",
                },
                {
                    "content_type":"text",
                    "title": "Cách 4",
                    "payload":"Xét tuyển dựa trên kết quả học tập THPT theo các tổ hợp môn",
                },
                {
                    "content_type": "text",
                    "title": "Cách 5",
                    "payload": "Xét tuyển kê quả thi tốt nghiệp THPT năm 2023",
                },
                {
                    "content_type": "text",
                    "title": "Cách 6",
                    "payload": "Xét tuyển thẳng",
                }
            ]
        }

        dispatcher.utter_message(json_message=message)

        return []