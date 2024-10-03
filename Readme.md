# PDF files for parser testing

To update index file just run:
```bash
python3 update_index.py
```
It has no specific dependencies, and it's possible to run
it with base system python interpreter.

Script for Alan Studio to index all PDF:
```js
corpus({
    title: `PDF-testing`,
    urls: [
        `https://anvlasov.github.io/PDF-testing/`,
          ],
    depth: 2,
    maxPages: 999,
    priority: 0,
});
```