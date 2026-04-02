"""
Create a demonstration piece with the enhanced Kirnberger generator
"""

# Import the game - need to handle module with spaces in name
import importlib.util
import os

spec = importlib.util.spec_from_file_location(
    "mozart_generator",
    os.path.join(os.path.dirname(__file__), "Mozart Music Generator.py")
)
mozart_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mozart_module)

KirnbergerGame = mozart_module.KirnbergerGame

# Create game instance
game = KirnbergerGame()

# Generate a beautiful composition with seed for reproducibility
print("Creating a specially crafted demonstration piece...")
print()

# Manually choose nice-sounding variants for a demonstration
# These choices were selected to create nice melodic flow
beautiful_choices = [
    2,   # Bar 1: G5 E5 C5 - descending arpeggio
    3,   # Bar 2: B4 C5 D5 - rising line
    2,   # Bar 3: C5 E5 A5 - expanding upward
    1,   # Bar 4: F4 A4 C5 - rising arpeggio
    2,   # Bar 5: B4 A4 G4 - stepwise descent
    2,   # Bar 6: E5 D5 C5 - classic cadence
    1,   # Bar 7: C5 D5 E5 - new phrase ascending
    5,   # Bar 8: G4 B4 D5 - building
    2,   # Bar 9: C5 E5 A5 - reaching higher
    3,   # Bar 10: B4 E5 G5 - more expansion
    2,   # Bar 11: A4 C5 F5 - continuing
    2,   # Bar 12: E5 D5 C5 - preparing cadence
    1,   # Bar 13: D5 C5 B4 - dominant tension
    2    # Bar 14: E5 D5 C5 - final resolution
]

composition = game.generate_with_choices(beautiful_choices)

# Print the composition
game.print_composition(composition)

# Generate MIDI with full accompaniment
print("\nGenerating enhanced MIDI file with:")
print("  - Melodic right hand part")
print("  - Chord accompaniment in left hand")
print()

game.create_midi(composition, "kirnberger_demo_enhanced.mid")

print()
print("=" * 70)
print("DONE! Play 'kirnberger_demo_enhanced.mid' in your media player")
print("=" * 70)
