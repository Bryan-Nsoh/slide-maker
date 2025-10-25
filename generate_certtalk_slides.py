#!/usr/bin/env python3
"""
Generate CertTalk presentation slides with professional layouts.
Creates 6 slides covering Approach (3) and Experiments (3).
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE


class CertTalkSlideGenerator:
    """Generate professional CertTalk presentation slides."""

    # Color scheme
    COLOR_AGENT_A = RGBColor(41, 128, 185)  # Blue
    COLOR_AGENT_B = RGBColor(39, 174, 96)   # Green
    COLOR_CONFLICT = RGBColor(231, 76, 60)  # Red
    COLOR_NEUTRAL = RGBColor(44, 62, 80)    # Dark gray
    COLOR_HIGHLIGHT = RGBColor(243, 156, 18) # Orange
    COLOR_BG_BOX = RGBColor(236, 240, 241)  # Light gray

    def __init__(self):
        self.prs = Presentation()
        self.prs.slide_width = Inches(10)
        self.prs.slide_height = Inches(7.5)

    def add_title_text(self, slide, title_text, top=0.3):
        """Add a centered title to the slide."""
        title_box = slide.shapes.add_textbox(
            Inches(0.5), Inches(top), Inches(9), Inches(0.6)
        )
        title_frame = title_box.text_frame
        title_frame.text = title_text
        p = title_frame.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.font.size = Pt(32)
        p.font.bold = True
        p.font.color.rgb = self.COLOR_NEUTRAL

    def add_textbox(self, slide, text, left, top, width, height,
                   font_size=14, bold=False, color=None, align=PP_ALIGN.LEFT,
                   font_name="Calibri"):
        """Add a text box with specified properties."""
        textbox = slide.shapes.add_textbox(
            Inches(left), Inches(top), Inches(width), Inches(height)
        )
        text_frame = textbox.text_frame
        text_frame.text = text
        text_frame.word_wrap = True

        for paragraph in text_frame.paragraphs:
            paragraph.alignment = align
            paragraph.font.size = Pt(font_size)
            paragraph.font.bold = bold
            paragraph.font.name = font_name
            if color:
                paragraph.font.color.rgb = color
            else:
                paragraph.font.color.rgb = self.COLOR_NEUTRAL

        return textbox

    def add_monospace_textbox(self, slide, text, left, top, width, height,
                             font_size=10, color=None):
        """Add a monospace text box for code/grids."""
        return self.add_textbox(slide, text, left, top, width, height,
                              font_size=font_size, color=color,
                              font_name="Courier New")

    def add_box(self, slide, left, top, width, height,
               fill_color=None, line_color=None, line_width=1.5):
        """Add a rectangular box/border."""
        shape = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(left), Inches(top), Inches(width), Inches(height)
        )

        if fill_color:
            shape.fill.solid()
            shape.fill.fore_color.rgb = fill_color
        else:
            shape.fill.background()

        shape.line.color.rgb = line_color if line_color else self.COLOR_NEUTRAL
        shape.line.width = Pt(line_width)

        return shape

    def add_arrow(self, slide, x1, y1, x2, y2, color=None, width=2.5):
        """Add an arrow connector."""
        connector = slide.shapes.add_connector(
            1,  # Straight connector
            Inches(x1), Inches(y1), Inches(x2), Inches(y2)
        )
        connector.line.color.rgb = color if color else self.COLOR_NEUTRAL
        connector.line.width = Pt(width)
        return connector

    def create_slide_1_problem_solution(self):
        """Slide 1: The Problem & Solution with grids."""
        slide = self.prs.slides.add_slide(self.prs.slide_layouts[6])  # Blank layout

        # Title
        self.add_title_text(slide, "Two Robots, Private Maps, One Question")

        # Grid A (Robot A sees)
        grid_a = """S . . . .
