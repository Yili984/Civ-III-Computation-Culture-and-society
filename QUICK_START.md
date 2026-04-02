# 🎮 Quick Start Guide - Kirnberger's Musical Dice Game

## Launch the Interactive Game

### Windows:
```bash
# Double-click this file:
PLAY_GAME.bat

# OR run in terminal:
py kirnberger_game_gui.py
```

## What You'll See

### Main Window Features:

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃   🎲 Kirnberger's Musical Dice Game 🎵      ┃
┃                                              ┃
┃  Roll the dice to compose your unique        ┃
┃  Mozart-style piece!                         ┃
┃                                              ┃
┃  Progress: Bar 1 of 14 (Period 1)           ┃
┃  [███░░░░░░░░░░░░░░░░░] 1/14               ┃
┃                                              ┃
┃  ┌──────────────────────────────────────┐  ┃
┃  │ Bar 1 - Harmony: I (C major)         │  ┃
┃  │                                       │  ┃
┃  │            🎲                         │  ┃
┃  │    (Animated dice rolling here!)     │  ┃
┃  │                                       │  ┃
┃  │   Click 'Roll Dice' to start!        │  ┃
┃  │                                       │  ┃
┃  │      [ 🎲 ROLL DICE ]                │  ┃
┃  └──────────────────────────────────────┘  ┃
┃                                              ┃
┃  Your Choices:                               ┃
┃  ┌──────────────────────────────────────┐  ┃
┃  │ (Your rolls appear here)             │  ┃
┃  └──────────────────────────────────────┘  ┃
┃                                              ┃
┃  [📊 Visualize] [▶️ Play] [💾 Save] [🔄]  ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

## Step-by-Step

### 1️⃣ Roll the Dice
- Click the **"🎲 ROLL DICE"** button
- Watch the animated dice roll
- See your result (1-11)

### 2️⃣ Watch Progress
- Your choice is recorded
- Progress bar fills up
- Move to next bar automatically

### 3️⃣ Complete 14 Bars
- Roll for each bar
- **Bars 1-6**: Period 1
- **Bars 7-14**: Period 2

### 4️⃣ View & Play!
After completing all 14 bars:
- **📊 Visualize Music** - See your score
- **▶️ Play Music** - Hear it play
- **💾 Save MIDI** - Export the file
- **🔄 New Composition** - Start again

## What Each Button Does

### 🎲 ROLL DICE (Main Button)
- **What:** Generates random number 1-11
- **When:** Available for each of 14 bars
- **Result:** Selects melodic variant for that bar

### 📊 Visualize Music
- **What:** Opens window with score details
- **Shows:** All 14 bars with notes
- **When:** Available after completing composition

### ▶️ Play Music
- **What:** Plays your composition
- **How:** Opens MIDI file in default player
- **Sound:** Full melody + chord accompaniment

### 💾 Save MIDI
- **What:** Export to custom filename
- **Format:** Standard MIDI (.mid)
- **Size:** ~960 bytes (with chords)

### 🔄 New Composition
- **What:** Reset and start over
- **Asks:** Confirmation first
- **Effect:** Clears all rolls, starts at bar 1

## Color Code

- 🔵 **Blue** - Roll button (main action)
- 🟣 **Purple** - Visualize (view score)
- 🟢 **Green** - Play (hear music)
- 🟠 **Orange** - Save (export file)
- 🔴 **Red** - Reset (new game)

## Example Session

```
Session Example:

1. Launch GUI
2. Click "Roll Dice" → Gets 5
   Bar 1 complete: Variant 5 selected
3. Click "Roll Dice" → Gets 3
   Bar 2 complete: Variant 3 selected
4. Continue for bars 3-14...
   [Progress bar fills up]
5. Bar 14 complete → Success message!
6. Click "Visualize" → See full score
7. Click "Play" → Hear your music!
8. Click "Save" → Export as "my_mozart.mid"
9. Click "New" → Start another piece
```

## Features Highlight

### ✨ Visual Elements
- ✅ Animated dice rolling
- ✅ Real-time progress tracking
- ✅ Color-coded buttons
- ✅ Scrollable choices log
- ✅ Period indicators (1 or 2)
- ✅ Harmony labels (I, V, vi, etc.)

### 🎵 Musical Features
- ✅ 14-bar composition
- ✅ Mozart-style melodies
- ✅ Chord accompaniment
- ✅ Proper voice leading
- ✅ Classical harmony
- ✅ MIDI playback

### 🎮 Interactive Elements
- ✅ One-click dice rolling
- ✅ Instant audio playback
- ✅ Score visualization
- ✅ File export
- ✅ Quick reset
- ✅ User-friendly interface

## File Locations

After playing the game:
```
Your project folder:
├── kirnberger_game_gui.py          # The game (double-click)
├── PLAY_GAME.bat                    # Quick launcher
├── dice_game_composition.mid        # Your latest piece
└── [your saved files].mid           # Any saved exports
```

## Tips

### 🎯 First Time Playing
1. Read the on-screen instructions
2. Roll through all 14 bars
3. Click "Play" to hear result
4. Try "Visualize" to see details
5. Click "New" and try again!

### 🎨 Creating Great Pieces
- **No wrong answers!** All combinations work
- **Experiment freely** - 379 trillion options
- **Try multiple times** - Each is unique
- **Save favorites** - Name them descriptively

### 🎼 Understanding the Music
- **Period 1 (bars 1-6)**: Opening phrase
- **Period 2 (bars 7-14)**: Answering phrase
- **Bar 6**: First cadence (resolution)
- **Bar 14**: Final cadence (grand ending)

## Troubleshooting

### GUI doesn't open?
```bash
# Check Python is installed
py --version

# Try running directly
py kirnberger_game_gui.py
```

### No sound when playing?
- Check speakers are on
- Open .mid file manually
- Install VLC or Windows Media Player

### Can't save file?
- Choose a folder you have access to
- Try Desktop or Documents folder
- Check disk space

## System Requirements

- **OS:** Windows 10/11 (tested)
- **Python:** 3.7+ (3.13+ recommended)
- **Libraries:** 
  - tkinter (built-in)
  - music21 (installed)
- **Sound:** Any MIDI-capable player

## What Makes This Special?

### Historical Significance
- Based on 18th-century composition game
- Early form of algorithmic music
- Used by Mozart and contemporaries

### Mathematical Beauty
- 379 trillion combinations
- Each piece statistically unique
- You'll never hear the same twice

### Educational Value
- Learn music theory
- Understand algorithmic composition
- Experience combinatorial creativity
- See classical harmony in action

## Next Steps

1. **Play the game** multiple times
2. **Save your favorites** with descriptive names
3. **Share with friends** - let them try
4. **Import to DAW** for further editing
5. **Study the code** to learn how it works

## Have Fun! 🎉

Every time you roll the dice, you're creating a piece of music that has likely **never existed before** and will **never exist again** unless you save it!

You're composing like Mozart, one dice roll at a time! 🎲🎵

---

**Quick Reference:**
- Launch: `py kirnberger_game_gui.py` or `PLAY_GAME.bat`
- Guide: See `GUI_GUIDE.md` for detailed info
- Help: See `README_KIRNBERGER.md` for music details
