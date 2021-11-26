#cd ChatBot_v1/
# Start rasa server with nlu model
rasa run -m models --enable-api --cors "*"
rasa run actions