import os

from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY not found")

    client = genai.Client(api_key=api_key)

    user_promt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    print(f"User prompt: {user_promt}")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_promt,
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
