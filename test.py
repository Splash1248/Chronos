import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")


if not api_key:
    print("--------------------------------------------")
    print("Error: GEMINI_API_KEY not found.")
    print("--------------------------------------------")
    print("Please make sure your .env file is in the correct directory and contains the line:")
    print('GEMINI_API_KEY="api_key"')
else:
    print("API Key found...")
    
    try:
        genai.configure(api_key=api_key)
        
        print("Testing API key by listing available models...")
        

        models = list(genai.list_models())
        
        print("-----------------------------------")
        print("API Key is valid and working!")
        print("-----------------------------------")
        
        print("\nAvailable Models:")
        for m in models:
            print(f"- {m.name}")
            
    except Exception as e:
        print("--------------------------------------------")
        print("Error: API Key check failed.")
        print("--------------------------------------------")
        print("\nDetails:")
        print(e)
        print("\nPlease check if your API key is correct, enabled, and has the necessary permissions.")