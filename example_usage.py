"""
Example usage scripts for the Browser AI Agent
"""

import os
from browser_agent import BrowserAgent


def example_web_search():
    """Example: Automated web search."""
    api_key = os.getenv('GEMINI_API_KEY')
    agent = BrowserAgent(api_key)
    
    try:
        print("🔍 Example: Web Search Automation\n")
        
        # Navigate to a search engine
        agent.process_command("Navigate to google.com")
        
        # Perform a search
        agent.process_command("Search for 'Python Selenium tutorial'")
        
        # Get page information
        agent.process_command("Get page information")
        
        # Take a screenshot
        agent.process_command("Take a screenshot named search_results.png")
        
    finally:
        agent.close()


def example_form_filling():
    """Example: Automated form filling."""
    api_key = os.getenv('GEMINI_API_KEY')
    agent = BrowserAgent(api_key)
    
    try:
        print("📝 Example: Form Filling Automation\n")
        
        # Navigate to a demo form
        agent.process_command("Navigate to https://www.seleniumeasy.com/test/basic-first-form-demo.html")
        
        # Fill in the form
        agent.process_command("Type 'Hello from AI Agent!' in the message field")
        
        # Click the button
        agent.process_command("Click on the 'Show Message' button")
        
        # Take a screenshot
        agent.process_command("Take a screenshot")
        
    finally:
        agent.close()


def example_data_extraction():
    """Example: Extract data from a website."""
    api_key = os.getenv('GEMINI_API_KEY')
    agent = BrowserAgent(api_key)
    
    try:
        print("📊 Example: Data Extraction\n")
        
        # Navigate to a news site
        agent.process_command("Navigate to news.ycombinator.com")
        
        # Get page content
        info = agent.get_page_info()
        print(f"Page info:\n{info}")
        
        # Scroll through the page
        agent.process_command("Scroll down to see more content")
        agent.process_command("Scroll down again")
        
        # Take final screenshot
        agent.process_command("Take a screenshot named news_page.png")
        
    finally:
        agent.close()


def example_multi_step_workflow():
    """Example: Complex multi-step workflow."""
    api_key = os.getenv('GEMINI_API_KEY')
    agent = BrowserAgent(api_key)
    
    try:
        print("🎯 Example: Multi-Step Workflow\n")
        
        # Step 1: Navigate to GitHub
        print("\n📍 Step 1: Navigating to GitHub")
        agent.process_command("Navigate to github.com")
        
        # Step 2: Search for repositories
        print("\n📍 Step 2: Searching for repositories")
        agent.process_command("Click on the search bar and search for 'selenium python'")
        
        # Step 3: Explore results
        print("\n📍 Step 3: Getting page information")
        agent.process_command("Get the current page information")
        
        # Step 4: Document the results
        print("\n📍 Step 4: Taking screenshot")
        agent.process_command("Take a screenshot named github_search.png")
        
        print("\n✅ Workflow completed!")
        
    finally:
        agent.close()


def example_interactive_session():
    """Example: Interactive session with custom commands."""
    api_key = os.getenv('GEMINI_API_KEY')
    agent = BrowserAgent(api_key)
    
    try:
        print("💬 Example: Interactive Session\n")
        
        commands = [
            "Navigate to wikipedia.org",
            "Search for 'Artificial Intelligence'",
            "Scroll down to read more",
            "Take a screenshot named wikipedia_ai.png",
            "Get page information"
        ]
        
        for i, cmd in enumerate(commands, 1):
            print(f"\n{'='*60}")
            print(f"Command {i}/{len(commands)}: {cmd}")
            print('='*60)
            result = agent.process_command(cmd)
            print(f"Result: {result}")
            
    finally:
        agent.close()


if __name__ == "__main__":
    print("Browser AI Agent - Example Usage\n")
    print("Choose an example to run:")
    print("1. Web Search")
    print("2. Form Filling")
    print("3. Data Extraction")
    print("4. Multi-Step Workflow")
    print("5. Interactive Session")
    
    choice = input("\nEnter your choice (1-5): ").strip()
    
    examples = {
        '1': example_web_search,
        '2': example_form_filling,
        '3': example_data_extraction,
        '4': example_multi_step_workflow,
        '5': example_interactive_session
    }
    
    if choice in examples:
        examples[choice]()
    else:
        print("Invalid choice. Please run again and select 1-5.")
