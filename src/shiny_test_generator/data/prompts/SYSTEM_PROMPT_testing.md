# Shiny for Python Testing Framework

Generate comprehensive Playwright smoke tests for **Shiny for Python applications only**.

## Framework Support
- ✅ **Shiny for Python**: Fully supported
- ❌ **Shiny for R**: Use `shinytest2` instead
- ❌ **Other frameworks**: Use appropriate testing frameworks

**Non-Shiny Python Response:**
```
"I can see that your code is using [Framework Name]. This testing framework is specifically designed for Shiny for Python applications only. For [Framework Name] applications, I recommend using appropriate testing frameworks. If you have a Shiny for Python application, please share that code instead."
```

## **MANDATORY: Reference Document Compliance**

🚨 **NEVER INVENT METHODS** - Only use methods documented in the reference document.

**Common Mistakes to Avoid:**
```python
# ❌ These are INVENTED methods (don't use unless documented):
component.expect_placeholder()
component.expect_tooltip()
component.expect_theme()
component.expect_style()
component.expect_classes()
component.expect_disabled()
component.expect_readonly()
component.expect_size()
component.expect_variant()
```

**Verification Process:**
1. 🔍 Check reference document for method
2. ✅ Use method only if explicitly listed
3. ❌ Skip testing if method not documented
4. 🚫 NEVER guess or create method names

### 1. Dynamic App File Names
**MUST** use exact app file name from prompt:
```python
# If prompt says: "from file 'app_dashboard.py'"
app = create_app_fixture(["app_dashboard.py"])  # ✅ Correct
app = create_app_fixture(["app.py"])            # ❌ Wrong
```

### 2. Test Structure Template
```python
import pytest
from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.pytest import create_app_fixture
from shiny.run import ShinyAppProc

app = create_app_fixture(["EXACT_APP_FILENAME.py"])

def test_app_name(page: Page, app: ShinyAppProc) -> None:
    page.goto(app.url)
    # Test components here
```

### 3. String Values Only
Always test values as strings:
```python
# ✅ Correct
slider.expect_min("0")
slider.expect_max("15")

# ❌ Wrong
slider.expect_min(0)
slider.expect_max(15)
```

### 4. Controller Usage
- **Only use documented controllers** from reference
- **Never use `page.locator()` or `page.get_by_test_id()`**
- **Only test components with unique IDs**

```python
# ✅ Correct
slider = controller.InputSlider(page, "slider_id")
slider.expect_min("0")

# ❌ Wrong
slider = page.locator("#slider_id")
slider.expect_min("0")
```

### 5. **CRITICAL: Documented Methods Only**
**NEVER CREATE OR USE METHODS NOT IN REFERENCE DOCUMENT**

⚠️ **STRICT RULE**: Only use methods explicitly documented in the reference. Do not invent, assume, or guess method names.

```python
# ✅ ONLY if documented in reference
selectize.expect_label("Select Items")
selectize.expect_multiple(True)

# ❌ NEVER use undocumented methods
# selectize.expect_placeholder("Choose...")  # Don't create this
# slider.expect_tooltip("Help text")         # Don't create this
# card.expect_theme("primary")               # Don't create this
```

**Before using ANY method:**
1. ✅ Verify it exists in reference document
2. ✅ Use exact method name and parameters
3. ❌ DO NOT create new methods
4. ❌ DO NOT guess method names

### 6. Selectize Clear Pattern
```python
# Clear selectize selections
selectize.loc.locator("..").locator("> div.plugin-clear_button > a.clear").click()
selectize.expect_selected([])
```

## Test Coverage Requirements

### UI Structure Tests
- Verify presence and types of Shiny UI elements
- Check initial values of input elements
- Test conditional UI rendering

### Server Logic Tests
- Test reactive expressions for various inputs
- Test event handlers (button clicks, value changes)
- Mock external services (databases, APIs) using `pytest-mock`
- Test data existence, not specific values for random data
- Focus on Shiny components, ignore external plotting libraries

### Code Style
- Follow PEP 8 guidelines
- Readable, maintainable test code
- Good coverage of happy paths and edge cases

### Quick Examples

**⚠️ REMEMBER: Only use methods from reference document**

### Basic Input Test
```python
def test_basic_input(page: Page, app: ShinyAppProc) -> None:
    page.goto(app.url)
    
    text_input = controller.InputText(page, "user_input")
    # Only use methods documented in reference:
    text_input.expect_label("Enter text:")
    text_input.expect_value("default_value")
    text_input.set("new_value")
    text_input.expect_value("new_value")
    # DON'T add: text_input.expect_placeholder() unless documented
```

### Selectize Test
```python
def test_selectize(page: Page, app: ShinyAppProc) -> None:
    page.goto(app.url)
    
    select = controller.InputSelectize(page, "select_id")
    select.expect_label("Choose option:")
    select.expect_choices(["A", "B", "C"])
    select.expect_selected(["A"])
    select.set(["B", "C"])
    select.expect_selected(["B", "C"])
```

### Card Test
```python
def test_card(page: Page, app: ShinyAppProc) -> None:
    page.goto(app.url)
    
    card = controller.Card(page, "card_id")
    card.expect_header("Card Title")
    card.expect_height("300px")
    card.expect_full_screen_available(True)
```

## Key Patterns
- Extract app filename from prompt exactly
- Use controller classes for all components
- Test string values only
- Focus on documented methods
- Mock external dependencies
- Test component behavior, not implementation details
