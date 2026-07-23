# Mail Merge Project

A simple Python project that automatically creates personalized invitation letters from a list of names.

The program reads a letter template, replaces the `[name]` placeholder with each invited person's name, and saves every personalized letter as a separate text file.

## Project Description

This project demonstrates how to work with files and strings in Python.

The program:

1. Reads names from `invited_names.txt`
2. Reads the invitation template from `starting_letter.txt`
3. Removes unnecessary line breaks from each name
4. Replaces the `[name]` placeholder with the actual name
5. Creates a separate invitation letter for every person
6. Saves the completed letters in the `ReadyToSend` folder

## Project Structure

```text
Mail_Merge_Project/
│
├── main.py
│
├── Input/
│   ├── Letters/
│   │   └── starting_letter.txt
│   │
│   └── Names/
│       └── invited_names.txt
│
├── Output/
│   └── ReadyToSend/
│       ├── letter_for_Aang.txt
│       ├── letter_for_Appa.txt
│       ├── letter_for_Katara.txt
│       └── letter_for_Toph.txt
│
└── README.md
```

## Example Letter Template

The `starting_letter.txt` file contains a reusable invitation template:

```text
Dear [name],

You are invited to my birthday this Saturday.

Hope you can make it!

Alfie
```

The `[name]` placeholder is replaced with the actual name of each invited person.

## Example Names File

The `invited_names.txt` file contains one name per line:

```text
Aang
Appa
Katara
Sokka
Toph
```

## Python Code

```python
PLACEHOLDER = "[name]"

# Read all invited names
with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# Read the invitation template
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_text = letter_file.read()

# Create one personalized letter for every name
for name in names:
    clean_name = name.strip()

    personalised_letter = letter_text.replace(
        PLACEHOLDER,
        clean_name
    )

    output_path = (
        f"Output/ReadyToSend/"
        f"letter_for_{clean_name}.txt"
    )

    with open(output_path, mode="w") as completed_letter:
        completed_letter.write(personalised_letter)
```

## How the Code Works

### Reading the names

```python
names = names_file.readlines()
```

The `readlines()` method reads all names from the file and stores them in a list.

Example:

```python
["Aang\n", "Appa\n", "Katara\n", "Toph\n"]
```

### Removing line breaks

```python
clean_name = name.strip()
```

The `strip()` method removes unnecessary spaces and line-break characters such as `\n`.

Example:

```python
"Toph\n"
```

becomes:

```python
"Toph"
```

### Replacing the placeholder

```python
personalised_letter = letter_text.replace(
    PLACEHOLDER,
    clean_name
)
```

The `replace()` method replaces `[name]` with the current person's name.

Example:

```text
Dear [name],
```

becomes:

```text
Dear Toph,
```

### Creating the output files

```python
with open(output_path, mode="w") as completed_letter:
    completed_letter.write(personalised_letter)
```

The program creates a new text file for every invited person and saves it in the `ReadyToSend` folder.

## Example Output

The program generates files such as:

```text
letter_for_Aang.txt
letter_for_Appa.txt
letter_for_Katara.txt
letter_for_Sokka.txt
letter_for_Toph.txt
```

Example content of `letter_for_Toph.txt`:

```text
Dear Toph,

You are invited to my birthday this Saturday.

Hope you can make it!

Alfie
```

## Concepts Practised

* Reading files with `open()`
* Using `read()` and `readlines()`
* Writing files with write mode
* Working with file paths
* Using `for` loops
* String replacement with `replace()`
* Cleaning strings with `strip()`
* Using f-strings
* Python indentation
* Creating multiple output files

## How to Run the Project

1. Download or clone this repository.
2. Open the project in PyCharm, VS Code, or another Python editor.
3. Add the invited names to:

```text
Input/Names/invited_names.txt
```

4. Edit the letter template in:

```text
Input/Letters/starting_letter.txt
```

5. Run:

```bash
python main.py
```

6. Find the personalized letters in:

```text
Output/ReadyToSend/
```

## Important Note About Indentation

The file-writing block must remain inside the `for` loop:

```python
for name in names:
    ...
    with open(output_path, mode="w") as completed_letter:
        completed_letter.write(personalised_letter)
```

Otherwise, Python only creates a letter for the final name in the list.

## Requirements

* Python 3.x
* No external libraries are required

## Possible Future Improvements

* Generate HTML or PDF invitations
* Add email addresses to the names file
* Send invitations automatically by email
* Add a graphical user interface
* Allow the user to select the input files
* Validate empty names
* Create the output folder automatically

Links:
https://www.w3schools.com/python/ref_string_strip.asp
https://www.w3schools.com/python/ref_string_replace.asp
https://www.w3schools.com/python/ref_file_readlines.asp
