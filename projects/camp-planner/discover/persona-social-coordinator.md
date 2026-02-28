# User Persona: The Social Coordinator

**Project:** Camp Planner
**Created:** 2026-02-27
**Status:** Grounded in research — based on Sari Gelzer session (2026-02-26). Treat as directional, not fully validated.

---

## Who They Are

A working parent with two children at different life stages — one actively in the camp market, one younger and aging into it. They are embedded in a parent network and use it constantly: programs are discovered through other parents, enrollment decisions are made in coordination with friends, and the goal is often to get kids into the same camps as their friends. Their planning is inherently social. The solo-user framing of most planning tools does not match how they actually work.

**Representative name:** Priya
**Household:** Two working parents, two children (ages 8 and 3)
**Planning style:** Network-first. Discovers through community, decides in coordination, and shares as a matter of course.

---

## How They Work

Priya starts hearing about summer programs through other parents — in the school pickup line, in parent group chats, in conversations after sports practice. She adds programs to her list partly because they look good and partly because her kids' friends are going. Getting kids into the same camps as their friends is not a nice-to-have; it is often the deciding factor between two otherwise equivalent options.

The enrollment moment is especially social. When a popular program opens registration, Priya wants to share it with friends at the same time — the sign-up link, the deadline, what to select. She described the ideal as sending a friend "the signup moment, a short description, and a button that will set them to sign up on time." This is not a passive share; it is active coordination.

She also thinks about schedule composition in a way Morgan doesn't. The question isn't just which weeks are covered — it's whether the summer is *balanced*. An active outdoor camp plus an intellectual or STEM camp plus a performing arts program is a goal, not a bonus. And for her younger child, she tracks what programs will be available as they age into eligibility.

---

## What They Need

- **One-tap program sharing.** Sending a friend a program — name, dates, registration link, deadline — is a primary behavior, not an edge case. If sharing requires copying fields manually, it won't happen.
- **Enrollment moment coordination.** Priya doesn't just want to know when registration opens. She wants to share the moment with another parent so they can both register at the same time and get their kids into the same session.
- **Schedule composition visibility.** The coverage view answers "is this week filled?" Priya is asking "is this summer well-composed?" She wants to see, at a glance, whether the summer is balanced across program types.
- **Age-forward awareness.** For her younger child, she needs to know which programs they'll be eligible for in future summers. A static view of current eligibility is not enough.
- **Lightweight household coordination.** Budget decisions involve her spouse. Even in a single-user tool, she needs to be able to show her spouse the plan and the spend — which means the plan has to be shareable in a readable format, not locked in an app.

---

## What Success Looks Like

Her child's summer matches her friend's child's summer for at least two programs. She sent the registration link to three friends before the deadline. The summer mixes active and creative programs. She didn't have to scramble to coordinate — the sharing moment was easy enough that it happened in the flow of planning, not as an extra step after.

---

## Current Workarounds and Their Failure Modes

| Workaround | What works | Where it breaks |
|---|---|---|
| Parent group chats | Great for discovery and social coordination | Ephemeral — links and dates get buried; hard to act on later |
| Notes app | Easy to add programs as she hears about them | Unstructured; can't share in a useful format |
| Google Calendar | Reminders work | No social layer; can't share the enrollment moment, just the date |
| Verbal coordination | Natural and fast | Relies on the other parent to also remember the deadline |

---

## Open Research Questions

1. **Is the social coordination behavior specific to Priya's profile, or is it widespread?** One participant mentioned coordinating with other parents four times across a single session. This is strong signal, but it reflects one parent with a particular social style. The next research session should probe whether solo planners (Jamie) see social features as irrelevant or actively confusing.
2. **Does Priya plan for both children simultaneously, or sequentially?** If she's tracking two children at once, a multi-child view becomes more important earlier than the brief assumes. If she plans one child at a time, the current single-child model may still work.
3. **How does Priya feel about features that don't serve her social workflow?** In prototype reviews, watch for moments where social friction breaks her flow — places where she wants to share and can't, or where sharing would require leaving the tool and going to a messaging app.
4. **Is the share behavior triggered by enrollment moments specifically, or is it ongoing?** Understanding whether Priya shares programs continuously (as she discovers them) or only at the enrollment moment affects where the share action should live in the UI.
