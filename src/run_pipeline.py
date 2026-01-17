import argparse
from pathlib import Path
import yaml

def main(config_path: str):
    config = yaml.safe_load(Path(config_path).read_text())
    print("Loaded config:", config)
    print("Pipeline scaffold ready.")
    print("Next: add ingest -> clean -> score -> export steps in src/ modules.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True, help="Path to YAML config file")
    args = parser.parse_args()
    main(args.config)
