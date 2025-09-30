# Slide Maker Toolkit

The toolkit combines a Python-based presentation builder and JavaScript HTML-to-PowerPoint helpers so you can quickly assemble polished slide decks.

## Repository layout

```
.
├── AGENTS.md           # Consolidated developer reference
├── README.md           # Getting started guide (this file)
├── examples/           # Sample Python entry points and JSON outlines
├── javascript/         # Node utilities (html2pptx renderer)
├── pyproject.toml      # Poetry configuration for the Python toolkit
├── requirements.txt    # Python dependency pinning for pip workflows
├── slides/             # Workspace for in-progress slide projects
├── src/                # Python package with CLI and PPTX creator class
├── templates/          # Template instructions and user-provided PPTX themes
└── tests/              # Automated tests for the Python toolkit
```

## Python environment

<ol>
  <li>Create and activate a virtual environment.
    <pre><code>python3 -m venv .venv
source .venv/bin/activate</code></pre>
  </li>
  <li>Install dependencies with pip or Poetry.
    <pre><code>pip install -r requirements.txt
# or
poetry install</code></pre>
  </li>
</ol>

### Running the CLI

<pre><code># Create a sample deck
python -m src.cli --sample slides/demo.pptx

# Build from a JSON outline
python -m src.cli --json examples/sample_outline.json --output slides/outline.pptx

# Export a starter outline
python -m src.cli --sample-json slides/new_outline.json
</code></pre>

### Using the Python API

<pre><code>from src.pptx_creator import PPTXCreator

creator = PPTXCreator()
creator.add_title_slide("Title", "Subtitle")
creator.add_content_slide("Agenda", ["Intro", "Highlights", "Next steps"])
creator.save_presentation("slides/team-update.pptx")
</code></pre>

## JavaScript utilities

<ul>
  <li>Install Node dependencies with <code>npm install</code>.</li>
  <li>Use <code>javascript/html2pptx.js</code> to turn approved HTML layouts into PPTX files with <code>pptxgenjs</code>.</li>
  <li>Run <code>npm run prepare:playwright</code> when you need to rasterize HTML in a headless browser for QA.</li>
</ul>

## Slides workspace

Store each engagement under <code>slides/&lt;project&gt;</code> so generated decks, outlines, and assets stay isolated. Keep templates in <code>templates/</code> (they are gitignored) and reference them from Python by passing the template path to <code>PPTXCreator</code>.

## Next steps

<ul>
  <li>Review <code>AGENTS.md</code> for the full set of docs extracted from the upstream zip bundle.</li>
  <li>Open <code>examples/basic_example.py</code> and run it to verify your environment.</li>
  <li>Use <code>tests/test_pptx_creator.py</code> as a template when extending functionality.</li>
</ul>
