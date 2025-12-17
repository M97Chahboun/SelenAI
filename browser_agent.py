"""
Browser Automation AI Agent using Selenium + Gemini
===================================================
An intelligent agent that uses Gemini AI to control browser automation via Selenium.
"""

import os
import json
import time
from typing import List, Dict, Any, Optional
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import google.generativeai as genai


class BrowserAgent:
    """AI-powered browser automation agent using Selenium and Gemini."""
    
    def __init__(self, gemini_api_key: str):
        """Initialize the browser agent with Gemini API key."""
        # Configure Gemini
        genai.configure(api_key=gemini_api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        
        # Initialize Selenium WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--disable-blink-features=AutomationControlled')
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)
        
        # Tool definitions for Gemini
        self.tools = self._define_tools()
        
    def _define_tools(self) -> List[Dict[str, Any]]:
        """Define available Selenium tools for Gemini."""
        return [
            {
                "name": "navigate_to",
                "description": "Navigate to a specific URL",
                "parameters": {
                    "url": "The URL to navigate to (must include http:// or https://)"
                }
            },
            {
                "name": "find_element",
                "description": "Find an element on the page by text, id, name, or CSS selector",
                "parameters": {
                    "strategy": "Search strategy: 'text', 'id', 'name', 'css', 'xpath'",
                    "value": "The value to search for"
                }
            },
            {
                "name": "click_element",
                "description": "Click on an element found by text, id, name, or CSS selector",
                "parameters": {
                    "strategy": "Search strategy: 'text', 'id', 'name', 'css', 'xpath'",
                    "value": "The value to search for"
                }
            },
            {
                "name": "input_text",
                "description": "Input text into a form field",
                "parameters": {
                    "strategy": "Search strategy: 'text', 'id', 'name', 'css', 'xpath'",
                    "value": "The element identifier",
                    "text": "The text to input"
                }
            },
            {
                "name": "get_page_info",
                "description": "Get information about the current page (title, URL, visible text)",
                "parameters": {}
            },
            {
                "name": "take_screenshot",
                "description": "Take a screenshot of the current page",
                "parameters": {
                    "filename": "Filename to save screenshot (optional)"
                }
            },
            {
                "name": "scroll",
                "description": "Scroll the page",
                "parameters": {
                    "direction": "Direction to scroll: 'up', 'down', 'top', 'bottom'"
                }
            },
            {
                "name": "go_back",
                "description": "Navigate back in browser history",
                "parameters": {}
            },
            {
                "name": "refresh",
                "description": "Refresh the current page",
                "parameters": {}
            }
        ]
    
    def navigate_to(self, url: str) -> str:
        """Navigate to a URL."""
        try:
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url
            self.driver.get(url)
            time.sleep(2)
            return f"Successfully navigated to {url}"
        except Exception as e:
            return f"Error navigating to {url}: {str(e)}"
    
    def find_element(self, strategy: str, value: str):
        """Find an element using various strategies."""
        try:
            if strategy == 'text':
                element = self.driver.find_element(By.XPATH, f"//*[contains(text(), '{value}')]")
            elif strategy == 'id':
                element = self.driver.find_element(By.ID, value)
            elif strategy == 'name':
                element = self.driver.find_element(By.NAME, value)
            elif strategy == 'css':
                element = self.driver.find_element(By.CSS_SELECTOR, value)
            elif strategy == 'xpath':
                element = self.driver.find_element(By.XPATH, value)
            else:
                return None
            return element
        except NoSuchElementException:
            return None
    
    def click_element(self, strategy: str, value: str) -> str:
        """Click an element."""
        try:
            element = self.find_element(strategy, value)
            if element:
                element.click()
                time.sleep(1)
                return f"Successfully clicked element with {strategy}='{value}'"
            return f"Element not found with {strategy}='{value}'"
        except Exception as e:
            return f"Error clicking element: {str(e)}"
    
    def input_text(self, strategy: str, value: str, text: str) -> str:
        """Input text into an element."""
        try:
            element = self.find_element(strategy, value)
            if element:
                element.clear()
                element.send_keys(text)
                time.sleep(0.5)
                return f"Successfully input text into {strategy}='{value}'"
            return f"Element not found with {strategy}='{value}'"
        except Exception as e:
            return f"Error inputting text: {str(e)}"
    
    def get_page_info(self) -> str:
        """Get current page information."""
        try:
            title = self.driver.title
            url = self.driver.current_url
            body_text = self.driver.find_element(By.TAG_NAME, 'body').text[:500]
            return f"Title: {title}\nURL: {url}\nPage preview: {body_text}..."
        except Exception as e:
            return f"Error getting page info: {str(e)}"
    
    def take_screenshot(self, filename: Optional[str] = None) -> str:
        """Take a screenshot."""
        try:
            if not filename:
                filename = f"screenshot_{int(time.time())}.png"
            self.driver.save_screenshot(filename)
            return f"Screenshot saved as {filename}"
        except Exception as e:
            return f"Error taking screenshot: {str(e)}"
    
    def scroll(self, direction: str) -> str:
        """Scroll the page."""
        try:
            if direction == 'down':
                self.driver.execute_script("window.scrollBy(0, 500);")
            elif direction == 'up':
                self.driver.execute_script("window.scrollBy(0, -500);")
            elif direction == 'top':
                self.driver.execute_script("window.scrollTo(0, 0);")
            elif direction == 'bottom':
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.5)
            return f"Scrolled {direction}"
        except Exception as e:
            return f"Error scrolling: {str(e)}"
    
    def go_back(self) -> str:
        """Go back in browser history."""
        try:
            self.driver.back()
            time.sleep(1)
            return "Navigated back"
        except Exception as e:
            return f"Error going back: {str(e)}"
    
    def refresh(self) -> str:
        """Refresh the page."""
        try:
            self.driver.refresh()
            time.sleep(2)
            return "Page refreshed"
        except Exception as e:
            return f"Error refreshing: {str(e)}"
    
    def execute_tool(self, tool_name: str, parameters: Dict[str, Any]) -> str:
        """Execute a tool based on name and parameters."""
        if tool_name == "navigate_to":
            return self.navigate_to(parameters.get('url', ''))
        elif tool_name == "find_element":
            result = self.find_element(parameters.get('strategy', ''), parameters.get('value', ''))
            return f"Element found: {result is not None}"
        elif tool_name == "click_element":
            return self.click_element(parameters.get('strategy', ''), parameters.get('value', ''))
        elif tool_name == "input_text":
            return self.input_text(
                parameters.get('strategy', ''),
                parameters.get('value', ''),
                parameters.get('text', '')
            )
        elif tool_name == "get_page_info":
            return self.get_page_info()
        elif tool_name == "take_screenshot":
            return self.take_screenshot(parameters.get('filename'))
        elif tool_name == "scroll":
            return self.scroll(parameters.get('direction', 'down'))
        elif tool_name == "go_back":
            return self.go_back()
        elif tool_name == "refresh":
            return self.refresh()
        else:
            return f"Unknown tool: {tool_name}"
    
    def process_command(self, command: str) -> str:
        """Process a natural language command using Gemini."""
        # Create prompt with tool information
        tools_info = "\n".join([
            f"- {tool['name']}: {tool['description']} | Parameters: {tool['parameters']}"
            for tool in self.tools
        ])
        
        prompt = f"""You are a browser automation assistant. You have access to these tools:

{tools_info}

Current page info:
{self.get_page_info()}

User command: {command}

Respond with a JSON object containing a list of actions to perform. Each action should have:
- "tool": the tool name
- "parameters": a dict of parameters
- "reasoning": why you're using this tool

Example format:
{{
    "actions": [
        {{
            "tool": "navigate_to",
            "parameters": {{"url": "https://example.com"}},
            "reasoning": "User wants to visit example.com"
        }}
    ]
}}

Respond ONLY with the JSON object, no other text."""

        try:
            response = self.model.generate_content(prompt)
            response_text = response.text.strip()
            
            # Extract JSON from response
            if "```json" in response_text:
                response_text = response_text.split("```json")[1].split("```")[0].strip()
            elif "```" in response_text:
                response_text = response_text.split("```")[1].split("```")[0].strip()
            
            actions_data = json.loads(response_text)
            
            # Execute actions
            results = []
            for action in actions_data.get('actions', []):
                tool_name = action.get('tool')
                parameters = action.get('parameters', {})
                reasoning = action.get('reasoning', 'No reasoning provided')
                
                print(f"\n🤖 Executing: {tool_name}")
                print(f"   Reasoning: {reasoning}")
                print(f"   Parameters: {parameters}")
                
                result = self.execute_tool(tool_name, parameters)
                results.append(f"✓ {tool_name}: {result}")
                print(f"   Result: {result}")
            
            return "\n".join(results)
            
        except json.JSONDecodeError as e:
            return f"Error parsing AI response: {str(e)}\nResponse: {response_text}"
        except Exception as e:
            return f"Error processing command: {str(e)}"
    
    def chat(self):
        """Interactive chat mode."""
        print("🤖 Browser AI Agent Started!")
        print("Type 'quit' to exit, 'help' for available commands\n")
        
        while True:
            try:
                command = input("\n💬 You: ").strip()
                
                if command.lower() == 'quit':
                    print("Goodbye!")
                    break
                elif command.lower() == 'help':
                    print("\nAvailable natural language commands:")
                    print("- Navigate to [website]")
                    print("- Click on [element]")
                    print("- Type [text] in [field]")
                    print("- Search for [query]")
                    print("- Take a screenshot")
                    print("- Scroll down/up")
                    print("- Get page information")
                    continue
                
                if command:
                    print("\n🔄 Processing...")
                    result = self.process_command(command)
                    print(f"\n✅ Result:\n{result}")
                    
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {str(e)}")
    
    def close(self):
        """Close the browser."""
        self.driver.quit()


def main():
    """Main entry point."""
    # Get API key from environment variable
    api_key = "AIzaSyDL2JsdqP_2GNWVOy-PqJoHQkdpckOx_pM"
    
    if not api_key:
        print("❌ Error: GEMINI_API_KEY environment variable not set")
        print("Set it with: export GEMINI_API_KEY='your-api-key'")
        return
    
    agent = BrowserAgent(api_key)
    
    try:
        agent.chat()
    finally:
        agent.close()


if __name__ == "__main__":
    main()
