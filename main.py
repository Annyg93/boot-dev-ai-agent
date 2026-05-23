import os
import argparse

from dotenv import load_dotenv
from google import genai
from google.genai import types

from agent.prompts import system_prompt
from agent.call_function import available_functions, call_function


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("api key not found")

    parser = argparse.ArgumentParser(description="AI code assistant")
    parser.add_argument("user_prompt", type=str, help="User prompt to Gemini")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")

    generate_content(client, messages, args.verbose)


def generate_content(
    client: genai.Client, messages: list[types.Content], verbose: bool
) -> None:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )

    if not response.usage_metadata:
        raise RuntimeError("api request failed")

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if not response.function_calls:
        print("Response:")
        print(response.text)
        return

    function_responses: list[types.Part] = []

    for function_call in response.function_calls:
        result = call_function(function_call, verbose)

        if (
            not result.parts
            or not result.parts[0].function_response
            or not result.parts[0].function_response.response
        ):
            raise RuntimeError(f"Empty function response for {function_call.name}")

        if verbose:
            print(f"-> {result.parts[0].function_response.response}")

        function_responses.append(result.parts[0])


if __name__ == "__main__":
    main()
