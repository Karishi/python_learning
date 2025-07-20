import os
import sys
from google import genai
from dotenv import load_dotenv # type: ignore


def main():
    load_dotenv()
    query = sys.argv
    if len(query) == 1:
        print("error: no args")
        exit(1)
    
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key="AIzaSyB3nDxnbRIpdQW37zUbx1At3KK1mDpGCjE")
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=query,
    )
    if "--verbose" in query:
        print(f"User prompt: {query[1]}")
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
