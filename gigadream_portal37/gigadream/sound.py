"""
GIGADREAM Sound Engine
Pure terminal bell sequences evoking:
- Ambient Beach waves (slow rolling)
- Spacey Orbital vibe (long sustained tones)
- Starjet (fast ascending energy)
- Portal whooshes & swirls (PORTAL 37)

Zero external dependencies. Optional: pip install simpleaudio for real audio.
"""

import time
import sys
import platform
import random
from typing import Dict

try:
    import simpleaudio as sa
    HAS_SIMPLEAUDIO = True
except ImportError:
    HAS_SIMPLEAUDIO = False

def _terminal_bell():
    """Cross-platform terminal bell."""
    sys.stdout.write('\a')
    sys.stdout.flush()

def _generate_sine_wave(freq: float, duration_sec: float, sample_rate: int = 44100):
    """Generate a simple sine wave for synth tones."""
    import numpy as np
    t = np.linspace(0, duration_sec, int(sample_rate * duration_sec), False)
    wave = np.sin(freq * t * 2 * np.pi)
    audio = (wave * 32767 / np.max(np.abs(wave))).astype(np.int16)
    return audio

def _play_synth_tone(pattern: str, intensity: float = 0.6, duration: float = 4.0):
    """Play synthesized tones with simpleaudio when available."""
    if not HAS_SIMPLEAUDIO:
        return
    
    import numpy as np
    sample_rate = 44100
    
    if pattern == "slow_roll":  # Ambient Beach — low rolling waves
        for _ in range(int(duration / 0.8)):
            freq = 80 + random.random() * 40
            wave = _generate_sine_wave(freq, 0.6 + random.random() * 0.4)
            sa.play_buffer(wave, 1, 2, sample_rate).wait_done()
            time.sleep(0.3 * (1.0 - intensity * 0.5))
    
    elif pattern == "long_tone":  # Spacey Orbital — dreamy sustains
        for _ in range(int(duration / 1.2)):
            freq = 180 + random.random() * 120
            wave = _generate_sine_wave(freq, 1.2, sample_rate)
            sa.play_buffer(wave * intensity, 1, 2, sample_rate).wait_done()
            time.sleep(random.uniform(0.4, 0.9))
    
    elif pattern == "fast_ascend":  # Starjet — sharp rising energy
        for _ in range(int(duration / 0.4)):
            base = 400 + random.random() * 300
            for step in range(5):
                freq = base + step * 80
                wave = _generate_sine_wave(freq, 0.08, sample_rate)
                sa.play_buffer(wave * intensity, 1, 2, sample_rate).wait_done()
            time.sleep(0.15)
    
    elif pattern == "swirl_whoosh":  # PORTAL 37 — swirling portal
        steps = int(duration * 2)
        for i in range(steps):
            freq = 120 + (i % 12) * 35 + random.random() * 80
            dur = 0.12 + abs(i % 5 - 2.5) * 0.04
            wave = _generate_sine_wave(freq, dur, sample_rate)
            sa.play_buffer(wave * intensity, 1, 2, sample_rate).wait_done()
            time.sleep(0.05)

def _beep_sequence(pattern: str, intensity: float = 0.6, duration: float = 4.0):
    """
    Play rhythmic bell patterns that evoke the vibe.
    Beach: slow deep rolls
    Orbital: long dreamy sustains
    Starjet: sharp fast ascents
    Portal: swirling whooshes with variation
    """
    start = time.time()
    count = 0
    
    if pattern == "slow_roll":  # Ambient Beach
        delays = [0.45, 0.55, 0.65, 0.5, 0.7]
        while time.time() - start < duration:
            _terminal_bell()
            time.sleep(random.choice(delays) * (1.1 - intensity * 0.4))
            count += 1
            if count > 18:
                break
    
    elif pattern == "long_tone":  # Spacey Orbital
        while time.time() - start < duration:
            for _ in range(random.randint(2, 4)):
                _terminal_bell()
                time.sleep(0.08)
            time.sleep(random.uniform(0.6, 1.1) * (1.0 - intensity * 0.3))
    
    elif pattern == "fast_ascend":  # Starjet
        while time.time() - start < duration:
            for i in range(random.randint(3, 7)):
                _terminal_bell()
                time.sleep(0.035 + (i * 0.008))
            time.sleep(random.uniform(0.15, 0.35))
    
    elif pattern == "swirl_whoosh":  # PORTAL 37
        while time.time() - start < duration:
            steps = random.randint(4, 9)
            for i in range(steps):
                _terminal_bell()
                delay = 0.04 + (abs(i - steps/2) * 0.015)
                time.sleep(delay * (0.7 + intensity * 0.6))
            time.sleep(random.uniform(0.25, 0.55))

def play_sequence(vibe: str = "portal", intensity: float = 0.6, duration: float = 4.0):
    """
    Main entry: Play a vibe sequence.
    Vibes: 'beach', 'orbital', 'starjet', 'portal'
    """
    pattern_map = {
        "beach": "slow_roll",
        "orbital": "long_tone",
        "starjet": "fast_ascend",
        "portal": "swirl_whoosh"
    }
    pattern = pattern_map.get(vibe, "swirl_whoosh")
    
    if HAS_SIMPLEAUDIO:
        try:
            _play_synth_tone(pattern, intensity, duration)
        except:
            _beep_sequence(pattern, intensity, duration)
    else:
        _beep_sequence(pattern, intensity, duration)

def play_ambient_layer(vibes: list = None, total_duration: float = 11.0):
    """Layer multiple vibes for rich ambient experience during animation."""
    if vibes is None:
        vibes = ["beach", "orbital", "portal"]
    
    # Play in background-ish by interleaving short bursts
    start = time.time()
    idx = 0
    while time.time() - start < total_duration:
        vibe = vibes[idx % len(vibes)]
        play_sequence(vibe, intensity=0.45 + random.random()*0.25, duration=1.8)
        time.sleep(0.6)
        idx += 1