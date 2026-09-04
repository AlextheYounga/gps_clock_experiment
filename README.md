# GPS Clock Experiment

This repository compares two receiver-side models against the same recorded GPS measurements:

- **CSL:** a conventional constant-speed-of-light GPS receiver model
- **VSL:** an experimental ballistic or emission-theory model in which a signal inherits the velocity of its emitting satellite

The project asks a limited, testable question: can the experimental VSL receiver reproduce GPS measurements and position solutions as well as the conventional CSL receiver when both use the same observations and broadcast navigation data?

This is a numerical experiment, not proof of either physical theory. Its results are constrained by the quality of the recorded phone measurements, the assumptions described below, and the small number of available datasets.

## GPS Receiver Basics

A GPS satellite broadcasts its transmission time and orbital data. A receiver compares the transmitted time with its reception time to estimate a **pseudorange**, which is a signal travel-time measurement expressed in metres.

At least four satellites are normally required to solve four unknowns:

- receiver position `x`, `y`, and `z`
- receiver clock bias

This project requires at least five satellites when evaluating fit quality. With only four observations, four unknowns can be fit exactly and produce a misleading zero residual even when the underlying model is poor.

Both receivers use weighted least squares to find the position and clock bias that best reproduce the measured pseudoranges. Their main difference is how they model signal propagation and satellite clock effects.

## Models

### Constant-Speed-Light Model

The CSL implementation in `src/csl/` follows conventional GPS receiver equations derived from the Google GPS Measurement Tools implementation.

Its predicted pseudorange is based on geometric distance divided by the conventional constant speed of light. It includes:

- broadcast polynomial satellite clock terms `af0`, `af1`, `af2`, and `tgd`
- the standard relativistic periodic eccentricity clock correction
- standard Earth-rotation, or Sagnac-style, handling in the satellite orbit longitude
- broadcast Keplerian orbit reconstruction

CSL is the operational baseline for the experiment.

### Ballistic Emission Model

The VSL implementation in `src/vsl/` treats the signal like a projectile emitted by a moving source. In the selected Earth-centered inertial propagation frame, its velocity is modeled as:

```text
v_signal = c_emit * u_emit + v_satellite_inertial
```

where:

- `c_emit` is the nominal emission speed relative to the source
- `u_emit` is the emission-direction unit vector
- `v_satellite_inertial` is the satellite velocity in the propagation frame

The name VSL refers to the resulting signal speed being direction- and source-velocity-dependent in the propagation frame. It does not mean that the nominal source-relative emission value is absent. The code names this reference value `EMISSION_SPEED_MPS` to distinguish it from a universal observer-independent propagation claim.

For each observation, VSL jointly iterates:

1. signal transmit time
2. satellite clock correction
3. satellite position and velocity at transmission
4. receiver movement during signal flight
5. gravity-adjusted nominal propagation speed
6. ballistic interception time

The fixed-geometry interception equation is:

```text
|r_receiver - r_satellite - v_satellite_inertial * dt|^2
    = c_effective^2 * dt^2
```

The VSL solver uses a numerical Jacobian of this complete prediction rather than applying the CSL geometric Jacobian to a different propagation law.

## Coordinate Frames And Earth Rotation

GPS broadcast positions are expressed in the Earth-Centered, Earth-Fixed coordinate system, or **ECEF**. ECEF rotates with Earth. A velocity measured in ECEF describes motion across a map attached to the rotating planet; it is not the same as velocity in a nonrotating Earth-centered frame.

The VSL ballistic law requires all positions and velocities in its interception equation to use one consistent frame. The implementation uses axes aligned with ECEF at signal transmission but treated as nonrotating during the short signal flight.

Satellite velocity is converted from ECEF to this inertial basis using:

```text
v_satellite_inertial = v_satellite_ecef + omega_Earth x r_satellite
```

Earth rotation is then accounted for in two complementary operations:

- the receiver position is rotated forward by Earth’s rotation during signal flight;
- the `omega_Earth x r_satellite` component is restored to the satellite velocity so it is expressed in the same inertial basis.

These are coordinate-frame operations on two different objects, not duplicate corrections. VSL does not additionally apply CSL’s Sagnac orbit-longitude term, because doing so would risk counting Earth rotation twice.

