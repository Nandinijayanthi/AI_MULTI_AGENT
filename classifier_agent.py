import json

def classify_input(content: str, source: str) -> dict:
    result = {
        "format": "PlainText",
        "intent": "Other"
    }

    content_strip = content.strip()

    if content_strip.startswith('{') and content_strip.endswith('}'):
        result["format"] = "JSON"
        try:
            data = json.loads(content_strip)

            # If JSON has 'test_cases' list with 'tasks' keys
            if "test_cases" in data and isinstance(data["test_cases"], list):
                if all("tasks" in case for case in data["test_cases"]):
                    result["intent"] = "Task Analysis"
                else:
                    result["intent"] = "Data Set"
            
            # Check for book related JSON
            elif "books" in data and isinstance(data["books"], list):
                result["intent"] = "Book Related"
            
            # Check for temperature/weather data
            elif any(key in data for key in ["temperature", "temp", "weather"]):
                result["intent"] = "Temperature/Weather"
            
            # Check for web scraping related data
            elif any(key in data for key in ["websites", "urls", "url", "scraped_data"]):
                result["intent"] = "Web Scraping"

            # Check for product or e-commerce data
            elif any(key in data for key in ["products", "price", "product_id"]):
                result["intent"] = "Product Data"

            # Check for employee or HR data
            elif any(key in data for key in ["employees", "salary", "department"]):
                result["intent"] = "Employee Data"

            else:
                result["intent"] = "Generic JSON"

        except Exception:
            result["intent"] = "Invalid JSON"

    elif "Subject:" in content and "From:" in content:
        result["format"] = "Email"
        result["intent"] = "Communication"

    elif "%PDF" in content[:100]:
        result["format"] = "PDF"
        result["intent"] = "Document"

    return result
