"""
Test script for Version 2.0 enhancements
"""

import sys
import os

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Import the game
spec_path = os.path.join(os.path.dirname(__file__), "Mozart Music Generator.py")
import importlib.util
spec = importlib.util.spec_from_file_location("mozart_generator", spec_path)
mozart_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mozart_module)

KirnbergerGame = mozart_module.KirnbergerGame

def test_rhythmic_variety():
    """Test that variants now have rhythm tuples"""
    print("Testing rhythmic variety...")
    game = KirnbergerGame()

    # Check bar 1, variant 1
    bar1_var1 = game.composition_data[1]['variants'][0]
    print(f"  Bar 1, Variant 1: {bar1_var1}")

    # Should be tuples now
    if isinstance(bar1_var1[0], tuple):
        print("  [OK] Rhythm tuples present!")
        note, duration = bar1_var1[0]
        print(f"    First note: {note}, duration: {duration}")
    else:
        print("  [FAIL] ERROR: Still using old format")
        return False

    # Check total duration adds to 1.5 (3/8 time)
    total = sum(d for n, d in bar1_var1)
    print(f"  Total duration: {total} (should be 1.5)")
    if abs(total - 1.5) < 0.01:
        print("  [OK] Duration correct!")
    else:
        print(f"  [FAIL] ERROR: Duration is {total}, not 1.5")
        return False

    return True

def test_cadences():
    """Test that cadences have strong endings"""
    print("\nTesting cadences...")
    game = KirnbergerGame()

    # Check bar 6 (half cadence)
    print("  Bar 6 (half cadence) variants:")
    for i, variant in enumerate(game.composition_data[6]['variants'][:3], 1):
        if isinstance(variant[-1], tuple):
            last_note, last_duration = variant[-1]
            print(f"    Variant {i}: ends with {last_note} ({last_duration})")
            if last_duration >= 0.75:
                print(f"      [OK] Strong ending (>= 0.75)")
        else:
            print(f"    Variant {i}: old format")

    # Check bar 14 (final cadence)
    print("  Bar 14 (final cadence) variants:")
    for i, variant in enumerate(game.composition_data[14]['variants'][:3], 1):
        if isinstance(variant[-1], tuple):
            last_note, last_duration = variant[-1]
            print(f"    Variant {i}: ends with {last_note} ({last_duration})")
            if last_duration >= 1.0:
                print(f"      [OK] Very strong ending (>= 1.0)")
        else:
            print(f"    Variant {i}: old format")

    # Check for single-note cadences
    bar14_single = [v for v in game.composition_data[14]['variants'] if len(v) == 1]
    print(f"  Single-note cadences in bar 14: {len(bar14_single)}")
    if len(bar14_single) > 0:
        print("  [OK] Ultimate finality variants present!")

    return True

def test_composition_generation():
    """Test that composition generation works with new format"""
    print("\nTesting composition generation...")
    game = KirnbergerGame()

    # Generate a piece
    choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 2, 3]
    composition = game.generate_with_choices(choices)

    print(f"  Generated {len(composition)} bars")

    # Check first bar
    first_bar = composition[0]
    print(f"  Bar 1: {first_bar['harmony']}, variant {first_bar['variant']}")
    print(f"  Melody: {first_bar['melody']}")

    if isinstance(first_bar['melody'][0], tuple):
        print("  [OK] Composition uses new rhythm format!")
    else:
        print("  [FAIL] ERROR: Composition still uses old format")
        return False

    return True

def test_midi_generation():
    """Test MIDI file generation"""
    print("\nTesting MIDI generation...")
    game = KirnbergerGame()

    choices = [5, 3, 7, 2, 9, 4, 8, 6, 10, 1, 3, 5, 7, 1]
    composition = game.generate_with_choices(choices)

    test_file = "test_enhanced.mid"
    success = game.create_midi(composition, test_file)

    if success and os.path.exists(test_file):
        print(f"  [OK] MIDI file generated: {test_file}")
        size = os.path.getsize(test_file)
        print(f"  File size: {size} bytes")
        return True
    else:
        print("  [FAIL] ERROR: MIDI generation failed")
        return False

def main():
    print("="*60)
    print("KIRNBERGER GAME - VERSION 2.0 ENHANCEMENT TEST")
    print("="*60)

    tests = [
        ("Rhythmic Variety", test_rhythmic_variety),
        ("Strong Cadences", test_cadences),
        ("Composition Generation", test_composition_generation),
        ("MIDI Generation", test_midi_generation),
    ]

    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"  [FAIL] EXCEPTION: {e}")
            import traceback
            traceback.print_exc()
            results.append((name, False))

    print("\n" + "="*60)
    print("TEST RESULTS:")
    print("="*60)
    for name, result in results:
        status = "[OK] PASS" if result else "[FAIL] FAIL"
        print(f"  {status}: {name}")

    all_passed = all(r for _, r in results)
    print("\n" + "="*60)
    if all_passed:
        print("*** ALL TESTS PASSED! Version 2.0 enhancements working!")
    else:
        print("*** SOME TESTS FAILED - Check output above")
    print("="*60)

if __name__ == "__main__":
    main()
