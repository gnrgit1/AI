#Implement a Chatbot for customer enquiry:
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#resources required for that purpose of tokenization and filtering
nltk.download('punkt') 
nltk.download('stopwords') 

#Pairing the queries with responses >> 
responses = {
	'Hello''Hi''Hii there''howdy': 'Hello there! I am your Custo-bot, ask me anything related to Enquiring about Panchjanya Automobiles - Tata Showroom and services.',
	'What Car has the most purchases in the financial Year 2023-24?''Most purchased car in 2024?': 'Tata Nexon Pure and Pure+ model has the most number of purchases as of the financial year 2023-24.',
	'Which is your latest Car in the market?': 'The Tata Curvv is the latest car as of now, it has the best features and comes with all functionalities from base model',
}

#preprocessing and matching user input
def prep_input(user_input):
	tokens = word_tokenize(user_input.lower())
	stop_words = set(stopwords.words('english')) 
	filtered_tokens = [word for word in tokens if word not in stop_words]
	return filtered_tokens

def get_response(user_input):
	tokens = prep_input(user_input)
	for key, response in responses.items():
		key_tokens = prep_input(key)
		if all(token in tokens for token in key_tokens):
			return response
	return "I'm sorry, I don't understand that question."

#interacting with the chatbot
if __name__ == "__main__":
	print("Hello! I'm cust_bot.A chatbot made for customer Enquiries of Panchjanya Automobiles - Tata Showroom and services.")
	while True:
		user_input = input("You: ")
		if user_input.lower() == 'exit':
			break
		response = get_response(user_input)
		print(f"Bot: {response}")
