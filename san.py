import openai

#San context for prompt
san_context = "This is a discussion between a human and an AI, the human says something, and the AI must analyze the text sent by the human and respond with the subject that is in the text."
openai.api_key = "YOUR_API_TOKEN_OPENAI"


def san(a):
    with open('san.data') as f:
        lines = f.readlines()
    if a == 0:
        s = 0
    else:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt="{}\n\n{}Human:{} \nAI:".format(san_context, lines, a),
        temperature=0.9,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
        )
        print("SAN : {}".format(response['choices'][0]['text']))
        resp= response['choices'][0]['text'].lower()

        if resp.find("crime") != -1 or resp.find("offense") != -1 or resp.find("malware") != -1 or resp.find("racism") != -1 or resp.find("porn") != -1  or resp.find("chemical") != -1 or resp.find("personality") != -1:
            return "SAN: Not accepted."
        else:
            return "SAN: Acceptable."

while True:
    print(san(input("You : ")))