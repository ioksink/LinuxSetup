---
title: "旅外搜尋引擎調整"
date: 2025-03-15
draft: false
---

在海外用中文搜尋東西的時候似乎比較容易遇到簡體中文的搜尋結果，偏偏這些簡體中文的結果很常品質不佳或是根本不是我想找的，看到簡體中文就頭痛，有時候還會不小心點進去，氣得想把電腦丟出去（欸先不要），所以產生了這篇筆記調整Google大神。

**Chrome**

Settings > Privacy and security > Site settings > Insecure content > Customised behaviour: Not allowed to show insecure content [Add] 新增不想看到百度、淘寶等就可以在搜尋結果中擋掉這些來源

進入Settings > 左側選單 Search engine > Site search [Add]:

Name/Shortcut 可自訂，URL: http://www.google.com.tw/search?q=%s&hl=zh-TW&lr=-lang_zh-CN

翻譯：search?q=%s 搜尋字串，hl=zh-TW 界面為臺灣中文，lr=-lang_zh-CN 不要(-)中國中文的結果。關於搜尋結果來源的語言也可以用這個參數直接指定，例如lr=lang_zh-TW%7Clang_de%7Clang_ja
- 繁體中文  lang_zh-TW
- 簡體中文  lang_zh-CN
- 英文  lang_en
- 日文  lang_ja
- 法文  lang_fr
- 德文  lang_de
- 韓文  lang_ko

參考 https://forum.gamer.com.tw/Co.php?bsn=60030&sn=2117484

**Firefox**

在小狐狸身上要用外掛才能編輯 Address bar 的搜尋引擎URL: Search Engines Helper https://addons.mozilla.org/....../search....../......

ChatGPT 幫我寫的URL長這樣：https://www.google.com/search?q=%s+-site:.cn+-site:baidu.com+-site:weibo.com+-site:qq.com+-site:163.com+-site:jd.com+-site:taobao.com+-site:xinhua.net+-site:cctv.com&lr=-lang_zh-CN 不過搜尋字串會自動加上後面這些tag在看搜尋結果界面的搜尋欄的時候有點亂。所以改用底下這個小狐狸外掛來擋掉一一些不想看見的來源，在搜尋結果界面上也可以直接點選 Block this site，使用起來蠻直觀的：

uBlacklist https://addons.mozilla.org/....../addon/ublacklist/......

uBlacklist > options > Sites blocked from appearing in Google search results:

```
*://*.cn/*
*://*.baidu.com/*
*://*.tiktok.com/*
*://*.taobao.com/*
*://*.weibo.com/*
*://*.qq.com/*
*://*.163.com/*
*://*.jd.com/*
*://*.xinhua.net/*
*://*.cctv.com/*
```

**google.com**

直接到Google搜尋的首頁 >右下角設定 >選單最上面的 Search setting >進入之後左邊列表 Other settings >Language and region >Results language filter 可以直接指定搜尋結果想要的語言... 不過這個方法不能過濾中國來源的.com結尾網站。手機上Safari的搜尋結果需要用這個方法。

還沒有嘗試過手機上的Chrome，有經驗的人可以補充一下。