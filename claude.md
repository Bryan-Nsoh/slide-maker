# Slide Maker Agent Guide

## IMPORTANT: Slide Creation Rules

<ul>
  <li><strong>MIRROR RULE</strong>: This file (claude.md) must always mirror AGENTS.md exactly.</li>
  <li><strong>MANDATORY WORKFLOW</strong>: When asked to create slides, you MUST use the instructions in AGENTS.md and all tools referred to in this project.</li>
  <li><strong>NO ALTERNATIVES</strong>: No other way of creating slides is allowed. Only use:
    <ul>
      <li>PPTXCreator Python API from <code>src/pptx_creator.py</code></li>
      <li>CLI tool via <code>python -m src.cli</code></li>
      <li>JSON outline workflow</li>
    </ul>
  </li>
  <li><strong>OUTPUT LOCATION</strong>: Always create slides in <code>slides/&lt;project-name&gt;/</code> to keep projects isolated.</li>
</ul>

## Working style

<ul>
  <li>Keep documentation in Markdown but use HTML list tags (`<ul>` and `<ol>`) instead of manual bullet symbols.</li>
  <li>Favor ASCII-safe characters inside XML or HTML that will eventually flow into PPTX packages.</li>
  <li>Store project-specific assets inside <code>slides/&lt;project&gt;</code> so experiments never clash.</li>
  <li>Use Python 3.10+ and Node 18+ when installing dependencies locally.</li>
</ul>

## PowerPoint Creator for Claude Code (README snapshot)

A Python tool for creating PowerPoint presentations programmatically using the <code>python-pptx</code> library. This project is designed to work seamlessly with Claude Code for automated presentation generation.

### Features

<ul>
  <li><strong>Programmatic PowerPoint Creation</strong>: Generate presentations entirely through code.</li>
  <li><strong>Multiple Slide Types</strong>: Support for title slides, bullet point slides, text slides, and image slides.</li>
  <li><strong>JSON-Based Outlines</strong>: Create presentations from structured JSON files.</li>
  <li><strong>Command Line Interface</strong>: Easy-to-use CLI for quick presentation generation.</li>
  <li><strong>Template Support</strong>: Use existing PowerPoint templates for consistent styling.</li>
  <li><strong>Template Analysis</strong>: Analyze existing presentations to understand layouts and structure.</li>
  <li><strong>Claude Code Integration</strong>: Designed specifically for use with Claude Code workflows.</li>
</ul>

### Installation

#### Prerequisites

<ul>
  <li>Python 3.10 or higher.</li>
  <li>Virtual environment (recommended).</li>
</ul>

#### Setup

<ol>
  <li>Clone or navigate to the project directory.
    <pre><code>cd /path/to/PPTX</code></pre>
  </li>
  <li>Create and activate a virtual environment.
    <pre><code>python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate</code></pre>
  </li>
  <li>Install dependencies.
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
</ol>

### Usage

#### Command Line Interface

<pre><code># Create a sample presentation
python -m src.cli --sample my_presentation.pptx

# Create from JSON outline
python -m src.cli --json examples/sample_outline.json --output my_presentation.pptx

# Generate sample JSON file
python -m src.cli --sample-json my_outline.json
</code></pre>

#### Python API

<pre><code>from src.pptx_creator import PPTXCreator

# Create a new presentation
creator = PPTXCreator()

# Add title slide
creator.add_title_slide(
    title="My Presentation",
    subtitle="Created with Python"
)

# Add content slide with bullet points
creator.add_content_slide(
    title="Key Points",
    content=[
        "First important point",
        "Second important point",
        "Third important point"
    ]
)

# Save the presentation
creator.save_presentation("my_presentation.pptx")
</code></pre>

#### Using Templates for Professional Styling

<pre><code>from src.pptx_creator import PPTXCreator

# Create presentation using an existing template
creator = PPTXCreator("templates/template.pptx")

# Add slides using template styling
creator.add_title_slide("Professional Presentation", "Using template styling")
creator.add_content_slide("Key Benefits", [
    "Consistent professional appearance",
    "Maintains corporate branding",
    "Uses predefined layouts and colors"
])

creator.save_presentation("styled_presentation.pptx")
</code></pre>

### JSON Outline Format

Create presentations from structured JSON files:

```json
{
  "title": "Presentation Title",
  "subtitle": "Optional Subtitle",
  "slides": [
    {
      "type": "content",
      "title": "Slide Title",
      "content": ["Bullet point 1", "Bullet point 2"]
    },
    {
      "type": "text",
      "title": "Text Slide",
      "content": "Paragraph content goes here."
    },
    {
      "type": "image",
      "title": "Image Slide",
      "image_path": "path/to/image.png"
    }
  ]
}
```

### Examples

<pre><code>cd examples
python basic_example.py
</code></pre>

This creates a sample presentation demonstrating various slide types.

### Project Structure

```
PPTX/
├── src/
│   ├── __init__.py
│   ├── pptx_creator.py    # Main PowerPoint creation class (includes template support)
│   └── cli.py             # Command-line interface
├── tests/
│   └── test_pptx_creator.py
├── examples/
│   ├── basic_example.py
│   └── sample_outline.json
├── templates/             # Place your .pptx templates here (gitignored)
├── content/               # Private notes and source materials (gitignored)
├── requirements.txt
├── pyproject.toml
```

