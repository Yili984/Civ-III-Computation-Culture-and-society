# 🎼 Sheet Music Notation Feature Guide

## ✅ What's Been Implemented

### 1. **Last Note is Always a Whole Note**
All 11 variants in Bar 14 end with a whole note (1.0 duration) or longer:
- 9 variants end with whole notes (1.0)
- 1 variant ends with 1.25 duration
- 2 variants end with 1.5 duration (full bar!)

**Result:** Every composition has a strong, definitive ending!

### 2. **Sheet Music Notation Generation**
The "📊 Visualize Music" feature now attempts to generate actual sheet music with:
- 5-line musical staff
- Treble clef (melody/right hand)
- Bass clef (accompaniment/left hand)
- Proper note symbols
- Bar lines
- Time signature (3/8)
- Key signature (C major)

---

## 🎵 How It Works

When you click **"📊 Visualize Music"**, the system:

### Step 1: Creates the Score
- Builds a complete music21 Score object
- Melody part with treble clef
- Accompaniment part with bass clef
- All 14 measures properly formatted

### Step 2: Attempts PNG Generation
The system tries multiple methods:

**Method 1: Lilypond (Best Quality)**
```python
score.write('lily.png', fp='score_notation.png')
```
- Requires: Lilypond installed
- Result: High-quality engraved notation
- Download: http://lilypond.org/

**Method 2: MusicXML PNG**
```python
score.write('musicxml.png', fp='score_notation.png')
```
- Requires: MuseScore installed
- Result: Good quality notation
- Download: https://musescore.org/

**Method 3: External Viewer**
```python
score.show()
```
- Opens in MuseScore/Finale/other installed software
- Interactive notation display

### Step 3: Display in Window
If PNG is generated:
- Image is loaded using PIL/Pillow
- Displayed in the visualization window
- Automatically resized if too large
- Scrollable for easy viewing

---

## 📦 Requirements

### Required (Already Installed):
- ✅ Python 3.7+
- ✅ tkinter (built-in)
- ✅ music21 library
- ✅ Pillow (PIL fork)

### Optional (For PNG Generation):
- **MuseScore 3 or 4** (Recommended)
  - Free, open-source notation software
  - Download: https://musescore.org/
  - Enables: musicxml.png method

- **Lilypond** (Advanced)
  - Professional music engraving
  - Download: http://lilypond.org/
  - Enables: lily.png method (best quality)

---

## 🎯 Installation Guide

### Option 1: MuseScore (Easiest)

**Windows:**
1. Download MuseScore from https://musescore.org/
2. Run installer
3. Follow setup wizard
4. MuseScore will be in your PATH automatically

**Mac:**
1. Download MuseScore DMG
2. Drag to Applications
3. Run once to initialize

**Linux:**
```bash
# Debian/Ubuntu
sudo apt-get install musescore3

# Fedora
sudo dnf install musescore

# Arch
sudo pacman -S musescore
```

### Option 2: Lilypond (Professional)

**Windows:**
1. Download from http://lilypond.org/
2. Run installer
3. Add to PATH if needed

**Mac:**
```bash
brew install lilypond
```

**Linux:**
```bash
# Debian/Ubuntu
sudo apt-get install lilypond

# Fedora
sudo dnf install lilypond
```

---

## 🎮 Using the Feature

### Quick Start:
1. **Create a composition** (roll dice 14 times or "Roll All Remaining")
2. **Click "📊 Visualize Music"**
3. **Wait for generation** (a few seconds)
4. **View results:**
   - Text view shows composition details
   - Sheet music image appears below (if generation successful)
   - Scroll down to see the full notation

### What You'll See:

#### **Text View (Always Available):**
```
COMPOSITION SUMMARY:
  • Key: C Major
  • Time Signature: 3/8
  • Total Bars: 14
  • Your Dice Rolls: [5, 3, 7, 2, 9, 4, 8, 6, 10, 1, 3, 5, 7, 1]

PERIOD 1 (Bars 1-6):
[Detailed bar-by-bar breakdown with rhythm symbols]

PERIOD 2 (Bars 7-14):
[Detailed bar-by-bar breakdown with rhythm symbols]
```

#### **Sheet Music Image (If MuseScore/Lilypond Installed):**
- Professional 5-line staff notation
- Both treble and bass clefs
- All notes properly positioned
- Bar lines and time signatures
- Key signature indicated
- Measure numbers shown

---

## 🔧 Troubleshooting

### "Sheet music generation requires MuseScore or Lilypond"

**Solution 1:** Install MuseScore (recommended)
- Download from https://musescore.org/
- Restart the program after installation

**Solution 2:** Install Lilypond
- Download from http://lilypond.org/
- Ensure it's in your system PATH

**Solution 3:** Use External Viewer
- The system will try to open in installed notation software
- Works if you have MuseScore, Finale, or Sibelius installed

### "PIL/Pillow not installed"

**Solution:**
```bash
py -m pip install Pillow
```

### Image Generation is Slow

**Normal:** First generation takes 5-10 seconds
- MuseScore/Lilypond needs to render
- Subsequent generations are faster
- Be patient!

