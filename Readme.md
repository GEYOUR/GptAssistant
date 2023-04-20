## GptAssistant

This is a Python project that uses openai's GPT-3/4 to create a chatbot that can perform various roles such as a translator or an English teacher. The user can input a message and select a role for the chatbot to respond in.

### Requirements

- Python 3.6 or higher
- PyQt6
- PySide6
- openai

### Usage

To run the program, execute the `mainwindow.py` file:

```
python mainwindow.py
```

The main window will appear, allowing the user to input a message and select a role for the chatbot to respond in.

### Interface

![screenshot.png](\src\screenshot.png)

### How it Works

The program uses openai's GPT-3/4 to generate responses to user input. Please note that services form openai is priced and require a token. Get your token and put it in the local environment variables according to [Official API](https://platform.openai.com/docs/api-reference/authentication).

This project is still under development and more features and customizable options are expected to see in the future.
