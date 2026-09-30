"""Plot every non-time column in the supplied laboratory CSV format.

Install: python -m pip install numpy matplotlib
Run: python plot_csv_columns.py your_data.csv
Add --show to also display each graph, one at a time.
"""

import argparse
import ast
from pathlib import Path

import numpy as np
import matplotlib


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("filename", type=Path, help="Path to your CSV file")
    parser.add_argument("--show", action="store_true", help="Display graphs one at a time")
    args = parser.parse_args()

    # Saving works even in a terminal without a graphical desktop.
    if not args.show:
        matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    filename = args.filename.expanduser().resolve()
    with filename.open(encoding="utf-8-sig") as file:
        groups = ast.literal_eval(file.readline().lstrip("#").strip())
        names_nested = ast.literal_eval(file.readline().lstrip("#").strip())
        labels_nested = ast.literal_eval(file.readline().lstrip("#").strip())

    # Each instrument lists its measurements, followed by its extra columns.
    names = [name for group in names_nested for section in group for name in section]
    labels = [label for group in labels_nested for section in group for label in section]
    instruments = [instrument for instrument, group in zip(groups, names_nested)
                   for section in group for _ in section]

    data = np.loadtxt(filename, delimiter=";", comments="#", ndmin=2,
                      encoding="utf-8-sig")
    if data.size == 0:
        raise ValueError("The file contains no data rows.")
    if not (data.shape[1] == len(names) == len(labels) == len(instruments)):
        raise ValueError("The number of data columns does not match the header.")

    time_column = names.index("unix-time")
    valid_time = np.isfinite(data[:, time_column])
    if not valid_time.any():
        raise ValueError("The file contains no valid timestamps.")
    if not valid_time.all():
        print(f"Skipping {(~valid_time).sum()} rows with missing timestamps.")
    data = data[valid_time]
    data = data[np.argsort(data[:, time_column], kind="stable")]
    time_minutes = (data[:, time_column] - data[0, time_column]) / 60

    output_folder = filename.parent / (filename.stem + "_plots")
    output_folder.mkdir(exist_ok=True)

    for column, name in enumerate(names):
        if column == time_column:
            continue
        values = data[:, column].copy()
        values[~np.isfinite(values)] = np.nan  # Leave gaps for missing values.
        fig, ax = plt.subplots(figsize=(10, 4.5))
        if np.isfinite(values).any():
            ax.plot(time_minutes, values, linewidth=1, marker=".", markersize=2)
        else:
            ax.text(0.5, 0.5, "No valid data (all values missing)",
                    ha="center", va="center", transform=ax.transAxes)
        if time_minutes[-1] > 0:
            ax.set_xlim(0, time_minutes[-1])
        ax.set_xlabel("Time since start (minutes)")
        ax.set_ylabel(labels[column])
        ax.set_title(f"{instruments[column]}: {name}", fontsize=10)
        ax.grid(True, alpha=0.3)
        fig.tight_layout()
        safe_name = "".join(c if c.isalnum() or c in "-_" else "_" for c in name)
        fig.savefig(output_folder / f"{column:02d}_{safe_name}.png", dpi=150)
        if args.show:
            plt.show()  # Close this graph to see the next one.
        plt.close(fig)

    print(f"Saved {len(names) - 1} separate graphs to: {output_folder}")


if __name__ == "__main__":
    main()
