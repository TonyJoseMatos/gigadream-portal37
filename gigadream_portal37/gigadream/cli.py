"""
GIGADREAM // PORTAL 37 — CLI
The official terminal transmission.

Run:
    gigadream
    portal37 --mode glitch --sound portal
    gigadream --help
"""

import argparse
import json
import os
import sys
import time
import random
from pathlib import Path

from .art import get_frames, render_frame, COLORS
from .sound import play_sequence, play_ambient_layer

CONFIG_PATH = Path(__file__).parent / "config" / "default.json"

def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(config):
    gigadream = config["gigadream"]
    branding = config["branding"]
    
    header = f"""
{COLORS['portal_pink']}{COLORS['bold']}
   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
  ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
   ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
{COLORS['reset']}{COLORS['gigadream_cyan']}
          {gigadream['title']}
{COLORS['reset']}{COLORS['starjet_gold']}
     {gigadream['subtitle']}
{COLORS['reset']}
{COLORS['sandtech_green']}   Focus: GIGADREAM  •  Hints: Beachpunk • PORTAL 37  •  TERRA II{COLORS['reset']}
"""
    print(header)
    print(f"{COLORS['dim']}   {branding['author']}  |  {branding['handle']}  |  {branding['studio']}{COLORS['reset']}\n")

def animate(config, args):
    frames = get_frames()
    glitch_int = args.intensity or config["gigadream"]["glitch_intensity_default"]
    speed = args.speed or config["gigadream"]["animation_speed"]
    duration = args.duration or config["gigadream"]["duration_default"]
    
    start = time.time()
    frame_idx = 0
    
    # Optional ambient sound layer
    if args.sound:
        print(f"{COLORS['orbital_purple']}[GIGADREAM] Sound layer engaged...{COLORS['reset']}")
        # Non-blocking-ish ambient
        import threading
        sound_thread = threading.Thread(
            target=play_ambient_layer, 
            args=(["beach", "orbital", "portal"], duration + 2),
            daemon=True
        )
        sound_thread.start()
    
    while time.time() - start < duration:
        clear()
        print_header(config)
        rendered = render_frame(frames[frame_idx % len(frames)], glitch_int, args.color)
        print(rendered)
        
        # Occasional single sound hit synced to animation
        if args.sound and random.random() < 0.35:
            vibe = random.choice(["beach", "orbital", "starjet", "portal"])
            play_sequence(vibe, intensity=0.5, duration=0.8)
        
        time.sleep(speed)
        frame_idx += 1
    
    # Final beautiful static frame
    clear()
    print_header(config)
    print(render_frame(frames[0], glitch_int * 0.6, args.color))
    
    print(f"\n{COLORS['starjet_gold']}{COLORS['bold']}    GIGADREAM TRANSMISSION COMPLETE. PORTAL 37 STAYS OPEN.{COLORS['reset']}")
    print(f"{COLORS['dim']}    Return whenever the waves call. No masters. Only gigadream.{COLORS['reset']}\n")

def main():
    config = load_config()
    
    parser = argparse.ArgumentParser(
        description="GIGADREAM // PORTAL 37 — Terminal ASCII Engine",
        epilog="Focus: GIGADREAM. Hints of Beachpunk. PORTAL 37 active."
    )
    parser.add_argument("-m", "--mode", choices=["animate", "static", "glitch", "secret"], default="animate")
    parser.add_argument("-i", "--intensity", type=float, help="Glitch intensity (0.0-1.0)")
    parser.add_argument("-s", "--speed", type=float, help="Animation speed in seconds")
    parser.add_argument("-d", "--duration", type=int, help="Total duration in seconds")
    parser.add_argument("--sound", action="store_true", help="Enable ambient sound layer (beach / orbital / starjet / portal)")
    parser.add_argument("--color", choices=["full", "minimal", "none"], default="full")
    parser.add_argument("--export", action="store_true", help="Export final frame to gigadream_portal37.txt")
    
    args = parser.parse_args()
    
    clear()
    print_header(config)
    
    try:
        if args.mode == "animate":
            animate(config, args)
        elif args.mode == "glitch":
            frames = get_frames()
            for _ in range(14):
                clear()
                print_header(config)
                print(render_frame(random.choice(frames), args.intensity or 0.45, args.color))
                if args.sound:
                    play_sequence(random.choice(["starjet", "portal"]), intensity=0.65, duration=0.6)
                time.sleep(0.28)
            animate(config, args)  # end with clean animation
        elif args.mode == "secret":
            # Hidden PORTAL 37 secret mode — pure Gigadream overload
            print(f"{COLORS['portal_pink']}{COLORS['bold']}    [SECRET TRANSMISSION — PORTAL 37 UNLOCKED]{COLORS['reset']}")
            frames = get_frames()
            for _ in range(22):
                clear()
                print_header(config)
                frame = random.choice(frames)
                print(render_frame(frame, 0.65, args.color))
                if args.sound:
                    play_sequence(random.choice(["portal", "starjet"]), intensity=0.85, duration=0.45)
                time.sleep(0.18)
            animate(config, args)
        else:  # static
            frames = get_frames()
            print(render_frame(frames[0], args.intensity or 0.15, args.color))
        
        if args.export:
            with open("gigadream_portal37.txt", "w", encoding="utf-8") as f:
                f.write(frames[0])
            print(f"{COLORS['sandtech_green']}    → Exported to gigadream_portal37.txt{COLORS['reset']}")
            
    except KeyboardInterrupt:
        clear()
        print_header(config)
        print(render_frame(get_frames()[0], 0.1))
        print(f"\n{COLORS['portal_pink']}    Transmission cut. The portal remains. GIGADREAM eternal.{COLORS['reset']}\n")

if __name__ == "__main__":
    main()