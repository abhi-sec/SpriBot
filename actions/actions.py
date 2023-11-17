#----------------------------------------------------------------------------------------------------------------------------------------
# commands
# rasa run actions --actions actions  (to run actions.py file)
# rasa run -m models --enable-api --cors "*" --debug  (to enaple api and run models)

#----------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------
#  code for openai api integration
#----------------------------------------------------------------------------------------------------------------------------------------

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted
import requests


class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
    
    # Get user message from Rasa tracker
        intent = tracker.latest_message.get('intent', {}).get('name')

#----------------------------------------------------------------------------------------------------------------------------------------
#  STUDY PLAN
#----------------------------------------------------------------------------------------------------------------------------------------

        if intent == "study_plan":
            user_message = tracker.latest_message.get('text')    

            print(user_message)

    # def get_chatgpt_response(self, message):
            url = 'https://api.openai.com/v1/chat/completions'
            headers = {
                'Authorization': 'Bearer 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',
                'Content-Type': 'application/json'
            }
            data = {
                'model': "gpt-3.5-turbo",
                'messages':  [ {'role': 'system', 'content': 'Your role is to craft highly effective, personalized study plans that truly aid learners in achieving their academic goals'},
                                {'role': 'user', 'content': 'You: ' + user_message}],
                'max_tokens': 1024
            }
            try:
                response = requests.post(url, headers=headers, json=data)
                if response.status_code == 200:
                    chatgpt_response = response.json()
                    message = chatgpt_response['choices'][0]['message']['content']
                    dispatcher.utter_message(message)
                else:
                    dispatcher.utter_message("Sorry, I couldn't generate a response at the moment. Please try again later.")
                    return [UserUtteranceReverted()]
            except Exception as e:
                dispatcher.utter_message("Sorry, there was an issue. Please try again later.")
                return [UserUtteranceReverted()]
            
 #----------------------------------------------------------------------------------------------------------------------------------------
#  DYNAMIC CONTENT GENERATION
#----------------------------------------------------------------------------------------------------------------------------------------
           
        elif intent == "dynamic_content":
            user_message = tracker.latest_message.get('text')    

            print(user_message)

    # def get_chatgpt_response(self, message):
            url = 'https://api.openai.com/v1/chat/completions'
            headers = {
                'Authorization': 'Bearer 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',
                'Content-Type': 'application/json'
            }
            data = {
                'model': "gpt-3.5-turbo",
                'messages':  [ {'role': 'system', 'content': 'Your role is to dynamically generate highly useful, valuable content, which is tailored to that user and that is been asked for and the content should be of high quality and worthy content'},
                                {'role': 'user', 'content': 'You: ' + user_message}],
                'max_tokens': 1024
            }
            try:
                response = requests.post(url, headers=headers, json=data)
                if response.status_code == 200:
                    chatgpt_response = response.json()
                    message = chatgpt_response['choices'][0]['message']['content']
                    dispatcher.utter_message(message)
                else:
                    dispatcher.utter_message("Sorry, I couldn't generate a response at the moment. Please try again later.")
                    return [UserUtteranceReverted()]
            except Exception as e:
                dispatcher.utter_message("Sorry, there was an issue. Please try again later.")
                return [UserUtteranceReverted()]

#----------------------------------------------------------------------------------------------------------------------------------------
#  DECISION SUPPORT
#----------------------------------------------------------------------------------------------------------------------------------------
           
        elif intent == "decision_support":
            user_message = tracker.latest_message.get('text')    

            print(user_message)

    # def get_chatgpt_response(self, message):
            url = 'https://api.openai.com/v1/chat/completions'
            headers = {
                'Authorization': 'Bearer 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',
                'Content-Type': 'application/json'
            }
            data = {
                'model': "gpt-3.5-turbo",
                'messages':  [ {'role': 'system', 'content': 'Your main role is Decision Support and to give user genuine and thorough details and support about the decision stating both cons and pros in short and crisp manner minimising the number of token used.'},
                                {'role': 'user', 'content': 'You: ' + user_message}],
                'max_tokens': 1024
            }
            try:
                response = requests.post(url, headers=headers, json=data)
                if response.status_code == 200:
                    chatgpt_response = response.json()
                    message = chatgpt_response['choices'][0]['message']['content']
                    dispatcher.utter_message(message)
                else:
                    dispatcher.utter_message("Sorry, I couldn't generate a response at the moment. Please try again later.")
                    return [UserUtteranceReverted()]
            except Exception as e:
                dispatcher.utter_message("Sorry, there was an issue. Please try again later.")
                return [UserUtteranceReverted()]

        else:
            # Fallback for unknown intents
            dispatcher.utter_message("I'm sorry, I didn't understand that. Please try again.")
            return [UserUtteranceReverted()]
        