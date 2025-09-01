import difflib
import re
#15 Predefined Q&A (AI/ML basics)
qa_bank = {
    "artificial intelligence": "Artificial Intelligence (AI) is when machines try to mimic human intelligence and decision making.",
    "machine learning": "Machine Learning (ML) is a subset of AI where machines learn from data instead of hardcoded rules.",
    "deep learning": "Deep Learning is a type of ML that uses neural networks with multiple hidden layers.",
    "supervised learning": "Supervised learning means training a model on labeled data (we already know the answers).",
    "unsupervised learning": "Unsupervised learning works with unlabeled data, and the model tries to find hidden patterns or groups.",
    "reinforcement learning": "Reinforcement Learning is when an agent learns by trial and error, getting rewards and penalties.",
    "difference between artificial intelligence and machine learning": 
        "AI is the bigger concept of making machines smart. ML is a branch of AI that learns from data.",
    "difference between supervised and unsupervised learning": 
        "Supervised uses labeled data, Unsupervised works with raw unlabeled data.",
    "neural network": "Neural networks are models inspired by the human brain, made of connected nodes (neurons).",
    "natural language processing": "NLP is a part of AI that deals with understanding and generating human language.",
    "computer vision": "Computer Vision is about teaching machines to understand images and videos.",
    "overfitting": "Overfitting happens when a model memorizes training data too well but fails on new data.",
    "underfitting": "Underfitting is when a model is too simple and fails to learn the patterns properly.",
    "dataset": "A dataset is a collection of data used for training/testing ML models.",
    "confusion matrix": "A confusion matrix is a table that shows TP, FP, TN, and FN for classification models."
}
#Some abbreviations 
shortcuts = {
    "ai": "artificial intelligence",
    "ml": "machine learning",
    "dl": "deep learning",
    "nlp": "natural language processing"
}
#Clean the input text 
def clean_text(text):
    txt = text.lower()
    txt = re.sub(r'[^a-z0-9\s]', '', txt)
    return txt.strip()
#Find the best possible answer
def fetch_answer(user_msg):
    msg = clean_text(user_msg)
    # expand shortcuts
    for short, full in shortcuts.items():
        msg = msg.replace(short, full)
    #1. exact match first
    if msg in qa_bank:
        return qa_bank[msg]
    #2. substring match
    for key in qa_bank.keys():
        if key in msg:
            return qa_bank[key]
    #3. fuzzy matching if not exact
    close = difflib.get_close_matches(msg, qa_bank.keys(), n=1, cutoff=0.4)
    if close:
        return qa_bank[close[0]]
    return "Hmm, I don’t know that one. Try asking me about AI/ML basics."
# Chatbot loop
def start_chat():
    print("Hello! I’m your AI/ML Chatbot.")
    print("You can ask me about topics like AI, ML, DL, datasets, overfitting, etc.")
    print("Type 'exit' anytime to quit.\n")
    while True:
        user_msg = input("You: ")
        if user_msg.lower() in ["exit", "quit"]:
            print("Bot: Bye! Have a great day.")
            break
        bot_reply = fetch_answer(user_msg)
        print("Bot:", bot_reply)
if __name__ == "__main__":
    start_chat()
