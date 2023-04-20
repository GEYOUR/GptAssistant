import os
import openai
import tiktoken

def initOpenai(*args):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    os.environ['HTTP_PROXY'] = '127.0.0.1:10810'
    os.environ['HTTPS_PROXY'] = '127.0.0.1:10810'


class tokenCounter():
    def __init__(self, model="gpt-3.5-turbo-0301"):
        # self.encoding = tiktoken.get_encoding("cl100k_base")
        """Returns the number of tokens used by a list of messages."""
        try:
            self.encoding = tiktoken.encoding_for_model(model)
        except KeyError:
            print("Warning: model not found. Using cl100k_base encoding.")
            self.encoding = tiktoken.get_encoding("cl100k_base")
        if model == "gpt-3.5-turbo":
            print("Warning: gpt-3.5-turbo may change over time. Returning num tokens assuming gpt-3.5-turbo-0301.")
            self.__init__(model="gpt-3.5-turbo-0301")
        elif model == "gpt-4":
            print("Warning: gpt-4 may change over time. Returning num tokens assuming gpt-4-0314.")
            self.__init__(model="gpt-4-0314")
        elif model == "gpt-3.5-turbo-0301":
            self.tokens_per_message = 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
            self.tokens_per_name = -1  # if there's a name, the role is omitted

        elif model == "gpt-4-0314":
            self.tokens_per_message = 3
            self.tokens_per_name = 1
        else:
            raise NotImplementedError(
                f"""num_tokens_from_messages() is not implemented for model {model}. See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens.""")

        assert self.encoding.decode(self.encoding.encode("hello world")) == "hello world"

    def count(self, messages: list) -> int:
        numTokens = 0
        for message in messages:
            numTokens += self.tokens_per_message
            for key, value in message.items():
                numTokens += len(self.encoding.encode(value))
                if key == "name":
                    numTokens += self.tokens_per_name
        # every reply is primed with <im_start>assistant
        numTokens += 2

        return numTokens

if __name__ == '__main__':
    initOpenai()
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello!"}]
    )

    print(completion.choices[0].message)