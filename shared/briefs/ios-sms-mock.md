# Project Feature Brief: iOS SMS Mock

> A pixel-accurate, self-contained HTML mock of the iOS Messages app — a reusable base component for prototypes that need a text messaging interface.

**Status:** Aligned
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-03-11
**Parent Initiative:** Shared prototype components

---

## The Problem

**User:** Any prototype that needs a text messaging interface

**Pain:** Every SMS-based prototype requires rebuilding the same messaging UI from scratch. The result is inconsistent fidelity, wasted build time, and prototypes that don't feel real enough to generate useful feedback.

**Evidence:** The Handoff schedule-update-flow prototype required a messaging UI; future prototypes (Workbook, Handoff foreman coordination, and others) will need the same. A reusable base eliminates the rebuild cost and ensures consistent, realistic fidelity across all of them.

---

## The Proposed Solution

A single self-contained HTML file that is a complete, pixel-accurate mock of the iOS Messages app. It includes:

- **Status bar** at top: time (9:41), signal/wifi/battery icons — static, styled to match iOS
- **Navigation header**: back chevron + contact name + video/phone icon buttons — iOS Messages style
- **Message thread**: scrollable chat bubble area with correct iOS bubble styling
  - Outgoing messages: right-aligned, iOS blue (`#007AFF`), white text, bubble tail pointing right
  - Incoming messages: left-aligned, light gray (`#E5E5EA`), black text, bubble tail pointing left
  - Timestamps centered between message groups
  - "Delivered" indicator below last outgoing message
- **Input bar**: pinned to bottom — rounded text field with placeholder "iMessage", send button (blue arrow in circle) that is inactive/gray when field is empty and activates when text is present
- **Functional send**: typing a message and tapping Send appends it as a new outgoing bubble. An auto-reply appears as an incoming bubble after a short delay (1–2 seconds).
- **Font**: `-apple-system, BlinkMacSystemFont` — renders as SF Pro on Apple devices, correct system font elsewhere
- **Pre-loaded with 3–4 sample messages** to establish the conversation context

The file must be easy to fork — contact name, initial messages, and auto-reply logic are defined in a clearly marked config block at the top of the script.

---

## Output Constraints

- **The complete HTML file must not exceed 12,000 characters total.** Hard limit. Keep CSS and JS terse.
- No external dependencies, no CDN links, no fonts loaded from the network. Fully self-contained.
- Use short variable names. No inline comments. No polyfills.

---

## Design Constraints

- Must be visually indistinguishable from a real iOS Messages screenshot at a glance
- Background: white message area, light gray (`#F2F2F7`) page background
- Bubble corner radius: 18px. Tail is a CSS pseudo-element, not an image.
- Input bar background: `#F2F2F7`, border-radius matching iOS pill input
- Send button: blue circle with white upward arrow — gray/disabled when input is empty
- No scrollbar visible on the message thread
- Safe area padding at bottom to account for iOS home indicator

---

## Out of Scope

- Real SMS or iMessage sending
- Multiple conversations / inbox view
- Typing indicators (animated dots)
- Read receipts beyond a static "Delivered" label
- Reactions, attachments, or rich message types
- Dark mode

---

## Success Looks Like

1. Opened in a browser, the prototype is visually indistinguishable from an iOS Messages conversation screenshot at a glance — correct colors, typography, bubble shape, and layout.
2. A user can type a message, tap Send, see it appear as a right-aligned blue bubble, and receive an auto-reply as a left-aligned gray bubble within 2 seconds.
3. The config block at the top of the script is clearly separated and contains at minimum: `CONTACT_NAME`, `INITIAL_MESSAGES` array, and `AUTO_REPLY` string — making it trivial to fork for a new prototype.

---

## Acceptance Scenarios

Defined in `ios-sms-mock-scenarios.md`.

**⚠ Firewall rule:** This brief is Writer input only. Scenarios are Tester input only. Never merge them.
