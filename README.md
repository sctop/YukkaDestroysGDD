# Yukka Destroys Game Development Club 优香摧毁游戏开发部！

此为存储 [ミチルっち「アリスゲーム配信！の巻」](https://www.youtube.com/watch?v=EMKcUr_OjbA) (国内B站翻译版：[【中文字幕/碧蓝档案】小满亲「爱丽丝游戏实况！之卷」](https://www.bilibili.com/video/BV1yV4y1Q7dJ/)) 视频中的直播聊天历史记录的存储库。在该次大型整活中，优香在被描绘成“大魔王优香”后立刻单人单杀游戏开发部，并强制让爱丽丝下了播。

This repository is for storing the live chat history of the video [ミチルっち「アリスゲーム配信！の巻」](https://www.youtube.com/watch?v=EMKcUr_OjbA), in which Yukka shut down the livestream immediately after being illustrated as a "demonic Yukka."

聊天记录使用 [Save Live Streaming Chats for YouTube™](https://chrome.google.com/webstore/detail/save-live-streaming-chats/bcclhcedlelimlnmcpfeiabljbpahnef) 扩展保存。

The live chat was saved through the plug-in [Save Live Streaming Chats for YouTube™](https://chrome.google.com/webstore/detail/save-live-streaming-chats/bcclhcedlelimlnmcpfeiabljbpahnef).

## 如何运行 How to run
除非你想这么干或者你想看看我的代码是怎么跑的，**不然一般情况下没人想亲自跑这些。**

If you would like to do so, or if you want to have a look at how my code works. **Normally though, nobody wants to run themselves.**

- Python 3.x environment
- Python Package `requests` (to install: `pip3 install requests`)


- Python 3.x 环境
- Python软件包 `requests` (安装命令：`pip install requests`)

After all the above 完成以上步骤后

- Run `main.py`

- 运行 `main.py`

## 文件 Files (数据集 Datasets)
### Chats (EMKcUr_OjbA) (original).csv

从扩展中直接保存的数据。由于抓取的过程中反复拉了几次进度条，因此部分数据存在重复的情况。您可使用根目录下的 `main.py` 进行一键去除。

The history data saved directly from the plug-in. Due to changing the progress bar back and forth for a few times when crawling, some data was repeated. You can get rid of those by running the `main.py` script.

### Chats (EMKcUr_OjbA) (original).csv.cn.csv

在过滤完重复数据后，不断向 Google翻译 API发起请求，以此来探测评论的语言后，筛选出仅被识别为中文的评论（含 `zh-cn` 与 `zh-TW` 两种）。

After filtering out the repeated data, out-put comments written in Chinese (both `zh-cn` and `zh-TW`) only by detecting language through requesting Google Translate API constantly.

### Chats (EMKcUr_OjbA) (original).csv.csv

已过滤了的数据。

Filtered data.

### Chats (EMKcUr_OjbA) (original).csv.json

已过滤了的数据，但是以JSON形式提供。

Filtered data, but in JSON format.

## 文件 Files (脚本 Scripts)

Python新手，代码质量比较答辩，还望各位大佬谅解。

I'm new to Python and my code quality is as bad as f##k. Please don't be too strict guys.
