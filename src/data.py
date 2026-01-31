"""Data loading and saving utilities."""


def load_raw_data(path: str):
    """Load raw data from the provided path."""
    raise NotImplementedError("Implement data loading.")


def save_processed_data(df, path: str) -> None:
    """Save processed data to the provided path."""
    raise NotImplementedError("Implement data saving.")
