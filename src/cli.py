#!/usr/bin/env python3
"""Command-line interface for PowerPoint creation."""

import argparse
import json
import logging
import sys
from pathlib import Path
from typing import Dict, Any

from .pptx_creator import PPTXCreator

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def create_sample_presentation(output_file: str) -> None:
    """Create a sample presentation to demonstrate functionality."""
    creator = PPTXCreator()
    
    # Title slide
    creator.add_title_slide(
        title="Sample Presentation",
        subtitle="Created with Claude Code & python-pptx"
    )
    
    # Content slide
    creator.add_content_slide(
        title="Key Features",
        content=[
            "Programmatic PowerPoint creation",
            "Support for text, bullets, and images",
            "Customizable layouts and styling",
            "Easy integration with Claude Code"
        ]
    )
    
    # Text slide
    creator.add_text_slide(
        title="About This Tool",
        text_content="This PowerPoint creation tool allows you to generate professional presentations "
                    "programmatically using Python. It's designed to work seamlessly with Claude Code "
                    "for automated content creation and formatting."
    )
    
    creator.save_presentation(output_file)
    print(f"Sample presentation created: {output_file}")


def create_from_json(json_file: str, output_file: str) -> None:
    """Create a presentation from a JSON outline file."""
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            outline = json.load(f)
    except FileNotFoundError:
        logger.error(f"JSON file not found: {json_file}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in file {json_file}: {e}")
        sys.exit(1)
    
    creator = PPTXCreator()
    try:
        creator.create_from_outline(outline)
        creator.save_presentation(output_file)
        print(f"Presentation created from {json_file}: {output_file}")
    except Exception as e:
        logger.error(f"Error creating presentation: {e}")
        sys.exit(1)


def create_sample_json(output_file: str) -> None:
    """Create a sample JSON outline file."""
    sample_outline = {
        "title": "My Presentation",
        "subtitle": "A presentation created from JSON",
        "slides": [
            {
                "type": "content",
                "title": "Introduction",
                "content": [
                    "Welcome to our presentation",
                    "This was created from a JSON file",
                    "It demonstrates the flexibility of our tool"
                ]
            },
            {
                "type": "text",
                "title": "Detailed Information",
                "content": "This slide contains paragraph text instead of bullet points. "
                          "You can use this format when you need to present more detailed "
                          "information or explanations."
            },
            {
                "type": "content",
                "title": "Next Steps",
                "content": [
                    "Customize the JSON file for your needs",
                    "Add more slides and content",
                    "Generate your presentation"
                ]
            }
        ]
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(sample_outline, f, indent=2, ensure_ascii=False)
    
    print(f"Sample JSON outline created: {output_file}")


def main() -> None:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Create PowerPoint presentations programmatically",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --sample presentation.pptx     # Create a sample presentation
  %(prog)s --json outline.json output.pptx # Create from JSON outline
  %(prog)s --sample-json outline.json      # Generate sample JSON file
        """
    )
    
    parser.add_argument(
        '--sample', 
        metavar='OUTPUT',
        help='Create a sample presentation'
    )
    
    parser.add_argument(
        '--json', 
        metavar='JSON_FILE',
        help='Create presentation from JSON outline file'
    )
    
    parser.add_argument(
        '--output', '-o',
        metavar='OUTPUT_FILE',
        help='Output PowerPoint file (required with --json)'
    )
    
    parser.add_argument(
        '--sample-json',
        metavar='JSON_FILE',
        help='Create a sample JSON outline file'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose logging'
    )
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Validate arguments
    if not any([args.sample, args.json, args.sample_json]):
        parser.print_help()
        sys.exit(1)
    
    if args.json and not args.output:
        parser.error("--output is required when using --json")
    
    # Execute commands
    try:
        if args.sample:
            create_sample_presentation(args.sample)
        elif args.json:
            create_from_json(args.json, args.output)
        elif args.sample_json:
            create_sample_json(args.sample_json)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        if args.verbose:
            raise
        sys.exit(1)


if __name__ == '__main__':
    main()