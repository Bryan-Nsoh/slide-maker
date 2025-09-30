# SLIDE MAKER - MANDATORY WORKFLOW

## CRITICAL INSTRUCTIONS

**YOU MUST USE THE INSTRUCTIONS IN THIS FILE (claude.md / AGENTS.md) AND ALL TOOLS IN THIS PROJECT TO CREATE SLIDES.**

**NO OTHER WAY OF CREATING SLIDES IS ALLOWED.**

### Available Tools for Slide Creation

1. **html2pptx.js** - Core library to convert HTML slides to PowerPoint
2. **thumbnail.py** - Generate visual thumbnail grids for verification
3. **inventory.py** - Extract text inventory from existing presentations
4. **replace.py** - Bulk replace text in presentations
5. **rearrange.py** - Duplicate, reorder, and delete slides
6. **pack.py** - Pack XML files into PPTX
7. **unpack.py** - Unpack PPTX into XML files
8. **validate.py** - Validate OOXML structure

### Workflow Requirements

- **For new presentations**: Use html2pptx.js workflow (HTML → PowerPoint)
- **For editing existing presentations**: Use unpack.py → edit XML → pack.py workflow
- **For template-based presentations**: Use rearrange.py → inventory.py → replace.py workflow
- **Always validate visually**: Use thumbnail.py to generate thumbnails and inspect slides
- **Output location**: Create all slides in project root or specified output directory

### Mirroring Rule

**IMPORTANT**: claude.md and AGENTS.md must always mirror each other exactly.

When making updates:
```bash
./mirror.sh  # Automatically sync claude.md → AGENTS.md
```

---