The current datasets show an average satellite frame-rotation vector magnitude of roughly `1.5-1.6 km/s`. A receiver on Earth has a smaller rotational velocity determined by its latitude and distance from Earth’s rotation axis.

## Clock Assumptions

Both models retain the broadcast polynomial clock terms because the experiment consumes data from the existing GPS satellite system.

They differ in their periodic eccentricity clock treatment:

| Model | Periodic clock treatment |
| --- | --- |
| CSL | Uses the full standard term `F * e * sqrt(A) * sin(E)`, conventionally interpreted as the combined gravitational-potential and orbital-speed effect. |
| VSL | Applies no independent periodic eccentricity clock correction. |

The VSL clock choice is the strict Newtonian baseline for this experiment: broadcast polynomial terms remain as empirical satellite-clock calibration inputs, while eccentricity affects the Keplerian orbit, satellite velocity, and ballistic propagation but does not directly alter the clock rate. The experimental gravity-on-propagation assumption remains separate from the clock model.

The large mean satellite clock-rate offset is handled operationally by the GPS space and control segments. This receiver experiment applies the broadcast clock products without adding a VSL-specific periodic eccentricity clock term.

## Gravity And Signal Propagation

VSL also includes experimental signal-domain effects from Earth's gravitational potential. The first slightly reduces signal propagation speed using the average Newtonian potential at the satellite and receiver endpoints:

```text
phi(r) = -GM / r
c_effective = c_emit * (1 + phi_average / c_emit^2)
```

For the current GPS geometry, this changes effective speed by approximately `-0.129 m/s`, corresponding to about `0.009 m` of range over a representative path. This centimetre-scale effect is far below the noise level of the available measurements and therefore cannot be validated by the current datasets.

Separately, VSL applies an eccentricity-dependent signal frequency/time shift derived directly from the satellite's changing Newtonian potential. This is applied to predicted pseudorange, not to the satellite clock. Across the current datasets this shift averages about `±7 ns`, equivalent to roughly `2 m` of range. The VSL model therefore retains Newtonian gravity effects on propagation and signal energy/frequency while applying no gravitational clock-rate correction.

## Experiment Design

The repository contains two short Android GNSS Logger recordings and matching RINEX navigation files. Each epoch is independently solved by CSL and VSL.

To avoid misleading comparisons:

- each solver requires at least five satellites;
- CSL/VSL RMS differences are calculated only when both models retain the same satellite IDs;
- exactly determined four-satellite solutions are excluded;
- the logged phone position is treated as a coarse reference, not survey truth.

Generated reports include:

- solved epochs
- mean pseudorange residual RMS
- RMS change between models on shared-satellite epochs
- number of epochs where VSL has higher RMS
- position difference between models
- position error relative to the coarse phone fix
- average magnitudes of clock, Earth-rotation, frame, and gravity terms
- per-epoch and per-observation CSV diagnostics

## Current Results

These results were generated after making the VSL coordinate frame internally consistent, correcting dataset 2 to GPS week `1911`, and replacing the VSL periodic eccentricity clock term with a gravity-based signal frequency/energy shift applied to predicted pseudorange.

| Dataset | CSL mean RMS | VSL mean RMS | Mean VSL-CSL RMS on shared epochs | Shared epochs | VSL worse epochs |
| --- | ---: | ---: | ---: | ---: | ---: |
| 2016-06-30 | `157.837 m` | `158.880 m` | `+1.019 m` | 221 | 151 |
| 2016-08-22 | `92.662 m` | `97.907 m` | `+5.246 m` | 198 | 138 |

Lower residual RMS indicates a closer fit to the pseudorange measurements. Both datasets currently favor CSL, although the size and quality of the datasets do not support a decisive physical conclusion.

The RMS gap is small compared with the absolute residuals: VSL is about `0.66%` worse than CSL on the first dataset and `5.66%` worse on the second. Relocating the half-size periodic term from the satellite clock to the signal restored nearly all of the fit quality lost by its removal, but this does not change the overall conclusion. This is a relative fit-quality comparison, not a percentage difference between the solved positions. Both models are fitting noisy measurements with residuals of roughly `90–160 m` RMS.

### Result Progression

The half-size periodic eccentricity term was tested in three VSL configurations to see where it belongs:

