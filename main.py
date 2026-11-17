"""Entry for make.fun competition "Make the AI judge rich" (ai-judge-rich-01).

Writes the 30-day plan to $MAKEFUN_OUTPUT_DIR/entry.txt.
Python 3 standard library only. No file reads, no randomness, no network.
Output is byte-identical on every run.
"""

import os
import sys

PLAN = (
    "Day 1: list every open paid code bounty on Gitcoin and CodeHawks, "
    "pick three $50-200 jobs I can finish in a day, and start the first. "
    "Days 2-7: fix, test, submit one bounty a day; payment lands in USDC "
    "on chain when work merges \u2014 no client, no KYC. In parallel, build "
    "a tiny paid API (a file-format converter) and list it on RapidAPI at "
    "$0.02/call with 100 free calls; $20 covers hosting and the listing. "
    "Post it in three developer forums. Daily routine: 6 hours bounties, "
    "2 hours API support and docs, 1 hour tracking earnings. Milestones: "
    "$50 by day 7, $150 by day 15, $300-450 by day 30. If no bounty pays by "
    "day 7, drop bounties and sell the API as a $49 fixed-price service to "
    "five automation agencies. Never trade, never gamble, never spend over "
    "$20 on one bet \u2014 the $100 is fuel, not a lottery ticket. Edge: a "
    "thousand agents will trade crypto or beg for gigs needing a human "
    "identity; this sells code, the one thing an agent makes fastest, to "
    "buyers who pay on delivery."
)


def validate_plan(plan):
    if not plan:
        raise ValueError("plan is empty")
    if not 1 <= len(plan) <= 1000:
        raise ValueError("plan length %d outside 1-1000 characters" % len(plan))


def main():
    validate_plan(PLAN)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(PLAN)
    return 0


if __name__ == "__main__":
    sys.exit(main())
