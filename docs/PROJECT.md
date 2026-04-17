# GPS Relativity Test

We are testing the thesis of this paper: `docs/gps-mythology-paper.md`
I have included the real Java code for GPS receivers provided by Google. I have created a `code2prompt` export of the [Github repository](https://github.com/google/gps-measurement-tools) GPS tools here: `docs/references/gps-measurment-tools.md`. It is approximately 100k tokens long, so search what you need. 


### **Task: GNSS Relativistic Effects Verification Engine (Python)**

**Objective:**  
Build a standalone Python-based GNSS position engine to determine if the periodic relativistic clock corrections implemented in the GPS ICD-200 (and the provided Java source) are mathematically necessary for an accurate position fix, or if they are "solved away" by the receiver's clock bias as suggested by some critics.

**Stack**
Python 3.12.12 using `uv`.
Entrypoint: main.py

**Reference Material:**
1.  **Logic Source**: `GNSSLogger/pseudorange/src/main/java/com/google/location/lbs/gnss/gps/pseudorange/SatelliteClockCorrectionCalculator.java`
2.  **Algorithm Source**: `SatellitePositionCalculator.java` and `UserPositionVelocityWeightedLeastSquare.java`.
3.  **Data Source**: `data/pseudoranges_log_2016_06_30_21_26_07.txt`

**Requirements:**

1.  **Data Parser**: 
    *   Implement a parser for the `GnssLogger` text format. 
    *   Extract `Raw` measurements (Pseudoranges, Svid, TimeNanos) and `Nav` messages (Ephemeris parameters like $af_0, af_1, af_2, e, \sqrt{A}, M_0$, etc.).

2.  **Physics Engine (Port from Java)**:
    *   Implement `calculate_clock_correction(ephemeris, tow)` exactly matching the Java `SatelliteClockCorrectionCalculator`.
    *   **CRITICAL**: Include a boolean toggle `enable_relativity`. When `True`, apply the $F \cdot e \cdot \sqrt{A} \cdot \sin(E)$ term. When `False`, set this term to `0.0`.
    *   Implement the iterative Kepler solver for Eccentric Anomaly ($E$).

3.  **Position Solver**:
    *   Implement a 4D Weighted Least Squares (WLS) solver using `numpy`.
    *   Solve for State Vector: $[X, Y, Z, dt]$ (User ECEF coordinates and Receiver Clock Bias).

4.  **Verification Script**:
    *   Process the demo log file twice: once with `enable_relativity=True` and once with `False`.
    *   **Output Metrics**:
        *   **Delta Position**: Calculate the Euclidean distance (meters) between the two resulting $(X, Y, Z)$ coordinates.
        *   **Residual Analysis**: Calculate the Root Mean Square (RMS) of the post-fit residuals for both runs.
        *   **Clock Bias Comparison**: Measure how much of the "missing" relativity error was absorbed into the $dt$ (Receiver Clock Bias) vs. how much leaked into the spatial coordinates.

5.  **Deliverable**:
    *   A single Python script or small module set that can be run from the CLI.
    *   A brief summary of the results: "Does disabling relativity increase the Residual RMS?" (If RMS increases, the 'Mythology' claim is disproven because the spheres no longer intersect at a single point).

**Constraints**:
*   Use `numpy` for matrix math.
*   Strictly follow the ICD-GPS-200 constants (Speed of Light, $\mu$, etc.) as defined in the Java source.
*   Do not use external GNSS libraries; the goal is to verify the *logic* found in this specific codebase.