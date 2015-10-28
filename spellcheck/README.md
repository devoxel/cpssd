# Wand

A coffeescript text-editor, performs magic on your text.

# Usage

To use it just browse to the the url or alternatively
just open `/dist/index.html` in a browser with local javascript support.

# Building from source

Coffeescript is a transcompiled language. It compiles to js, which
is placed in a file called `/dist/main.js`.

That file is then loaded by the `/dist/index.html`.

To build you'll need nodejs and npm.

Find [Linux/ Mac instructions here](https://docs.npmjs.com/getting-started/installing-node).
Find [Windows instructions here](http://blog.teamtreehouse.com/install-node-js-npm-windows)

I recommend v4.0.0 for node, but most versions should work.

Once that's done run:

```
npm install
```

That will make npm will read from my `package.json` and handle the
coffeescript dependencies.

I'm also using npm as a build tool with it's scripts decleration. If you're
interested you can read more about the process
[here](http://blog.keithcirkel.co.uk/how-to-use-npm-as-a-build-tool/)

Run `npm run` to see a list of all the scripts.

# Limitations of wand

Wand was not designed with real world text editing in mind. It's slower than
most modern text editors and doesn't actually keep track of things like cursor
position or what's currently being rendered.

# Scripts

#### `npm run build`

This will build the coffeescript

#### `npm run build:watch`

This will build the coffeescript any time it detects a change.

# Dependincies

- [nodejs](https://nodejs.org/en/)

- [npm](https://www.npmjs.com/)

- [coffee-script](http://coffeescript.org/)

- [coffeescript-concat](https://www.npmjs.com/package/coffeescript-concat)

- [watch](https://www.npmjs.com/package/watch)

- [jQuery](https://jquery.com/)

- [word-list](https://github.com/sindresorhus/word-list)

# References

- https://github.com/sindresorhus/word-list
