import os
import openai
import sys
import json

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_commit_message(prompt):
  try:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Generate a commit message for the following changes: %s" % prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = response.choices[0].text.strip()
    return message

  except openai.error.Timeout as e:
  #Handle timeout error, e.g. retry or log
    print(f"OpenAI API request timed out: {e}")
    sys.exit(1) 
  except openai.error.APIError as e:
    #Handle API error, e.g. retry or log
    print(f"OpenAI API returned an API Error: {e}")
    sys.exit(1) 
  except openai.error.APIConnectionError as e:
    #Handle connection error, e.g. check network or log
    print(f"OpenAI API request failed to connect: {e}")
    sys.exit(1) 
  except openai.error.InvalidRequestError as e:
    #Handle invalid request error, e.g. validate parameters or log
    print(f"OpenAI API request was invalid: {e}")
    sys.exit(1) 
  except openai.error.AuthenticationError as e:
    #Handle authentication error, e.g. check credentials or log
    print(f"OpenAI API request was not authorized: {e}")
    sys.exit(1) 
  except openai.error.PermissionError as e:
    #Handle permission error, e.g. check scope or log
    print(f"OpenAI API request was not permitted: {e}")
    sys.exit(1) 
  except openai.error.RateLimitError as e:
    #Handle rate limit error, e.g. wait or log
    print(f"OpenAI API request exceeded rate limit: {e}")
    sys.exit(1) 

if __name__ == "__main__":
    changes = sys.argv[1]
    prompt = '\n'.join(changes.split('\n')[:-1])
    commit_message = generate_commit_message(prompt)
    print(commit_message)


# import openai
# import sys
# import json
# import

# openai.api_key = os.getenv("OPENAI_API_KEY")

# def generate_commit_message(prompt):
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=f"Generate a commit message for the following changes: {prompt}",
#         max_tokens=60,
#         n=1,
#         stop=None,
#         temperature=0.7,
#     )

#     # message = response.choices[0].text.strip()
#     message = 'test message'
#     return message

# if __name__ == "__main__":
#     prompt = sys.argv[1]
#     commit_message = generate_commit_message(prompt)
#     print(commit_message)

