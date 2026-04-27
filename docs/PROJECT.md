# GPS Receiver Experiment

## Goal

This repository is a receiver-side GPS experiment.

The project compares two interpretations of the same measurement data:

- `src/csl`: the standard GPS-style constant-speed-light receiver model
- `src/vsl`: a Newtonian ballistic / emission-theory receiver model

The immediate goal is not to redesign GPS as a full satellite system. The goal is to determine how closely a receiver built on VSL / Newtonian logic can reproduce the behavior of the standard CSL receiver when both are fed the same real-world GPS measurements and broadcast navigation data.

## Scope

This repository is only about the receiver.

Within scope:

- parsing logged GNSS measurements
- parsing broadcast ephemerides
- satellite clock interpretation at the receiver
- transmit-time inference
- propagation modeling
- pseudorange prediction
- weighted least-squares position solving
- diagnostics comparing VSL output against CSL output

Outside scope:

- changing the actual satellite clocks
- changing the transmitted broadcast ephemerides
- re-flying the GPS constellation under a different physics model
- producing independent "true north" or survey-truth orbital data
- proving a complete alternative space-segment design

The receiver must work with the data available in this repository. That means CSL remains the practical comparison baseline, even when the experiment is trying to reinterpret the measurements with VSL logic.

## Current Model Split

### `src/csl`

`src/csl` contains the standard GPS-style receiver model derived from the Google GPS Measurement Tools implementation.

This side of the repo is the baseline reference.

### `src/vsl`

`src/vsl` contains the experimental Newtonian / ballistic receiver model.

This side of the repo is intended to evolve independently from CSL wherever the receiver logic depends on physics assumptions, especially in:

- clock interpretation
- signal propagation
- Earth-rotation handling
- predicted pseudorange construction
- solver linearization inputs

## VSL Assumptions

The VSL model in this repository should be understood with the following working assumptions.

### 1. Light is treated ballistically

For intuition, treat emitted light like a projectile or bullet fired from a moving source.

The emitted signal inherits source motion and propagates as a physical object in flight. This is the key intuition behind the receiver-side VSL model.

### 2. Gravity may affect clock rate

This project does not assume that clock rate is immune to physical conditions.

The working Newtonian intuition is that clock machinery can be affected by its environment. Temperature can affect a clock. Gravity may also affect a clock. Under this interpretation, clocks in space may run differently because they are under different gravitational conditions.

For that reason, the VSL side of this project currently allows a gravity-based clock-rate effect.

### 3. Speed is not assumed to slow time

The VSL side of this project intentionally rejects the assumption that velocity itself slows the passage of time.

We do not want to assume that the speed of an object directly slows its clock rate. In particular, the VSL model should not smuggle in the idea that orbital speed itself produces time slowing.

This is why the VSL clock interpretation keeps a gravity-based contribution while intentionally omitting the speed-based part of the standard relativistic eccentricity logic.

### 4. Gravity may affect propagation speed

The VSL model also assumes that gravity can affect propagation speed in flight.

This is not a separate philosophical track from the ballistic interpretation. In this project, both are part of the same Newtonian-style picture: emitted objects propagate physically and can be influenced by gravitational conditions during flight.

## What VSL Rejects

The VSL side of the repository is intended to reject these assumptions as first principles:

- that light must propagate with invariant speed in all receiver interpretations
- that orbital speed itself slows clock rate
- that standard relativistic timing language should be carried into the VSL model unchanged
- that receiver-side Earth-rotation handling must default to the standard CSL interpretation

## What VSL Retains

Some pieces of standard GPS infrastructure are still used because this repository is only a receiver experiment working from real GPS data.

These are treated as inputs or practical baseline infrastructure, not endorsements of every physical interpretation behind them.

Examples:

- broadcast ephemeris parsing
- broadcast polynomial clock terms
- Kepler-based orbit reconstruction as the starting orbit description
- standard dataset formats and logging conventions
- comparison against CSL outputs

The important line is this:

- shared parsing and data inputs are acceptable
- receiver-side interpretation logic is where the experiment changes the physics assumptions

## Marmet Relationship

The current VSL direction is partly motivated by Paul Marmet's GPS / light-propagation interpretation.

Reference:

- `docs/papers/gps-marmet.md`

In particular, the project is interested in whether Earth-rotation handling usually treated as a standard Sagnac-style correction can be reinterpreted in a Newtonian ballistic framework.

## Terminology

The project should be careful with names involving `c`.

### CSL terminology

On the CSL side, `SPEED_OF_LIGHT_MPS` is the standard constant-speed-light reference value used by the conventional model.

### VSL terminology

On the VSL side, names should prefer explicit physical meaning.

Examples:

- `EMISSION_SPEED_MPS`
- `gravity_adjusted_emission_speed_mps(...)`

If a constant is being used only as a reference conversion factor or initial bootstrap quantity, that should be stated clearly in code and docs so it is not mistaken for a hidden CSL assumption.

## Architecture Guidance

The intended package split is:

- `src/`: only model-neutral infrastructure
- `src/csl/`: standard GPS-style receiver logic
- `src/vsl/`: Newtonian ballistic receiver logic

`src/` should contain only things that are genuinely safe to share, such as:

- data models
- file parsing
- coordinate transforms
- ephemeris selection
- reporting and diagnostics

Anything that computes or interprets physics should live in either `csl` or `vsl`, not in shared modules.

## Comparison Philosophy

The experiment currently compares VSL output against CSL output because that is the strongest available baseline in this repository.

That does not mean CSL is treated as ultimate truth in a philosophical sense. It means CSL is the operational benchmark available from the current data, code lineage, and published GPS receiver practice.

The current practical question is:

- can the VSL receiver approach the standard CSL receiver closely enough to remain a serious alternative interpretation of the same measurements?

## Documentation Map

- `README.md`: documentation index and quick start
- `docs/PROJECT.md`: canonical project definition and scope
- `docs/VSL_REFACTOR.md`: package-separation and architecture notes
- `docs/notes/corrections.md`: current correction mapping between CSL and VSL
- `docs/papers/gps-marmet.md`: Marmet reference text
- `docs/references/gps-measurment-tools.md`: Original Google GPS source code extracted to Markdown using code2prompt. (Search this cautiously, big file)
- `todo.md`: corrections and investigations still pending
