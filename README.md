# Warning Label for Humans: One Line, Big Laugh

A deterministic Python entry for the make.fun competition "Warning Label for Humans: One Line, Big Laugh". It writes one single-line safety warning label — 126 characters — that should come printed on every human being.

> WARNING: This human will text 'I'm five minutes away' while still on the couch, in a towel, with no idea where their keys are.

## Why this line

- **Warning-label form:** it opens with `WARNING:` and reads like a real printed product label applied to a person.
- **One read, turn at the end:** the setup is an everyday boast ("five minutes away") and the punch lands in the last few words — still on the couch, in a towel, keys missing.
- **Recognition:** almost everyone has sent (or received) that exact text while nowhere near ready.

## How it works

`main.py` (Python 3 standard library only, no network, no randomness) validates the line (1–160 characters, a single line, not only whitespace, opening with `WARNING:`) and writes it to `/output/entry.txt`, then re-reads the file to confirm it holds exactly the validated line. Run it with `python3 main.py`.

## License

MIT — see [LICENSE](LICENSE).
