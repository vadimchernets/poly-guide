# Poly shelf: the duel on your computer

A link from the Poly A1 phone app (`https://polyhelper.ai/get/?to=duel&...`) opens here, and the same cases come out in the same order as on the phone. No server, no account, no network: the computer only reads the link.

```
python3 poly.py duel "<the link from your friend>" --ai
```

Prints the cases for you, or for your own AI (Claude Code, Codex, any) to answer. Then:

```
python3 poly.py duel "<the link>" --answers 2,1,3
```

Scores the answers and prints the link to send back. On the phone, opening it adds the result to the table of that duel. `python3 poly.py duel --new` starts a duel of your own and prints the link to send to a friend.

- Needs `poly.py` from the Poly kit (it ships with a `games/` folder beside it). Development tree: `npm run games:pack -- --out games` and `--data games`.
- Only one-tap games take part (the ones with a choice or a mark); a duel never carries free text, only the seed, the game, a nick mask (a hero and six digits) and the result.
- "Play with your own AI" is the same command: the AI sees the same cases the phone shows, answers by number, and its score is a row in the table.
