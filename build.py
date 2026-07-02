from pathlib import Path


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    required_files = [
        base_dir / "regmodel.pkl",
        base_dir / "scaler.pkl",
        base_dir / "templates" / "home.html",
    ]

    missing_files = [str(path) for path in required_files if not path.exists()]
    if missing_files:
        raise FileNotFoundError(
            "Missing required deployment files: " + ", ".join(missing_files)
        )

    print("Build checks passed.")


if __name__ == "__main__":
    main()