# Kirnberger's Musical Dice Game

A Python implementation of Kirnberger's algorithmic composition system.

## Features

✅ **All 4 Features Implemented:**

### 1. Actual Musical Data
- 14 bars with Mozart-style melodic variants
- Period 1: 6 bars (I-V-vi-IV-V-I)
- Period 2: 8 bars (I-V-vi-iii-IV-I6/4-V-I)
- 11 unique melodic variants per bar
- Each bar contains 3 eighth notes in 3/8 time

### 2. MIDI Output
- Generates playable MIDI files (.mid)
- Uses music21 library
- Proper tempo (120 BPM) and key signature (C major)
- Can export to MusicXML for notation software

### 3. Interactive Mode
- **Option 1:** Generate random composition
- **Option 2:** Roll dice for each bar (simulates traditional dice game)
- **Option 3:** Manually choose variants (1-11 for each of 14 bars)
- **Option 4:** Generate with seed (reproducible results)
- **Option 5:** View statistics
- Save outputs as MIDI or JSON

### 4. Sample Data
- Complete with 154 pre-composed melodic variants (11 × 14 bars)
- Harmonically correct progressions
- Classical period style

## Usage

### Quick Start
```bash
py "Mozart Music Generator.py"
```

Choose from three modes:
1. **Demo mode** - Runs two example compositions automatically
2. **Interactive mode** - Full control over composition
3. **Quick random** - Generate one random piece instantly

### Interactive Mode Examples

#### Generate Random Piece
```
Choose mode: 2 (Interactive)
Choose option: 1 (Random composition)
Save as MIDI? y
```

#### Manual Composition (Dice Game Style)
```
Choose mode: 2 (Interactive)
Choose option: 3 (Manually choose variants)
Enter 1-11 for each of the 14 bars
```

#### Reproducible Generation
```
Choose mode: 2 (Interactive)
Choose option: 4 (Generate with seed)
Enter seed: 12345
```

## File Structure

```
Mozart Music Generator.py    # Main program
kirnberger_example1.mid     # Demo output 1
kirnberger_example2.mid     # Demo output 2
composition.json            # Optional JSON export
```

## Statistics

- **Total bars:** 14 (6 + 8)
- **Variants per bar:** 11
- **Total possible compositions:** 379,749,833,583,241
- That's **379 trillion** unique pieces!
- Would take 12 million years to hear them all (at 1 per second)

## Musical Structure

### Period 1 (6 bars)
```
Bar 1: I (C major)
Bar 2: V (G major)
Bar 3: vi (A minor)
Bar 4: IV (F major)
Bar 5: V (G major)
Bar 6: I (C major) - Cadence
```

### Period 2 (8 bars)
```
Bar 7:  I (C major)
Bar 8:  V (G major)
Bar 9:  vi (A minor)
Bar 10: iii (E minor)
Bar 11: IV (F major)
Bar 12: I6/4 (C major second inversion)
Bar 13: V (G major)
Bar 14: I (C major) - Final cadence
```

## Requirements

```bash
py -m pip install music21
```

## Example Output

```
Bar  1 | I      | Variant  5 | G4 E5 C5
Bar  2 | V      | Variant  3 | B4 D5 B4
Bar  3 | vi     | Variant  7 | A5 E5 C5
...
```

## Advanced Usage

### Programmatic Use
```python
from Mozart_Music_Generator import KirnbergerGame

game = KirnbergerGame()

# Generate random composition
composition = game.generate_piece()

# Generate with specific seed
composition = game.generate_piece(seed=42)

# Generate with manual choices
choices = [1, 5, 3, 7, 2, 9, 4, 8, 6, 10, 1, 3, 5, 7]
composition = game.generate_with_choices(choices)

# Export to MIDI
game.create_midi(composition, "my_piece.mid")

# Export to MusicXML
game.create_score(composition, "my_piece.xml")

# Save to JSON
game.save_composition(composition, "my_piece.json")
```

## Historical Context

Kirnberger's Musical Dice Game (Musikalisches Würfelspiel) represents an early form of algorithmic composition, where music is created through a systematic selection process. This implementation captures that spirit while providing modern MIDI output capabilities.

## License

Educational use for UChicago Civ III course.
