# GPS Clock Experiment

Receiver-side GPS experiment comparing a standard constant-speed-light receiver model against an experimental Newtonian ballistic / emission-theory receiver model.

## Documentation

- `docs/PROJECT.md`: canonical project definition, assumptions, and scope
- `docs/VSL_REFACTOR.md`: architecture notes on keeping CSL and VSL logic structurally separate
- `docs/notes/corrections.md`: current map of which corrections exist on each side of the codebase
- `docs/papers/gps-marmet.md`: Paul Marmet reference text used for Earth-rotation / propagation interpretation
- `todo.md`: pending corrections and investigations

## Repository Layout

- `src/csl`: standard GPS-style constant-speed-light receiver logic
- `src/vsl`: Newtonian ballistic / emission-theory receiver logic
- `src/`: model-neutral infrastructure such as parsing, coordinates, data models, and diagnostics
- `data/`: bundled measurement logs and navigation files
- `output/`: generated diagnostics CSVs

## Running

```bash
uv run python main.py
uv run python main.py --dataset 1
uv run python main.py --dataset 2
```

## Current Intent

The practical goal is to see how closely the VSL receiver can reproduce the behavior of the CSL receiver while changing the receiver-side interpretation of clock and propagation physics.
