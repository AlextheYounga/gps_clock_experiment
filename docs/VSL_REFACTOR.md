# VSL Refactor Plan

## Goal

Refactor the repository so the constant-speed-light implementation and the variable-speed-light implementation are structurally separated.

The main purpose of this refactor is to prevent shared code from silently carrying constant-light-speed assumptions into the VSL / ballistic pipeline.

## Design Principle

Only code that is genuinely model-neutral should remain under `src/`.

Anything that encodes a physics assumption about:

- signal propagation
- transmit-time solving
- satellite clock interpretation
- predicted pseudorange construction
- solver linearization based on a model-specific observation equation

should live in either `csl/` or `vsl/`, not in `src/`.

## Current Problem

The current `src/` package mixes:

- shared parsing and datamodels
- standard GPS-style constant-light-speed logic
- experimental ballistic logic

This creates a high risk of hybrid behavior, where VSL code still depends on helpers built around standard constant-`c` assumptions.

The largest risk areas are:

- `src/gnss_physics.py`
- `src/gnss_solver.py`

because both currently contain branched logic for multiple physics models.

## Refactor Target

Target package layout:

```text
main.py

src/
  __init__.py
  constants.py
  models.py
  coordinates.py
  nav_parser.py
  measurement_parser.py
  ephemeris_selection.py
  diagnostics.py

csl/
  __init__.py
  config.py
  clock.py
  orbit.py
  propagation.py
  observation_model.py
  solver.py

vsl/
  __init__.py
  config.py
  clock.py
  orbit.py
  propagation.py
  observation_model.py
  solver.py
```

## Ownership Rules

### `src/`

`src/` should contain only model-neutral infrastructure.

Allowed in `src/`:

- dataclasses for parsed measurements and ephemerides
- file parsing
- coordinate transforms
- ephemeris selection helpers
- reporting and diagnostics utilities
- constants that are purely geometric, calendar, or file-format related

Not allowed in `src/`:

- pseudorange prediction logic
- transmit-time backsolve logic
- ballistic propagation logic
- standard Sagnac / light-time logic
- clock correction logic that depends on the chosen physics model
- a single solver class that branches between CSL and VSL

### `csl/`

`csl/` owns the standard GPS-style model.

It should contain:

- standard satellite clock correction
- standard transmit-time solving
- standard orbit / light-time handling
- standard pseudorange prediction
- solver using only CSL observation equations

### `vsl/`

`vsl/` owns the Newtonian ballistic model.

It should contain:

- VSL / ballistic clock interpretation
- VSL propagation solve
- moving-receiver interception logic
- VSL pseudorange prediction
- solver using only VSL observation equations

## Module Mapping From Current Code

### Current `src/gnss_parser.py`

Split into:

- `src/models.py`
- `src/nav_parser.py`
- `src/measurement_parser.py`

Move these dataclasses into `src/models.py`:

- `SatelliteObservation`
- `EpochMeasurements`
- `FixRecord`
- `Ephemeris`

### Current `src/gnss_physics.py`

This file should not remain as a mixed shared module.

Split responsibilities into:

- `csl/clock.py`
- `csl/orbit.py`
- `csl/propagation.py`
- `vsl/clock.py`
- `vsl/orbit.py`
- `vsl/propagation.py`

Functions that should become model-specific:

- `calculate_clock_correction()`
- `calculate_corrected_transmit_tow_and_week()`
- `calculate_satellite_position()`
- `_calculate_satellite_state_at_tow()`
- `compute_ballistic_predicted_pseudorange()`

### Current `src/gnss_solver.py`

This file should not remain as a single solver with internal mode branching.

Split responsibilities into:

- `src/ephemeris_selection.py`
- `csl/observation_model.py`
- `csl/solver.py`
- `vsl/observation_model.py`
- `vsl/solver.py`

The current `_select_ephemeris()` helper is a good candidate for `src/ephemeris_selection.py`.