. . # . .
. . # . .
. . . . .
. . . . G"""

        self.add_textbox(slide, "Robot A sees:", 0.5, 1.2, 2.5, 0.3,
                        font_size=12, bold=True, color=self.COLOR_AGENT_A)
        self.add_monospace_textbox(slide, grid_a, 0.5, 1.5, 2.5, 1.5, font_size=16)
        self.add_box(slide, 0.45, 1.45, 2.6, 1.6, line_color=self.COLOR_AGENT_A)

        # Grid B (Robot B sees)
        grid_b = """S . . # .
. . . . .
. # . . .
. . . . #
. . . . G"""

        self.add_textbox(slide, "Robot B sees:", 3.2, 1.2, 2.5, 0.3,
                        font_size=12, bold=True, color=self.COLOR_AGENT_B)
        self.add_monospace_textbox(slide, grid_b, 3.2, 1.5, 2.5, 1.5, font_size=16)
        self.add_box(slide, 3.15, 1.45, 2.6, 1.6, line_color=self.COLOR_AGENT_B)

        # Union grid
        grid_union = """S . . # .
. . # . .
. # # . .
. . . . #
. . . . G"""

        self.add_textbox(slide, "Union U = A∪B:", 5.9, 1.2, 2.5, 0.3,
                        font_size=12, bold=True, color=self.COLOR_NEUTRAL)
        self.add_monospace_textbox(slide, grid_union, 5.9, 1.5, 2.5, 1.5, font_size=16)
        self.add_box(slide, 5.85, 1.45, 2.6, 1.6, line_color=self.COLOR_NEUTRAL, line_width=2.5)

        # Question
        self.add_textbox(slide, "Question: Can we reach G from S?", 0.5, 3.3, 8, 0.4,
                        font_size=18, bold=True, align=PP_ALIGN.CENTER)

        # Certificate boxes
        self.add_box(slide, 1, 4.1, 3.5, 2.3, fill_color=self.COLOR_BG_BOX)
        self.add_textbox(slide, "PATH_CERT", 1.2, 4.2, 3, 0.3,
                        font_size=16, bold=True, color=self.COLOR_AGENT_A)
        self.add_textbox(slide, '"Here\'s the route"', 1.2, 4.6, 3, 0.3,
                        font_size=14)
        self.add_textbox(slide, "S→→↓↓↓↓→→→G", 1.2, 5.0, 3, 0.4,
                        font_size=16, font_name="Courier New")
        self.add_textbox(slide, "12 bytes", 1.2, 5.6, 3, 0.3,
                        font_size=12, color=RGBColor(100, 100, 100))

        self.add_box(slide, 5.5, 4.1, 3.5, 2.3, fill_color=self.COLOR_BG_BOX)
        self.add_textbox(slide, "CUT_CERT", 5.7, 4.2, 3, 0.3,
                        font_size=16, bold=True, color=self.COLOR_CONFLICT)
        self.add_textbox(slide, '"Here\'s the barrier"', 5.7, 4.6, 3, 0.3,
                        font_size=14)
        self.add_textbox(slide, "████", 5.7, 5.0, 3, 0.4,
                        font_size=18)
        self.add_textbox(slide, "20 bytes", 5.7, 5.6, 3, 0.3,
                        font_size=12, color=RGBColor(100, 100, 100))

    def create_slide_2_protocol_flow(self):
        """Slide 2: Protocol Flow with sequence diagram."""
        slide = self.prs.slides.add_slide(self.prs.slide_layouts[6])

        # Title
        self.add_title_text(slide, "How Agents Talk")

        # Agent labels
        self.add_textbox(slide, "AGENT A", 1.5, 1.2, 2, 0.3,
                        font_size=14, bold=True, color=self.COLOR_AGENT_A,
                        align=PP_ALIGN.CENTER)
        self.add_textbox(slide, "(Initiator)", 1.5, 1.5, 2, 0.3,
                        font_size=11, align=PP_ALIGN.CENTER)

        self.add_textbox(slide, "AGENT B", 6.5, 1.2, 2, 0.3,
                        font_size=14, bold=True, color=self.COLOR_AGENT_B,
                        align=PP_ALIGN.CENTER)
        self.add_textbox(slide, "(Responder)", 6.5, 1.5, 2, 0.3,
                        font_size=11, align=PP_ALIGN.CENTER)

        # Fast path - vertical lines for agents
        agent_a_x = 2.5
        agent_b_x = 7.5

        # Message 1: PATH_PROPOSE
        self.add_arrow(slide, agent_a_x, 2.2, agent_b_x, 2.4, color=self.COLOR_AGENT_A)
        self.add_textbox(slide, "PATH_PROPOSE", 3.5, 2.0, 3, 0.25,
                        font_size=11, bold=True, color=self.COLOR_AGENT_A,
                        align=PP_ALIGN.CENTER)
        self.add_textbox(slide, '"Try this route: ↓↓↓→→→"', 3.5, 2.25, 3, 0.25,
                        font_size=9, align=PP_ALIGN.CENTER)

        # Check annotation
        self.add_textbox(slide, "Check against\nprivate map", 7.8, 2.5, 1.5, 0.4,
                        font_size=9)

        # Message 2: PATH_CERT
        self.add_arrow(slide, agent_b_x, 3.0, agent_a_x, 3.2, color=self.COLOR_AGENT_B)
        self.add_textbox(slide, "PATH_CERT", 3.8, 2.8, 3, 0.25,
                        font_size=11, bold=True, color=self.COLOR_AGENT_B,
                        align=PP_ALIGN.CENTER)
        self.add_textbox(slide, '"Certified ✓"', 3.8, 3.05, 3, 0.25,
                        font_size=9, align=PP_ALIGN.CENTER)

        # Message 3: ACK
        self.add_arrow(slide, agent_a_x, 3.6, agent_b_x, 3.8, color=self.COLOR_AGENT_A)
        self.add_textbox(slide, 'ACK "Got it"', 4.2, 3.5, 2, 0.25,
                        font_size=10, align=PP_ALIGN.CENTER)

        # Done markers
        self.add_textbox(slide, "● DONE (3 messages)", 1.2, 4.2, 3, 0.3,
                        font_size=12, bold=True)
        self.add_textbox(slide, "●", 6.5, 4.2, 1, 0.3,
                        font_size=12, bold=True, color=self.COLOR_AGENT_B)

        # Conflict path section
        self.add_textbox(slide, "With conflicts:", 0.5, 4.7, 2, 0.3,
                        font_size=12, bold=True)

        conflict_text = """│  CUT_PROPOSE "Barrier: cells X,Y,Z"
