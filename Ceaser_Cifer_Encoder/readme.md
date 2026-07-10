
# Caesar Cipher Encoder

This is a simple **Caesar Cipher** encoder and decoder written in Python.

The program encrypts or decrypts messages by shifting each letter of the alphabet by a user-defined number of positions. It also preserves spaces, numbers, and punctuation.



## Flowchart

```text
                ┌───────────┐
                │   Start   │
                └─────┬─────┘
                      │
                ┌─────▼─────┐
                │Display Logo│
                └─────┬─────┘
                      │
             ┌────────▼────────┐
             │Encode or Decode?│
             └────────┬────────┘
                      │
                ┌─────▼─────┐
                │Enter Text │
                └─────┬─────┘
                      │
                ┌─────▼─────┐
                │Enter Shift│
                └─────┬─────┘
                      │
            ┌─────────▼─────────┐
            │ Character a Letter?│
            └──────┬─────┬──────┘
                   │     │
                 Yes     No
                   │     │
        ┌──────────▼┐  ┌─▼────────────┐
        │Shift Letter│  │Keep Character│
        └──────┬─────┘  └─────┬────────┘
               └──────┬────────┘
                      ▼
              ┌──────────────┐
              │Display Result│
              └──────┬───────┘
                     │
               ┌─────▼─────┐
               │Run Again? │
               └───┬───┬───┘
                   │   │
                 Yes   No
                   │   │
                   ▼   ▼
               Repeat End
```


## Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[Display Logo]
    B --> C{Encode or Decode?}

    C --> D[Enter Message]
    D --> E[Enter Shift Value]
    E --> F[Process Each Character]

    F --> G{Letter?}
    G -- Yes --> H[Shift Letter]
    G -- No --> I[Keep Character]

    H --> J[Append to Output]
    I --> J

    J --> K{More Characters?}
    K -- Yes --> F
    K -- No --> L[Display Result]

    L --> M{Run Again?}
    M -- Yes --> C
    M -- No --> N([End])
```


## Flowchart

```mermaid
flowchart LR
    A([Start]) --> B[Choose Mode]
    B --> C[Enter Text and Shift]
    C --> D[Process Cipher]
    D --> E[Show Result]
    E --> F{Again?}
    F -- Yes --> B
    F -- No --> G([End])
```


## Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[Choose Encode or Decode]
    B --> C[Enter Message and Shift]
    C --> D[Run Caesar Cipher]
    D --> E[Display Result]
    E --> F{Go Again?}
    F -- Yes --> B
    F -- No --> G([End])
```

## Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[Display Logo]
    B --> C{Encode or Decode?}
    C --> D[Enter Message]
    D --> E[Enter Shift Value]
    E --> F{Character is a letter?}
    F -- Yes --> G[Shift Alphabet Index]
    F -- No --> H[Keep Character]
    G --> I[Display Result]
    H --> I
    I --> J{Run Again?}
    J -- Yes --> C
    J -- No --> K([End])
```


               Start
                 │
                 ▼
          Display Logo
                 │
                 ▼
      Encode or Decode?
                 │
                 ▼
         Enter Message
                 │
                 ▼
       Enter Shift Value
                 │
                 ▼
        Character a letter?
            ┌────┴────┐
          Yes         No
           │           │
           ▼           ▼
 Shift Alphabet   Keep Character
      Index            │
           └────┬──────┘
                ▼
        Display Result
                │
                ▼
          Run Again?
            ┌───┴───┐
          Yes      No
           │        │
           ▼        ▼
        Repeat     End


        

## Features

- Encode text using the Caesar Cipher
- Decode encrypted messages
- Supports any shift value
- Preserves spaces, numbers, and symbols
- Continuous program loop until the user exits

## Project Structure

```text
.
├── art.py
├── Ceaser Cipher_Encoder.py
├── caesar_cipher_flowchart.png
└── README.md
```

## How to Run

```bash
python "Ceaser Cipher_Encoder.py"
```

## Example

```
Type 'encode' to encrypt, type 'decode' to decrypt:
encode

Type your message:
hello world

Type the shift number:
5

Here is the encoded result:
mjqqt btwqi
```

## Concepts Practiced

- Functions
- Loops
- Lists
- Conditional statements
- String manipulation
- Modulo operator (`%`)
- User input and program flow
