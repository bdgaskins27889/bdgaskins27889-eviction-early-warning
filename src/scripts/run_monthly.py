import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--county", choices=["pitt", "bay"], required=True)
    parser.add_argument("--disaster", action="store_true")
    args = parser.parse_args()

    print(f"Pipeline stub running for county={args.county}, disaster={args.disaster}")
    print("Next: add data loaders + scoring functions once data paths are finalized.")

if __name__ == "__main__":
    main()
