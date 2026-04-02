# 🎲 Kirnberger's Musical Dice Game - Interactive GUI Guide

## Quick Start

### Launch the Game:
```bash
# Method 1: Double-click
PLAY_GAME.bat

# Method 2: Command line
py kirnberger_game_gui.py
```

## How to Play

### Step-by-Step Instructions:

#### 1. **Start Rolling** 🎲
- The game starts at **Bar 1 of 14**
- You'll see the current harmony (e.g., "I - C major")
- Click the **"ROLL DICE"** button

#### 2. **Watch the Animation** ✨
- The dice will animate with a fun rolling effect
- After ~0.5 seconds, you'll see your result (1-11)
- The variant is automatically selected

#### 3. **Review Your Choice** 📝
- Your roll is recorded in the "Your Choices" section
- You'll see:
  - Bar number
  - Period (1 or 2)
  - Harmony
  - Roll number
  - Selected melody notes

#### 4. **Continue Rolling** 🔄
- Repeat for all **14 bars**
- **Period 1:** Bars 1-6
- **Period 2:** Bars 7-14
- Progress bar shows your advancement

#### 5. **Composition Complete!** 🎉
- After bar 14, you'll see a success message
- Three action buttons become available:
  - 📊 **Visualize Music**
  - ▶️ **Play Music**
  - 💾 **Save MIDI**

## Features

### 🎯 Visual Elements

#### Progress Tracker
- Shows current bar (1-14)
- Indicates which period you're in
- Progress bar fills as you compose

#### Dice Display
- Large animated dice emoji
- Shows your roll result
- Satisfying visual feedback

#### Choices Log
- Scrollable text area
- Shows all your decisions
- Format: `Bar | Period | Harmony | Roll | Melody Notes`

### 🎵 Action Buttons

#### 📊 Visualize Music
- Opens a new window
- Shows your complete composition
- Displays all 14 bars with details
- Lists your dice rolls
- Shows melody notes for each bar

#### ▶️ Play Music
- Plays your composition immediately
- Uses your system's default MIDI player
- Full stereo with melody + chords
- Automatically generated MIDI file

#### 💾 Save MIDI
- Save your composition with custom name
- Choose location on your computer
- Default name: "my_kirnberger_composition.mid"
- Includes both melody and accompaniment

#### 🔄 New Composition
- Start fresh composition
- Resets all bars
- Asks for confirmation
- Quick way to create multiple pieces

## Game Window Layout

