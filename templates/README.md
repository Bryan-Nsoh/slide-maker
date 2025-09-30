# Templates Directory

Place your PowerPoint template files (<code>.pptx</code>) in this directory to use them with the PPTXCreator.

## How to Use Templates

<ol>
  <li><strong>Add your template file</strong> to this directory (for example <code>my_template.pptx</code>).</li>
  <li><strong>Clean your template</strong> (important!).
    <ol>
      <li>Open your template in PowerPoint.</li>
      <li>Delete all content slides, keeping only the slide master and layouts.</li>
      <li>Save the file.</li>
    </ol>
  </li>
  <li><strong>Use in your code</strong>.
    <pre><code>from src.pptx_creator import PPTXCreator

creator = PPTXCreator("templates/my_template.pptx")
creator.add_title_slide("My Presentation", "Using template styling")
creator.save_presentation("output.pptx")
</code></pre>
  </li>
</ol>

## Template Preparation Tips

<ul>
  <li><strong>Keep slide masters and layouts</strong> because they preserve styling, fonts, colors, and branding.</li>
  <li><strong>Remove content slides</strong> to avoid mixing old content with new.</li>
  <li><strong>Test your template</strong> by creating a simple presentation to ensure it works correctly.</li>
</ul>

## File Structure

```
templates/
├── README.md          # This file
├── my_template.pptx   # Your template files (gitignored)
└── other_template.pptx
```

Template <code>.pptx</code> files are automatically ignored by git to keep personal or company templates private while allowing the folder structure to be shared.
