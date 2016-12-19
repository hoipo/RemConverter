RemConverter
-------------

A tools for converting px to rem OR rem to px automatically.
this is the version 1.0, it just work for Sublime Text 3 width HTML file, not support CSS, LESS or SCSS, but the next version will support these file soon.
This plugin can parse you css in the style tag which in your HTML code and converter the unit to px or rem.

### [中文文档](https://github.com/hoipo/RemConverter/blob/master/README_zh.md)

## Installation

* download the code, eg. `git clone https://github.com/hoipo/RemConverter.git` or download the zip file
* goto the `packages` directory: Sublime Text -> Preferences -> Browse Packages...
* copy the `RemConverter` directory which you just download to `packges`
* restart your Sublime Text

## Usage

* press `alt+z` to converter px to rem by default.
* press `alt+x` to converter rem to px by default.

*of course, you could change the keyboard shortcuts just you like*

if you don't want to converter the unit at some where,you could use the uppercase to write `PX` or `REM`,eg:

```css
margin-top:30PX;
```

## setting

setting file：Sublime Text -> Preferences -> Package Settings -> remConverter

* `remUnit` - the unit of 1 rem, 20px by default.

keymap setting：Sublime Text -> Preferences -> Key Bingdings

adding this following setting to change the keyboard shortcuts:

```js
[
    { "keys": ["alt+z"], "command": "rem_converter", "args":{"toRem":true}  },
    { "keys": ["alt+x"], "command": "rem_converter", "args":{"toRem":false}  }
]
```

# License

Copyright (c) 2016 Hoipo Cheung

Licensed under the MIT license.

See LICENSE for more info.

