"""
GIGADREAM Art Engine
Hyper-kinetic, hallucinatory ASCII frames.
Focus: GIGADREAM. Hints: Beachpunk • PORTAL 37 • Sandtech • TERRA II
"""

import random
from typing import List

# ANSI Colors - Gigadream Cyber-Neon Palette
COLORS = {
    'reset': '\033[0m',
    'gigadream_cyan': '\033[38;5;51m',
    'portal_pink': '\033[38;5;201m',
    'starjet_gold': '\033[38;5;220m',
    'orbital_purple': '\033[38;5;93m',
    'sandtech_green': '\033[38;5;118m',
    'glitch_red': '\033[38;5;196m',
    'wave_blue': '\033[38;5;39m',
    'bold': '\033[1m',
    'dim': '\033[2m',
    'italic': '\033[3m'
}

def glitch(text: str, intensity: float = 0.2) -> str:
    """Apply beautiful glitch distortion."""
    if random.random() > intensity:
        return text
    glitch_chars = ['█', '▓', '▒', '░', '■', '□', '◉', '◌', '◍', '◐', '◑', '◒', '◓']
    result = []
    for char in text:
        if random.random() < intensity * 0.7 and char.isalnum():
            result.append(random.choice(glitch_chars))
        elif random.random() < intensity * 0.3:
            result.append(random.choice(['/', '\\', '|', '-', '~', '*', '·']))
        else:
            result.append(char)
    return ''.join(result)

def get_frames() -> List[str]:
    """Return a rich set of GIGADREAM frames. Beachpunk hinted. PORTAL 37 active."""
    frames = [
        # Frame 0 — Portal Awakening (GIGADREAM focus)
        r"""
              ⋆ ˚｡⋆୨୧˚   G I G A D R E A M   ˚୨୧⋆｡˚ ⋆
                    ╔════════════════════════════╗
                    ║     P O R T A L   3 7      ║
                    ╚════════════════════════════╝
           
         .-'~'-..-'~'-..-'~'-..-'~'-..-'~'-..-'~'-.
        /   _   _   _   _   _   _   _   _   _   _   \
       |  | | | | | | | | | | | | | | | | | | | | |  |
        \   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   /
         '-..-'~'-..-'~'-..-'~'-..-'~'-..-'~'-..-'

              🌊  Latinobionic Orbit Activated  🌊
                   Sandtech • No Masters
        """,

        # Frame 1 — Starjet Ignition
        r"""
              ⋆ ˚｡⋆୨୧˚   G I G A D R E A M   ˚୨୧⋆｡˚ ⋆
                    ╔════════════════════════════╗
                    ║     P O R T A L   3 7      ║
                    ╚════════════════════════════╝
           
         .-'~'-..-'~'-..-'~'-..-'~'-..-'~'-..-'~'-.
        /   _   _   _   _   _   _   _   _   _   _   \
       |  | | | | | | | | | | | | | | | | | | | | |  |
        \   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   /
         '-..-'~'-..-'~'-..-'~'-..-'~'-..-'~'-..-'

           ★  STARJET RISING  ★   Beachpunk Echoes
              TERRA II • Diamond Riot Protocol
        """,

        # Frame 2 — Full Orbital Glitch
        r"""
              ⋆ ˚｡⋆୨୧˚   G I G A D R E A M   ˚୨୧⋆｡˚ ⋆
                    ╔════════════════════════════╗
                    ║  [ P O R T A L   3 7 ]     ║
                    ╚════════════════════════════╝
           
         .-'~'-..-'~'-..-'~'-..-'~'-..-'~'-..-'~'-.
        /   _   _   _   _   _   _   _   _   _   _   \
       |  | | | | | | | | | | | | | | | | | | | | |  |
        \   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   /
         '-..-'~'-..-'~'-..-'~'-..-'~'-..-'~'-..-'

        🌊🌊  GIGADREAM TRANSMISSION  🌊🌊   PORTAL OPEN
              Latinobionic • Sandtech Fury • No Masters
        """,

        # Frame 3 — Beachpunk Hint (subtle)
        r"""
              ⋆ ˚｡⋆୨୧˚   G I G A D R E A M   ˚୨୧⋆｡˚ ⋆
                    ╔════════════════════════════╗
                    ║     P O R T A L   3 7      ║
                    ╚════════════════════════════╝
           
         .-'~'-..-'~'-..-'~'-..-'~'-..-'~'-..-'~'-.
        /   _   _   _   _   _   _   _   _   _   _   \
       |  | | | | | | | | | | | | | | | | | | | | |  |
        \   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   /
         '-..-'~'-..-'~'-..-'~'-..-'~'-..-'~'-..-'

           ~~~  BEACHPUNK VIBES ~~~   Waves of Diamond
              Puerto Rican Futurism • Gigabionic Heart
        """,

        # Frame 4 — Deep Portal
        r"""
              ⋆ ˚｡⋆୨୧˚   G I G A D R E A M   ˚୨୧⋆｡˚ ⋆
                    ╔════════════════════════════╗
                    ║   [GLITCH CORE] PORTAL 37  ║
                    ╚════════════════════════════╝
           
         .-'~'-..-'~'-..-'~'-..-'~'-..-'~'-..-'~'-.
        /   _   _   _   _   _   _   _   _   _   _   \
       |  | | | | | | | | | | | | | | | | | | | | |  |
        \   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   /
         '-..-'~'-..-'~'-..-'~'-..-'~'-..-'~'-..-'

              ◉  SWORDS WITH NO MASTERS  ◉
                   Enter the Gigadream
        """,

        # Frame 5 — Climactic
        r"""
              ⋆ ˚｡⋆୨୧˚   G I G A D R E A M   ˚୨୧⋆｡˚ ⋆
                    ╔════════════════════════════╗
                    ║     P O R T A L   3 7      ║
                    ╚════════════════════════════╝
           
         .-'~'-..-'~'-..-'~'-..-'~'-..-'~'-..-'~'-.
        /   _   _   _   _   _   _   _   _   _   _   \
       |  | | | | | | | | | | | | | | | | | | | | |  |
        \   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   /
         '-..-'~'-..-'~'-..-'~'-..-'~'-..-'~'-..-'

           ★★★  GIGADREAM ETERNAL  ★★★   Beachpunk Soul
              Latinobionic Orbit • Diamond Riot Forever
        """,

        # Frame 6 — Hidden Sandtech Wave
        r"""
              ⋆ ˚｡⋆୨୧˚   G I G A D R E A M   ˚୨୧⋆｡˚ ⋆
                    ╔════════════════════════════╗
                    ║     P O R T A L   3 7      ║
                    ╚════════════════════════════╝
           
         .-'~'-..-'~'-..-'~'-..-'~'-..-'~'-..-'~'-.
        /   _   _   _   _   _   _   _   _   _   _   \
       |  | | | | | | | | | | | | | | | | | | | | |  |
        \   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   /
         '-..-'~'-..-'~'-..-'~'-..-'~'-..-'~'-..-'

           🌴🌊  BEACHPUNK SANDSHIFT  🌊🌴
              Gigabionic Puerto Rico Rising
        """,

        # Frame 7 — Pure Gigadream Core
        r"""
              ⋆ ˚｡⋆୨୧˚   G I G A D R E A M   ˚୨୧⋆｡˚ ⋆
                    ╔════════════════════════════╗
                    ║   [∞] P O R T A L   3 7   [∞]║
                    ╚════════════════════════════╝
           
         .-'~'-..-'~'-..-'~'-..-'~'-..-'~'-..-'~'-.
        /   _   _   _   _   _   _   _   _   _   _   \
       |  | | | | | | | | | | | | | | | | | | | | |  |
        \   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   /
         '-..-'~'-..-'~'-..-'~'-..-'~'-..-'~'-..-'

              ∞  THE GIGADREAM IS THE ONLY REALITY  ∞
                   No Masters. Only Transmission.
        """,

        # Frame 8 — Diamond Riot Explosion
        r"""
              ⋆ ˚｡⋆୨୧˚   G I G A D R E A M   ˚୨୧⋆｡˚ ⋆
                    ╔════════════════════════════╗
                    ║     P O R T A L   3 7      ║
                    ╚════════════════════════════╝
           
         .-'~'-..-'~'-..-'~'-..-'~'-..-'~'-..-'~'-.
        /   _   _   _   _   _   _   _   _   _   _   \
       |  | | | | | | | | | | | | | | | | | | | | |  |
        \   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   /
         '-..-'~'-..-'~'-..-'~'-..-'~'-..-'~'-..-'

           💎💥  DIAMOND RIOT PROTOCOL  💥💎
              Latinobionic Chaos • Eternal Vibe
        """
    ]
    return frames