│  ────────────> NACK "Can't verify Y"
│  PROBE "Is Y blocked?"
│  ────────────> PROBE_REPLY "Yes"
│  CUT_PROPOSE (revised)
│  ────────────> CUT_CERT ✓
●  DONE (5-6 messages)"""

        self.add_monospace_textbox(slide, conflict_text, 0.8, 5.0, 8, 1.5,
                                  font_size=10)

    def create_slide_3_witness_bits(self):
        """Slide 3: Witness Bits explanation."""
        slide = self.prs.slides.add_slide(self.prs.slide_layouts[6])

        # Title
        self.add_title_text(slide, "How Agents Agree on Unseen Obstacles")

        # Proposal context
        self.add_textbox(slide, "A proposes cut: cells (2,1), (2,2), (2,3), (2,4)",
                        0.5, 1.3, 9, 0.3, font_size=13)

        # Main explanation box
        self.add_box(slide, 0.5, 1.8, 9, 3.2, fill_color=self.COLOR_BG_BOX)

        # Column headers
        self.add_textbox(slide, "A's view:", 0.7, 2.0, 2, 0.3,
                        font_size=12, bold=True, color=self.COLOR_AGENT_A)
        self.add_textbox(slide, "Witness bits:", 3.2, 2.0, 2.5, 0.3,
                        font_size=12, bold=True, color=self.COLOR_HIGHLIGHT)
        self.add_textbox(slide, "B's rule:", 6.2, 2.0, 2.5, 0.3,
                        font_size=12, bold=True, color=self.COLOR_AGENT_B)

        # Row 1
        self.add_textbox(slide, "(2,1) ← A sees #", 0.7, 2.4, 2.3, 0.25, font_size=10)
        self.add_textbox(slide, 'bit=0 "A vouches"', 3.2, 2.4, 2.5, 0.25, font_size=10)
        self.add_textbox(slide, "Accept if:", 6.2, 2.4, 2.5, 0.25, font_size=10)

        # Row 2
        self.add_textbox(slide, "(2,2) ← A sees #", 0.7, 2.7, 2.3, 0.25, font_size=10)
        self.add_textbox(slide, 'bit=0 "A vouches"', 3.2, 2.7, 2.5, 0.25, font_size=10)
        self.add_textbox(slide, "- B sees #", 6.2, 2.7, 2.5, 0.25, font_size=10)

        # Row 3
        self.add_textbox(slide, "(2,3) ← A sees #", 0.7, 3.0, 2.3, 0.25, font_size=10)
        self.add_textbox(slide, 'bit=1 "B vouches"', 3.2, 3.0, 2.5, 0.25, font_size=10,
                        color=self.COLOR_AGENT_B)
        self.add_textbox(slide, "OR", 6.2, 3.0, 2.5, 0.25, font_size=10, bold=True)

        # Row 4
        self.add_textbox(slide, "(2,4) ← A sees .", 0.7, 3.3, 2.3, 0.25, font_size=10)
        self.add_textbox(slide, 'bit=1 "B vouches"', 3.2, 3.3, 2.5, 0.25, font_size=10,
                        color=self.COLOR_AGENT_B)
        self.add_textbox(slide, "- bit=0", 6.2, 3.3, 2.5, 0.25, font_size=10)

        # Verification flow
        self.add_textbox(slide, "↓", 3.5, 3.7, 1, 0.3,
                        font_size=20, align=PP_ALIGN.CENTER)

        # Verification results
        self.add_textbox(slide, "B checks (2,3): B sees #  ✓ Accept", 1.5, 4.1, 5, 0.25,
                        font_size=11, color=self.COLOR_AGENT_B)
        self.add_textbox(slide, "B checks (2,4): B sees #  ✓ Accept", 1.5, 4.4, 5, 0.25,
                        font_size=11, color=self.COLOR_AGENT_B)

        # Failure case
        self.add_textbox(slide, "If witness=1 but B sees free → NACK → PROBE", 1.5, 4.8, 6, 0.3,
                        font_size=11, color=self.COLOR_CONFLICT)

        # Cost/benefit
        self.add_box(slide, 0.5, 5.5, 9, 1.3, line_color=self.COLOR_HIGHLIGHT, line_width=2)
        self.add_textbox(slide, "Cost: 1 bit per cell (~6-12 cells typical)", 0.7, 5.7, 8.5, 0.3,
                        font_size=12)
        self.add_textbox(slide, "Benefit: Accept peer-attested cells without seeing them", 0.7, 6.1, 8.5, 0.4,
                        font_size=12, bold=True, color=self.COLOR_HIGHLIGHT)

    def create_slide_4_experimental_setup(self):
        """Slide 4: Experimental Setup."""
        slide = self.prs.slides.add_slide(self.prs.slide_layouts[6])

        # Title
        self.add_title_text(slide, "Test Arena")

        # Dataset box
        self.add_box(slide, 0.5, 1.3, 9, 1.3, fill_color=self.COLOR_BG_BOX)
        self.add_textbox(slide, "1,000 cached instances", 0.7, 1.5, 8.5, 0.3,
                        font_size=14, bold=True)

        bullets = """• 10×10 grids, 4-neighbor movement
