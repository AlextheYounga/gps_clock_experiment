# Experiment Results History

This file records the solver results found in the repository history and in
the local OpenCode session database. It is intended to preserve the numerical
progression as the VSL model changed.

## Reading The Results

- `RMS delta` is VSL mean residual RMS minus CSL mean residual RMS on shared
  comparable epochs. Positive values favor CSL; negative values favor VSL.
- `worse` is the number of shared epochs where VSL has higher residual RMS.
- `position diff` is the mean 3D separation between the independently solved
  VSL and CSL positions.
- A result is only directly comparable with another result when the dataset,
  GPS week, retained-satellite rules, solver logic, and model configuration
  are the same.

The absolute residuals are large (`about 90–160 m RMS`) because the current
phone pseudoranges are reconstructed from noisy measurements. Small changes
in RMS should therefore not be interpreted as precise physical validation.

## Controlled VSL Progression

These runs use the corrected dataset configuration, including GPS week `1911`
for the 2016-08-22 recording. They isolate the treatment of the half-size
periodic eccentricity term and the later Newtonian-style propagation model.

| Configuration | Dataset 1: 2016-06-30 | Dataset 2: 2016-08-22 |
| --- | ---: | ---: |
| CSL baseline | `157.837 m` mean RMS | `92.662 m` mean RMS |
| A. VSL gravity-only clock term | `158.828 m`, `+1.009 m` delta, 149/220 worse | `97.861 m`, `+5.381 m` delta, 140/199 worse |
| B. VSL no periodic term | `160.538 m`, `+2.714 m` delta, 206/222 worse | `99.287 m`, `+6.622 m` delta, 150/197 worse |
| C. VSL signal frequency/time shift | `158.880 m`, `+1.019 m` delta, 151/221 worse | `97.907 m`, `+5.246 m` delta, 138/198 worse |
| D. VSL Newtonian corpuscle speed (current) | `160.479 m`, `+2.702 m` delta, 205/221 worse | `99.285 m`, `+6.608 m` delta, 149/196 worse |

### Progression Notes

1. Configuration A used the original VSL hybrid: half of the standard
   periodic eccentricity term was treated as a gravity-only clock effect.
2. Configuration B removed the periodic term from the VSL clock entirely.
   Fit quality worsened by approximately `1.7 m` and `1.2 m` of RMS delta.
3. Configuration C restored the same numerical term as a signal-domain
   frequency/time shift instead of a clock correction. Its results returned
   close to configuration A, showing that receiver pseudorange residuals
   cannot distinguish those two placements.
4. Configuration D removed the signal-domain term and replaced the former
   path-average speed formula with Newtonian-style corpuscle propagation.
   Conservation of mechanical energy makes falling light slightly faster;
   the effective speed shift is about `+0.079 m/s`, only millimetres of range.
   The results consequently return to nearly configuration B.

The current configuration D is not the worst measured configuration. It is
effectively tied with B; B is marginally worse on both datasets.

## Earlier Development Runs

The following outputs were also found in OpenCode history, but are not part of
the controlled A–D comparison because they used earlier code and/or dataset
settings.

### Initial Multi-Mode Run

Recorded on 2026-04-17 before the later frame, comparison, and GPS-week
corrections:

| Dataset | CSL | CSL without relativistic eccentricity | VSL |
| --- | ---: | ---: | ---: |
| 2016-06-30 | `157.837 m` | `161.068 m` (`+3.231 m`) | `160.545 m` (`+2.708 m`) |
| 2016-08-22 | `92.197 m` | `94.222 m` (`+2.025 m`) | `94.186 m` (`+1.989 m`) |

The second dataset used GPS week `1910` in these runs, whereas the corrected
configuration uses week `1911`. The numbers are retained as development
history, not as a direct baseline for current results.

### First Gravity-Propagation Run

After adding the original path-average gravity speed model, but before the
later configuration cleanup and dataset correction, the recorded VSL results
were:

| Dataset | VSL mean RMS | VSL-CSL RMS delta |
| --- | ---: | ---: |
| 2016-06-30 | `158.838 m` | `+1.001 m` |
| 2016-08-22 | `92.054 m` | `-0.144 m` |

These runs also included the earlier VSL clock treatment and the old dataset 2
GPS week, so they are historical context only.

## Provenance

The controlled results were reported in OpenCode sessions for this repository
on 2026-09-04. Earlier outputs were recovered from
`~/.local/share/opencode/opencode.db` by searching completed tool outputs for
the solver summary rows.

Relevant repository commits marking the implementation stages include:

- `f3a7ce0`: initial VSL gravitational correction work
- `a923b68`: original gravity effect on VSL light speed
- `cc3084b`: removed the VSL gravitational clock correction
- `de25915`: added the temporary signal-domain energy correction
- `d031c2a`: documented that temporary signal-domain result

The current configuration D includes subsequent working-tree changes that
replace the temporary signal correction with the Newtonian-style corpuscle
speed model.
