#!/usr/bin/env python3
"""Create grid visualizations for CertTalk slides using matplotlib."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from pathlib import Path

# Output directory
img_dir = Path("workspace/images")
img_dir.mkdir(parents=True, exist_ok=True)

# Colors
COLOR_BLOCKED = '#2c3e50'  # Dark gray for blocked cells
COLOR_FREE = '#ecf0f1'     # Light gray for free cells
COLOR_PATH = '#3498db'     # Blue for path
COLOR_CUT = '#e74c3c'      # Red for cut
COLOR_GRID = '#95a5a6'     # Gray for grid lines
COLOR_TEXT = '#2c3e50'     # Dark text

def create_grid_base(ax, size=5):
    """Create base grid with styling."""
    ax.set_xlim(-0.5, size - 0.5)
    ax.set_ylim(-0.5, size - 0.5)
    ax.set_aspect('equal')
    ax.invert_yaxis()  # (0,0) at top-left

    # Remove ticks
    ax.set_xticks([])
    ax.set_yticks([])

    # Draw grid lines
    for i in range(size + 1):
        ax.axhline(i - 0.5, color=COLOR_GRID, linewidth=1.5, zorder=1)
        ax.axvline(i - 0.5, color=COLOR_GRID, linewidth=1.5, zorder=1)

def add_cell(ax, row, col, cell_type, size=5):
    """Add a cell to the grid."""
    if cell_type == '#':  # Blocked
        rect = patches.Rectangle((col - 0.4, row - 0.4), 0.8, 0.8,
                                 facecolor=COLOR_BLOCKED, edgecolor=COLOR_BLOCKED,
                                 zorder=2)
        ax.add_patch(rect)
    elif cell_type == 'S':  # Start
        circle = patches.Circle((col, row), 0.35, facecolor='#27ae60',
                               edgecolor='#229954', linewidth=2, zorder=3)
        ax.add_patch(circle)
        ax.text(col, row, 'S', ha='center', va='center', fontsize=20,
               fontweight='bold', color='white', zorder=4)
    elif cell_type == 'G':  # Goal
        circle = patches.Circle((col, row), 0.35, facecolor='#f39c12',
                               edgecolor='#d68910', linewidth=2, zorder=3)
        ax.add_patch(circle)
        ax.text(col, row, 'G', ha='center', va='center', fontsize=20,
               fontweight='bold', color='white', zorder=4)
    elif cell_type == 'X':  # Cut marker
        # Draw X
        ax.plot([col - 0.3, col + 0.3], [row - 0.3, row + 0.3],
               color=COLOR_CUT, linewidth=4, zorder=3)
        ax.plot([col - 0.3, col + 0.3], [row + 0.3, row - 0.3],
               color=COLOR_CUT, linewidth=4, zorder=3)
    elif cell_type in ['→', '↓', '↑', '←']:  # Path arrows
        ax.text(col, row, cell_type, ha='center', va='center',
               fontsize=24, color=COLOR_PATH, fontweight='bold', zorder=3)

def create_grid_from_pattern(pattern, filename, title="", with_legend=False):
    """Create grid image from pattern string."""
    rows = [r.strip() for r in pattern.strip().split('\n')]
    size = len(rows)

    fig, ax = plt.subplots(figsize=(6, 6), facecolor='white')
    create_grid_base(ax, size)

    # Fill in cells
    for r, row in enumerate(rows):
        cells = row.split()
        for c, cell in enumerate(cells):
            if cell != '.':
                add_cell(ax, r, c, cell, size)
            else:
                # Fill free cells with light color
                rect = patches.Rectangle((c - 0.45, r - 0.45), 0.9, 0.9,
                                        facecolor=COLOR_FREE, edgecolor='none',
                                        zorder=0)
                ax.add_patch(rect)

    # Add title
    if title:
        ax.set_title(title, fontsize=16, fontweight='bold', pad=15, color=COLOR_TEXT)

    # Add legend if requested
    if with_legend:
        legend_elements = [
            patches.Patch(facecolor='#27ae60', edgecolor='#229954', label='S = Start'),
            patches.Patch(facecolor='#f39c12', edgecolor='#d68910', label='G = Goal'),
            patches.Patch(facecolor=COLOR_BLOCKED, label='# = Blocked'),
            patches.Patch(facecolor=COLOR_FREE, label='. = Free')
        ]
        ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(0, 1.2),
                 frameon=True, fontsize=14, ncol=2, fancybox=True, shadow=True,
                 framealpha=0.95, edgecolor='#95a5a6', facecolor='white')

    plt.tight_layout()
    plt.savefig(img_dir / filename, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"✓ Created {filename}")

def create_grid_with_path(pattern, filename, title=""):
    """Create grid with path overlay."""
    create_grid_from_pattern(pattern, filename, title)

def create_grid_with_cut(pattern, filename, title=""):
    """Create grid with cut markers."""
    create_grid_from_pattern(pattern, filename, title)

# Slide 1: Robot A's map
grid_a = """S . . . .
. . # . .
. . # . .
. . . . .
. . . . G"""

create_grid_from_pattern(grid_a, "grid_robot_a.png", "Robot A sees:")

# Slide 1: Robot B's map
grid_b = """S . . # .
. . . . .
. # . . .
. . . . #
. . . . G"""

create_grid_from_pattern(grid_b, "grid_robot_b.png", "Robot B sees:")

# Slide 1: Union map (with legend)
grid_union = """S . . # .
. . # . .
. # # . .
. . . . #
. . . . G"""

create_grid_from_pattern(grid_union, "grid_union.png", "Union (A ∪ B):", with_legend=True)

# Slide 2: Path certificate example
grid_path = """S . . . .
↓ . # . .
↓ # # . .
↓ . . . #
→ → → → G"""

create_grid_with_path(grid_path, "grid_path_cert.png", "PATH Certificate")

# Slide 2: Cut certificate example
grid_cut = """S . X # .
. . X . .
. # X . .
. . X . #
. . X . G"""

create_grid_with_cut(grid_cut, "grid_cut_cert.png", "CUT Certificate")

# Slide 3: Witness bits example grids
# Grid showing cells in question
grid_witness = """S . . # .
. # # # .
. # # # .
. . . . #
. . . . G"""

create_grid_from_pattern(grid_witness, "grid_witness.png", "")

# Slide 5: Example instances
# Instance 1: Path exists
grid_ex1 = """S . # . .
. . # . .
. . . . .
. . . . .
. . . . G"""
create_grid_from_pattern(grid_ex1, "grid_example1.png", "")

# Instance 2: Blocked
grid_ex2 = """S # # # .
. . . . .
. . . . .
. . . . .
. . . . G"""
create_grid_from_pattern(grid_ex2, "grid_example2.png", "")

# Instance 3: Blocked barrier (complete wall)
grid_ex3 = """S . . . .
# # # # #
. . . . .
. . . . .
. . . . G"""
create_grid_from_pattern(grid_ex3, "grid_example3.png", "")

# Instance 4: Easy path (direct route to G)
grid_ex4 = """S → → → →
. . . . ↓
. . . . ↓
. . . . ↓
. . . . G"""
create_grid_from_pattern(grid_ex4, "grid_example4.png", "")

print("\n✓ All grid images created in workspace/images/")
