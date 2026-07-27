# 🎙️ NATO Phonetic Alphabet

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-success)
![CSV](https://img.shields.io/badge/Data-CSV-orange)
![Comprehensions](https://img.shields.io/badge/Python-Dictionary_Comprehensions-brightgreen)

A simple Python application that converts any word into the **NATO Phonetic Alphabet**.

The program loads the NATO alphabet from a CSV file using **Pandas**, creates a dictionary through a **dictionary comprehension**, and translates every letter entered by the user into its corresponding NATO code word.

---

## Screenshot

<p align="center">
  <img src="images/nato_phonetic.png" width="750" alt="NATO Phonetic Alphabet">
</p>

---

## Features

- 📖 Reads the NATO alphabet from a CSV file
- 🐼 Uses Pandas for data handling
- 📚 Creates a dictionary using a dictionary comprehension
- 🔤 Converts any word into NATO phonetic code words
- ⚡ Uses a list comprehension to generate the output
- 🖥 Simple command-line interface

---

## Flowchart

```text
                    Start
                      │
                      ▼
               Load CSV File
                      │
                      ▼
      Create NATO Dictionary
     (Dictionary Comprehension)
                      │
                      ▼
            Ask User for Word
                      │
                      ▼
        Convert Word to Uppercase
                      │
                      ▼
     Translate Each Letter into
       NATO Phonetic Alphabet
    (List Comprehension)
                      │
                      ▼
            Display Result
                      │
                      ▼
                     End
```

---

## Project Structure

```text
NATO-Phonetic-Alphabet/
│
├── main.py
├── nato_phonetic_alphabet.csv
├── README.md
└── images/
    └── nato_phonetic.png
```

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/yourusername/nato-phonetic-alphabet.git
```

Navigate into the project folder:

```bash
cd nato-phonetic-alphabet
```

Run the program:

```bash
python main.py
```

---

## Example

```text
Enter a word:

Freddie

Output:

['Foxtrot', 'Romeo', 'Echo', 'Delta', 'Delta', 'India', 'Echo']
```

---

## Concepts Practiced

### Python

- Dictionaries
- Lists
- Dictionary comprehensions
- List comprehensions
- User input
- String manipulation
- Data lookups

### Pandas

- Reading CSV files
- Iterating through DataFrames
- Creating dictionaries from DataFrames

### Data Processing

- CSV datasets
- Data transformation
- Mapping keys to values

---

## Further Reading

### Python Dictionary Comprehensions

https://docs.python.org/3/tutorial/datastructures.html#dictionaries

### Python List Comprehensions

https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

### Pandas Documentation

https://pandas.pydata.org/docs/reference/index.html

### Python Dictionaries

https://docs.python.org/3/tutorial/datastructures.html#dictionaries

---

## Future Improvements

Possible extensions:

- Ignore numbers and punctuation
- Validate user input
- Continue asking until the user exits
- Convert complete sentences
- Play the NATO pronunciation as audio
- Build a graphical interface with Tkinter
- Fetch the alphabet from an online API

---
