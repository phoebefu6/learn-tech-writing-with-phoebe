# learn tech writing with phoebe

A practitioner's course in technical writing for data and AI teams. Eight 45-minute
sessions plus four self-paced deep dives, taught by documenting one real thing end to
end: **Pulse**, a small CSV-to-metrics pipeline that ships here undocumented, on purpose.

**Live site:** https://phoebefu6.github.io/learn-tech-writing-with-phoebe/

## The arc

| # | Session | You build |
|---|---------|-----------|
| 1 | Why docs fail: the audience equation | Pulse audience statement + doc plan |
| 2 | Sentences that work | the NOTES.txt rescue |
| 3 | Structure readers can scan | run procedure + config table |
| 4 | The README (milestone 1) | Pulse's front door |
| 5 | Diátaxis: the four kinds of docs | first how-to guide |
| 6 | Reference, ADRs, changelogs (milestone 2) | the project's memory |
| 7 | Docs as code (milestone 3) | Vale linting + review norms |
| 8 | Edit like a pro, ship v1.0 (milestone 4) | the finished doc set |

Deep dives: writing helpful error messages, accessible writing, runbooks and ops docs,
and a Google vs Microsoft style-guide face-off.

## Sources

Built from the free material Google trains its own engineers on, plus the community
canon: Google Technical Writing One + Two, the Error Messages and Accessibility courses,
the [Diátaxis framework](https://diataxis.fr), the Google and Microsoft style guides,
[Write the Docs](https://www.writethedocs.org/guide/), and the standard templates
(makeareadme, Nygard ADR, keepachangelog, SRE runbooks) with the Vale prose linter.
Certificates and facilitated in-class exercises stay with the free official sources.

## The running project

`pulse/` is a working pipeline: `ingest.py` -> `clean.py` -> `metrics.py`, driven by
`config.yaml`, with deliberately undocumented code and one awful `NOTES.txt`. The course
turns it into a doc set you would be proud to inherit.

by Phoebe Fu
