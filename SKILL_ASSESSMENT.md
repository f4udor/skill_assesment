# Skill Assessment — Meeting Room Booking System

Welcome, and thanks for taking part.

You'll build a small meeting-room booking system and grow it through a series of levels.
The goal is **not** a finished, production-ready product — we want to understand how you
reason, how you handle changing requirements, and how you communicate your decisions.
We care far more about *how* you work than *how much* you finish.

There's no time limit. Work at a pace that lets you do your best thinking. Most people
don't reach the final levels, and that's completely fine — by design.

---

## What this is *not* about

- Producing polished, production-ready software.
- Knowing every language feature, library, or framework.
- Fancy patterns or over-engineering.
- Reaching the last level.

Reaching Level 2 with clean, well-reasoned code that you can explain is a better result
than racing to Level 4 with a tangled design you can't account for. The ladder exists so
there's always somewhere to go — not as a checklist to complete.

---

## Format

- **Language / environment:** Your choice — whatever you're most comfortable with.
- **Interface:** Up to you — a CLI, a small HTTP API, a web page, or just a script with a
  `main()` that demonstrates the behavior. Pick whatever lets you focus on the logic.
- **Storage:** In-memory is fine. No database required.
- **Resources:** Official documentation, search engines, and Stack Overflow are all fine.

**What to hand back:**

- The working code, with clear instructions to run it.
- The short written reflection described at the end.

---

## The base task

Build a booking system for a **single** conference room that lets a user:

- **Create a booking** with a name (who is booking), a start time, and an end time.
- **List all current bookings.**

Keep the code simple and readable, and handle invalid input sensibly — you decide what
"sensibly" means, and be ready to explain your choice.

If something in the requirements is ambiguous, note your assumption and move on (e.g.
"I'm assuming bookings may be in the past unless told otherwise"). Spotting ambiguity and
making a reasoned call is a strength.

---

## The levels

Each level adds one requirement. Work through them **in order**, and try to get each one
working *and* tidy before moving on — the point is to grow the design cleanly, not to
bolt features on. Don't try to anticipate later levels; just write clean, reasonable code
for what's in front of you.

### Level 1 — Reject overlapping bookings

A new booking must not overlap an existing one. Reject it if it does.

Think carefully about the boundary: a booking ending at 10:00 and one starting at 10:00
should **not** conflict — touching is fine.

### Level 2 — Sensible validation

Decide what counts as invalid input and reject it. Consider: a start that's after the
end, a zero-length booking, and whether bookings in the past should be allowed (either
answer is fine if you can defend it).

Think about how the caller finds out *why* a booking was rejected.

### Level 3 — Cancel (and optionally update) a booking

Let a user cancel a booking. Optionally, let them change its time.

Consider what actually identifies a booking once you can remove or change one.

### Level 4 — Multiple rooms

Support several rooms. Overlap only matters *within* the same room.

Your original design assumed a single room — adapt it thoughtfully rather than copying
the logic for each room.

### Level 5 — Find available slots

Given a room and a day or time window, report when it's free.

Think about the edge cases: a completely empty window, and a fully-booked one.

### Level 6 — Concurrency (optional, discussion)

Two people try to book the same slot at the exact same instant — what happens? You don't
need to implement a solution. We're interested in whether you can spot the problem and
describe how you'd handle it. Feel free to answer this one in writing rather than code.

---

## Final reflection

Please include a short written reflection with your submission. Answer briefly:

1. Where is the weakest part of your solution right now?
2. What would you do differently with more time?
3. Which level forced the biggest rethink, and would your original design have made it
   easier?
4. What did you deliberately decide *not* to handle, and why was that the right call?
5. (If you reached it) Level 6: where exactly is the problem, and how would you handle it?

---

A few reminders: it's fine to get stuck — tell us where and how you worked through it.
It's fine to throw away code and start over if you find a better approach. And it's fine
not to finish.

Good luck, and have fun with it.