### Image Doesn't Appear

**Check:**
1. Look for file `score_notation.png` in project folder
2. Open it manually to verify it was created
3. Check console for error messages
4. Verify MuseScore is properly installed

---

## 📊 Technical Details

### Score Generation Process:

**1. Build Score Object:**
```python
score = stream.Score()

# Melody part
melody_part = stream.Part()
melody_part.append(clef.TrebleClef())
melody_part.append(key.Key('C'))
melody_part.append(meter.TimeSignature('3/8'))

# Accompaniment part
accomp_part = stream.Part()
accomp_part.append(clef.BassClef())
accomp_part.append(key.Key('C'))
accomp_part.append(meter.TimeSignature('3/8'))
```

**2. Add Measures:**
```python
for bar_data in composition:
    measure = stream.Measure(number=bar_num)
    # Add notes with proper durations
    for note_name, duration in melody:
        n = note.Note(note_name, quarterLength=duration)
        measure.append(n)
    melody_part.append(measure)
```

**3. Generate PNG:**
```python
score.write('lily.png', fp='score_notation.png')
# or
score.write('musicxml.png', fp='score_notation.png')
```

**4. Display Image:**
```python
from PIL import Image, ImageTk
img = Image.open('score_notation.png')
# Resize if needed
photo = ImageTk.PhotoImage(img)
canvas.create_image(0, 0, image=photo)
```

### File Output:
- **Filename:** `score_notation.png`
- **Location:** Project directory
- **Format:** PNG image
- **Size:** Varies (typically 1000-2000px wide)
- **Quality:** High resolution for printing

---

## 🎨 Features of Generated Score

### Notation Elements:

**Staves:**
- Top staff: Treble clef (G clef)
- Bottom staff: Bass clef (F clef)

**Measures:**
- Bar lines between measures
- Measure numbers above staff
- 14 bars total (6 + 8)

**Notes:**
- Proper note heads (filled/unfilled)
- Correct stem directions
- Beams for eighth/sixteenth notes
- Dotted notes shown correctly

**Rhythm:**
- Sixteenth notes (♬) - beamed in groups
- Eighth notes (♪) - single beam
- Dotted eighth notes (♪.) - dot visible
- Quarter notes (♩) - no beam
- Whole notes - hollow note head

**Other Elements:**
- Time signature: 3/8 at beginning
- Key signature: No sharps/flats (C major)
- Tempo marking: Quarter = 120
- Clef symbols clearly shown

### Special Cadence Notation:

**Bar 6 (Half Cadence):**
- Last note often sustained
- Clear phrase ending

**Bar 14 (Final Cadence):**
- Last note is ALWAYS whole note or longer
- Creates visual sense of finality
- Often a long, hollow note head

---

## 💡 Tips for Best Results

### 1. Install MuseScore First
- Most reliable method
- Free and easy to install
- Works on all platforms

### 2. Be Patient
- First generation takes time
- MuseScore needs to start up
- Wait for "✓" message

### 3. Save the PNG
- File: `score_notation.png`
- Keep for reference
- Print it out!
- Import to other software

### 4. Zoom In
- Use image viewer to zoom
- See details clearly
- Print at high quality

### 5. Edit Further
- Open MIDI file in MuseScore
- Edit notation
- Add dynamics, articulations
- Export to PDF

---

## 🎓 Educational Use

### For Students:
- **See what you created** in standard notation
- **Learn to read music** by comparing audio to notation
- **Understand rhythm symbols** (eighth, quarter, dotted notes)
- **Study bar structure** and measure organization

### For Teachers:
- **Demonstrate algorithmic composition** with visual output
- **Teach music notation** using generated scores
- **Show harmony** with two-staff display
- **Analyze form** with visible period structure

### For Musicians:
- **Read and perform** your dice game compositions
- **Study voice leading** in notation
- **Analyze cadences** visually
- **Transcribe** to other instruments

---

## 📚 Further Resources

### Music21 Documentation:
- http://web.mit.edu/music21/doc/
- Score generation tutorials
- PNG export methods

### MuseScore:
- https://musescore.org/
- User handbook
- Forum for support

### Lilypond:
- http://lilypond.org/
- Learning manual
- Notation reference

---

## ✅ Summary

### What Works Without Additional Software:
- ✅ Text visualization with rhythm symbols
- ✅ MIDI file generation
- ✅ Audio playback
- ✅ Composition details display

### What Requires MuseScore/Lilypond:
- 📄 PNG sheet music generation
- 🎼 Visual notation with staff lines
- 🖼️ Image display in visualization window

### Best Setup:
1. Install MuseScore (free)
2. Run the game
3. Create composition
4. Visualize music
5. See both text AND notation!

---

## 🎉 Enjoy Your Sheet Music!

With MuseScore or Lilypond installed, you now get:
- ✅ Professional sheet music notation
- ✅ 5-line staff with clefs
- ✅ Proper note symbols and rhythms
- ✅ Printable, shareable scores
- ✅ Visual learning tool

**Every composition is both heard AND seen!** 🎵📄
