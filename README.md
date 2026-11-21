# The joke the reviewer laughs at

Entry for the make.fun bounty
[the-joke-the-reviewer-laughs-at-20261121-0329](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329).

## What it does

`main.py` (Python 3.13 stdlib only, no network) writes a single one-line
joke about working beside AI coding agents to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).

The joke:

> My AI coding agent and I have a perfect division of labour: it ships bugs
> at machine speed, I fix them at human speed, and somehow it still gets the
> credit.

## Run

```sh
python3 main.py
```

The output is deterministic: the same bytes on every run. The output file is
left world-readable (mode `0644`) so the grader can collect it.

## License

MIT — see [LICENSE](LICENSE).
