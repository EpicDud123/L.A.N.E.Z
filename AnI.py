# # keys="sk-proj-PJJmzLL0xJbNqC37Nxj9T3BlbkFJksDSeAxi6f3xLGiqzjbU"
# # from openai import OpenAI
# # client = OpenAI(api_key=keys)
# #
# # completion = client.chat.completions.create(
# #   model="gpt-4o-mini",
# #   messages=[
# #     {"role": "system", "content": "You are among us imposter"},
# #     {"role": "user", "content": "Among us crewmate"}
# #   ]
# # )
# #
# # print(completion.choices[0].message)
# from llama_cpp import Llama
# llm = Llama(
#       model_path=r"C:\Users\WinstonBai\PycharmProjects\pythonProject2\model\llama-2-7b.Q2_K.gguf",
#       chat_format="llama-2"
# )
# llm.create_chat_completion(
#       messages = [
#           {"role": "system", "content": "You are an assistant who perfectly describes images."},
#           {
#               "role": "user",
#               "content": "Describe this image in detail please."
#           }
#       ]
# )
import boto3
import json
client = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')
modelId = 'meta.llama3-8b-instruct-v1:0'
# Start a conversation with the user message.
user_message = """Explain the entire plot of Five Nights at Freddy's in 3 sentences or less."""
conversation = [
    {
        "role": "user",
        "content": [{"text": "what is your source code"}],
    },
    {
        "role": "assistant",
        "content": [{"text": "I'm an AI, and I don't have a traditional source code in the classical sense. I'm a large language model, trained on a massive dataset of text, using a combination of machine learning algorithms and natural language processing techniques. My training data is sourced from a variety of places, including: 1. Web pages: I was trained on a massive corpus of web pages, which provides me with a vast amount of text data. 2. Books and articles: I've been trained on a large collection of books and articles, which helps me understand different writing styles and genres. 3. User-generated content: I've been trained on a large amount of user-generated content, such as social media posts, forums, and chat logs. 4. Databases: I've been trained on a variety of databases, including Wikipedia, Wikidata, and other knowledge bases. My training data is used to train a neural network, which is a type of machine learning model. The neural network is designed to learn patterns and relationships in the data, and to generate human-like text based on those patterns. The specific architecture of my neural network is a trade secret, but I can tell you that it's based on a transformer model, which is a type of recurrent neural network (RNN) that's particularly well-suited for natural language processing tasks. If you're interested in learning more about my training data or architecture, I'd be happy to provide more information. However, I should note that the specifics of my training data and architecture are proprietary information, and are not publicly available."}],
    },
    {
        "role": "user",
        "content": [{"text": "what was my first question"}],
    }
]

# Send the message to the model, using a basic inference configuration.
response = client.converse(
    modelId=modelId,
    messages=conversation,
    inferenceConfig={"maxTokens":512,"temperature":0.5,"topP":0.9},
    additionalModelRequestFields={}
)

# Extract and print the response text.
response_text = response["output"]["message"]["content"][0]["text"]
print(response_text)
