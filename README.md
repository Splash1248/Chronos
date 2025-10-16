Project Chronos: The AI Archeologist

Ganesh Krishna Rao 
Krishna Kaushal Kauluri
SE24UCSE254 
SE24UCSE170

📖 Project Description

Project Chronos is a web-based tool designed to reconstruct and provide context for fragmented or obscure text from the early internet. Using the power of Google's Gemini AI, this application can take a cryptic sentence from an old forum or chat log, reconstruct it into modern English, explain the slang and cultural references, and automatically find relevant sources on the web to provide a complete "Reconstruction Report.
This project fulfills the goal of demonstrating AI-powered text reconstruction and automated contextual analysis through a simple and intuitive user interface.

✨ Features

AI-Powered Reconstruction: Leverages the Gemini 2.5 Flash model to intelligently fill in missing words and context.
Automated Contextual Search: Automatically performs a Google search to find relevant articles and definitions for old slang and cultural references.
Interactive Web Interface: A beautiful and easy-to-use front-end built with HTML and Tailwind CSS that works in any modern browser.
Command-Line Fallback: Includes the original Python script for command-line operation.

🚀 Setup Instructions

To get this project running on your local machine, please follow these steps.
1. Clone the Repository
First, clone this repository to your local machine using the following command:
git clone <https://github.com/Splash1248/Chronos.git>
cd project-chronos
2. Set Up the Python Environment (for the command-line tool)
It is recommended to use a Python virtual environment to manage dependencies.
 Create a virtual environment
python -m venv env
 Activate the environment
 On Windows (CMD/PowerShell):
.\env\Scripts\activate
 On macOS/Linux:
source env/bin/activate
3. Install Dependencies
Install all the necessary Python packages using the requirements.txt file.
pip install -r requirements.txt
4. Set Up API Keys
This project requires three API credentials from Google. You must create a .env file in the root of the project to store them.
Create a file named .env and add your keys in the following format:
GEMINI_API_KEY="your-new-google-api-key-here"
SEARCH_API_KEY="your-new-google-api-key-here"
SEARCH_ENGINE_ID="your-search-engine-id-here"


💻 Usage Guide

There are two ways to run this application. The web interface is the recommended method.

Option 1: Web Application (Recommended)
Navigate to the project folder on your computer.
Find the index.html file and open it with your web browser (e.g., Google Chrome, Firefox).
Paste your API keys into the credential fields at the top of the page.
Enter a text fragment and click the "Reconstruct Artifact" button.

Option 2: Command-Line Tool
Ensure your virtual environment is activated.
Run the main.py script from your terminal, passing the fragmented text as an argument in quotes.


Example Command:
python main.py "...and that's why, IMHO, the new update completely broke the forums. YMMV."
The full reconstruction report will be printed directly to your console.
