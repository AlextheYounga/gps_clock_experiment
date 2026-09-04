# CSL vs VSL Corrections in Current Code

This document compares items present on the CSL side of the current codebase with the corresponding VSL / Newtonian-ballistic status in the current code. It is intentionally limited to implemented code paths, not every correction used in full GPS literature.

| CSL-side item in current code | VSL status in current code |
| --- | --- |
| Relativistic eccentricity clock term in `src/csl/clock.py`: `F * e * sqrt(A) * sin(E)` | Removed from `src/vsl/clock.py`. VSL keeps eccentricity in the Keplerian orbit and ballistic propagation, applies no independent eccentricity-dependent clock correction, and applies a separate gravity-induced signal frequency/time shift in `src/vsl/propagation.py`. |
| Earth-rotation / Sagnac-style orbit longitude term in `src/csl/orbit.py`: `- OMEGA_E_DOT_RAD_S * (toe + user_sat_range / c)` | Replaced by moving-receiver interception in `src/vsl/propagation.py`. Satellite velocity is converted from ECEF to the same transmit-time inertial basis with `v_inertial = v_ecef + omega_Earth x r_sat`, and the VSL solver uses a numerical Jacobian of that full propagation model. No separate Sagnac orbit term is added. |
| Polynomial satellite clock correction in `src/csl/clock.py`: `af0`, `af1`, `af2`, `tgd` | Shared in both models. Implemented in `src/vsl/clock.py`. Not a relativistic correction. |
| Broadcast orbit model / Kepler solution in `src/csl/orbit.py` | Shared in both models as the base orbit geometry. Implemented in `src/vsl/orbit.py`. Not a relativistic correction. |
| Constant-`c` geometric pseudorange prediction in `src/csl/observation_model.py` | Replaced by ballistic full-vector propagation in `src/vsl/propagation.py`, with predicted pseudorange still expressed in metres through an emission-speed reference quantity. This is a propagation-law replacement, not a direct Newtonian equivalent of the CSL assumption set. |

## Interpretation

- The only clearly relativistic correction present on the CSL side of the current repo is the eccentricity clock term as interpreted by the standard model.
- On the VSL side, that periodic clock term is deleted. The current VSL baseline treats the broadcast polynomial terms as empirical calibration inputs and does not add a gravity- or speed-based eccentricity clock effect.
- This does not remove eccentricity from VSL. Eccentricity remains in the Newtonian Keplerian orbit and changes satellite position, velocity, and ballistic signal propagation.
- VSL retains the gravity-dependent propagation-speed model and additionally treats the satellite's changing Newtonian potential as a signal frequency/energy effect. `gravity_signal_time_shift_s(...)` is applied to predicted pseudorange, not satellite clock correction; it is derived directly from `MU_M3_S2` and does not use `F_RELATIVISTIC`.
- The other major CSL/VSL difference is Earth-rotation handling: CSL uses the standard orbit longitude correction, while VSL handles Earth rotation through moving-receiver interception and a frame-consistent inertial satellite velocity.
- Polynomial clock terms and broadcast orbit equations are shared receiver inputs in this repo, not proof that both models share the same physical interpretation.

## Result Progression

The half-size periodic eccentricity term was tested in three VSL configurations:

| VSL configuration | 2016-06-30 | 2016-08-22 |
| --- | ---: | ---: |
| A. Gravity-only clock term (initial hybrid) | `+1.009 m` RMS delta, 149/220 worse | `+5.381 m` RMS delta, 140/199 worse |
| B. No periodic term (strict Newtonian clock) | `+2.714 m` RMS delta, 206/222 worse | `+6.622 m` RMS delta, 150/197 worse |
| C. Gravity signal frequency/energy shift on predicted pseudorange (current) | `+1.019 m` RMS delta, 151/221 worse | `+5.246 m` RMS delta, 138/198 worse |

- Removing the term (A to B) degraded fit quality by roughly `1.7 m` and `1.2 m` of RMS delta.
- Restoring the same magnitude as a signal-domain shift (B to C) recovered the fit to within `0.01 m` and `0.14 m` of configuration A, on slightly different shared-epoch sets.
- Configurations A and C are numerically near-equivalent because `gravity_signal_time_shift_s(...)` equals half of the standard periodic eccentricity correction, and a pseudorange residual cannot tell whether a term of that size was applied to the satellite clock or to the received signal.
- The current data therefore cannot determine where the half-size eccentricity term physically belongs. Clock-rate versus signal-frequency placement is an open question for better measurements or an independent observable.