## CLAUDE.md highlights

This toolkit allows programmatic generation of presentations through code, CLI, or JSON outlines.

### Environment setup

<ul>
  <li><strong>Virtual Environment</strong>: Always use <code>source venv/bin/activate</code> before running Python commands.</li>
  <li><strong>Dependencies</strong>: Install via <code>requirements.txt</code> with latest stable versions.</li>
  <li><strong>Python Version</strong>: 3.10+ required.</li>
</ul>

### Project structure

```
src/
├── pptx_creator.py    # Main PowerPoint creation class (includes template support)
└── cli.py             # Command-line interface

tests/
└── test_pptx_creator.py

examples/
├── basic_example.py
└── sample_outline.json

templates/
├── README.md          # Template usage instructions
└── *.pptx             # User template files (gitignored)

content/
└── *.md, *.txt, etc.  # Private notes and source materials (gitignored)
```

#### Content folder

The <code>content/</code> directory stores private notes, meeting minutes, and source documents. It is gitignored to keep sensitive materials out of version control.

### Development commands

#### Testing

<pre><code>source venv/bin/activate
python -m pytest tests/ -v
</code></pre>

#### Code quality

<pre><code># Format code
python -m black src/ tests/ examples/

# Sort imports
python -m isort src/ tests/ examples/

# Type checking
python -m mypy src/
</code></pre>

#### Running examples

<pre><code># CLI sample presentation
python -m src.cli --sample output.pptx

# From JSON outline
python -m src.cli --json examples/sample_outline.json --output report.pptx

# Basic Python example
cd examples && python basic_example.py
</code></pre>

### Code patterns

#### Creating presentations

Always use the <code>PPTXCreator</code> class.

<pre><code>from src.pptx_creator import PPTXCreator

creator = PPTXCreator()
creator.add_title_slide("Title", "Subtitle")
creator.add_content_slide("Content", ["Point 1", "Point 2"])
creator.save_presentation("output.pptx")
</code></pre>

#### Template-based presentations

<pre><code>from src.pptx_creator import PPTXCreator

creator = PPTXCreator("templates/my_template.pptx")
creator.add_title_slide("Professional Title", "Uses template styling")
creator.add_content_slide("Content", ["Point 1", "Point 2"])
creator.save_presentation("styled_output.pptx")
</code></pre>

### JSON structure

Use this format for outline-based presentations:

```json
{
  "title": "Presentation Title",
  "subtitle": "Optional Subtitle",
  "slides": [
    {"type": "content", "title": "Title", "content": ["Point 1"]},
    {"type": "text", "title": "Title", "content": "Paragraph text"},
    {"type": "image", "title": "Title", "image_path": "path/to/image.png"}
  ]
}
```

### Common tasks

#### Using templates

<ol>
  <li><strong>Prepare your template</strong>.
    <ol>
      <li>Open template in PowerPoint.</li>
      <li>Delete all content slides (keep only slide master and layouts).</li>
      <li>Save as cleaned template in <code>templates/</code>.</li>
    </ol>
  </li>
  <li><strong>Use in code</strong>.
    <pre><code>creator = PPTXCreator("templates/your_template.pptx")
</code></pre>
  </li>
  <li><strong>Template files are gitignored</strong> so personal templates stay private.</li>
</ol>

#### Adding new slide types

<ol>
  <li>Add method to <code>PPTXCreator</code> class in <code>src/pptx_creator.py</code>.</li>
  <li>Update <code>create_from_outline</code> to handle the new type.</li>
  <li>Add tests in <code>tests/test_pptx_creator.py</code>.</li>
  <li>Update CLI help text and examples.</li>
</ol>

#### Extending CLI

<ul>
  <li>Modify <code>src/cli.py</code> for new options.</li>
  <li>Follow existing argument parsing patterns.</li>
  <li>Add help text and usage examples.</li>
</ul>

### Testing requirements

<ul>
  <li>All new features must have tests.</li>
  <li>Tests must pass before committing.</li>
  <li>Use <code>pytest</code> with descriptive names.</li>
  <li>Test both success and error cases.</li>
</ul>

### Dependencies to remember

<ul>
  <li><strong>python-pptx</strong>: Core PowerPoint creation.</li>
  <li><strong>pytest</strong>: Testing framework.</li>
  <li><strong>black</strong>: Code formatting.</li>
  <li><strong>isort</strong>: Import sorting.</li>
  <li><strong>mypy</strong>: Type checking.</li>
</ul>

### File naming conventions

<ul>
  <li>PowerPoint files: <code>*.pptx</code>.</li>
  <li>JSON outlines: <code>*_outline.json</code> or <code>*.json</code>.</li>
  <li>Test files: <code>test_*.py</code>.</li>
  <li>Example files: <code>*_example.py</code>.</li>
</ul>

### Error handling

<ul>
  <li>Validate file paths before using images.</li>
  <li>Handle missing JSON keys gracefully.</li>
  <li>Provide meaningful error messages.</li>
  <li>Log important operations with appropriate levels.</li>
</ul>

### Performance notes

<ul>
  <li>Activate the virtual environment for all operations.</li>
  <li>Large presentations may take time to generate.</li>
</ul>

## Template instructions (concise)

Refer to <code>templates/README.md</code> for detailed steps on cleaning and using template decks. Templates remain gitignored so branded assets stay private.
