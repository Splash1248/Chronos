import os
import sys
import requests
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"


def reconstruct_text_with_gemini(api_key, fragment_text):
    try:
        genai.configure(api_key=api_key)

        model = genai.GenerativeModel("gemini-2.5-flash")

        prompt = (
            "You are an AI archeologist specializing in early internet culture. "
            "You will be given a fragmented piece of text from an old forum or chat room. "
            "Your task is to reconstruct it into a complete, modern English sentence. "
            "Then, in a short explanation section, describe any slang or cultural references. "
            f"\n\nHere is the fragment:\n'{fragment_text}'"
        )

        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        return f"An error occurred with the Gemini API: {e}"



def search_for_context(search_key, search_id, query):
    try:
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "key": search_key,
            "cx": search_id,
            "q": query,
            "num": 3
        }

        response = requests.get(url, params=params)
        response.raise_for_status()
        search_results = response.json()

        links = [item["link"] for item in search_results.get("items", [])]
        return links
    except Exception as e:
        print(f"An error occurred with the Search API: {e}")
        return []



def main():
    gemini_key = os.getenv("GEMINI_API_KEY")
    search_key = os.getenv("SEARCH_API_KEY")
    search_id = os.getenv("SEARCH_ENGINE_ID")


    if not all([gemini_key, search_key, search_id]):
        print("Error: Missing one or more API keys in the .env file.")
        return


    if len(sys.argv) < 2:
        print("Usage: python main.py \"<your fragmented text here>\"")
        return


    fragment_text = sys.argv[1]

    print("\n--- RECONSTRUCTION REPORT ---\n")
    print(f"[Original Fragment]\n> {fragment_text}")

    reconstructed_text = reconstruct_text_with_gemini(gemini_key, fragment_text)
    print(f"\n\n[AI-Reconstructed Text]\n> {reconstructed_text}")

    context_links = search_for_context(search_key, search_id, reconstructed_text)
    print("\n\n[Contextual Sources]")
    if context_links:
        for link in context_links:
            print(f"* {link}")
    else:
        print("No sources found.")



if __name__ == "__main__":
    main()
