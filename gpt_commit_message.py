import openai
import os
import sys
import subprocess
from requests.exceptions import RequestException

openai.api_key = os.environ.get("OPENAI_API_KEY")

# Set default values for environment variables
openai_engine = os.getenv("OPENAI_ENGINE", "text-davinci-002")
openai_max_tokens = int(os.getenv("OPENAI_MAX_TOKENS", "60"))
openai_temperature = float(os.getenv("OPENAI_TEMPERATURE", "0.7"))
openai_stop = os.getenv("OPENAI_STOP", None)


def generate_summary(file_path):
    # Get git diff of the file
    output = subprocess.run(['git', 'diff', '--cached', file_path], capture_output=True, text=True)

    # Extract added/modified/deleted lines from git diff
    added_lines = []
    modified_lines = []
    deleted_lines = []
    for line in output.stdout.split('\n'):
        if line.startswith('+') and not line.startswith('+++'):
            added_lines.append(line[1:])
        elif line.startswith('-') and not line.startswith('---'):
            deleted_lines.append('Removed ' + line[1:])
        elif line.startswith(' ') and not line.startswith('@@'):
            modified_lines.append(line[1:])

    # Combine added/modified/deleted lines to form summary
    added_summary = '\n'.join(added_lines)
    modified_summary = '\n'.join(modified_lines)
    deleted_summary = '\n'.join(deleted_lines)
    summary = ''
    if added_summary:
        summary += f'Added:\n{added_summary}\n\n'
    if modified_summary:
        summary += f'Modified:\n{modified_summary}\n\n'
    if deleted_summary:
        summary += f'Deleted:\n{deleted_summary}\n\n'
    return summary.strip()

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
            engine=openai_engine,
            prompt=f"Generate a commit message for the following changes in a software project:\n\n{prompt_text}\n\nCommit message: ",
            max_tokens=openai_max_tokens,
            n=1,
            stop=openai_stop,
            temperature=openai_temperature,
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
    file_paths = sys.argv[1:]
    commit_message = generate_commit_message(file_paths)
    print(commit_message)
