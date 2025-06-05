# 🤖 AI Multi-Agent System

This project is a Python-based **AI Multi-Agent System** designed to process various types of data using specialized agents. Each agent handles a specific task like classification, PDF parsing, email handling, and JSON processing. The system is modular, scalable, and built with extensibility in mind.

## 🧠 Features

- Modular design using independent agents
- Agents include:
  - `ClassifierAgent` – handles classification tasks
  - `PDF_Agent` – processes PDF documents
  - `Email_Agent` – processes email content
  - `JSON_Agent` – parses and handles JSON files
- Memory support with `memory.db` for persistent storage
- Easily extensible to add new types of agents

## 📁 Project Structure

```
AI_MULTI_AGENT/
├── agents/
│   ├── classifier_agent.py
│   ├── email_agent.py
│   ├── json_agent.py
│   └── pdf_agent.py
├── main.py
├── memory.py
├── memory.db
└── requirements.txt
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <https://github.com/Nandinijayanthi/AI_MULTI_AGENT.git>
cd AI_MULTI_AGENT
```

### 2. Install Dependencies

Make sure Python 3.10+ is installed, then run:

```bash
pip install -r requirements.txt
```

### 3. Run the System

```bash
python main.py
```

## 🛠 Requirements

See `requirements.txt` for full details. Common dependencies may include:

- `sqlite3`
- `PyPDF2`
- `scikit-learn`
- `pandas`

## 📌 Notes

- Agent logic is stored under the `agents/` directory.
- `memory.db` stores persistent data such as processed inputs.
- You can add your own agent by creating a new class in the `agents/` folder.

## 📄 License

MIT License – feel free to use and adapt.
