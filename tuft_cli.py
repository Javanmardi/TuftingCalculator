import argparse
from fractions import Fraction
import math

def calculate_tuft_weight(ga, st, pl, den, pile_type):
    """
    Calculate tufting carpet weight based on pile type.
    """
    if pile_type.lower() == "cut":
        tuft = (1/ga) * (1000/25.4) * st * 10 * ((pl * 2) + (10/st)) * 0.001 * (den / 9000)
    else:  # loop
        tuft = (1/ga) * (1000/25.4) * st * 10 * ((pl * 2) + (20/st)) * 0.001 * (den / 9000)
    
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tufting Carpet Weight Calculator")
    parser.add_argument("--gauge", type=str, help="Gauge (e.g. 1/8 or 0.125)")
    parser.add_argument("--stitch", type=str, help="Stitch rate (per dm)")
    parser.add_argument("--pile", type=str, help="Pile height (mm)")
    parser.add_argument("--den", type=str, help="Yarn denier (den)")
    parser.add_argument("--piletype", type=str, choices=["Cut", "Loop"], help="Pile type (Cut or Loop)")
    parser.add_argument('--about', action='store_true', help="Show author and license info")

    args = parser.parse_args()

    if args.about:
        print("Tufting Carpet Weight Calculator\nAuthor: Behrouz Javanmardi\nGitHub: https://github.com/Javanmardi/TuftingCalculator\nLicense: MIT\nVersion: 1.0.0")
        exit()

    if args.gauge and args.stitch and args.pile and args.den and args.piletype:
        # Command-line mode
        ga = parse_number(args.gauge)
        st = parse_number(args.stitch)
        pl = parse_number(args.pile)
        den = parse_number(args.den)
        pile_type = args.piletype
        tuft_weight = calculate_tuft_weight(ga, st, pl, den, pile_type)
        print(f"\nTufting carpet weight = {math.ceil(tuft_weight)} gram")
    else:
        # Interactive mode
        print("Tufting Carpet Weight Calculator (Interactive Mode)\n")
        ga = parse_number(input("Enter gauge (inch, e.g. 1/8 or 0.125): "))
        st = parse_number(input("Enter stitch rate (per dm): "))
        pl = parse_number(input("Enter pile height (mm): "))
        den = parse_number(input("Enter yarn denier (den): "))
        pile_type = input("Enter pile type (Cut or Loop): ").strip()
        if pile_type.lower() not in ["cut", "loop"]:
            print("Invalid pile type. Defaulting to Cut.")
            pile_type = "Cut"
        tuft_weight = calculate_tuft_weight(ga, st, pl, den, pile_type)
        print(f"\nTufting carpet weight = {math.ceil(tuft_weight)} gram")
        print("\nThank you for using the Tufting Carpet Weight Calculator.")
        print("Visit https://github.com/Javanmardi/TuftingCalculator for updates and source code.")

