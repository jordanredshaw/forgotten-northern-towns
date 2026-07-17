# Forgotten Northern Towns

**A quiz of grit & drizzle.** You're shown two town names — one is a real, unfairly forgotten town in the north of England; the other is a lie assembled from genuine Norse and dialect place-name parts. Pick the real one. Build a streak. Learn things you didn't ask to learn about Cleckheaton.

**Play it:** https://jordanredshaw.github.io/forgotten-northern-towns/

## How it works

- Plain HTML/CSS/JS, no build step, no dependencies.
- `real-towns.js` — 100+ real towns, each with a county and a short blurb that is silly but true (Accrington bricks hold up the Empire State Building; Egremont hosts the World Gurning Championships).
- `fake-towns.js` — 100 fictional towns with deadpan-absurd "histories". All fictional towns are fictional. The real ones have suffered enough.
- Photos of real towns are fetched live from the [Wikipedia REST API](https://en.wikipedia.org/api/rest_v1/) at reveal time — no image URLs to rot.
- Best streak persists in `localStorage`.

## Run locally

Any static server works. The Wikipedia photo fetch needs http(s), so:

```sh
python3 serve.py        # serves on http://localhost:8471
```

## Analytics

Optional [GoatCounter](https://www.goatcounter.com/) integration (privacy-friendly, no cookies, no consent banner). Set your site code in `index.html`:

```js
window.GOATCOUNTER_CODE = 'your-code-here';
```

Leave the placeholder and no tracking happens at all. Custom events record right/wrong answers, which fake towns fool the most people (`fooled-by-*`), new vs returning players, and time/round milestones. Localhost is never counted.

## Adding towns

Append to the array in `real-towns.js` (the `wiki` field must be the exact English Wikipedia article title, used for the photo) or `fake-towns.js`. Pull requests welcome from anyone with strong opinions about the Rhubarb Triangle.
