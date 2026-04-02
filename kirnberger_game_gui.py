"""
Interactive Kirnberger's Musical Dice Game - GUI Version

Features:
- Roll dice for each bar
- Visual feedback and progress
- Music sheet visualization
- Playback button
"""

import tkinter as tk
from tkinter import ttk, messagebox
import random
import os
import importlib.util

# Import the Kirnberger game
spec = importlib.util.spec_from_file_location(
    "mozart_generator",
    os.path.join(os.path.dirname(__file__), "Mozart Music Generator.py")
)
mozart_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mozart_module)

KirnbergerGame = mozart_module.KirnbergerGame
MUSIC21_AVAILABLE = mozart_module.MUSIC21_AVAILABLE

if MUSIC21_AVAILABLE:
    from music21 import midi as m21midi


class DiceGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Kirnberger's Musical Dice Game")
        self.root.geometry("900x750")
        self.root.configure(bg='#f0f0f0')

        # Maximize window for best display
        try:
            self.root.state('zoomed')  # Windows
        except:
            try:
                self.root.attributes('-zoomed', True)  # Linux
            except:
                pass  # MacOS uses different approach

        # Game state
        self.game = KirnbergerGame()
        self.current_bar = 1
        self.choices = []
        self.composition = None
        self.midi_filename = "dice_game_composition.mid"

        # Create UI
        self.create_widgets()

    def create_widgets(self):
        # Title
        title = tk.Label(
            self.root,
            text="🎲 Kirnberger's Musical Dice Game 🎵",
            font=("Arial", 24, "bold"),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        title.pack(pady=15)

        # Description frame with background
        desc_frame = tk.Frame(self.root, bg='#ecf0f1', relief=tk.GROOVE, borderwidth=2)
        desc_frame.pack(pady=10, padx=40, fill=tk.X)

        # About the game
        about_text = (
            "About: Kirnberger's Musikalisches Würfelspiel (Musical Dice Game) is an 18th-century\n"
            "algorithmic composition method. Roll dice to select melodic variants for each measure,\n"
            "creating one of 379 trillion unique Mozart-style minuets in C major (3/8 time).\n"
            "Each piece follows classical harmony: Period 1 (bars 1-6) and Period 2 (bars 7-14)."
        )
        about_label = tk.Label(
            desc_frame,
            text=about_text,
            font=("Arial", 9),
            bg='#ecf0f1',
            fg='#2c3e50',
            justify=tk.LEFT,
            wraplength=800
        )
        about_label.pack(pady=8, padx=10)

        # Instructions
        instructions = tk.Label(
            self.root,
            text="Roll the dice to compose your unique piece!\nRoll for each of the 14 bars, then visualize and play your composition.",
            font=("Arial", 11, "bold"),
            bg='#f0f0f0',
            fg='#16a085',
            justify=tk.CENTER
        )
        instructions.pack(pady=10)

        # Progress frame
        progress_frame = tk.Frame(self.root, bg='#f0f0f0')
        progress_frame.pack(pady=15)

        tk.Label(
            progress_frame,
            text="Progress:",
            font=("Arial", 12, "bold"),
            bg='#f0f0f0'
        ).pack(side=tk.LEFT, padx=5)

        self.progress_label = tk.Label(
            progress_frame,
            text="Bar 1 of 14 (Period 1)",
            font=("Arial", 12),
            bg='#f0f0f0',
            fg='#e74c3c'
        )
        self.progress_label.pack(side=tk.LEFT)

        # Progress bar
        self.progress_bar = ttk.Progressbar(
            self.root,
            length=500,
            mode='determinate',
            maximum=14
        )
        self.progress_bar.pack(pady=5)

        # Dice display frame
        dice_frame = tk.Frame(self.root, bg='#ecf0f1', relief=tk.RAISED, borderwidth=3)
        dice_frame.pack(pady=20, padx=30, fill=tk.BOTH, expand=False)

        # Current bar info
        self.bar_info_label = tk.Label(
            dice_frame,
            text="Bar 1 - Harmony: I (C major)",
            font=("Arial", 14, "bold"),
            bg='#ecf0f1',
            fg='#16a085'
        )
        self.bar_info_label.pack(pady=10)

        # Dice result display
        self.dice_display = tk.Label(
            dice_frame,
            text="🎲",
            font=("Arial", 80),
            bg='#ecf0f1'
        )
        self.dice_display.pack(pady=10)

        self.result_label = tk.Label(
            dice_frame,
            text="Click 'Roll Dice' to start!",
            font=("Arial", 12),
            bg='#ecf0f1',
            fg='#7f8c8d'
        )
        self.result_label.pack(pady=5)

        # Roll buttons frame
        roll_buttons_frame = tk.Frame(dice_frame, bg='#ecf0f1')
        roll_buttons_frame.pack(pady=15)

        self.roll_button = tk.Button(
            roll_buttons_frame,
            text="🎲 ROLL DICE",
            font=("Arial", 16, "bold"),
            bg='#3498db',
            fg='white',
            activebackground='#2980b9',
            activeforeground='white',
            command=self.roll_dice,
            padx=30,
            pady=15,
            relief=tk.RAISED,
            borderwidth=3,
            cursor='hand2'
        )
        self.roll_button.pack(side=tk.LEFT, padx=5)

        self.roll_all_button = tk.Button(
            roll_buttons_frame,
            text="⚡ ROLL ALL REMAINING",
            font=("Arial", 14, "bold"),
            bg='#e67e22',
            fg='white',
            activebackground='#d35400',
            activeforeground='white',
            command=self.roll_all_remaining,
            padx=20,
            pady=15,
            relief=tk.RAISED,
            borderwidth=3,
            cursor='hand2'
        )
        self.roll_all_button.pack(side=tk.LEFT, padx=5)

        # Choices display
        choices_frame = tk.Frame(self.root, bg='#f0f0f0')
        choices_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        tk.Label(
            choices_frame,
            text="Your Choices:",
            font=("Arial", 12, "bold"),
            bg='#f0f0f0'
        ).pack()

        # Scrollable text widget for choices
        self.choices_text = tk.Text(
            choices_frame,
            height=8,
            width=80,
            font=("Courier", 10),
            bg='#ffffff',
            relief=tk.SUNKEN,
            borderwidth=2
        )
        self.choices_text.pack(pady=5, padx=20)
        self.choices_text.config(state=tk.DISABLED)

        # Action buttons frame
        button_frame = tk.Frame(self.root, bg='#f0f0f0')
        button_frame.pack(pady=10)

        self.visualize_button = tk.Button(
            button_frame,
            text="📊 Visualize Music",
            font=("Arial", 12, "bold"),
            bg='#9b59b6',
            fg='white',
            command=self.visualize_music,
            padx=20,
            pady=10,
            state=tk.DISABLED,
            cursor='hand2'
        )
        self.visualize_button.pack(side=tk.LEFT, padx=10)

        self.play_button = tk.Button(
            button_frame,
            text="▶️ Play Music",
            font=("Arial", 12, "bold"),
            bg='#27ae60',
            fg='white',
            command=self.play_music,
            padx=20,
            pady=10,
            state=tk.DISABLED,
            cursor='hand2'
        )
        self.play_button.pack(side=tk.LEFT, padx=10)

        self.save_button = tk.Button(
            button_frame,
            text="💾 Save MIDI",
            font=("Arial", 12, "bold"),
            bg='#f39c12',
            fg='white',
            command=self.save_midi,
            padx=20,
            pady=10,
            state=tk.DISABLED,
            cursor='hand2'
        )
        self.save_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(
            button_frame,
            text="🔄 New Composition",
            font=("Arial", 12, "bold"),
            bg='#e74c3c',
            fg='white',
            command=self.reset_game,
            padx=20,
            pady=10,
            cursor='hand2'
        )
        self.reset_button.pack(side=tk.LEFT, padx=10)

        # Display reminder
        reminder_frame = tk.Frame(self.root, bg='#fff3cd', relief=tk.FLAT, borderwidth=1)
        reminder_frame.pack(pady=10, padx=40, fill=tk.X)

        reminder_label = tk.Label(
            reminder_frame,
            text="💡 Tip: Maximize this window or use full screen to ensure all interface features are properly displayed.",
            font=("Arial", 9, "italic"),
            bg='#fff3cd',
            fg='#856404',
            justify=tk.CENTER
        )
        reminder_label.pack(pady=5)

    def roll_dice(self):
        """Animate dice roll and record choice"""
        # Disable button during animation
        self.roll_button.config(state=tk.DISABLED)

        # Animate dice roll
        self.animate_dice_roll()

    def animate_dice_roll(self, count=0):
        """Animate the dice rolling"""
        if count < 10:  # 10 frames of animation
            # Show random dice faces
            dice_faces = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']
            self.dice_display.config(text=random.choice(dice_faces))
            self.root.after(50, lambda: self.animate_dice_roll(count + 1))
        else:
            # Final roll
            roll = random.randint(1, 11)
            self.record_choice(roll)

    def record_choice(self, roll):
        """Record the dice roll and update display"""
        self.choices.append(roll)

        # Get bar info
        bar_info = self.game.composition_data[self.current_bar]
        harmony = bar_info['harmony']
        melody = bar_info['variants'][roll - 1]

        # Update dice display with result
        dice_emoji = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅', '⚀', '⚁', '⚂', '⚃', '⚄']
        self.dice_display.config(text=dice_emoji[roll - 1])
        self.result_label.config(
            text=f"Rolled: {roll} | Variant {roll} selected",
            fg='#27ae60',
            font=("Arial", 12, "bold")
        )

        # Add to choices display
        self.choices_text.config(state=tk.NORMAL)
        # Format melody string from tuples
        melody_notes = []
        for note_data in melody:
            if isinstance(note_data, tuple):
                note_name, duration = note_data
                melody_notes.append(note_name)
            else:
                melody_notes.append(note_data)
        melody_str = ' - '.join(melody_notes)
        period = "Period 1" if self.current_bar <= 6 else "Period 2"
        self.choices_text.insert(
            tk.END,
            f"Bar {self.current_bar:2d} ({period}) | {harmony:6s} | Roll: {roll:2d} | {melody_str}\n"
        )
        self.choices_text.see(tk.END)
        self.choices_text.config(state=tk.DISABLED)

        # Update progress
        self.progress_bar['value'] = self.current_bar

        # Move to next bar or finish
        if self.current_bar < 14:
            self.current_bar += 1
            next_harmony = self.game.composition_data[self.current_bar]['harmony']
            period = "Period 1" if self.current_bar <= 6 else "Period 2"
            self.progress_label.config(text=f"Bar {self.current_bar} of 14 ({period})")
            self.bar_info_label.config(text=f"Bar {self.current_bar} - Harmony: {next_harmony}")
            self.result_label.config(
                text="Click 'Roll Dice' for next bar",
                fg='#7f8c8d',
                font=("Arial", 12)
            )
            self.roll_button.config(state=tk.NORMAL)
        else:
            # Composition complete!
            self.finish_composition()

    def roll_all_remaining(self):
        """Automatically roll dice for all remaining bars"""
        if self.current_bar > 14:
            messagebox.showinfo("Complete", "Composition already complete!")
            return

        # Confirm action
        remaining = 14 - self.current_bar + 1
        result = messagebox.askyesno(
            "Roll All Remaining",
            f"Automatically roll dice for the remaining {remaining} bars?\n\n"
            f"This will complete your composition instantly."
        )

        if result:
            # Disable buttons during auto-roll
            self.roll_button.config(state=tk.DISABLED)
            self.roll_all_button.config(state=tk.DISABLED)

            # Roll for all remaining bars
            while self.current_bar <= 14:
                roll = random.randint(1, 11)
                self.record_choice(roll)

            # Enable buttons might already be handled by finish_composition
            # but the roll_all_button should stay disabled

    def finish_composition(self):
        """Called when all 14 bars are complete"""
        self.progress_label.config(text="✨ Composition Complete! ✨", fg='#27ae60')
        self.result_label.config(
            text="🎉 All 14 bars composed!",
            fg='#27ae60',
            font=("Arial", 14, "bold")
        )
        self.roll_button.config(state=tk.DISABLED)
        self.roll_all_button.config(state=tk.DISABLED)

        # Generate the composition
        self.composition = self.game.generate_with_choices(self.choices)

        # Generate MIDI file
        self.game.create_midi(self.composition, self.midi_filename)

        # Enable action buttons
        self.visualize_button.config(state=tk.NORMAL)
        self.play_button.config(state=tk.NORMAL)
        self.save_button.config(state=tk.NORMAL)

        messagebox.showinfo(
            "Composition Complete!",
            "Your unique Mozart-style piece is ready!\n\n"
            "• Click 'Visualize Music' to see the score\n"
            "• Click 'Play Music' to hear it\n"
            "• Click 'Save MIDI' to export\n\n"
            f"Total combinations: {11**14:,}"
        )

    def visualize_music(self):
        """Display music notation in a new window"""
        if not self.composition:
            messagebox.showerror("Error", "No composition to visualize!")
            return

        if not MUSIC21_AVAILABLE:
            messagebox.showerror("Error", "music21 library not available!")
            return

        # Create visualization window
        viz_window = tk.Toplevel(self.root)
        viz_window.title("Music Score Visualization - Kirnberger Dice Game")
        viz_window.geometry("1000x700")
        viz_window.configure(bg='white')

        # Title
        tk.Label(
            viz_window,
            text="🎼 Your Unique Composition 🎼",
            font=("Arial", 20, "bold"),
            bg='white',
            fg='#2c3e50'
        ).pack(pady=10)

        # Create a frame with scrollbar for the score
        frame = tk.Frame(viz_window, bg='white')
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Text widget to show notation
        text = tk.Text(frame, width=100, height=35, font=("Courier", 9), bg='#f9f9f9', wrap=tk.NONE)
        scrollbar = tk.Scrollbar(frame, command=text.yview)
        text.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Display composition details
        text.insert(tk.END, "=" * 90 + "\n")
        text.insert(tk.END, "       KIRNBERGER'S MUSICAL DICE GAME - YOUR UNIQUE COMPOSITION\n")
        text.insert(tk.END, "=" * 90 + "\n\n")

        # Summary information
        text.insert(tk.END, "COMPOSITION SUMMARY:\n")
        text.insert(tk.END, f"  • Key: C Major\n")
        text.insert(tk.END, f"  • Time Signature: 3/8\n")
        text.insert(tk.END, f"  • Total Bars: 14 (Period 1: 6 bars, Period 2: 8 bars)\n")
        text.insert(tk.END, f"  • Your Dice Rolls: {self.choices}\n")
        text.insert(tk.END, f"  • Possible Combinations: {11**14:,}\n\n")

        text.insert(tk.END, "RHYTHM LEGEND: ♬=16th ♪=8th ♪.=dotted-8th ♩=quarter ♩.=dotted-quarter 𝅗𝅥.=dotted-half\n")
        text.insert(tk.END, "=" * 90 + "\n\n")

        text.insert(tk.END, "╔══════════════════════════════════════════════════════════════════════════════╗\n")
        text.insert(tk.END, "║  PERIOD 1 (Bars 1-6) - First Phrase                                         ║\n")
        text.insert(tk.END, "║  Harmonic Progression: I → V → vi → IV → V → I (Half Cadence)               ║\n")
        text.insert(tk.END, "╚══════════════════════════════════════════════════════════════════════════════╝\n\n")

        for i, item in enumerate(self.composition[:6]):
            bar_num = item['bar']
            melody_notes = []
            for note_data in item['melody']:
                if isinstance(note_data, tuple):
                    note_name, duration = note_data
                    # Show rhythm symbols
                    if duration == 0.25:
                        rhythm = '♬'
                    elif duration == 0.5:
                        rhythm = '♪'
                    elif duration == 0.75:
                        rhythm = '♪.'
                    elif duration == 1.0:
                        rhythm = '♩'
                    elif duration == 1.25:
                        rhythm = '♩.'
                    elif duration == 1.5:
                        rhythm = '𝅗𝅥.'
                    else:
                        rhythm = f'({duration})'
                    melody_notes.append(f"{note_name:4s}{rhythm}")
                else:
                    melody_notes.append(f"{note_data:4s}")
            melody_str = '  '.join(melody_notes)

            # Highlight bar 6 (half cadence)
            if bar_num == 6:
                text.insert(tk.END, f">>> Bar {bar_num:2d} | {item['harmony']:6s} | Dice Roll: {self.choices[i]:2d} | Variant {item['variant']:2d} | {melody_str}\n")
                text.insert(tk.END, "         *** HALF CADENCE - End of Period 1 ***\n\n")
            else:
                text.insert(tk.END, f"    Bar {bar_num:2d} | {item['harmony']:6s} | Dice Roll: {self.choices[i]:2d} | Variant {item['variant']:2d} | {melody_str}\n")

        text.insert(tk.END, "\n\n")
        text.insert(tk.END, "╔══════════════════════════════════════════════════════════════════════════════╗\n")
        text.insert(tk.END, "║  PERIOD 2 (Bars 7-14) - Second Phrase                                       ║\n")
        text.insert(tk.END, "║  Harmonic Progression: I → V → vi → iii → IV → I6/4 → V → I (Final Cadence) ║\n")
        text.insert(tk.END, "╚══════════════════════════════════════════════════════════════════════════════╝\n\n")

        for i, item in enumerate(self.composition[6:], 6):
            bar_num = item['bar']
            melody_notes = []
            for note_data in item['melody']:
                if isinstance(note_data, tuple):
                    note_name, duration = note_data
                    if duration == 0.25:
                        rhythm = '♬'
                    elif duration == 0.5:
                        rhythm = '♪'
                    elif duration == 0.75:
                        rhythm = '♪.'
                    elif duration == 1.0:
                        rhythm = '♩'
                    elif duration == 1.25:
                        rhythm = '♩.'
                    elif duration == 1.5:
                        rhythm = '𝅗𝅥.'
                    else:
                        rhythm = f'({duration})'
                    melody_notes.append(f"{note_name:4s}{rhythm}")
                else:
                    melody_notes.append(f"{note_data:4s}")
            melody_str = '  '.join(melody_notes)

            # Highlight cadential approach (bars 12-14)
            if bar_num == 12:
                text.insert(tk.END, f"    Bar {bar_num:2d} | {item['harmony']:6s} | Dice Roll: {self.choices[i]:2d} | Variant {item['variant']:2d} | {melody_str}\n")
                text.insert(tk.END, "         (Cadential 6/4 - preparation for final cadence)\n")
            elif bar_num == 13:
                text.insert(tk.END, f"    Bar {bar_num:2d} | {item['harmony']:6s} | Dice Roll: {self.choices[i]:2d} | Variant {item['variant']:2d} | {melody_str}\n")
                text.insert(tk.END, "         (Dominant 7th - building tension for resolution)\n")
            elif bar_num == 14:
                text.insert(tk.END, f">>> Bar {bar_num:2d} | {item['harmony']:6s} | Dice Roll: {self.choices[i]:2d} | Variant {item['variant']:2d} | {melody_str}\n")
                text.insert(tk.END, "         *** FINAL CADENCE - Grand Resolution! ***\n")
            else:
                text.insert(tk.END, f"    Bar {bar_num:2d} | {item['harmony']:6s} | Dice Roll: {self.choices[i]:2d} | Variant {item['variant']:2d} | {melody_str}\n")

        text.insert(tk.END, "\n" + "=" * 90 + "\n")
        text.insert(tk.END, f"COMPOSITION COMPLETE!\n")
        text.insert(tk.END, f"  • MIDI File Saved: {self.midi_filename}\n")
        text.insert(tk.END, f"  • Features: Enhanced cadences with V7 chords and sustained bass notes\n")
        text.insert(tk.END, f"  • Final Bar: Uses whole notes for ultimate finality\n")
        text.insert(tk.END, "=" * 90 + "\n")

        # Try to generate music21 visualization
        try:
            text.insert(tk.END, "\n\n📊 GENERATING NOTATION SCORE...\n")
            text.insert(tk.END, "-" * 80 + "\n")
            viz_window.update()

            # Create full score using music21 with both parts
            from music21 import stream, note, key, meter, tempo, chord, clef

            score = stream.Score()

            # Melody part (right hand)
            melody_part = stream.Part()
            melody_part.id = 'Melody'
            melody_part.append(clef.TrebleClef())
            melody_part.append(key.Key('C'))
            melody_part.append(meter.TimeSignature('3/8'))
            melody_part.append(tempo.MetronomeMark(number=120))

            for bar_data in self.composition:
                measure = stream.Measure(number=bar_data['bar'])
                for note_data in bar_data['melody']:
                    if isinstance(note_data, tuple):
                        note_name, duration = note_data
                    else:
                        note_name, duration = note_data, 0.5
                    n = note.Note(note_name, quarterLength=duration)
                    measure.append(n)
                melody_part.append(measure)

            # Accompaniment part (left hand)
            accomp_part = stream.Part()
            accomp_part.id = 'Accompaniment'
            accomp_part.append(clef.BassClef())
            accomp_part.append(key.Key('C'))
            accomp_part.append(meter.TimeSignature('3/8'))

            for bar_data in self.composition:
                measure = stream.Measure(number=bar_data['bar'])
                chord_notes = bar_data['chord_notes']
                # Bass note
                bass_note = chord_notes[0].replace('4', '3').replace('5', '3')
                bass = note.Note(bass_note, quarterLength=0.75)
                measure.append(bass)
                # Chord
                chord_pitches = [chord_notes[0].replace('4', '3').replace('5', '3'),
                                chord_notes[1].replace('5', '4'),
                                chord_notes[2].replace('5', '4')]
                ch = chord.Chord(chord_pitches, quarterLength=0.75)
                measure.append(ch)
                accomp_part.append(measure)

            score.append(melody_part)
            score.append(accomp_part)

            # Generate sheet music notation as PNG
            text.insert(tk.END, "✓ Score created successfully!\n")
            text.insert(tk.END, "  - 14 bars with melody and accompaniment\n")
            text.insert(tk.END, "  - Properly formatted in 3/8 time\n")
            text.insert(tk.END, "  - C major key signature\n\n")

            text.insert(tk.END, "📄 GENERATING SHEET MUSIC NOTATION...\n")
            text.insert(tk.END, "-" * 80 + "\n")
            viz_window.update()

            # Try to generate PNG notation
            score_image_path = None
            try:
                # Try to write PNG using lilypond or musicxml
                score_image_path = "score_notation.png"

                # Attempt PNG generation
                try:
                    # Try lilypond first (if installed)
                    score.write('lily.png', fp=score_image_path)
                    text.insert(tk.END, "✓ Sheet music generated using Lilypond\n")
                except:
                    try:
                        # Try musicxml with conversion
                        score.write('musicxml.png', fp=score_image_path)
                        text.insert(tk.END, "✓ Sheet music generated using MusicXML\n")
                    except:
                        # Fallback: try to open in MuseScore which can display notation
                        text.insert(tk.END, "⚠ PNG generation requires MuseScore or Lilypond\n")
                        text.insert(tk.END, "  Attempting to open in notation software...\n")
                        try:
                            score.show()
                            text.insert(tk.END, "✓ Score opened in external notation software!\n")
                        except:
                            text.insert(tk.END, "⚠ Could not generate or display sheet music.\n")
                            text.insert(tk.END, "  Install MuseScore from https://musescore.org/\n")
                            text.insert(tk.END, "  or Lilypond from http://lilypond.org/\n")
                        score_image_path = None

                # If PNG was successfully created, display it in the window
                if score_image_path and os.path.exists(score_image_path):
                    text.insert(tk.END, f"✓ Sheet music saved: {score_image_path}\n\n")

                    # Create a new frame to display the image
                    try:
                        from PIL import Image, ImageTk

                        # Create image display section
                        text.insert(tk.END, "\n" + "=" * 80 + "\n")
                        text.insert(tk.END, "SHEET MUSIC NOTATION:\n")
                        text.insert(tk.END, "=" * 80 + "\n")
                        text.insert(tk.END, "(See image below - scroll down)\n\n")

                        # Create a canvas to display the image
                        img_canvas = tk.Canvas(viz_window, bg='white')
                        img_canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

                        # Load and display image
                        img = Image.open(score_image_path)

                        # Resize if too large
                        max_width = 950
                        if img.width > max_width:
                            ratio = max_width / img.width
                            new_height = int(img.height * ratio)
                            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)

                        photo = ImageTk.PhotoImage(img)
                        img_canvas.create_image(10, 10, anchor=tk.NW, image=photo)
                        img_canvas.image = photo  # Keep reference
                        img_canvas.config(scrollregion=img_canvas.bbox(tk.ALL))

                        text.insert(tk.END, "✓ Sheet music displayed below!\n")

                    except ImportError:
                        text.insert(tk.END, "⚠ PIL/Pillow not installed - cannot display image\n")
                        text.insert(tk.END, f"  View the image at: {score_image_path}\n")
                    except Exception as e:
                        text.insert(tk.END, f"⚠ Could not display image: {e}\n")
                        text.insert(tk.END, f"  View the image at: {score_image_path}\n")

            except Exception as e:
                text.insert(tk.END, f"⚠ Sheet music generation failed: {e}\n")
                text.insert(tk.END, "  You can still open the MIDI file in MuseScore\n")

        except Exception as e:
            text.insert(tk.END, f"\n⚠ Notation generation issue: {str(e)}\n")
            text.insert(tk.END, "You can still open the MIDI file in MuseScore to see notation.\n")

        text.config(state=tk.DISABLED)

        # Close button
        tk.Button(
            viz_window,
            text="Close",
            command=viz_window.destroy,
            font=("Arial", 12),
            bg='#e74c3c',
            fg='white',
            padx=20,
            pady=10
        ).pack(pady=10)

    def play_music(self):
        """Play the composed music"""
        if not self.composition:
            messagebox.showerror("Error", "No composition to play!")
            return

        if not os.path.exists(self.midi_filename):
            messagebox.showerror("Error", f"MIDI file {self.midi_filename} not found!")
            return

        try:
            if MUSIC21_AVAILABLE:
                # Try to play with music21
                messagebox.showinfo(
                    "Playing...",
                    f"Playing your composition!\n\n"
                    f"The music will play through your default MIDI player.\n"
                    f"File: {self.midi_filename}"
                )

                # Use music21 to play
                try:
                    from music21 import converter
                    score = converter.parse(self.midi_filename)
                    score.show('midi')
                except:
                    # Fallback: open with default program
                    import subprocess
                    import platform

                    if platform.system() == 'Windows':
                        os.startfile(self.midi_filename)
                    elif platform.system() == 'Darwin':  # macOS
                        subprocess.call(['open', self.midi_filename])
                    else:  # Linux
                        subprocess.call(['xdg-open', self.midi_filename])
            else:
                # Open with default program
                import subprocess
                import platform

                if platform.system() == 'Windows':
                    os.startfile(self.midi_filename)
                elif platform.system() == 'Darwin':
                    subprocess.call(['open', self.midi_filename])
                else:
                    subprocess.call(['xdg-open', self.midi_filename])

                messagebox.showinfo("Playing", f"Opening {self.midi_filename} with default player")

        except Exception as e:
            messagebox.showerror("Error", f"Could not play music: {str(e)}")

    def save_midi(self):
        """Save MIDI with custom filename"""
        if not self.composition:
            messagebox.showerror("Error", "No composition to save!")
            return

        from tkinter import filedialog

        filename = filedialog.asksaveasfilename(
            defaultextension=".mid",
            filetypes=[("MIDI files", "*.mid"), ("All files", "*.*")],
            initialfile="my_kirnberger_composition.mid"
        )

        if filename:
            try:
                self.game.create_midi(self.composition, filename)
                messagebox.showinfo("Success", f"MIDI file saved as:\n{filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {str(e)}")

    def reset_game(self):
        """Reset and start a new composition"""
        result = messagebox.askyesno(
            "New Composition",
            "Start a new composition?\nCurrent progress will be lost."
        )

        if result:
            self.current_bar = 1
            self.choices = []
            self.composition = None

            self.progress_bar['value'] = 0
            self.progress_label.config(text="Bar 1 of 14 (Period 1)", fg='#e74c3c')
            self.bar_info_label.config(text="Bar 1 - Harmony: I (C major)")
            self.dice_display.config(text="🎲")
            self.result_label.config(
                text="Click 'Roll Dice' to start!",
                fg='#7f8c8d',
                font=("Arial", 12)
            )

            self.choices_text.config(state=tk.NORMAL)
            self.choices_text.delete(1.0, tk.END)
            self.choices_text.config(state=tk.DISABLED)

            self.roll_button.config(state=tk.NORMAL)
            self.roll_all_button.config(state=tk.NORMAL)
            self.visualize_button.config(state=tk.DISABLED)
            self.play_button.config(state=tk.DISABLED)
            self.save_button.config(state=tk.DISABLED)


def main():
    root = tk.Tk()
    app = DiceGameGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
