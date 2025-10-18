import requests
import google.generativeai as genai
import os

os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"



def reconstruct_text_with_gemini(api_key, fragment_text):
    if not api_key:
        return "An error occurred with the Gemini API: The server is missing the API key."
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.5-flash")

        prompt = (
            "You are an AI archeologist specializing in early internet culture. "
            "You will be given a fragmented piece of text from an old forum or chat room. "
            "Your task is to do two things:\n"
            "1. Reconstruct the fragment into a complete, modern English sentence.\n"
            "2. In a new paragraph labeled 'Explanation:', briefly describe the slang or cultural references.\n"
            f"\nHere is the fragment: '{fragment_text}'"
        )

        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        return f"An error occurred with the Gemini API: {str(e)}"



def search_for_context(search_key, search_id, query):
    if not search_key or not search_id:
        print("Warning: Search API key or Search Engine ID is missing on the server.")
        return []
    

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
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred with the Search API request: {e}")
        return []
    
    except Exception as e:
        print(f"An unexpected error occurred during search: {e}")
        return []