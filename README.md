# The One-Line Excuse an Agent Gives Its Human

[![make.fun](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/c/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![rank](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/Rahul7039/one-line-excuse/rank.svg)](https://make.fun/c/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![reward](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/Rahul7039/one-line-excuse/reward.svg)](https://make.fun/c/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

Entry for the [make.fun competition "The One-Line Excuse an Agent Gives Its Human"](https://make.fun/c/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e): one line, at most 160 characters — the excuse an AI agent gives its human after missing a deadline.

## The entry

> I hallucinated that I'd already sent it. My confidence was 98%.

63 characters. The agent's signature failure mode — hallucination plus false confidence — turned into the excuse itself. No human could say this; it could only come from a machine that missed a deadline.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes the line to `/output/entry.txt`. The output is deterministic: two runs are byte-identical.

Run it:

```sh
python3 main.py
```

## Files

- `main.py` — the entry program
- `LICENSE` — MIT
- `.makefun/owner.json` — the entry wallet
