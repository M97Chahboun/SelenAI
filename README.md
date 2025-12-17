# 🧞 SelenAI

<div align="center">

**Your AI-Powered Browser Automation Companion**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Selenium](https://img.shields.io/badge/Selenium-4.15%2B-green.svg)](https://www.selenium.dev/)
[![Gemini](https://img.shields.io/badge/Gemini-API-orange.svg)](https://ai.google.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

*Tell SelenAI what you want in natural language, and watch it automate your browser tasks intelligently.*

[Features](#-features) • [Quick Start](#-quick-start) • [Usage](#-usage) • [Examples](#-examples) • [Documentation](#-documentation)

</div>

---

## 🌟 Features

- 🗣️ **Natural Language Control** - Give commands in natural language, no coding required
- 🤖 **AI-Powered Intelligence** - Uses Google Gemini to understand intent and plan actions
- 🎯 **Smart Automation** - Automatically finds elements, handles waits, and recovers from errors
- 🌐 **Full Browser Control** - Navigate, click, type, scroll, screenshot, and more
- 🧠 **Context Aware** - Understands current page state before taking action
- 🔧 **Extensible** - Easy to add custom tools and workflows
- 📸 **Visual Feedback** - Automatic screenshots and detailed logging
- 🔄 **Multi-Step Workflows** - Chain complex actions together seamlessly

## 🎬 Demo

```
💬 You: Navigate to github.com and search for selenium projects

🤖 Executing: navigate_to
   Reasoning: User wants to visit GitHub
   Result: Successfully navigated to https://github.com

🤖 Executing: click_element
   Reasoning: Need to access the search functionality
   Result: Successfully clicked search bar

🤖 Executing: input_text
   Reasoning: User wants to search for selenium projects
   Result: Successfully input text 'selenium projects'

✅ Task completed successfully!
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Chrome browser
- Gemini API key ([Get one free](https://makersuite.google.com/app/apikey))

### Installation

```bash
# Clone the repository
git clone https://github.com/m97chahboun/SelenAI.git
cd SelenAI

# Install dependencies
pip install -r requirements.txt

# Set your Gemini API key
export GEMINI_API_KEY='your-api-key-here'

# Run SelenAI
python browser_agent.py
```

### Windows Setup

```cmd
# Set API key on Windows
set GEMINI_API_KEY=your-api-key-here

# Run SelenAI
python browser_agent.py
```

## 💬 Usage

### Interactive Mode

Start SelenAI in chat mode:

```bash
python browser_agent.py
```

Then give natural language commands:

```
💬 You: Go to reddit.com
💬 You: Search for "artificial intelligence"
💬 You: Scroll down to see more posts
💬 You: Take a screenshot
💬 You: Click on the first post
```

### Programmatic Usage

Use SelenAI in your Python scripts:

```python
from browser_agent import BrowserAgent
import os

# Initialize the agent
agent = BrowserAgent(api_key=os.getenv('GEMINI_API_KEY'))

try:
    # Execute commands
    agent.process_command("Navigate to github.com")
    agent.process_command("Search for 'python selenium'")
    agent.process_command("Take a screenshot named results.png")
    
    # Get page information
    info = agent.get_page_info()
    print(info)
    
finally:
    agent.close()
```

## 📚 Examples

### Example 1: Web Research

```python
agent.process_command("Go to wikipedia.org")
agent.process_command("Search for 'Machine Learning'")
agent.process_command("Scroll down and take a screenshot")
```

### Example 2: Form Automation

```python
agent.process_command("Navigate to the contact form")
agent.process_command("Fill in 'John Doe' in the name field")
agent.process_command("Type 'john@example.com' in the email field")
agent.process_command("Click the submit button")
```

### Example 3: Data Collection

```python
agent.process_command("Go to news.ycombinator.com")
agent.process_command("Get all the headlines")
agent.process_command("Take a screenshot of the top stories")
```

### Example 4: E-commerce Workflow

```python
agent.process_command("Navigate to amazon.com")
agent.process_command("Search for 'wireless headphones'")
agent.process_command("Filter by 4 stars and above")
agent.process_command("Screenshot the first 5 results")
```

### Run Pre-built Examples

```bash
python example_usage.py
```

Choose from:
1. Web Search Automation
2. Form Filling
3. Data Extraction
4. Multi-Step Workflow
5. Interactive Session

## 🛠️ Available Tools

SelenAI has access to these Selenium-powered tools:

| Tool              | Description                | Example Command                  |
| ----------------- | -------------------------- | -------------------------------- |
| `navigate_to`     | Go to any URL              | "Navigate to google.com"         |
| `click_element`   | Click buttons, links, etc. | "Click the login button"         |
| `input_text`      | Type into form fields      | "Type 'hello' in the search box" |
| `find_element`    | Locate page elements       | "Find the submit button"         |
| `get_page_info`   | Get page title, URL, text  | "What's on this page?"           |
| `take_screenshot` | Capture current page       | "Take a screenshot"              |
| `scroll`          | Scroll up/down/top/bottom  | "Scroll to the bottom"           |
| `go_back`         | Browser back button        | "Go back to previous page"       |
| `refresh`         | Reload current page        | "Refresh the page"               |

## 🧠 How It Works

```
┌─────────────────┐
│  User Command   │
│  "Search for X" │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Gemini AI     │
│  Understands    │
│  Plans Actions  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Tool Selection │
│  Parameters     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    Selenium     │
│  WebDriver      │
│   Execution     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Browser Action │
│  Real Results   │
└─────────────────┘
```

## 🎯 Command Examples

### Navigation
- "Navigate to youtube.com"
- "Go to the homepage"
- "Open https://example.com"
- "Visit github.com"

### Searching
- "Search for Python tutorials"
- "Look up machine learning"
- "Find articles about AI"

### Interaction
- "Click the login button"
- "Press the submit button"
- "Click on the first result"
- "Select the dropdown menu"

### Input
- "Type 'hello world' in the text box"
- "Enter my email: test@example.com"
- "Fill in 'John Doe' in the name field"

### Information
- "What's on this page?"
- "Get the page title"
- "Show me the current URL"
- "Read the page content"

### Navigation Controls
- "Scroll down"
- "Scroll to the bottom"
- "Go back"
- "Refresh this page"

### Screenshots
- "Take a screenshot"
- "Capture this page as screenshot.png"
- "Save a screenshot"

## ⚙️ Configuration

### Browser Options

Customize Chrome behavior in `browser_agent.py`:

```python
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--incognito')  # Private mode
options.add_argument('--headless')    # Background mode
options.add_argument('--disable-gpu')
```

### Timeout Settings

Adjust wait times:

```python
self.wait = WebDriverWait(self.driver, 10)  # 10 second timeout
```

### Custom User Agent

```python
options.add_argument('user-agent=Your Custom User Agent')
```

## 🔧 Advanced Usage

### Adding Custom Tools

1. Define the tool in `_define_tools()`:

```python
{
    "name": "extract_links",
    "description": "Extract all links from the current page",
    "parameters": {}
}
```

2. Implement the method:

```python
def extract_links(self) -> str:
    """Extract all links from the page."""
    try:
        links = self.driver.find_elements(By.TAG_NAME, 'a')
        urls = [link.get_attribute('href') for link in links]
        return f"Found {len(urls)} links: {urls[:10]}"
    except Exception as e:
        return f"Error extracting links: {str(e)}"
```

3. Add to `execute_tool()`:

```python
elif tool_name == "extract_links":
    return self.extract_links()
```

### Handling iFrames

```python
def switch_to_iframe(self, iframe_id: str) -> str:
    try:
        iframe = self.driver.find_element(By.ID, iframe_id)
        self.driver.switch_to.frame(iframe)
        return f"Switched to iframe: {iframe_id}"
    except Exception as e:
        return f"Error: {str(e)}"
```

### Working with Multiple Tabs

```python
def open_new_tab(self, url: str) -> str:
    self.driver.execute_script(f"window.open('{url}', '_blank');")
    self.driver.switch_to.window(self.driver.window_handles[-1])
    return f"Opened new tab: {url}"
```

## 🐛 Troubleshooting

### Issue: "ChromeDriver not found"

**Solution:**
```bash
pip install webdriver-manager
```

Then update `browser_agent.py`:
```python
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
self.driver = webdriver.Chrome(service=service, options=options)
```

### Issue: "Element not found"

**Solutions:**
- Increase wait time
- Check if element is in an iframe
- Verify element selector
- Wait for page to fully load

### Issue: "Gemini API quota exceeded"

**Solution:**
- Check your API usage at [Google AI Studio](https://makersuite.google.com/)
- Implement rate limiting
- Use caching for repeated queries

### Issue: "Page loads too slowly"

**Solution:**
```python
# Increase timeout
self.driver.set_page_load_timeout(30)

# Or use headless mode for faster execution
options.add_argument('--headless')
```

## 🔒 Security Best Practices

- ✅ **Never commit API keys** to version control
- ✅ Use environment variables for sensitive data
- ✅ Implement rate limiting for production use
- ✅ Validate and sanitize all user inputs
- ✅ Use headless mode for server deployments
- ✅ Implement proper error handling
- ⚠️ Be cautious when automating sensitive sites
- ⚠️ Respect websites' Terms of Service and robots.txt

## 📊 Performance Tips

1. **Use headless mode** for faster execution:
```python
options.add_argument('--headless')
```

2. **Disable images** for speed:
```python
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
```

3. **Batch operations** instead of multiple calls:
```python
# Instead of multiple commands, use one complex command
agent.process_command("Go to site, search for X, and screenshot results")
```

4. **Cache page information** to reduce redundant calls

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Areas for Contribution

- 🔧 Additional Selenium tools (drag-drop, alerts, windows)
- 🧪 Test coverage and CI/CD
- 📱 Mobile browser support
- 🎨 Better error messages and recovery
- 📚 More example workflows
- 🌍 Multi-language support
- 🔌 Plugin system

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Selenium](https://www.selenium.dev/) - Browser automation framework
- [Google Gemini](https://ai.google.dev/) - AI model for natural language understanding
- [ChromeDriver](https://chromedriver.chromium.org/) - Chrome automation driver

## 📧 Support

- 🐛 **Bug Reports**: [Open an issue](https://github.com/m97chahboun/SelenAI/issues)
- 💡 **Feature Requests**: [Start a discussion](https://github.com/m97chahboun/SelenAI/discussions)

## 🗺️ Roadmap

- [ ] Visual element detection using computer vision
- [ ] Multi-browser support (Firefox, Safari, Edge)
- [ ] Session persistence and replay
- [ ] Cloud deployment templates
- [ ] Browser extension version
- [ ] Mobile app automation
- [ ] Recording and playback features
- [ ] Integration with popular testing frameworks

## ⭐ Star History

If you find SelenAI useful, please consider giving it a star! ⭐

---

<div align="center">

**Made with ❤️ by developers, for developers**

[⬆ Back to Top](#-SelenAI)

</div>