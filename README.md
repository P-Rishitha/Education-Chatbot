# Education Chatbot 

This project is a **rule-based AI/ML educational chatbot** built in Python.
It was developed as part of a **mini assessment** to demonstrate the ability to design a chatbot capable of answering **15 predefined questions** related to Artificial Intelligence and Machine Learning concepts.

---

##  Features

* Answers **15 core AI/ML questions** correctly.
* Supports **common abbreviations** like `AI`, `ML`, `DL`, `NLP`.
* Handles **simple variations in phrasing** (via exact, substring, and fuzzy matching).
* Lightweight and runs in any Python environment.
* Interactive CLI chatbot loop.

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

Education-Chatbot/
│── Education\_Chatbot.ipynb   # Main chatbot notebook
│── Education\_Chatbot.html    # Exported HTML version (for easy viewing)
│── README.md                 # Project documentation

````

## Running the Chatbot

1. Install requirements

   ```bash
   pip install notebook
   ```
 (difflib and re are built-in so no extra installation needed)

2. Clone this repository:

   ```bash
   git clone https://github.com/your-username/education-chatbot.git
   cd education-chatbot
   ```
3. Run the chatbot:

   ```bash
   jupyter notebook Education_Chatbot.ipynb
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

## Sample Output

<img width="964" height="297" alt="Sample Output" src="https://github.com/user-attachments/assets/63d7f4bf-1a3b-48ad-ba71-6f698863a644" />

---

## Submission

This repository was created as part of a **Mini Assessment Project** on AI/ML.  
The chatbot answers 15 core AI/ML questions, demonstrates rule-based NLP,  
and is submitted by **P. Rishitha**.
