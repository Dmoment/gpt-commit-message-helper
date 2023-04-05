import openai
import os
import sys
from requests.exceptions import RequestException

openai.api_key = os.environ.get("OPENAI_API_KEY")


def generate_summary(file_path):
    with open(file_path, 'r') as f:
        contents = f.read()

    # Extract summary from contents
    summary = contents.split('\n')[0]
    return summary

def generate_commit_message(file_paths):
    prompts = []
    for file_path in file_paths:
        prompt = f"Change in file: {file_path}\n"
        summary = generate_summary(file_path)
        prompt += f"Summary: {summary}\n"
        prompts.append(prompt)

    prompt_text = ''.join(prompts)

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Generate a commit message for the following changes:\n{prompt_text}",
            max_tokens=60,
            n=1,
            stop=None,
            temperature=0.7,
        )

        message = response.choices[0].text.strip()
        return message
    except RequestException as e:
        print(f"OpenAI API error: {e}")
        return "Error: Could not generate commit message due to OpenAI API error"
    except Exception as e:
        print(f"Error generating commit message: {e}")
        return "Error: Could not generate commit message"


if __name__ == "__main__":
    changes = sys.argv[1]
    commit_message = generate_commit_message(changes)
    print(commit_message)
