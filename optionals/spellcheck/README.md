Wand
====

A coffeescript text-editor, performs *magic* on your text.



Usage
-----

Open `/dist/index.html` in a browser with local JavaScript support.

This may cause issues however, due to browsers limiting JavaScript
in a local environment.

I would recommend instead building from source,
as per the instructions below, and running the server, with

    npm run server




Building from source
--------------------


### Coffeescript

Coffeescript is a transcompiled language. It compiles to JavaScript, which
is placed in a file called `/dist/dist.js`.

That file is then loaded by the `/dist/index.html`.

Note that the generated JavaScript also relies on jQuery.


### Requirements

To build the project you'll need nodejs and npm.

I recommend v4.0.0 of node or newer, but most versions should work.


#### [Mac/Windows instructions](http://tinyurl.com/qejfed4)

#### Linux Instructions:


    $ cd ~/Downloads # or ~/downloads
    $ wget https://nodejs.org/dist/v4.2.2/node-v4.2.2-linux-x64.tar.gz

    # or if that doesn't work
    $ wget --no-check-certificate https://nodejs.org/dist/v4.2.2/node-v4.2.2-linux-x64.tar.gz

    $ cd /usr/local
    $ sudo tar --strip-components 1 -xzy ~/Downloads/node-v4.2.2-linux-x64.tar.gz
    $ sudo rm -f LICENSE README.md CHANGELOG.md

    # then get up a new terminal and do
    $ node -v
    v4.2.2

  [Source of information](http://www.thegeekstuff.com/2015/10/install-nodejs-npm-linux/)


### Using NPM to fetch the dependencies

    # inside the project directory run:
    $ npm install
    # a note on the warnings is at the bottom of this README.md


npm will read from my `package.json` and handle the coffeescript dependencies.


I'm also using npm as a build tool with it's scripts declaration. If you're
interested you can read more about the process
[here](http://blog.keithcirkel.co.uk/how-to-use-npm-as-a-build-tool/)


You can then run `npm run` to see a list of all the scripts.


Scripts
-------

#### `npm run build`

This will build the coffeescript


#### `npm run server`

Starts a `nano-server` instance which hosts the files in the `dist/` directory
at `127.0.0.1:8123`



Limitations of wand
-------------------

Wand was not designed with real world text editing in mind. It's slower than
most modern text editors and doesn't actually keep track of things like cursor
position or what's currently being rendered.



Dependencies
------------


#### [nodejs](https://nodejs.org/en/)

`nodejs` is used by `coffescript` and `npm`


#### [npm](https://www.npmjs.com/)

`npm` is used as a build tool. It downloads the dependencies, and acts as
somewhat of a build tool by executing the right series of commands.


#### [coffee-script](http://coffeescript.org/)

`coffee-script` is the language Wand is built in. It's takes the nice parts of
JavaScript and adds a few important features that JavaScript was always missing.

It compiles to JavaScript and as such allows me to use JavaScript libraries
such as jQuery.


#### [coffeescript-concat](https://www.npmjs.com/package/coffeescript-concat)

`coffeescript-concat` is a nice little tool to essentially allows me to split
my source into multiple files.


#### [jQuery](https://jquery.com/)

`jQuery` simplifies the task of accessing and modifying the HTML DOM.

It provides some very useful features like cross-compatable event binding,
DOM traversal, and essentially allows me to get to the meat of the assignment
rather than worrying about a lot of things.

`jQuery` is loaded by `index.html` and lives in the `dist/` folder.


#### [nano-server](https://github.com/tsherif/nano-server)

`nano-server` provides a way to host the files locally, which reduces helps me
test them without having to worry about problems that occur when testing
JavaScript sites locally, which stem from browsers trying to protect their
computers from local JavaScript.


#### [octo-wordlist](https://github.com/devoxel/octo_wordlist)

A set of word-lists compiled by me. This project uses the large one.



Note on Warnings
----------------

When you install the project dependencies with npm

    npm WARN package.json Wand@0.1.0 No repository field.
    npm WARN package.json Wand@0.1.0 scripts['server'] should probably be scripts['start'].
    npm WARN package.json Wand@0.1.0 No license field.

This is simply because I haven't defined some stuff in the package.json that
doesn't exist, like a repository or a LICENSE.
