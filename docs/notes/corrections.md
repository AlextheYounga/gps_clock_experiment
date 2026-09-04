# CSL vs VSL Corrections in Current Code

This document compares items present on the CSL side of the current codebase with the corresponding VSL / Newtonian-ballistic status in the current code. It is intentionally limited to implemented code paths, not every correction used in full GPS literature.

| CSL-side item in current code | VSL status in current code |
| --- | --- |
| Relativistic eccentricity clock term in `src/csl/clock.py`: `F * e * sqrt(A) * sin(E)` | Reinterpreted in `src/vsl/clock.py` as a gravity-only periodic clock term. The VSL side intentionally omits the speed-based part of the standard relativistic interpretation. |
| Earth-rotation / Sagnac-style orbit longitude term in `src/csl/orbit.py`: `- OMEGA_E_DOT_RAD_S * (toe + user_sat_range / c)` | Replaced by moving-receiver interception in `src/vsl/propagation.py`. Satellite velocity is converted from ECEF to the same transmit-time inertial basis with `v_inertial = v_ecef + omega_Earth x r_sat`, and the VSL solver uses a numerical Jacobian of that full propagation model. No separate Sagnac orbit term is added. |
| Polynomial satellite clock correction in `src/csl/clock.py`: `af0`, `af1`, `af2`, `tgd` | Shared in both models. Implemented in `src/vsl/clock.py`. Not a relativistic correction. |
| Broadcast orbit model / Kepler solution in `src/csl/orbit.py` | Shared in both models as the base orbit geometry. Implemented in `src/vsl/orbit.py`. Not a relativistic correction. |
| Constant-`c` geometric pseudorange prediction in `src/csl/observation_model.py` | Replaced by ballistic full-vector propagation in `src/vsl/propagation.py`, with predicted pseudorange still expressed in metres through an emission-speed reference quantity. This is a propagation-law replacement, not a direct Newtonian equivalent of the CSL assumption set. |

## Interpretation

- The only clearly relativistic correction present on the CSL side of the current repo is the eccentricity clock term as interpreted by the standard model.
- On the VSL side, that periodic term is not deleted outright. It is being reinterpreted as a gravity-based clock effect while rejecting the idea that orbital speed itself slows the clock.
- The other major CSL/VSL difference is Earth-rotation handling: CSL uses the standard orbit longitude correction, while VSL handles Earth rotation through moving-receiver interception and a frame-consistent inertial satellite velocity.
- Polynomial clock terms and broadcast orbit equations are shared receiver inputs in this repo, not proof that both models share the same physical interpretation.
