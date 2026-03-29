# Operation Wakanda

Interactive branching red team assessment case study based on a real security home assignment.

## Overview

A narrative-driven security assessment simulation where the user chooses an operative (T'Challa or Shuri), maps an attack surface, makes investigation choices, encounters dead ends, discovers vulnerabilities, and delivers a findings report.

## Features

- **Role Selection**: T'Challa (strategic) vs Shuri (technical) with different narrative voices
- **14 Chapters** across 7 branching paths
- **3 New Investigation Vectors**: API probe, AWS metadata, credential testing
- **Dead End Path**: Direct admin access attempt (blocked, must return)
- **Mini-map**: Always-visible node map showing progress
- **Mission Objectives**: 5 trackable objectives with completion indicators
- **Scanning Transitions**: Animated loading between chapters with glitch effects
- **Typing Dialogue**: Character speech with typewriter effect
- **Terminal Animation**: Line-by-line terminal output reveal
- **Particle Effects**: Gold burst on evidence discovery
- **Sound Effects**: Web Audio API (click, evidence, dead end, win)
- **Mission Timer**: Elapsed time tracking
- **End Stats**: Time, intel collected, paths explored, assessment rating

## Roles

**T'Challa** - Field-oriented, risk-forward, decisive. "Every exposed service is a potential entry."

**Shuri** - Systems-oriented, precision-driven, analytical. "Systematic enumeration of all visible services."

## Assessment Rating

Based on paths explored:
- **Elite Analyst** (5+ paths)
- **Strategic Operative** / **Thorough Explorer** (3+ paths)
- **Direct Strike** (minimal paths)

## Tech

Single HTML file. No dependencies. GitHub Pages ready.

## Author

Nevo Ben Ami - [GitHub](https://github.com/N3V044)

*Based on a real home assignment. All evidence is simulated. No systems were compromised.*