```
┌─────────────────────────────────────────────────────────┐
│     🎲 Kirnberger's Musical Dice Game 🎵                │
│                                                          │
│  Roll the dice to compose your unique Mozart-style...   │
│                                                          │
│  Progress: Bar 1 of 14 (Period 1)                       │
│  [████████░░░░░░░░░░░░░░░░░░░░] 1/14                   │
│                                                          │
│ ┌─────────────────────────────────────────────────────┐ │
│ │  Bar 1 - Harmony: I (C major)                       │ │
│ │                                                      │ │
│ │                    🎲                                │ │
│ │                                                      │ │
│ │          Click 'Roll Dice' to start!                │ │
│ │                                                      │ │
│ │            [🎲 ROLL DICE]                           │ │
│ └─────────────────────────────────────────────────────┘ │
│                                                          │
│  Your Choices:                                           │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ Bar  1 (Period 1) | I      | Roll:  5 | G4-C5-E5   │ │
│ │ Bar  2 (Period 1) | V      | Roll:  3 | B4-C5-D5   │ │
│ │ ...                                                  │ │
│ └─────────────────────────────────────────────────────┘ │
│                                                          │
│  [📊 Visualize] [▶️ Play] [💾 Save] [🔄 New]          │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

## Musical Structure

### Period 1 (Bars 1-6)
- **Bar 1:** I (C major) - Opening
- **Bar 2:** V (G major) - Tension
- **Bar 3:** vi (A minor) - Color
- **Bar 4:** IV (F major) - Subdominant
- **Bar 5:** V (G major) - Dominant
- **Bar 6:** I (C major) - **First Cadence**

### Period 2 (Bars 7-14)
- **Bar 7:** I (C major) - Fresh start
- **Bar 8:** V (G major) - Building
- **Bar 9:** vi (A minor) - Development
- **Bar 10:** iii (E minor) - Mediant
- **Bar 11:** IV (F major) - Preparation
- **Bar 12:** I6/4 (C major 2nd inv.) - Cadential
- **Bar 13:** V (G major) - **Final Dominant**
- **Bar 14:** I (C major) - **GRAND FINALE**

## Tips for Best Results

### 🎯 Creating Beautiful Pieces

1. **Listen to Examples First**
   - Play the demo MIDIs before rolling
   - Understand what different variants sound like

2. **No Wrong Choices!**
   - Every combination is valid
   - The system ensures musical consistency
   - All variants follow voice leading rules

3. **Experiment Freely**
   - Try multiple compositions
   - Compare different results
   - Notice patterns in your favorites

4. **Pay Attention to Cadences**
   - Bars 6 and 14 are special
   - These are where phrases resolve
   - Different variants give different moods

### 🎨 Creative Ideas

- **Contrast:** Use high variants followed by low
- **Repetition:** Repeat the same roll for multiple bars
- **Climax:** Build to higher numbers toward bar 13
- **Symmetry:** Mirror choices between periods

## Technical Details

### What Happens When You Roll?

1. **Random Number Generation**
   - Python's `random.randint(1, 11)`
   - Each number 1-11 equally likely
   - True randomness (not predetermined)

2. **Variant Selection**
   - Roll number maps to melodic variant
   - Each variant: 3 eighth notes
   - Pre-composed for good voice leading

3. **Composition Building**
   - Stores your 14 choices
   - Generates complete piece
   - Creates MIDI with accompaniment

4. **MIDI Generation**
   - Right hand: Melody (your rolled variants)
   - Left hand: Chord accompaniment
   - Tempo: 120 BPM
   - Time: 3/8
   - Key: C Major

### File Output

When you play/save, the system creates:
- **dice_game_composition.mid** - Your current piece
- Includes melody + chords
- Standard MIDI Format
- ~960 bytes

## Statistics

### The Mathematics
- **14 bars** total
- **11 variants** per bar
- **11^14 = 379,749,833,583,241** combinations
- That's **379+ TRILLION** unique pieces!

### Time Calculations
If you composed one per second:
- **12 million years** to hear them all
- **870,000x** the age of recorded history
- Truly infinite for practical purposes

## Troubleshooting

### GUI Won't Start
```bash
# Check Python installation
py --version

# Check tkinter (should be included)
py -c "import tkinter; print('OK')"
```

### Music Won't Play
- Install a MIDI player (Windows Media Player, VLC)
- Check that speakers are on
- Look for the .mid file and open manually

### Can't Save File
- Check you have write permissions
- Choose a folder you own
- Try Desktop or Documents

### Want to See Notation?
- Install **MuseScore** (free)
- Open the saved .mid file
- View full musical notation
- Print, edit, transpose, etc.

## Advanced Usage

### Quick Multiple Compositions
1. Roll through all 14 bars
2. Click "Play" to hear it
3. Click "New Composition"
4. Repeat!

### Compare Versions
1. Create first piece → Save as "version1.mid"
2. Reset → Create second → Save as "version2.mid"
3. Play both and compare

### Educational Use
- Demonstrate algorithmic composition
- Show combinatorial explosion
- Teach musical form (period structure)
- Explore harmony progressions
- Study Mozart-era style

## Keyboard Shortcuts

Currently available:
- **Ctrl+W** - Close window (standard)
- **Alt+F4** - Close application (Windows)

Future additions could include:
- **Space** - Roll dice
- **Enter** - Confirm/Continue
- **R** - Reset/New composition

## Credits

**Based on:** Kirnberger's Musikalisches Würfelspiel (18th century)

**Implementation:** Python + tkinter + music21

**Created for:** UChicago Civ III Course

**Features:**
- Interactive dice rolling
- Real-time composition
- MIDI playback
- Music visualization

## Have Fun! 🎵

Remember: **Every composition you create is unique!**

With 379 trillion possibilities, you could play this game every day for millions of years and never hear the same piece twice.

Happy composing! 🎲🎵

---

**Need help?** Check the main README files:
- `README_KIRNBERGER.md` - General information
- `ENHANCEMENTS.md` - Technical details
- This file - GUI-specific guide