def render_frame(frame: str, glitch_intensity: float = 0.2, color_mode: str = "full") -> str:
    """Render frame with glitch and color."""
    lines = frame.strip().split('\n')
    rendered_lines = []
    
    for line in lines:
        processed = line
        if color_mode == "full":
            if "GIGADREAM" in line or "G I G A" in line:
                processed = COLORS['gigadream_cyan'] + COLORS['bold'] + glitch(processed, glitch_intensity) + COLORS['reset']
            elif "PORTAL" in line or "P O R T A L" in line:
                processed = COLORS['portal_pink'] + COLORS['bold'] + glitch(processed, glitch_intensity * 0.8) + COLORS['reset']
            elif "STARJET" in line or "★" in line:
                processed = COLORS['starjet_gold'] + glitch(processed, glitch_intensity) + COLORS['reset']
            elif "🌊" in line or "wave" in line.lower() or "BEACH" in line.upper():
                processed = COLORS['wave_blue'] + glitch(processed, glitch_intensity * 0.6) + COLORS['reset']
            elif "Sandtech" in line or "Latinobionic" in line:
                processed = COLORS['sandtech_green'] + glitch(processed, glitch_intensity * 0.5) + COLORS['reset']
            else:
                processed = COLORS['orbital_purple'] + glitch(processed, glitch_intensity * 0.4) + COLORS['reset']
        else:
            processed = glitch(processed, glitch_intensity)
        
        rendered_lines.append(processed)
    
    return '\n'.join(rendered_lines)