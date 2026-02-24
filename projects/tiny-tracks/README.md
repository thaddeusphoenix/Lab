# Tiny Tracks

A browser-based 3D simulator for designing and running model train layouts. The experience is the act of building — placing track, painting terrain, adding scenery, watching a locomotive run the layout you created.

**Phase: Discover**
**Brief:** [`briefs/strategic-initiative-brief.md`](briefs/strategic-initiative-brief.md)

## The Concept

This is not a train driving simulator. It simulates the *craft* of model railroading — the decisions and satisfaction of assembling a miniature landscape and layout, without the physical space, cost, or setup of the real hobby.

## Prototypes

| Artifact | Fidelity | Description |
|---|---|---|
| [`discover/builder-prototype.html`](discover/builder-prototype.html) | Cardboard | Working 3D layout builder — terrain painting, track placement, scenery, animated locomotive. Built in Three.js. Open directly in a browser. |

## Current Capabilities (Cardboard Prototype)

- 20×20 grid terrain with four paint types: grass, dirt, ballast, water
- 9 track piece types: straight (NS/EW), curves (4 orientations), crossing, switch left/right
- 4 scenery objects: pine tree, oak tree, cottage, boulder
- Animated locomotive that pathfinds along connected track
- Switch toggle with visual lever indicator
- Ghost preview on hover, R key or FAB button to rotate
- Right-click drag to orbit camera, scroll to zoom
- Touch-friendly for mobile

## Controls

| Input | Action |
|---|---|
| Left click / tap | Paint or place selected tool |
| Right-click drag | Rotate camera |
| Scroll / pinch | Zoom |
| R key | Rotate selected item |
| FAB button (bottom right) | Rotate selected item (touch) |
