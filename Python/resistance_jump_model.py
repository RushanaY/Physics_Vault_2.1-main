"""Calculate a wire-resistance jump from two modelled temperature profiles.

Use one temperature profile for the reference state (for example, discharge
off) and one for the signal state (for example, discharge on).  The function
integrates the local resistance along the wire, so it also works when the
temperature is not uniform.
"""

from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy as np


@dataclass
class ResistanceJumpResult:
    """Numerical results returned by ``calculate_resistance_jump``."""

    mean_temperature_reference_K: float
    mean_temperature_signal_K: float
    mean_temperature_jump_K: float
    resistance_reference_ohm: float
    resistance_signal_ohm: float
    resistance_jump_ohm: float
    relative_jump: float


def spatial_mean_temperature(x_m, temperature_K):
    """Return (1/L) times the integral of T(x) along the wire."""

    x_m = np.asarray(x_m, dtype=float)
    temperature_K = np.asarray(temperature_K, dtype=float)

    if x_m.ndim != 1 or temperature_K.ndim != 1:
        raise ValueError("x_m and temperature_K must be one-dimensional arrays.")
    if x_m.size != temperature_K.size:
        raise ValueError("x_m and temperature_K must have the same length.")
    if x_m.size < 2:
        raise ValueError("At least two position points are required.")
    if np.any(np.diff(x_m) <= 0.0):
        raise ValueError("x_m must be strictly increasing.")
    if not np.all(np.isfinite(temperature_K)):
        raise ValueError("The temperature profile contains NaN or infinity.")

    wire_length_m = x_m[-1] - x_m[0]
    return float(np.trapezoid(temperature_K, x_m) / wire_length_m)


def resistance_from_profile(
    x_m,
    temperature_K,
    resistance_at_reference_ohm,
    alpha_resistivity_per_K,
    reference_temperature_K,
):
    """Calculate total resistance for a linear resistivity-temperature law.

    The model is

        rho(T) = rho_ref * [1 + alpha_R * (T - T_ref)].

    For a uniform wire this gives

        R = R_ref * [1 + alpha_R * (T_mean - T_ref)].

    ``resistance_at_reference_ohm`` should preferably be the measured wire
    resistance when the whole wire is at ``reference_temperature_K``.
    """

    mean_temperature_K = spatial_mean_temperature(x_m, temperature_K)

    resistance_ohm = resistance_at_reference_ohm * (
        1.0
        + alpha_resistivity_per_K
        * (mean_temperature_K - reference_temperature_K)
    )

    return float(resistance_ohm), mean_temperature_K


def calculate_resistance_jump(
    x_reference_m,
    temperature_reference_K,
    x_signal_m,
    temperature_signal_K,
    resistance_at_reference_ohm,
    alpha_resistivity_per_K,
    reference_temperature_K,
):
    """Calculate R_signal - R_reference from two temperature profiles."""

    resistance_reference_ohm, mean_reference_K = resistance_from_profile(
        x_reference_m,
        temperature_reference_K,
        resistance_at_reference_ohm,
        alpha_resistivity_per_K,
        reference_temperature_K,
    )

    resistance_signal_ohm, mean_signal_K = resistance_from_profile(
        x_signal_m,
        temperature_signal_K,
        resistance_at_reference_ohm,
        alpha_resistivity_per_K,
        reference_temperature_K,
    )

    resistance_jump_ohm = resistance_signal_ohm - resistance_reference_ohm
    relative_jump = resistance_jump_ohm / resistance_reference_ohm

    return ResistanceJumpResult(
        mean_temperature_reference_K=mean_reference_K,
        mean_temperature_signal_K=mean_signal_K,
        mean_temperature_jump_K=mean_signal_K - mean_reference_K,
        resistance_reference_ohm=resistance_reference_ohm,
        resistance_signal_ohm=resistance_signal_ohm,
        resistance_jump_ohm=resistance_jump_ohm,
        relative_jump=relative_jump,
    )


def print_resistance_jump(result):
    """Print the most useful resistance-jump quantities."""

    print(f"Mean reference temperature = {result.mean_temperature_reference_K:.6f} K")
    print(f"Mean signal temperature    = {result.mean_temperature_signal_K:.6f} K")
    print(f"Mean temperature jump      = {result.mean_temperature_jump_K:.6f} K")
    print()
    print(f"Reference resistance       = {result.resistance_reference_ohm:.9f} ohm")
    print(f"Signal resistance          = {result.resistance_signal_ohm:.9f} ohm")
    print(f"Resistance jump            = {result.resistance_jump_ohm:.9f} ohm")
    print(f"Resistance jump            = {result.resistance_jump_ohm * 1000.0:.6f} milliohm")
    print(f"Relative resistance jump   = {result.relative_jump * 100.0:.9f} %")
    print(f"Relative resistance jump   = {result.relative_jump * 1.0e6:.3f} ppm")


def plot_temperature_profiles(
    x_reference_m,
    temperature_reference_K,
    x_signal_m,
    temperature_signal_K,
):
    """Plot the reference and signal temperature profiles together."""

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.plot(
        np.asarray(x_reference_m) * 1000.0,
        temperature_reference_K,
        label="Reference state",
        linewidth=2.0,
    )
    ax.plot(
        np.asarray(x_signal_m) * 1000.0,
        temperature_signal_K,
        label="Signal state",
        linewidth=2.0,
    )

    ax.set_xlabel("Position along the wire [mm]")
    ax.set_ylabel("Temperature [K]")
    ax.set_title("Modelled temperature profiles used for the resistance jump")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()
    plt.show(block=True)


# ---------------------------------------------------------------------------
# HOW TO USE THIS WITH YOUR temp_profile FUNCTION
# ---------------------------------------------------------------------------
#
# First change the last line of temp_profile from
#
#     return T_plot, T_mean
#
# to
#
#     return x_plot, T_plot, T_mean
#
# Then, after the temp_profile definition, use for example:
#
#     x_off, T_off, _ = temp_profile(
#         a_diss=0.0,
#         f_v=0.37,
#         d=5.0e-6,
#         p=5.0e-3,
#         I=1.0e-3,
#     )
#
#     x_on, T_on, _ = temp_profile(
#         a_diss=0.05,
#         f_v=0.37,
#         d=5.0e-6,
#         p=5.0e-3,
#         I=1.0e-3,
#     )
#
#     result = calculate_resistance_jump(
#         x_reference_m=x_off,
#         temperature_reference_K=T_off,
#         x_signal_m=x_on,
#         temperature_signal_K=T_on,
#         resistance_at_reference_ohm=107.523,
#         alpha_resistivity_per_K=4.9e-3,
#         reference_temperature_K=293.15,
#     )
#
#     print_resistance_jump(result)
#     plot_temperature_profiles(x_off, T_off, x_on, T_on)

