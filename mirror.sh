#!/bin/bash
# Mirror claude.md and AGENTS.md

if [ ! -f claude.md ]; then
    echo "Error: claude.md not found"
    exit 1
fi

cp claude.md AGENTS.md
echo "✓ Mirrored claude.md to AGENTS.md"
