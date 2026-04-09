# Mars

## Overview

This project simulates a Mars rover performing multiple tasks such as navigation, coordinate transformation, signal decoding, system checks, and optimization. It integrates Linux commands, Bash scripting, and Python programming to demonstrate practical problem-solving.

## Learning Experience

* Developed proficiency in Linux terminal commands and Bash scripting
* Understood coordinate transformations between camera, rover, and world frames
* Applied matrix operations and rotations using NumPy
* Learned dynamic programming for optimization problems
* Implemented decoding techniques and data filtering methods

## Equations and Concepts

**Transformation Equation**
[
P_{world} = R_{rover} \cdot (R_{camera} \cdot P_{camera} + T_{camera}) + T_{rover}
]

**Cost Function**
[
Cost = |ΔInner| \cdot W1 + |ΔMiddle| \cdot W2 + |ΔOuter| \cdot W3
]

**Constraints**
[
Inner + Middle + Outer = Target
]
[
|Inner - Outer| \leq D
]

## Approach

### Linux Tasks

Used commands such as `mkdir`, `cd`, `touch`, `mv`, `find`, `grep`, `wc`, `date`, and `top` to manage files and system information.

### Bash Script

Implemented a system check script that evaluates battery level and network connectivity before confirming operational status.

### Coding Tasks

* Coordinate transformation using rotation matrices and translation vectors
* Morse code decoding using dictionary mapping
* Message decoding using reverse shifting logic
* Noise removal using mean, median, and hybrid filters
* Optimization of manipulator movement using dynamic programming
* Arena mapping and shortest path computation avoiding obstacles

## Challenges Faced

* Understanding transformation chains and rotation order
* Handling edge cases in decoding problems
* Designing efficient dynamic programming solutions
* Selecting optimal filtering techniques using variance
* Representing obstacle data correctly in matrix form

## Resources Used

* Linux command line documentation
* GeeksforGeeks
* NumPy documentation
* Python official documentation

## Conclusion

The project demonstrates the integration of mathematical concepts, system-level operations, and programming techniques to solve complex, multi-domain problems.

![alt text][def]

