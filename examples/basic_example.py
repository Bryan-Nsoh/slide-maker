#!/usr/bin/env python3
"""Basic example of creating a PowerPoint presentation."""

import sys
import os

# Add src to path for importing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from pptx_creator import PPTXCreator


def create_basic_presentation():
    """Create a basic presentation with different slide types."""
    creator = PPTXCreator()
    
    # Title slide
    creator.add_title_slide(
        title="Welcome to PowerPoint Creation",
        subtitle="Automated presentation generation with Python"
    )
    
    # Content slide with bullet points
    creator.add_content_slide(
        title="What We'll Cover",
        content=[
            "Setting up the environment",
            "Creating different slide types",
            "Customizing presentations",
            "Saving and sharing your work"
        ]
    )
    
    # Text slide with paragraph content
    creator.add_text_slide(
        title="Why Automate Presentations?",
        text_content="Automating PowerPoint creation saves time and ensures consistency "
                    "across multiple presentations. It's especially useful for reports, "
                    "data visualization, and templated content that needs regular updates."
    )
    
    # Another content slide
    creator.add_content_slide(
        title="Benefits of This Approach",
        content=[
            "Consistent formatting and styling",
            "Easy integration with data sources",
            "Version control for presentation content",
            "Scalable for multiple presentations",
            "Reduces manual formatting work"
        ]
    )
    
    # Final slide
    creator.add_text_slide(
        title="Thank You!",
        text_content="This presentation was created programmatically using the python-pptx "
                    "library. You can now customize and extend this code for your specific needs."
    )
    
    # Save the presentation
    output_file = "basic_presentation.pptx"
    creator.save_presentation(output_file)
    print(f"Created presentation with {creator.get_slide_count()} slides: {output_file}")


if __name__ == "__main__":
    create_basic_presentation()