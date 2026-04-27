# Ballistic GPS Experiment Plan

## Goal

Build and test a working GPS position solver that uses a Newtonian `c+v` propagation model instead of Einsteinian relativistic light-propagation corrections.

The immediate goal is not to prove or disprove a broad worldview. The goal is narrower and operational:

- can a ballistic light model explain the measured GPS pseudoranges well enough to produce accurate, stable position fixes
- can it do so without the explicit relativistic correction terms used in the current standard-style implementation

## Scope

This document defines the first ballistic model we will implement.

First model choice:

- full vector inheritance of source velocity
- Earth-centered inertial frame for propagation
- moving receiver interception during signal flight
- no separate Einsteinian light-propagation correction layered on top

This is intended to be the strongest fair test of a Newtonian ballistic claim in this repository.

## Primary Model Definition

We will model signal propagation in an Earth-centered inertial frame.

At emission time `t_tx`:

- the satellite is at position `r_sat(t_tx)`
- the satellite has velocity `v_sat(t_tx)`
- the emitted signal inherits the satellite velocity vector

Signal velocity in the inertial frame:

`v_sig = c * u_emit + v_sat`

Where:

- `c` is the usual light-speed constant used by the current codebase
- `u_emit` is the unit vector of the emitted ray
- `v_sat` is the satellite velocity vector at emission

The receiver is not treated as stationary during flight. It moves with the rotating Earth, so the arrival condition is an interception problem:

`r_sat(t_tx) + v_sig * (t_rx - t_tx) = r_rcv(t_rx)`

This means the ballistic model includes both:

- source-velocity inheritance
- receiver motion during propagation

without treating them as unrelated add-on corrections.

## Why This Model

This is the most pragmatic starting point for a ballistic GPS receiver because:

- it is a single coherent Newtonian kinematic model
- it gives the ballistic claim its strongest practical form
- it avoids mixing a ballistic propagation law with standard constant-`c` travel-time assumptions
- it naturally includes Earth rotation through receiver motion rather than through a separate interpretive correction

## What We Already Know

We already tested the Marmet-style Earth-rotation interpretation in another branch.

Working assumption for this branch:

- Marmet-style treatment is operationally very close to standard Sagnac handling
- the main new question is not whether Marmet can be reproduced
- the main new question is whether a stronger ballistic `c+v` propagation law can still produce a working GPS fix

## Fair-Test Principles

To avoid misrepresenting the ballistic claim:

- do not keep standard constant-`c` propagation and then merely bolt on extra source and receiver corrections
- do not double-count Earth-rotation effects
- do not compare the ballistic model to a deliberately broken baseline
- do not change unrelated parts of the solver while testing propagation

The ballistic model should stand or fall on a clean propagation law, not on unrelated implementation changes.

## What Stays Fixed Initially

These parts should remain unchanged in the first implementation unless there is a concrete ballistic reason to replace them:

- GNSS logger parser
- RINEX navigation parser
- ephemeris selection logic
- weighted least squares solve structure
- residual filtering and outlier rejection
- broadcast orbit model used to compute satellite position from ephemeris
- satellite clock polynomial terms `af0`, `af1`, `af2`
- group delay term `tgd`

Reason:

- the first ballistic experiment should isolate the propagation law, not rewrite the whole receiver

## What Changes In The First Ballistic Experiment

### 1. Remove the explicit relativistic eccentricity clock term

Current code includes the ICD / Google clock correction term:

`F * e * sqrt(A) * sin(E)`

In this repository this is controlled by `enable_relativity` in `gnss_physics.py`.

For the ballistic model, this term should be disabled.

### 2. Replace constant-c transmit-time backsolve

Current code estimates transmit time using:

- `pseudorange / c`

This is a standard constant-light-speed assumption and must be replaced for the ballistic model.

### 3. Replace standard light-time / Sagnac-style propagation handling

Current code also includes Earth-rotation handling in the satellite-position calculation through the usual broadcast-orbit longitude correction term.

For the ballistic model, we need to ensure we are not:

- keeping the standard propagation correction active
- and then adding a ballistic propagation model on top of it

The final ballistic path should use one propagation model, not two overlapping ones.

## Code Areas Affected

The main touchpoints in the current code are:

- `gnss_physics.py`
  - `calculate_clock_correction()`
  - `calculate_corrected_transmit_tow_and_week()`
  - `_calculate_satellite_position()`
  - `calculate_satellite_position()`
- `gnss_solver.py`
  - `_compute_residuals()`
  - predicted pseudorange construction