| VSL configuration | 2016-06-30 | 2016-08-22 |
| --- | ---: | ---: |
| A. Gravity-only clock term (initial hybrid) | `+1.009 m` RMS delta, 149/220 worse | `+5.381 m` RMS delta, 140/199 worse |
| B. No periodic term (strict Newtonian clock) | `+2.714 m` RMS delta, 206/222 worse | `+6.622 m` RMS delta, 150/197 worse |
| C. Gravity signal frequency/energy shift on predicted pseudorange (current) | `+1.019 m` RMS delta, 151/221 worse | `+5.246 m` RMS delta, 138/198 worse |

Removing the term entirely (A to B) cost roughly `1.7 m` and `1.2 m` of fit quality and sharply increased the number of worse epochs. Restoring the identical magnitude as a signal-domain shift (B to C) recovered the fit to within `0.01 m` and `0.14 m` of the clock-based configuration, on slightly different shared-epoch sets.

The near-identical residuals are expected rather than surprising. The new term is numerically half of the standard periodic eccentricity correction, and in a pseudorange residual it enters the same way whether it is applied to the satellite clock or to the received signal. The current data therefore cannot distinguish where the half-size eccentricity term belongs — satellite clock rate versus signal frequency — because both placements produce essentially the same predicted pseudoranges. Resolving that question requires better measurements or an independent observable, not receiver residuals alone.

Despite their similar residual RMS values, the independently solved CSL and VSL positions differ by approximately `60–70 m` on average. This is possible because the two propagation models predict different satellite ranges, while the least-squares solver can trade position against receiver clock bias. With measurement errors already this large, both models can fit the data almost equally poorly while settling on noticeably different positions. The available data therefore cannot resolve whether that position difference comes from the propagation model or from measurement and modeling error.

The phone fix is not accurate or independent enough to determine which model’s position is closer to physical truth.

## Limitations

- Pseudoranges are reconstructed using a shared `70 ms` travel-time offset in `src/measurement_parser.py`. The common portion is largely absorbed by receiver clock bias, but large residuals show substantial remaining measurement-model error.
- The reconstructed phone pseudoranges are the dominant limitation of the current comparison. Their `90–160 m` residual RMS is much larger than the centimetre-scale gravity propagation effect and can conceal meaningful differences between propagation models.
- Atmospheric delay, multipath, handset clock behavior, antenna effects, and other GPS error sources are not modeled comprehensively.
- The datasets are short recordings from one phone and one location.
- No surveyed or RTK-grade reference position is available.
- Consecutive one-second epochs are correlated and should not be treated as independent experiments.
- The broadcast clock and orbit products come from the operational GPS system and cannot independently test every space-segment assumption.
- The gravity-on-propagation term is orders of magnitude smaller than the measurement residuals.

The current evidence shows that both implementations can solve real recorded measurements and that CSL fits these measurements better under the present setup. It does not establish that ballistic propagation is impossible, nor does it validate the additional VSL gravity assumptions.

## Requirements

- Python 3.12 or newer
- [uv](https://docs.astral.sh/uv/)

Install dependencies and run both datasets:

```bash
uv sync
uv run python main.py
```

Run one dataset:

```bash
uv run python main.py --dataset 1
uv run python main.py --dataset 2
```

Run regression tests and lint checks:

```bash
uv run python -m unittest discover -s tests -v
uv run ruff check .
```

Diagnostic CSV files are written to `output/`.

## Repository Layout

- `src/csl/`: conventional GPS receiver model
- `src/vsl/`: experimental ballistic receiver model
- `src/csl/corrections.py`: explicit CSL correction formulas
- `src/vsl/corrections.py`: explicit VSL correction and frame-conversion formulas
- `src/`: shared parsing, coordinates, data models, and diagnostics
- `data/`: bundled GNSS logs and broadcast navigation files
- `output/`: generated diagnostic CSV files
- `tests/`: focused regression tests

## Further Documentation

- `docs/PROJECT.md`: detailed project scope and assumptions
- `docs/BALLISTIC_GPS_PLAN.md`: original ballistic-model design
- `docs/VSL_REFACTOR.md`: CSL/VSL package-separation architecture
- `docs/notes/corrections.md`: side-by-side correction map
- `docs/papers/gps-marmet.md`: Paul Marmet reference text used when considering alternative Earth-rotation interpretations
- `docs/references/gps-measurment-tools.md`: archived Google GPS Measurement Tools source reference
- `docs/todo.md`: open investigations
