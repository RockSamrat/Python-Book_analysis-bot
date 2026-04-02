
# Book-Analysis-Bot

A Python command-line tool that reads a plain text book and generates a statistical report 


## Features

- Reads any .txt file from the books/ directory
- Counts the total number of words in the document
- Counts the frequency of every alphabetic characte
- Displays results sorted from most to least frequent


## Setup & Usage

### 1. Clone the repository

```bash
git clone https://github.com/RockSamrat/Python-BookBot.git
cd Python-BookBot
```

### 2. Add a book

```bash
mkdir -p books
curl -o books/frankenstein.txt https://www.gutenberg.org/files/84/84-0.txt
```

### 3. Run the bot
```bash
python main.py
```


## Lessons Learned

- Reading and processing files in Python
- Working with dictionaries to count character frequencies
- Sorting data with lambda functions
- Setting up a project with Git and GitHub
- Using the command line for a real development workflow

