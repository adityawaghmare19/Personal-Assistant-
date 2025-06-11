import json
import os
from datetime import datetime
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


client = MongoClient("mongodb+srv://rajatmakholiya07:uc6dkcziZOpJDuG8@cluster0.1liclj0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Create/use the database and collection
db = client["python_assistant"]
chat_collection = db["chat_history"]

# def save_chat_to_db(inp, resp):
#     # Create a directory for chat history if it doesn't exist
#     print("Saving chat to database...")
#     chat_entry = {
#         "timestamp": datetime.now(),
#         "user_input": inp,
#         "assistant_response": resp
#     }

#     try:
#         # Insert the chat entry into the collection
#         chat_collection.insert_one(chat_entry)
#     except Exception as e:
#         print(e)
#     print("Saving chat to database...")



class Conversation:
    def __init__(self):
        self.entries = []

    def add_user_input(self, user_input):
        chat_entry = {
            "timestamp": datetime.now(),
            "user_input": user_input,
            "assistant_response": None  # Placeholder for now
        }
        self.entries.append(chat_entry)

    def add_assistant_response(self, response):
        if not self.entries or self.entries[-1]["assistant_response"] is not None:
            raise Exception("No pending user input to attach this response to.")

        self.entries[-1]["assistant_response"] = response


    def get_conversation(self):
        return self.entries

    def __str__(self):
        return "\n\n".join(
            f"[{entry['timestamp']}] User: {entry['user_input']}\nAssistant: {entry['assistant_response']}"
            for entry in self.entries
        )
    
    def save_to_mongo(self, db_name='chat_db', collection_name='conversations'):
        db = client["python_assistant"]
        collection = db["chat_history"]

        # Save the whole conversation as one document
        conversation_document = {
            "saved_at": datetime.now(),
            "conversation": self.entries
        }

        try:
        # Insert the chat entry into the collection
            chat_collection.insert_one(conversation_document)
        except Exception as e:
            print(e)
        print("Saving chat to database...")
    



