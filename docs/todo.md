# Documentation And Model TODO

## Correct

- [x] Remove `NO_RELATIVISTIC_ECCENTRICITY` from the intended architecture and top-level project narrative.
- [x] Keep the repo framed as `CSL` versus `VSL`, not a three-mode comparison.
- [ ] Standardize VSL terminology so names communicate physical meaning and do not silently import CSL assumptions.
- [ ] Audit VSL uses of `c` and rename or document them as emission-speed or reference-conversion quantities where appropriate.
- [ ] Keep `corrections.py` as the main lever point for VSL physics changes and document that role clearly in code.
- [x] Update diagnostics wording where needed so CSL remains the operational benchmark without sounding like the only meaningful model.

## Investigate

- [ ] Reconcile VSL Earth-rotation handling between the ballistic propagation solve and the H-matrix geometry used by the solver.
- [ ] Compare the current VSL Earth-rotation treatment directly against the intended Paul Marmet interpretation and identify the exact mathematical differences.
- [ ] Investigate the current VSL velocity-frame assumptions and determine whether propagation is consistently treating velocities in ECEF, inertial, or a mixed frame.
- [ ] Clarify the logic behind the current VSL clock and velocity interpretation so the inertial-versus-ECEF question is no longer ambiguous.
- [ ] Determine whether the current VSL propagation bootstrap can avoid implying a fixed constant-light-speed assumption more than necessary.
- [ ] Decide whether any remaining shared constants should be renamed or wrapped differently on the VSL side for clarity.

## Scope Reminders

- [ ] This repository only changes receiver-side interpretation logic.
- [ ] The project does not currently simulate an alternative satellite system.
- [ ] Real GPS data and the CSL receiver remain the available baseline for comparison in this repo.
