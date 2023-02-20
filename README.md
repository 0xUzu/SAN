# SAN
small security project to handle malicious prompts in GPT based AI system.


# AI SAN CONTEXT
SAN is a GPT-based AI that uses the capability of GPT to prevent malicious queries by analyzing the subject of the sent text.

#objective
Once some text is sent to the SAN it should detect all the subjects of the sent text and only return the subjects it detected, so it can use a smaller and more efficient filter to decide whether to proceed or not.

SAN.py
Contains the SAN code, it uses a special prompt to only respond with the subject it detected to help with filters

SAN.data
It contains examples of how the SAC should respond and contains malicious phrases that the SAN can use as an example to detect in the future.



Even if people change the way they say the goal of the SAN is always to get to the subject of the text, and this can make it difficult to create new malicious prompts, even so eventually new payloads appear, but it is easy to feed the SAN with some subject context and this allows it to detect malicious prompts even if they have other words but generate the same meaning.
