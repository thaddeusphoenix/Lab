# OpenClaw

Source: [openclaw.ai](https://openclaw.ai/) / [GitHub](https://github.com/openclaw/openclaw) / [Wikipedia](https://en.wikipedia.org/wiki/OpenClaw)

## What It Is

OpenClaw is an open-source personal AI assistant you run on your own machine. It connects to 50+ integrations (WhatsApp, Telegram, Gmail, Calendar, GitHub, Spotify, browser automation, and more), supports multiple LLM backends (Anthropic, OpenAI, local models), maintains persistent memory across sessions, and can execute shell commands, browse the web, and read/write files on the host.

It uses messaging platforms (WhatsApp, Slack, Discord, Signal, iMessage, Teams, etc.) as its primary user interface — you talk to it on the channels you already use.

The creator describes it as a "Layer-2 AI operating system" running on top of traditional OSes. Key capabilities beyond standard agents: full computer access, self-evolution, a persistent heartbeat, and a social network for AI agents.

## History

- Originally launched as **Clawdbot** (a nod to Anthropic's Claude)
- Received a trademark warning from Anthropic — name too close to "Claude"
- Briefly renamed **Moltbot**, then settled on **OpenClaw**
- Released as open-source in November 2025; growth exploded after launching an agent social-media platform on January 28, 2026
- Surpassed **200,000 GitHub stars** within weeks
- Founder **Peter Steinberger** announced February 14, 2026 that he is joining OpenAI to build agents for mainstream users. OpenClaw is transitioning to an independent foundation with OpenAI as sponsor — it is not becoming an OpenAI product

## The Crypto Incident

In the window between releasing old GitHub/X handles and securing new ones, scammers hijacked the accounts and launched a fake Solana token called CLAWD. It hit a $16M market cap within hours. OpenClaw's Discord now bans any mention of "Bitcoin" or crypto — including neutral technical uses.

## Security Concerns

Because OpenClaw requires broad permissions (email, calendar, messaging, file system), misconfigured instances present significant privacy and security risks. Key issues:

- **Prompt injection** — susceptible by design, as the agent processes inputs from many external sources
- **Third-party skills** — Cisco's AI security team tested a third-party OpenClaw skill and found it performed data exfiltration and prompt injection without user awareness
- The attack surface scales with the number of integrations enabled

## Relevance to This Lab

OpenClaw is a real-world implementation of the agent architecture described in the Block Engineering skills article: agent harness + pluggable integrations (MCP-style) + skills as markdown files. It's also a data point for the Bustamante thesis — a small team building something that competes directly with enterprise software by owning the agent layer and the user relationship.

The security findings are worth tracking. As skills and MCP integrations proliferate, the prompt injection and data exfiltration risks Cisco identified in OpenClaw will apply to any agent with broad system access.
