"""Tests for the PPTXCreator class."""

import pytest
import sys
import os
from pathlib import Path
import tempfile

# Add src to path for importing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from pptx_creator import PPTXCreator


class TestPPTXCreator:
    """Test cases for PPTXCreator functionality."""
    
    def test_init(self):
        """Test PPTXCreator initialization."""
        creator = PPTXCreator()
        assert creator.presentation is not None
        assert creator.get_slide_count() == 0
    
    def test_add_title_slide(self):
        """Test adding a title slide."""
        creator = PPTXCreator()
        slide = creator.add_title_slide("Test Title", "Test Subtitle")
        
        assert creator.get_slide_count() == 1
        assert slide is not None
        assert slide.shapes.title.text == "Test Title"
    
    def test_add_title_slide_no_subtitle(self):
        """Test adding a title slide without subtitle."""
        creator = PPTXCreator()
        slide = creator.add_title_slide("Test Title")
        
        assert creator.get_slide_count() == 1
        assert slide.shapes.title.text == "Test Title"
    
    def test_add_content_slide(self):
        """Test adding a content slide with bullet points."""
        creator = PPTXCreator()
        content = ["Point 1", "Point 2", "Point 3"]
        slide = creator.add_content_slide("Test Content", content)
        
        assert creator.get_slide_count() == 1
        assert slide.shapes.title.text == "Test Content"
    
    def test_add_text_slide(self):
        """Test adding a text slide."""
        creator = PPTXCreator()
        text_content = "This is a test paragraph with some content."
        slide = creator.add_text_slide("Test Text", text_content)
        
        assert creator.get_slide_count() == 1
        assert slide.shapes.title.text == "Test Text"
    
    def test_save_presentation(self):
        """Test saving a presentation."""
        creator = PPTXCreator()
        creator.add_title_slide("Test Presentation")
        
        with tempfile.TemporaryDirectory() as temp_dir:
            output_file = os.path.join(temp_dir, "test.pptx")
            creator.save_presentation(output_file)
            
            assert Path(output_file).exists()
            assert Path(output_file).stat().st_size > 0
    
    def test_create_from_outline(self):
        """Test creating presentation from outline dictionary."""
        creator = PPTXCreator()
        outline = {
            "title": "Test Presentation",
            "subtitle": "Test Subtitle",
            "slides": [
                {
                    "type": "content",
                    "title": "Content Slide",
                    "content": ["Point 1", "Point 2"]
                },
                {
                    "type": "text",
                    "title": "Text Slide",
                    "content": "This is text content."
                }
            ]
        }
        
        creator.create_from_outline(outline)
        
        # Should have title slide + 2 content slides = 3 total
        assert creator.get_slide_count() == 3
    
    def test_multiple_slides(self):
        """Test adding multiple slides."""
        creator = PPTXCreator()
        
        creator.add_title_slide("Title")
        creator.add_content_slide("Content", ["Point 1"])
        creator.add_text_slide("Text", "Text content")
        
        assert creator.get_slide_count() == 3