The current `_geometry_matrix()` can either:

- remain duplicated in both solvers for maximum separation, or
- move to a small shared numerical helper if it stays purely geometric

The safer first step is duplication, not sharing.

### Current `src/gnss_types.py`

This should no longer be the central control point for mixed physics models.

Instead:

- `csl/config.py` should define CSL configuration presets
- `vsl/config.py` should define VSL configuration presets

If a tiny shared config protocol becomes useful later, it can be added, but the first refactor should prefer explicit separation.

## Proposed Shared Modules

### `src/constants.py`

Put only constants here that are safely shared.

Examples:

- GPS week length
- WGS84 ellipsoid constants
- Earth rotation rate if treated as a physical Earth constant
- Earth gravitational parameter if treated as shared orbit input

Open question:

- whether nominal `c = 299792458.0` should remain in `src/constants.py` as a reporting/unit constant, or be defined separately in `csl/` and `vsl/` to avoid ambiguity

For now, this should stay an explicit design decision rather than an accidental default.

### `src/coordinates.py`

Good candidates:

- `lla_to_ecef()`
- Euclidean distance helpers
- future ECEF / ECI transforms

### `src/diagnostics.py`

Good candidates:

- CSV writers
- summary formatting helpers
- per-epoch reporting

## Why Separate Solvers

This is the most important architectural choice.

We should not keep one solver class with branches like:

- if standard do this
- if ballistic do that

That structure makes it too easy for:

- standard timing assumptions
- standard geometry linearization
- standard transmit-time helpers

to leak into the VSL path.

Instead, we should have:

- `csl.solver.WeightedLeastSquaresSolver`
- `vsl.solver.WeightedLeastSquaresSolver`

These may share numerical style, but they should not share physics helpers unless we are certain they are assumption-free.

## Safe Sharing Rule

When deciding whether code belongs in `src/` or a model package, use this rule:

- if it parses, formats, or transforms coordinates, it is probably safe to share
- if it computes transmit time, predicted pseudorange, clock correction, or observation residuals, it is probably model-specific

More specific rule:

- if a function uses pseudorange to infer transmit time, treat it as model-specific
- if a function computes predicted pseudorange, treat it as model-specific
- if a function contains a light-time or propagation formula, treat it as model-specific

## Entry Point Shape After Refactor

`main.py` should become an experiment orchestrator that imports explicit model packages.

Example:

```python
from csl.solver import WeightedLeastSquaresSolver as CslSolver
from vsl.solver import WeightedLeastSquaresSolver as VslSolver
```

Or more explicitly:

```python
from csl.config import STANDARD_CONFIG, NO_RELATIVITY_CONFIG
from vsl.config import BALLISTIC_FULL_VECTOR_CONFIG
```

This keeps the comparison logic clear and prevents `main.py` from relying on hybrid shared internals.

## Migration Order

Recommended order:

1. Extract shared dataclasses from `src/gnss_parser.py` into `src/models.py`.
2. Split parsing into `src/nav_parser.py` and `src/measurement_parser.py`.
3. Extract shared coordinate helpers into `src/coordinates.py`.
4. Extract ephemeris selection into `src/ephemeris_selection.py`.
5. Create `csl/` and move the current standard path into it first.
6. Update `main.py` to use `csl/` from the new package layout.
7. Create `vsl/` and move the ballistic path into it.
8. Remove model-branching from the shared code.
9. Delete or retire the old mixed modules once the new paths are stable.

## First Refactor Success Criteria

The refactor is successful when:

- `src/` contains no hidden CSL or VSL propagation logic
- the CSL path reproduces the current standard results
- the VSL path can evolve independently without reusing mixed helpers
- `main.py` compares explicit model packages rather than internal branches

## Immediate Next Step

Start by extracting `src/models.py` and splitting `src/gnss_parser.py`, because that is the cleanest low-risk first move and gives both `csl/` and `vsl/` a neutral shared foundation.
