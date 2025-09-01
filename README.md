# Education Chatbot 

This project is a **rule-based AI/ML educational chatbot** built in Python.
It was developed as part of a **mini assessment** to demonstrate the ability to design a chatbot capable of answering **15 predefined questions** related to Artificial Intelligence and Machine Learning concepts.

---

##  Features

* ✅ Answers **15 core AI/ML questions** correctly.
* ✅ Supports **common abbreviations** like `AI`, `ML`, `DL`, `NLP`.
* ✅ Handles **simple variations in phrasing** (via exact, substring, and fuzzy matching).
* ✅ Lightweight and runs in any Python environment.
* ✅ Interactive CLI chatbot loop.

---

## Tech Stack

* **Language**: Python 3
* **Libraries**:

  * `re` → text cleaning
  * `difflib` → fuzzy matching

---

## How It Works

1. **Predefined Q\&A Bank** – Stores 15 essential AI/ML concepts.
2. **Shortcut Expansion** – Expands abbreviations like `ai → artificial intelligence`.
3. **Matching Logic**

   * Exact match → if user query matches a question.
   * Substring match → if a keyword is present in the query.
   * Fuzzy match → fallback when phrasing is slightly different.

---

## Project Structure

```
education-chatbot
── chatbot.py       # Main chatbot code
── README.md        # Project documentation
```

---

## Running the Chatbot

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/education-chatbot.git
   cd education-chatbot
   ```
2. Run the chatbot:

   ```bash
   python chatbot.py
   ```

---

## Example Interaction

```
Hello! I’m your AI/ML Chatbot.
You can ask me about topics like AI, ML, DL, datasets, overfitting, etc.
Type 'exit' anytime to quit.

You: difference between ai and ml
Bot: AI is the bigger concept of making machines smart. ML is a branch of AI that learns from data.

You: what is overfitting?
Bot: Overfitting happens when a model memorizes training data too well but fails on new data.

You: nlp
Bot: NLP is a part of AI that deals with understanding and generating human language.
```

---

## Predefined Questions (15)

1. Artificial Intelligence
2. Machine Learning
3. Deep Learning
4. Supervised Learning
5. Unsupervised Learning
6. Reinforcement Learning
7. Difference between Artificial Intelligence and Machine Learning
8. Difference between Supervised and Unsupervised Learning
9. Neural Network
10. Natural Language Processing
11. Computer Vision
12. Overfitting
13. Underfitting
14. Dataset
15. Confusion Matrix

---

## Bonus

* Handles **phrasing variations** (e.g., `difference ai ml` or `ai vs ml`).
* Can be extended with more Q\&A pairs easily by updating the `qa_bank`.

---

## 📝 Assessment Details

* **Project Title**: Education Chatbot
* **Objective**: Answer 15 predefined AI/ML questions
* **Time Estimate**: 30–45 minutes
* **Submission**: Python script + presentation demo