• s=(0,0) → t=(9,9) for all
• Mixed reachable/unreachable
• Varied obstacle density"""
        self.add_textbox(slide, bullets, 0.9, 1.9, 8, 0.8, font_size=12)

        # Constraints box
        self.add_textbox(slide, "Constraints (same for all systems):", 0.5, 2.8, 5, 0.3,
                        font_size=13, bold=True)
        self.add_box(slide, 0.5, 3.2, 9, 1.2, fill_color=self.COLOR_BG_BOX)

        constraints = """Max messages: 64
Max per packet: 256 bytes
Max total: 3,072 bytes
Deterministic agents (no randomness)"""
        self.add_textbox(slide, constraints, 0.9, 3.4, 8, 0.9, font_size=12)

        # Metrics section
        self.add_textbox(slide, "What we measure:", 0.5, 4.7, 3, 0.3,
                        font_size=13, bold=True)

        metrics = """• Success rate (oracle accepts certificate)
• Bytes per transcript
• Messages per transcript
• Interpretability (ends in certificate)"""
        self.add_textbox(slide, metrics, 0.7, 5.1, 8.5, 1.2, font_size=12)

    def create_slide_5_four_systems(self):
        """Slide 5: Four Systems Under Test."""
        slide = self.prs.slides.add_slide(self.prs.slide_layouts[6])

        # Title
        self.add_title_text(slide, "Baseline Comparison")

        # Send-All box (top left)
        self.add_box(slide, 0.3, 1.3, 2.2, 2.3, fill_color=self.COLOR_BG_BOX)
        self.add_textbox(slide, "Send-All", 0.4, 1.4, 2, 0.3,
                        font_size=13, bold=True)
        flow1 = """A: dumps
