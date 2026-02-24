# Strategic Initiative Brief: Tiny Tracks

> A browser-based 3D simulator for designing and running model train layouts — the satisfaction of the hobby without the physical cost, space, or setup.

**Status:** Draft
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-02-24
**Features:** *(none yet — first feature brief pending)*

---

## The Opportunity

Model railroading is a $1B+ hobby with high barriers to entry: it requires significant physical space, hundreds to thousands of dollars in hardware, and months of patient, hands-on construction. The result is that many people who are drawn to the hobby — the craft of building miniature landscapes, laying track, running trains — never actually get to do it.

The opportunity is not to replace the physical hobby. It is to simulate the *act of building* — the decisions, the creativity, the satisfaction of watching a train run a loop you just designed — in a browser, with no cost and no setup. The medium is different. The appeal is the same.

The working prototype demonstrates the core mechanic is viable: a 3D grid-based layout builder with terrain painting, track placement, scenery, and an animated locomotive that follows the track you lay. All in a single HTML file.

## Why Now

- Browser-based 3D via WebGL/Three.js is mature enough to deliver a tactile, visually satisfying experience in a single HTML file with no install
- The prototype proves the core interaction loop works — terrain, track, scenery, animated trains — without a backend or build system
- No competitive browser-based product captures the *model building* experience specifically; existing simulators focus on driving trains, not constructing layouts

## Why Us

- Starting with a functional Cardboard prototype, not a whiteboard idea
- The "building simulator" framing is intentional and differentiated — we are simulating the craft of assembly, not a train driving game
- The single-file architecture means the path to a shareable, embeddable, no-install experience is short

## What We're Building

A progressively realistic browser-based model train layout simulator. The experience is the act of designing and building — placing track, painting terrain, adding scenery, watching the locomotive run the layout you created.

Current state (Cardboard prototype):
- 20×20 grid terrain with four paint types (grass, dirt, ballast, water)
- 9 track piece types including curves, crossings, and switches with animation state
- 4 scenery objects (pine tree, oak tree, cottage, boulder)
- Animated locomotive that pathfinds along connected track
- Ghost preview on hover, rotate with R key or FAB button
- Right-click + drag orbit camera, scroll to zoom
- Mobile-friendly touch controls

Future direction: higher visual fidelity (textures, lighting, realistic materials), save/load layouts, more rolling stock, more scenery categories, layout validation feedback, and eventually a richer building simulation (elevated terrain, tunnels, bridges).

## What We're Not Building (Now)

- Multiplayer or shared layouts
- Train physics simulation (acceleration, derailment, grades)
- A backend, accounts, or server-side persistence
- A mobile app (browser-first, touch-responsive)
- Monetization

## Success Looks Like

| Metric | Target |
|---|---|
| Session length | Average session > 10 minutes in first cohort |
| Return rate | >30% of first-time users return within 7 days |
| Completion behavior | Users who lay a connected loop run the train on it |
| Qualitative | Users describe the building experience as satisfying, not frustrating |

## Biggest Unknowns

1. **Does the "building simulator" framing resonate, or do users want to drive the train?** The core bet is that the satisfaction is in constructing the layout. If users primarily want to control the locomotive, the product direction shifts significantly.

2. **How much visual fidelity is needed before it feels compelling enough to share?** The current prototype is functional but minimal. There is a threshold of visual quality below which the experience feels like a toy rather than a simulation. We do not know where that threshold is.

3. **Is localStorage enough for retention, or does the lack of save/load kill return visits?** Without save/load, every session starts blank. Users may invest time in a layout, close the tab, and never return. This is the most likely cause of poor retention and should be validated quickly.