- `main.py`
  - experiment wiring and comparison output

We should likely introduce an explicit propagation mode abstraction so the standard and ballistic models can be run side by side.

## Proposed Refactor

Add an explicit propagation-mode decision point.

The current `enable_relativity` switch is still useful, but its scope is too narrow to serve as the main physics control for this experiment.

Historically it only controlled the explicit satellite clock eccentricity correction:

- `F * e * sqrt(A) * sin(E)`

The current CSL-vs-VSL architecture no longer treats this as a separate runtime ablation mode.

Recommended structural redesign:

- separate `clock model` from `propagation model`
- keep the existing relativity toggle in spirit, but rename or wrap it so its meaning is precise
- pass a single explicit model configuration into the solver

Suggested shape:

- `CSL/STANDARD`
- `VSL/FULL_VECTOR`

Suggested implementation shape:

- `calculate_clock_correction()` should depend on the selected clock model
- transmit-time and flight-time solving should depend on the selected propagation model
- `WeightedLeastSquaresSolver` should accept a single model configuration rather than a standalone boolean

This matters because the ballistic experiment is broader than one clock-term toggle. It changes the propagation law itself, so the code should make that distinction explicit.

Suggested modes:

- `standard`
- `ballistic_full_vector`

Possible later modes:

- `ballistic_los_projected`
- `receiver_motion_only`
- `source_velocity_only`
- `no_earth_rotation` as a control

The standard mode must reproduce current results as closely as possible.

## Ballistic Solve Strategy

For each observation:

1. Start with an initial estimate of receive time and user state.
2. Use ephemeris to compute satellite position and velocity near candidate transmit time.
3. Solve for emission direction and flight time under:
   `r_sat(t_tx) + (c * u_emit + v_sat(t_tx)) * dt = r_rcv(t_rx)`
4. Use the resulting ballistic flight time to connect transmit and receive geometry.
5. Build the predicted pseudorange from the ballistic interception solution, satellite clock terms, and receiver clock bias.

This may require an inner iteration loop inside each observation model evaluation.

## Initial Simplifying Assumptions

To keep the first version tractable:

- use the existing broadcast orbit equations for satellite state
- approximate receiver inertial motion from Earth rotation during signal flight
- keep the existing least-squares framework
- accept a first-order iterative solution if it converges robustly

We do not need the perfect final form in the first pass. We need a coherent, testable one.

## Evaluation Criteria

The ballistic model should be compared against the current standard model using the same data and solver framework.

Primary metrics:

- epochs solved
- mean residual RMS
- median residual RMS
- 95th percentile residual RMS
- mean position delta versus standard
- mean clock-bias delta versus standard

If truth reference is available:

- mean position error versus known or logged reference position

## Diagnostics To Add

Per observation:

- epoch index
- receiver TOW
- propagation mode
- satellite ID
- residual
- predicted pseudorange
- geometric range equivalent
- ballistic flight time
- source velocity magnitude
- source velocity projected on line of sight
- receiver rotational velocity projected on line of sight

Per epoch:

- mode
- solved XYZ
- solved clock bias
- number of satellites used
- residual RMS

## Interpretation Standard

The correct operational question is:

- given the same measurements, can a Newtonian ballistic propagation model produce GPS fixes as well as or better than the current standard model

This experiment does not need to settle every philosophical claim about relativity. It only needs to answer whether the ballistic model works on actual GPS measurements.

## Development Order

1. Reintroduce a propagation-mode abstraction.
2. Preserve current standard behavior exactly.
3. Separate explicit relativity toggle from propagation-mode selection.
4. Implement ballistic full-vector propagation in the observation model.
5. Disable the explicit relativistic eccentricity term for the ballistic run.
6. Ensure no standard propagation correction is being double-counted.
7. Add CSV diagnostics for side-by-side comparison.
8. Compare standard versus ballistic on the existing dataset.
9. Repeat on additional datasets.

## Success And Failure Conditions

Evidence the ballistic model is operationally promising:

- it solves most or all epochs
- residual RMS is comparable to or better than standard
- positions remain stable across epochs
- there is no hidden reliance on the removed relativistic term

Evidence against the ballistic model in this codebase:

- it fails to converge reliably
- residual RMS is consistently worse than standard
- solved positions are unstable or biased
- it only works after quietly reintroducing equivalent standard light-time corrections

## Immediate Next Step

Implement a propagation-mode refactor that preserves the current standard path exactly, then add a first-pass `ballistic_full_vector` observation model using inertial-frame signal inheritance and moving-receiver interception.