all indices
↓
B: synth
union
↓
B: certify

Raw data
approach"""
        self.add_textbox(slide, flow1, 0.5, 1.8, 1.8, 1.6, font_size=10)

        # CertTalk box (top center - emphasized)
        self.add_box(slide, 2.7, 1.3, 2.5, 2.3,
                    fill_color=RGBColor(240, 248, 255),
                    line_color=self.COLOR_HIGHLIGHT, line_width=3)
        self.add_textbox(slide, "CertTalk", 2.8, 1.4, 2.3, 0.3,
                        font_size=14, bold=True, color=self.COLOR_HIGHLIGHT)
        self.add_textbox(slide, "(this work)", 2.8, 1.7, 2.3, 0.25,
                        font_size=10)
        flow2 = """A: proposes
complete
artifact
+ witness
↓
B: validates
locally
↓
B: certify
or NACK

1 probe/
branch"""
        self.add_textbox(slide, flow2, 2.9, 2.0, 2.1, 1.5, font_size=10)

        # Greedy-Probe box (top right)
        self.add_box(slide, 5.4, 1.3, 2.2, 2.3, fill_color=self.COLOR_BG_BOX)
        self.add_textbox(slide, "Greedy-Probe", 5.5, 1.4, 2, 0.3,
                        font_size=13, bold=True)
        flow3 = """A: probes
then
proposes
↓
B: checks
& certifies

Explore
first"""
        self.add_textbox(slide, flow3, 5.6, 1.8, 1.8, 1.6, font_size=10)

        # Responder-MinCut box (bottom left)
        self.add_box(slide, 0.3, 3.8, 2.5, 2.3, fill_color=self.COLOR_BG_BOX)
        self.add_textbox(slide, "Responder-", 0.4, 3.9, 2.3, 0.3,
                        font_size=13, bold=True)
        self.add_textbox(slide, "MinCut", 0.4, 4.2, 2.3, 0.3,
                        font_size=13, bold=True)
        flow4 = """B: leads
with cut
↓
A: probes
conflicts

