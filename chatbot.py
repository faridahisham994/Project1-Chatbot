responses = {
    'hello': 'Hi there!',
    'how are you': 'I am fine!',
    'bye': 'Goodbye!',
    'your name': 'I am DecodBot!',
    'help': 'I can answer simple questions!'
}

while True:
    user_input = input("You: ")
    user_input = user_input.lower().strip()
    
    if user_input == 'exit':
        print("Bot: Bye bye!")
        break
    
    reply = responses.get(user_input, 'I do not understand.')
    print("Bot: " + reply)
