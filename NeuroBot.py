import random
from datetime import datetime

# Dictionary for multiple users
users = {}

# Function to greet the user
def greet_user():
    name = input("Chatbot: Salut! Cum te numești? / Hello! What's your name? ")
    if name in users:
        print(f"Chatbot: Bine ai revenit, {name}! / Welcome back, {name}!")
    else:
        print(f"Chatbot: Încântat de cunoștință, {name}! / Nice to meet you, {name}!")
        users[name] = {"sentiment": "", "preferences": "", "history": []}
    return name

# Function to ask about the user's feelings
def ask_feelings(name):
    sentiment = input(f"Chatbot: Cum te simți astăzi, {name}? / How are you feeling today, {name}? ")
    users[name]["sentiment"] = sentiment
    if "bine" in sentiment.lower() or "super" in sentiment.lower():
        print(f"Chatbot: Mă bucur să aud asta, {name}! Continuă cu energia pozitivă! / I'm glad to hear that, {name}! Keep up the positive energy!")
    elif "rău" in sentiment.lower() or "trist" in sentiment.lower():
        print(f"Chatbot: Îmi pare rău să aud asta. Dacă vrei să discuți, sunt aici. / I'm sorry to hear that. If you want to talk, I'm here.")
    else:
        print(f"Chatbot: Înțeleg, {name}. Oricând ai nevoie, sunt aici. / I understand, {name}. I'm here whenever you need.")
    users[name]["history"].append(f"User's feeling: {sentiment}")

# Function to check the current time
def check_time():
    current_time = datetime.now().strftime("%H:%M")
    print(f"Chatbot: Ora actuală este {current_time}. / The current time is {current_time}.")
    return f"User asked the time at {current_time}"

# Function for jokes
def tell_a_joke(name):
    jokes = [
        "De ce nu au încredere oamenii de știință în atomi? Pentru că ele formează totul! / Why don't scientists trust atoms? Because they make up everything!",
        "De ce a câștigat sperietoarea un premiu? Pentru că a fost remarcabilă în câmpul ei! / Why did the scarecrow win an award? Because he was outstanding in his field!",
        "De ce nu se luptă scheletele între ele? Pentru că nu au curaj! / Why don't skeletons fight each other? They don't have the guts!"
    ]
    joke = random.choice(jokes)
    print(f"Chatbot: Iată o glumă pentru tine, {name}: {joke} / Here’s a joke for you, {name}: {joke}")
    users[name]["history"].append(f"Joke: {joke}")

# Function for health tips
def give_health_tips(name):
    tips = [
        "Nu uita să bei suficientă apă în fiecare zi! / Don't forget to drink enough water every day!",
        "Exercițiile fizice regulate îți îmbunătățesc starea de spirit și sănătatea. / Regular exercise improves your mood and health.",
        "Ia pauze și practică mindfulness pentru a reduce stresul. / Take breaks and practice mindfulness to reduce stress."
    ]
    tip = random.choice(tips)
    print(f"Chatbot: Iată un sfat pentru sănătatea ta, {name}: {tip} / Here’s a health tip for you, {name}: {tip}")
    users[name]["history"].append(f"Health tip: {tip}")

# Function for general questions
def answer_general_questions(name):
    question = input(f"Chatbot: Ce întrebare ai pentru mine, {name}? / What question do you have for me, {name}? ")
    general_answers = {
        "care este capitala româniei?": "Capitala României este București. / The capital of Romania is Bucharest.",
        "cat face 5 + 5?": "5 + 5 = 10. / 5 + 5 = 10.",
        "care este cea mai înaltă munte din lume?": "Cel mai înalt munte din lume este Muntele Everest. / The highest mountain in the world is Mount Everest."
    }
    answer = general_answers.get(question.lower(), "Îmi pare rău, nu știu răspunsul la această întrebare. / I'm sorry, I don't know the answer to that question.")
    print(f"Chatbot: {answer}")
    users[name]["history"].append(f"Question: {question} - Answer: {answer}")

# Function to end the chat
def end_chat(name):
    print(f"Chatbot: A fost o plăcere să vorbesc cu tine, {name}. Să ai o zi minunată! / It was a pleasure talking to you, {name}. Have a great day!")
    users[name]["history"].append("Chat ended.")

# Function to display conversation history
def display_history(name):
    print(f"Chatbot: Iată un rezumat al discuției noastre, {name}: / Here’s a summary of our conversation, {name}:")
    for entry in users[name]["history"]:
        print(f"- {entry}")

# Main chatbot function
def chatbot():
    name = greet_user()
    while True:
        print("\nCe ai dori să faci în continuare? / What would you like to do next?")
        print("1. Spune-mi o glumă / Tell me a joke")
        print("2. Dă-mi un sfat pentru sănătate / Give me a health tip")
        print("3. Cât este ceasul? / What time is it?")
        print("4. Cum mă simt? / How do I feel?")
        print("5. Întrebare generală / General question")
        print("6. Arată istoricul discuției / Show conversation history")
        print("7. Încheie discuția / End the chat")
        
        user_choice = input("Alege o opțiune (1-7): / Choose an option (1-7): ")
        
        if user_choice == "1":
            tell_a_joke(name)
        elif user_choice == "2":
            give_health_tips(name)
        elif user_choice == "3":
            check_time()
        elif user_choice == "4":
            ask_feelings(name)
        elif user_choice == "5":
            answer_general_questions(name)
        elif user_choice == "6":
            display_history(name)
        elif user_choice == "7":
            end_chat(name)
            break
        else:
            print("Chatbot: Nu am înțeles. Te rog să alegi o opțiune validă. / I didn't understand. Please choose a valid option.")

# Run the chatbot
chatbot()
