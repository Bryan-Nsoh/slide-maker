#!/usr/bin/env python3
"""
Render each slide's content directly to PNG images for review.
"""

from PIL import Image, ImageDraw, ImageFont
import os


class SlideRenderer:
    """Render slides to images."""

    # Color scheme
    COLOR_AGENT_A = (41, 128, 185)  # Blue
    COLOR_AGENT_B = (39, 174, 96)   # Green
    COLOR_CONFLICT = (231, 76, 60)  # Red
    COLOR_NEUTRAL = (44, 62, 80)    # Dark gray
    COLOR_HIGHLIGHT = (243, 156, 18) # Orange
    COLOR_BG_BOX = (236, 240, 241)  # Light gray

    def __init__(self, width=1200, height=900):
        self.width = width
        self.height = height

        # Load fonts
        try:
            self.font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 42)
            self.font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
            self.font_medium = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
            self.font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
            self.font_mono = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 20)
            self.font_mono_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 14)
        except:
            print("Warning: Could not load fonts, using default")
            self.font_title = ImageFont.load_default()
            self.font_large = ImageFont.load_default()
            self.font_medium = ImageFont.load_default()
            self.font_small = ImageFont.load_default()
            self.font_mono = ImageFont.load_default()
            self.font_mono_small = ImageFont.load_default()

    def create_slide_1(self):
        """Slide 1: The Problem & Solution."""
        img = Image.new('RGB', (self.width, self.height), color='white')
        draw = ImageDraw.Draw(img)

        # Title
        title = "Two Robots, Private Maps, One Question"
        bbox = draw.textbbox((0, 0), title, font=self.font_title)
        title_width = bbox[2] - bbox[0]
        draw.text(((self.width - title_width) // 2, 30), title, fill=self.COLOR_NEUTRAL, font=self.font_title)

        # Grid A
        grid_a = """S . . . .
. . # . .
. . # . .
. . . . .
. . . . G"""

        draw.text((50, 150), "Robot A sees:", fill=self.COLOR_AGENT_A, font=self.font_medium)
        draw.text((50, 190), grid_a, fill=self.COLOR_NEUTRAL, font=self.font_mono)
        draw.rectangle([45, 185, 280, 380], outline=self.COLOR_AGENT_A, width=2)

        # Grid B
        grid_b = """S . . # .
. . . . .
. # . . .
. . . . #
. . . . G"""

        draw.text((360, 150), "Robot B sees:", fill=self.COLOR_AGENT_B, font=self.font_medium)
        draw.text((360, 190), grid_b, fill=self.COLOR_NEUTRAL, font=self.font_mono)
        draw.rectangle([355, 185, 590, 380], outline=self.COLOR_AGENT_B, width=2)

        # Union grid
        grid_union = """S . . # .
. . # . .
. # # . .
. . . . #
. . . . G"""

        draw.text((670, 150), "Union U = A∪B:", fill=self.COLOR_NEUTRAL, font=self.font_medium)
        draw.text((670, 190), grid_union, fill=self.COLOR_NEUTRAL, font=self.font_mono)
        draw.rectangle([665, 185, 900, 380], outline=self.COLOR_NEUTRAL, width=3)

        # Question
        question = "Question: Can we reach G from S?"
        bbox = draw.textbbox((0, 0), question, font=self.font_large)
        q_width = bbox[2] - bbox[0]
        draw.text(((self.width - q_width) // 2, 420), question, fill=self.COLOR_NEUTRAL, font=self.font_large)

        # PATH_CERT box
        draw.rectangle([100, 500, 520, 840], fill=self.COLOR_BG_BOX, outline=self.COLOR_NEUTRAL, width=2)
        draw.text((130, 520), "PATH_CERT", fill=self.COLOR_AGENT_A, font=self.font_large)
        draw.text((130, 570), '"Here\'s the route"', fill=self.COLOR_NEUTRAL, font=self.font_medium)
        draw.text((130, 620), "S→→↓↓↓↓→→→G", fill=self.COLOR_NEUTRAL, font=self.font_mono)
        draw.text((130, 780), "12 bytes", fill=(100, 100, 100), font=self.font_small)

        # CUT_CERT box
        draw.rectangle([620, 500, 1040, 840], fill=self.COLOR_BG_BOX, outline=self.COLOR_NEUTRAL, width=2)
        draw.text((650, 520), "CUT_CERT", fill=self.COLOR_CONFLICT, font=self.font_large)
        draw.text((650, 570), '"Here\'s the barrier"', fill=self.COLOR_NEUTRAL, font=self.font_medium)
        draw.text((650, 620), "████", fill=self.COLOR_NEUTRAL, font=self.font_mono)
        draw.text((650, 780), "20 bytes", fill=(100, 100, 100), font=self.font_small)

        return img

    def create_slide_2(self):
        """Slide 2: Protocol Flow."""
        img = Image.new('RGB', (self.width, self.height), color='white')
        draw = ImageDraw.Draw(img)

        # Title
        title = "How Agents Talk"
        bbox = draw.textbbox((0, 0), title, font=self.font_title)
        title_width = bbox[2] - bbox[0]
        draw.text(((self.width - title_width) // 2, 30), title, fill=self.COLOR_NEUTRAL, font=self.font_title)

        # Agent labels
        draw.text((200, 120), "AGENT A", fill=self.COLOR_AGENT_A, font=self.font_large)
        draw.text((195, 155), "(Initiator)", fill=self.COLOR_NEUTRAL, font=self.font_small)

        draw.text((850, 120), "AGENT B", fill=self.COLOR_AGENT_B, font=self.font_large)
        draw.text((840, 155), "(Responder)", fill=self.COLOR_NEUTRAL, font=self.font_small)

        # Vertical timelines
        agent_a_x = 270
        agent_b_x = 920
        y_start = 200

        # Timeline lines
        draw.line([(agent_a_x, y_start), (agent_a_x, y_start + 300)], fill=(200, 200, 200), width=2)
        draw.line([(agent_b_x, y_start), (agent_b_x, y_start + 300)], fill=(200, 200, 200), width=2)

        # Message 1: PATH_PROPOSE
        y1 = y_start + 20
        draw.line([(agent_a_x, y1), (agent_b_x, y1 + 20)], fill=self.COLOR_AGENT_A, width=3)
        draw.polygon([(agent_b_x, y1 + 20), (agent_b_x - 10, y1 + 15), (agent_b_x - 10, y1 + 25)],
                    fill=self.COLOR_AGENT_A)
        draw.text((450, y1 - 20), "PATH_PROPOSE", fill=self.COLOR_AGENT_A, font=self.font_medium)
        draw.text((420, y1 + 5), '"Try this route: ↓↓↓→→→"', fill=self.COLOR_NEUTRAL, font=self.font_small)

        # Check annotation
        draw.text((930, y1 + 30), "Check against", fill=self.COLOR_NEUTRAL, font=self.font_small)
        draw.text((930, y1 + 50), "private map", fill=self.COLOR_NEUTRAL, font=self.font_small)

        # Message 2: PATH_CERT
        y2 = y_start + 120
        draw.line([(agent_b_x, y2), (agent_a_x, y2 + 20)], fill=self.COLOR_AGENT_B, width=3)
        draw.polygon([(agent_a_x, y2 + 20), (agent_a_x + 10, y2 + 15), (agent_a_x + 10, y2 + 25)],
                    fill=self.COLOR_AGENT_B)
        draw.text((480, y2 - 20), "PATH_CERT", fill=self.COLOR_AGENT_B, font=self.font_medium)
        draw.text((495, y2 + 5), '"Certified ✓"', fill=self.COLOR_NEUTRAL, font=self.font_small)

        # Message 3: ACK
        y3 = y_start + 200
        draw.line([(agent_a_x, y3), (agent_b_x, y3 + 20)], fill=self.COLOR_AGENT_A, width=3)
        draw.polygon([(agent_b_x, y3 + 20), (agent_b_x - 10, y3 + 15), (agent_b_x - 10, y3 + 25)],
                    fill=self.COLOR_AGENT_A)
        draw.text((520, y3 - 5), 'ACK "Got it"', fill=self.COLOR_NEUTRAL, font=self.font_medium)

        # Done markers
        draw.text((200, y_start + 280), "● DONE (3 messages)", fill=self.COLOR_NEUTRAL, font=self.font_medium)
        draw.text((920, y_start + 280), "●", fill=self.COLOR_AGENT_B, font=self.font_medium)

        # Conflict path
        draw.text((50, 550), "With conflicts:", fill=self.COLOR_NEUTRAL, font=self.font_large)

        conflict_text = """CUT_PROPOSE "Barrier: cells X,Y,Z"
────────────> NACK "Can't verify Y"
PROBE "Is Y blocked?"
────────────> PROBE_REPLY "Yes"
CUT_PROPOSE (revised)
────────────> CUT_CERT ✓
DONE (5-6 messages)"""

        draw.text((80, 590), conflict_text, fill=self.COLOR_NEUTRAL, font=self.font_mono_small)

        return img

    def create_slide_3(self):
        """Slide 3: Witness Bits."""
        img = Image.new('RGB', (self.width, self.height), color='white')
        draw = ImageDraw.Draw(img)

        # Title
        title = "How Agents Agree on Unseen Obstacles"
        bbox = draw.textbbox((0, 0), title, font=self.font_title)
        title_width = bbox[2] - bbox[0]
        draw.text(((self.width - title_width) // 2, 30), title, fill=self.COLOR_NEUTRAL, font=self.font_title)

        # Proposal
        draw.text((50, 130), "A proposes cut: cells (2,1), (2,2), (2,3), (2,4)",
                 fill=self.COLOR_NEUTRAL, font=self.font_medium)

        # Main explanation box
        draw.rectangle([50, 180, 1150, 600], fill=self.COLOR_BG_BOX, outline=self.COLOR_NEUTRAL, width=2)

        # Headers
        draw.text((70, 200), "A's view:", fill=self.COLOR_AGENT_A, font=self.font_medium)
        draw.text((400, 200), "Witness bits:", fill=self.COLOR_HIGHLIGHT, font=self.font_medium)
        draw.text((750, 200), "B's rule:", fill=self.COLOR_AGENT_B, font=self.font_medium)

        # Table rows
        y_offset = 250
        row_height = 40

        rows = [
            ("(2,1) ← A sees #", 'bit=0 "A vouches"', "Accept if:", self.COLOR_NEUTRAL),
            ("(2,2) ← A sees #", 'bit=0 "A vouches"', "- B sees #", self.COLOR_NEUTRAL),
            ("(2,3) ← A sees #", 'bit=1 "B vouches"', "OR", self.COLOR_AGENT_B),
            ("(2,4) ← A sees .", 'bit=1 "B vouches"', "- bit=0", self.COLOR_AGENT_B),
        ]

        for i, (col1, col2, col3, color2) in enumerate(rows):
            y = y_offset + i * row_height
            draw.text((70, y), col1, fill=self.COLOR_NEUTRAL, font=self.font_small)
            draw.text((400, y), col2, fill=color2, font=self.font_small)
            draw.text((750, y), col3, fill=self.COLOR_NEUTRAL, font=self.font_small)

        # Arrow and verification
        draw.text((580, 420), "↓", fill=self.COLOR_NEUTRAL, font=self.font_title)

        draw.text((200, 480), "B checks (2,3): B sees #  ✓ Accept",
                 fill=self.COLOR_AGENT_B, font=self.font_medium)
        draw.text((200, 520), "B checks (2,4): B sees #  ✓ Accept",
                 fill=self.COLOR_AGENT_B, font=self.font_medium)

        # Failure case
        draw.text((180, 560), "If witness=1 but B sees free → NACK → PROBE",
                 fill=self.COLOR_CONFLICT, font=self.font_medium)

        # Cost/benefit box
        draw.rectangle([50, 640, 1150, 850], outline=self.COLOR_HIGHLIGHT, width=3)
        draw.text((70, 660), "Cost: 1 bit per cell (~6-12 cells typical)",
                 fill=self.COLOR_NEUTRAL, font=self.font_medium)
        draw.text((70, 750), "Benefit: Accept peer-attested cells without seeing them",
                 fill=self.COLOR_HIGHLIGHT, font=self.font_large)

        return img

    def create_slide_4(self):
        """Slide 4: Experimental Setup."""
        img = Image.new('RGB', (self.width, self.height), color='white')
        draw = ImageDraw.Draw(img)

        # Title
        title = "Test Arena"
        bbox = draw.textbbox((0, 0), title, font=self.font_title)
        title_width = bbox[2] - bbox[0]
        draw.text(((self.width - title_width) // 2, 30), title, fill=self.COLOR_NEUTRAL, font=self.font_title)

        # Dataset box
        draw.rectangle([50, 130, 1150, 310], fill=self.COLOR_BG_BOX, outline=self.COLOR_NEUTRAL, width=2)
        draw.text((70, 150), "1,000 cached instances", fill=self.COLOR_NEUTRAL, font=self.font_large)

        bullets = [
            "• 10×10 grids, 4-neighbor movement",
            "• s=(0,0) → t=(9,9) for all",
            "• Mixed reachable/unreachable",
            "• Varied obstacle density"
        ]

        for i, bullet in enumerate(bullets):
            draw.text((100, 200 + i * 30), bullet, fill=self.COLOR_NEUTRAL, font=self.font_medium)

        # Constraints
        draw.text((50, 340), "Constraints (same for all systems):",
                 fill=self.COLOR_NEUTRAL, font=self.font_large)
        draw.rectangle([50, 390, 1150, 570], fill=self.COLOR_BG_BOX, outline=self.COLOR_NEUTRAL, width=2)

        constraints = [
            "Max messages: 64",
            "Max per packet: 256 bytes",
            "Max total: 3,072 bytes",
            "Deterministic agents (no randomness)"
        ]

        for i, constraint in enumerate(constraints):
            draw.text((100, 410 + i * 40), constraint, fill=self.COLOR_NEUTRAL, font=self.font_medium)

        # Metrics
        draw.text((50, 600), "What we measure:", fill=self.COLOR_NEUTRAL, font=self.font_large)

        metrics = [
            "• Success rate (oracle accepts certificate)",
            "• Bytes per transcript",
            "• Messages per transcript",
            "• Interpretability (ends in certificate)"
        ]

        for i, metric in enumerate(metrics):
            draw.text((100, 650 + i * 40), metric, fill=self.COLOR_NEUTRAL, font=self.font_medium)

        return img

    def create_slide_5(self):
        """Slide 5: Four Systems."""
        img = Image.new('RGB', (self.width, self.height), color='white')
        draw = ImageDraw.Draw(img)

        # Title
        title = "Baseline Comparison"
        bbox = draw.textbbox((0, 0), title, font=self.font_title)
        title_width = bbox[2] - bbox[0]
        draw.text(((self.width - title_width) // 2, 30), title, fill=self.COLOR_NEUTRAL, font=self.font_title)

        # Send-All box
        draw.rectangle([30, 130, 300, 480], fill=self.COLOR_BG_BOX, outline=self.COLOR_NEUTRAL, width=2)
        draw.text((50, 150), "Send-All", fill=self.COLOR_NEUTRAL, font=self.font_large)
        send_all_text = """A: dumps
all indices
↓
B: synth
union
↓
B: certify

Raw data
approach"""
        draw.text((60, 200), send_all_text, fill=self.COLOR_NEUTRAL, font=self.font_small)

        # CertTalk box (emphasized)
        draw.rectangle([330, 130, 680, 480], fill=(240, 248, 255), outline=self.COLOR_HIGHLIGHT, width=4)
        draw.text((350, 150), "CertTalk", fill=self.COLOR_HIGHLIGHT, font=self.font_large)
        draw.text((350, 185), "(this work)", fill=self.COLOR_NEUTRAL, font=self.font_small)
        certtalk_text = """A: proposes
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
        draw.text((360, 220), certtalk_text, fill=self.COLOR_NEUTRAL, font=self.font_small)

        # Greedy-Probe box
        draw.rectangle([710, 130, 980, 480], fill=self.COLOR_BG_BOX, outline=self.COLOR_NEUTRAL, width=2)
        draw.text((730, 150), "Greedy-Probe", fill=self.COLOR_NEUTRAL, font=self.font_large)
        greedy_text = """A: probes
then
proposes
↓
B: checks
& certifies

Explore
first"""
        draw.text((740, 200), greedy_text, fill=self.COLOR_NEUTRAL, font=self.font_small)

        # Responder-MinCut box
        draw.rectangle([30, 510, 350, 820], fill=self.COLOR_BG_BOX, outline=self.COLOR_NEUTRAL, width=2)
        draw.text((50, 530), "Responder-MinCut", fill=self.COLOR_NEUTRAL, font=self.font_large)
        responder_text = """B: leads
with cut
↓
A: probes
conflicts

Cut-only
(unreach)"""
        draw.text((60, 580), responder_text, fill=self.COLOR_NEUTRAL, font=self.font_small)

        # Legend
        legend = "Each system uses different strategy to minimize communication"
        bbox = draw.textbbox((0, 0), legend, font=self.font_medium)
        leg_width = bbox[2] - bbox[0]
        draw.text(((self.width - leg_width) // 2, 850), legend, fill=self.COLOR_NEUTRAL, font=self.font_medium)

        return img

    def create_slide_6(self):
        """Slide 6: Evaluation Dimensions."""
        img = Image.new('RGB', (self.width, self.height), color='white')
        draw = ImageDraw.Draw(img)

        # Title
        title = "Evaluation Dimensions"
        bbox = draw.textbbox((0, 0), title, font=self.font_title)
        title_width = bbox[2] - bbox[0]
        draw.text(((self.width - title_width) // 2, 30), title, fill=self.COLOR_NEUTRAL, font=self.font_title)

        # Dimension 1: Correctness
        draw.rectangle([50, 130, 1150, 280], fill=self.COLOR_BG_BOX, outline=self.COLOR_NEUTRAL, width=2)
        draw.text((70, 150), "1. Correctness", fill=self.COLOR_AGENT_A, font=self.font_large)
        draw.text((90, 190), "Oracle accepts final certificate?", fill=self.COLOR_NEUTRAL, font=self.font_medium)
        draw.text((90, 230), "(PATH_CERT or CUT_CERT passes verification)",
                 fill=self.COLOR_NEUTRAL, font=self.font_small)

        # Dimension 2: Communication Cost
        draw.rectangle([50, 310, 1150, 520], fill=self.COLOR_BG_BOX, outline=self.COLOR_NEUTRAL, width=2)
        draw.text((70, 330), "2. Communication Cost", fill=self.COLOR_AGENT_B, font=self.font_large)
        draw.text((90, 370), "• Total bytes in transcript", fill=self.COLOR_NEUTRAL, font=self.font_medium)
        draw.text((90, 410), "• Number of messages exchanged", fill=self.COLOR_NEUTRAL, font=self.font_medium)
        draw.text((90, 450), "(median + 95% bootstrap CI)", fill=self.COLOR_NEUTRAL, font=self.font_small)

        # Dimension 3: Interpretability
        draw.rectangle([50, 550, 1150, 780], fill=self.COLOR_BG_BOX, outline=self.COLOR_NEUTRAL, width=2)
        draw.text((70, 570), "3. Interpretability", fill=self.COLOR_HIGHLIGHT, font=self.font_large)
        draw.text((90, 610), "Does transcript end in human-readable proof?",
                 fill=self.COLOR_NEUTRAL, font=self.font_medium)
        draw.text((90, 650), '• PATH_CERT: "Route through these cells"',
                 fill=self.COLOR_NEUTRAL, font=self.font_medium)
        draw.text((90, 690), '• CUT_CERT: "Barrier at these cells"',
                 fill=self.COLOR_NEUTRAL, font=self.font_medium)
        draw.text((90, 730), "vs raw data requiring solver to interpret",
                 fill=self.COLOR_NEUTRAL, font=self.font_small)

        # Bottom note
        note = "All systems evaluated on same 1,000 instances"
        bbox = draw.textbbox((0, 0), note, font=self.font_large)
        note_width = bbox[2] - bbox[0]
        draw.text(((self.width - note_width) // 2, 820), note,
                 fill=self.COLOR_NEUTRAL, font=self.font_large)

        return img

    def render_all_slides(self, output_dir="slide_images"):
        """Render all slides to PNG images."""
        os.makedirs(output_dir, exist_ok=True)

        slides = [
            ("Slide 1: Problem & Solution", self.create_slide_1),
            ("Slide 2: Protocol Flow", self.create_slide_2),
            ("Slide 3: Witness Bits", self.create_slide_3),
            ("Slide 4: Experimental Setup", self.create_slide_4),
            ("Slide 5: Four Systems", self.create_slide_5),
            ("Slide 6: Evaluation Dimensions", self.create_slide_6),
        ]

        for i, (name, func) in enumerate(slides, 1):
            print(f"Rendering {name}...")
            img = func()
            output_path = f"{output_dir}/slide_{i}.png"
            img.save(output_path)
            print(f"  Saved to {output_path}")

        print(f"\n✓ All slides rendered to {output_dir}/")


if __name__ == "__main__":
    renderer = SlideRenderer()
    renderer.render_all_slides()
