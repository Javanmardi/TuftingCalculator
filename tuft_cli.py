"""
Tufting Carpet Weight Calculator (CLI Version)
Author: Behrouz Javanmardi
Formula: Dr. Mohsen Bahador
GitHub: https://github.com/Javanmardi/TuftingCalculator
License: MIT
Version: 1.0.0
"""

import argparse
from fractions import Fraction
import math

def calculate_tuft_weight(ga, st, pl, den, pile_type):
    """
    Calculate tufting carpet weight based on pile type.
    """
    if pile_type.lower() == "cut":
        tuft = (1/ga) * (1000/25.4) * st * 10 * ((pl * 2) + (100/st)) * 0.001 * (den / 9000)
    else:  # loop
        tuft = (1/ga) * (1000/25.4) * st * 10 * ((pl * 2) + (200/st)) * 0.001 * (den / 9000)
    
    # Round up to next integer
    return math.ceil(tuft)

def parse_number(value):
    """
    Parse input as either float or fraction (e.g. '1/8').
    """
    try:
        return float(Fraction(value))
    except ValueError:
        return float(value)

def validate_pile_type(value):
    if value and value.lower() in ["cut", "loop"]:
        return value.lower()
    print("Invalid or missing pile type. Defaulting to Cut.")
    return "cut"

# def prompt_interactive():
#     ga = parse_number(input("Enter gauge (inch, e.g. 1/8 or 0.125): "))
#     st = parse_number(input("Enter stitch rate (per dm): "))
#     pl = parse_number(input("Enter pile height (mm): "))
#     den = parse_number(input("Enter yarn denier (den): "))
#     pile_type = validate_pile_type(input("Enter pile type (Cut or Loop): ").strip())
#     return ga, st, pl, den, pile_type

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tufting Carpet Weight Calculator")
    parser.add_argument("--gauge", type=str, help="Gauge (e.g. 1/8 or 0.125)")
    parser.add_argument("--stitch", type=str, help="Stitch rate (per dm)")
    parser.add_argument("--pile", type=str, help="Pile height (mm)")
    parser.add_argument("--den", type=str, help="Yarn denier (den)")
    parser.add_argument("--piletype", type=str, default="cut", help="Pile type (Cut or Loop). Defaults to Cut.")
    parser.add_argument('--about', action='store_true', help="Show author and license info")

    args = parser.parse_args()

    if args.about:
        print("Tufting Carpet Weight Calculator\nAuthor: Behrouz Javanmardi\nGitHub: https://github.com/Javanmardi/TuftingCalculator\nLicense: MIT\nVersion: 1.0.0")
        exit()

    if args.gauge and args.stitch and args.pile and args.den:
        # Command-line mode
        ga = parse_number(args.gauge)
        st = parse_number(args.stitch)
        pl = parse_number(args.pile)
        den = parse_number(args.den)
        pile_type = validate_pile_type(args.piletype)

        tuft_weight = calculate_tuft_weight(ga, st, pl, den, pile_type)
        print(f"\nTufting carpet weight = {tuft_weight} gram/m\u00b2")
    else:
        # Interactive mode
        # ga, st, pl, den, pile_type = prompt_interactive()
        print("Tufting Carpet Weight Calculator (Interactive Mode)\n")
        ga = parse_number(input("Enter gauge (inch, e.g. 1/8 or 0.125): "))
        st = parse_number(input("Enter stitch rate (per dm): "))
        pl = parse_number(input("Enter pile height (mm): "))
        den = parse_number(input("Enter yarn denier (den): "))
        pile_type = validate_pile_type(input("Enter pile type (Cut or Loop): ").strip())
        tuft_weight = calculate_tuft_weight(ga, st, pl, den, pile_type)
        print(f"\nTufting carpet weight = {tuft_weight} gram/m\u00b2")
        print("\nThank you for using the Tufting Carpet Weight Calculator.")
        print("Visit https://github.com/Javanmardi/TuftingCalculator for updates and source code.")
        input("Press any key to exit...")




