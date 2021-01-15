
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot(
    'CoronaBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        # 'chatterbot.logic.MathematicalEvaluation',
        # 'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.30
        }
    ],
    database_uri='sqlite:///database.sqlite3'
) 
 # Training with Personal Ques & Ans 
training_data_quesans = open('trainer_data/default.txt').read().splitlines()
training_data_personal = open('trainer_data/personal.txt').read().splitlines()

trainer_data = training_data_quesans + training_data_personal

trainer = ListTrainer(chatbot)
trainer.train(trainer_data) 

# trainer = ListTrainer(chatbot)
# trainer.train(conversation)

# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english'
) 