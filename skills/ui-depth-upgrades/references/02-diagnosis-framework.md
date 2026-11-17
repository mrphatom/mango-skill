# Diagnosis Framework

Map what the user is complaining about to the right move. Do not skip this step.

## Symptom → Move mapping

| User language | Likely symptom | Primary move | Supporting move |
|---|---|---|---|
| boring, plain, same-size, template, stock photo in a box | Timid layout / weak hierarchy | 1 Oversized subject + overlap | light 2 |
| flat, lifeless, sterile, cards on solid colour, no atmosphere | Single plane / no depth | 2 Scene + layers | light 3 |
| generic, default Material/iOS, no personality, AI-looking | No shared visual language | 3 Cohesive motif | — |
| all of the above | Mixed | Diagnose the strongest first | at most one more |

## Quick diagnosis questions

1. Is the main subject trapped inside a rectangle or card? → Move 1 candidate.
2. Is the background a solid fill or a tiny hero image? → Move 2 candidate.
3. Do the images, type, and controls look like they came from three different design systems? → Move 3 candidate.

## Anti-patterns to watch for

- Applying all three moves to a data-dense screen (banking, settings, tables) → usually hurts scanability. Prefer light Move 3 only.
- Oversizing a subject that carries critical data (charts, dense lists) → keep those subjects contained.
- Scene backgrounds that fight the content's mood or reduce contrast below AA.

## Output of diagnosis

Always state in one sentence:

> "This is [flat / boring / generic] because [specific observation]. Primary move: [1/2/3]."

Then proceed to the technique reference.
