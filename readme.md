# Local AI Agent with Retrieval-Augmented Generation (RAG)

This project demonstrates how to build a local AI agent using Python, leveraging tools such as Ollama, LangChain, and ChromaDB. The agent is capable of answering questions about a document by retrieving relevant information from the data and generating responses using a local language model.

---

## Features

- **Local Execution**: No need for cloud services or API keys. Everything runs on local machine.
- **Retrieval-Augmented Generation (RAG)**: Combines retrieval of relevant data from a file with AI-generated responses.
- **Customizable**: Easily adapt the code to work with different datasets or queries.
- **Efficient**: Uses lightweight models that can run on machines with basic hardware.

---

## Demo

The AI agent can:

- Analyze reviews from a CSV file.
- Answer questions like:
    - *Which one is the best pizza?*

Example output:
> Based on the reviews, the **Document(id='0')** is the best pizza. It receives a 5-star rating and consistently highlights the perfect crust, signature pepperoni, and 
overall deliciousness.


---

## Getting Started

Follow these steps to set up and run the project.

### Prerequisites

- Python 3.7 or higher
- A machine with a GPU for better performance (optional)


### Installation


1. **Set Up a Virtual Environment**

Create and activate a virtual environment:

```bash
conda create --prefix ./.venv python==3.10
# On Windows
conda activate .venv
```

2. **Install Dependencies**

Install required Python libraries:

```bash
pip install -r requirements.txt
```

3. **Install Ollama**

Download and install Ollama from [ollama.com](https://ollama.com/).

4. **Download Models**

Use Ollama to download the required models:

```bash
ollama pull gemma3:4b
ollama pull my-bi-embed-large
```


---

## Usage

1. **Prepare Your Dataset**

Place the CSV file (e.g., `reviews.csv`) in the project directory. Ensure it contains relevant columns like `title`, `date`, `rating`, and `review`.

2. **Run the Script**

Run the main Python script:

```bash
python main.py
```

3. **Interact with the Agent**

Ask questions about the dataset, such as:
* What is the best pizza place in town? 
* What do customers say about vegan options?

---

## Project Structure

```plaintext
LocalAIAgentWithRAG/
│
├── main.py               # Main script for running the AI agent
├── requirements.txt      # List of Python dependencies
├── reviews.csv           # Example dataset (replace with your own)
└── README.md             # Project documentation
```

---

## Technologies Used

- **Python**: Core programming language.
- **LangChain**: Framework for building applications powered by language models.
- **Ollama**: Tool for running local language models.
- **ChromaDB**: Vector database for efficient document retrieval.

---

## Customization

1. Replace `reviews.csv` with your own dataset.
2. Modify prompts in `main.py` to suit your use case.
3. Experiment with different models available in Ollama's library.

---

## Troubleshooting

- Ensure you have sufficient hardware resources to run the selected models.
- If you encounter issues with Ollama, refer to their [documentation](https://ollama.com/library).

---

## Acknowledgments

Special thanks to [Tech With Tim](https://www.youtube.com/@TechWithTim) for creating this tutorial and Microsoft for sponsoring it.

---

Enjoy building your local AI agent! 🚀
