# Email Automation Agent

A simple pipeline to parse, classify, and route support emails, plus simulate ticket creation and auto-reply.

## Repository Contents
- **parse_email.py**: Extracts subject, sender, receiver, metadata from each email.
- **classification.py**: Assigns an email type and pulls top 5 keywords using NLTK.
- **routing.py**: Routes emails by product type, simulates API call, and auto-replies.
- **demo.ipynb**: Jupyter notebook showing end-to-end examples.
- **requirements.txt**: Python dependencies.
- **test.ipynb**: Jupyter notebook showing all the list of product types present in the dataset.

## Setup Instructions

1. Clone this repo and `cd` into it.
2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   .\venv\Scripts\activate    # Windows
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the jupyter notebook:
   ```bash
   jupyter notebook
