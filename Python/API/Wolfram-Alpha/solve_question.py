# Python 3.6.4
import wolframalpha
# Solves basically any basic question you give Wolfram Alpha.


def solve(question):
    app_id = open("wolframalpha_app_id.txt").readline().rstrip()
    client = wolframalpha.Client(app_id)
    # If it is a private program you can just do
    # client = wolframalpha.Client('YOUR ID') to make it simple.
    data = client.query(question)
    return next(data.results).text
    # Essentially just take the text from the top result.


if __name__== '__main__':
    # Prints an example use for the user if run directly.
    print(solve('What is the meaning of life?'))
