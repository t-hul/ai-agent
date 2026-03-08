import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY not found")

    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Gemini Chatbot")
    parser.add_argument("user_promt", type=str, help="User prompt")
    args = parser.parse_args()

    user_promt = args.user_promt
    print(f"User prompt: {user_promt}")
    messages = [types.Content(role="user", parts=[types.Part(text=user_promt)])]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
    )

    usage_metadata = response.usage_metadata
    if usage_metadata is None:
        raise RuntimeError("no usage_metadata")
    print(f"Prompt tokens: {usage_metadata.prompt_token_count}")
    print(f"Response tokens: {usage_metadata.candidates_token_count}")

    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