Cut-only
(unreach)"""
        self.add_textbox(slide, flow4, 0.5, 4.6, 2.1, 1.4, font_size=10)

        # Legend at bottom
        self.add_textbox(slide,
                        "Each system uses different strategy to minimize communication",
                        1, 6.5, 8, 0.4, font_size=11, align=PP_ALIGN.CENTER)

    def create_slide_6_evaluation_dimensions(self):
        """Slide 6: What We Measure."""
        slide = self.prs.slides.add_slide(self.prs.slide_layouts[6])

        # Title
        self.add_title_text(slide, "Evaluation Dimensions")

        # Dimension 1: Correctness
        self.add_box(slide, 0.5, 1.3, 9, 1.0, fill_color=self.COLOR_BG_BOX)
        self.add_textbox(slide, "1. Correctness", 0.7, 1.4, 8.5, 0.3,
                        font_size=14, bold=True, color=self.COLOR_AGENT_A)
        self.add_textbox(slide, "Oracle accepts final certificate?", 0.9, 1.7, 8, 0.25,
                        font_size=11)
        self.add_textbox(slide, "(PATH_CERT or CUT_CERT passes verification)", 0.9, 1.95, 8, 0.25,
                        font_size=10)

        # Dimension 2: Communication Cost
        self.add_box(slide, 0.5, 2.5, 9, 1.3, fill_color=self.COLOR_BG_BOX)
        self.add_textbox(slide, "2. Communication Cost", 0.7, 2.6, 8.5, 0.3,
                        font_size=14, bold=True, color=self.COLOR_AGENT_B)
        comm_bullets = """• Total bytes in transcript
• Number of messages exchanged
(median + 95% bootstrap CI)"""
        self.add_textbox(slide, comm_bullets, 0.9, 2.95, 8, 0.75, font_size=11)

        # Dimension 3: Interpretability
        self.add_box(slide, 0.5, 4.0, 9, 1.8, fill_color=self.COLOR_BG_BOX)
        self.add_textbox(slide, "3. Interpretability", 0.7, 4.1, 8.5, 0.3,
                        font_size=14, bold=True, color=self.COLOR_HIGHLIGHT)
        self.add_textbox(slide, "Does transcript end in human-readable proof?", 0.9, 4.45, 8, 0.25,
                        font_size=11)
        interp_bullets = """• PATH_CERT: "Route through these cells"
• CUT_CERT: "Barrier at these cells"
vs raw data requiring solver to interpret"""
        self.add_textbox(slide, interp_bullets, 0.9, 4.75, 8, 0.9, font_size=11)

        # Bottom note
        self.add_textbox(slide, "All systems evaluated on same 1,000 instances",
                        0.5, 6.2, 9, 0.4, font_size=12, bold=True,
                        align=PP_ALIGN.CENTER, color=self.COLOR_NEUTRAL)

    def generate_presentation(self, output_file="CertTalk_Presentation.pptx"):
        """Generate all slides and save presentation."""
        print("Generating Slide 1: Problem & Solution...")
        self.create_slide_1_problem_solution()

        print("Generating Slide 2: Protocol Flow...")
        self.create_slide_2_protocol_flow()

        print("Generating Slide 3: Witness Bits...")
        self.create_slide_3_witness_bits()

        print("Generating Slide 4: Experimental Setup...")
        self.create_slide_4_experimental_setup()

        print("Generating Slide 5: Four Systems...")
        self.create_slide_5_four_systems()

        print("Generating Slide 6: Evaluation Dimensions...")
        self.create_slide_6_evaluation_dimensions()

        self.prs.save(output_file)
        print(f"\n✓ Presentation saved to: {output_file}")
        print(f"✓ Total slides: {len(self.prs.slides)}")


def main():
    """Main entry point."""
    generator = CertTalkSlideGenerator()
    generator.generate_presentation()


if __name__ == "__main__":
    main()
