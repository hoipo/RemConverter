RemConverter
-------------

一个CSS的px值和rem值相互转换的Sublime Text插件。
只支持Sublime Text 3，支持HTML,CSS,LESS,SCSS和SASS。

这个插件可以在HTML代码中解析出style标签中的CSS，然后把px值转成rem值，或者是rem转px。(*^__^*) 

## 安装

因为功能还不完善，暂且不想提交给package control.暂时只能下载我的项目源码来安装
* 下载我的项目, 比如. `git clone https://github.com/hoipo/RemConverter.git` 或者直接在github主页下载zip包
* 进入`packages`目录: Sublime Text -> Preferences -> Browse Packages...
* 复制`RemConverter`文件夹到 `packges`目录
* 可能你要重启一下你的Sublime Text

## 使用方法

* 按 `alt+z` 把px转换成rem.
* 按 `alt+x` 把rem转换成px.

如果你不想你的px或rem被这个插件转换了，那就用大写的`PX`或`REM`吧，插件会跳过他们的,比如:

```css
margin-top:30PX;
```

## 配置

配置文件：Sublime Text -> Preferences -> Package Settings -> remConverter

* `remUnit` - 一个rem等于多少个px,默认值 20px.

快捷键配置：Sublime Text -> Preferences -> Key Bingdings

把以下配置复制到Key Bingdings即可更改快捷键:

```js
[
    { "keys": ["alt+z"], "command": "rem_converter", "args":{"toRem":true}  },
    { "keys": ["alt+x"], "command": "rem_converter", "args":{"toRem":false}  }
]
```

# 协议

Copyright (c) 2016 Hoipo Cheung

Licensed under the MIT license.

See LICENSE for more info.

