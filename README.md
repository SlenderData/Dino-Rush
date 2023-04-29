# 🦖 Dino-Rush

使用 Python 复刻的 Google Chrome 小游戏。

## ✨ 主要特点

- 使用简单的操作（空格键或向上键跳跃，向下键下蹲）控制恐龙的动作
- 随机生成云朵、仙人掌和翼龙作为障碍物
- 实时更新得分和最高分，并提供相应的音效提示
- 使用开源像素绘画软件 `Asprite` 重新绘制了恐龙等界面元素
- 使用经典的像素风格街机游戏字体 `Joystix Monospace` 渲染字符元素
- 使用 Python 集成的 `SQLite` 来存储每次游玩结束时的 UNIX 时间戳及分数信息

## 🖼️ 游戏截图

在游戏运行过程中，玩家可以看到恐龙、障碍物、云朵以及当前得分和最高分。

![screenshot_1](screenshots/screenshot_1.png)

![screenshot_2](screenshots/screenshot_2.png)

![screenshot_3](screenshots/screenshot_3.png)

## ❓ 如何运行游戏

1. 确保已安装 `Python` 和 `Pygame` 库
2. 克隆或下载本仓库的代码文件
3. 在终端或命令行界面中，进入代码文件所在的目录
4. 运行以下命令启动游戏：

   ```shell
   python Game.py
   ```

## 🎮 游戏操作说明

- 按下空格键或向上键：恐龙跳跃
- 按住向下键：恐龙下蹲
- 松开向下键：恐龙恢复站立状态

## ⌨️ 开发环境

- **操作系统**
  - Windows
  - macOS
  - Linux
- **Python 环境**
  - Python 3.11
- **使用到的软件**
  - [PyCharm Professional Edition](https://www.jetbrains.com/pycharm/)
  - [Aseprite](https://www.aseprite.org/)
    - [GitHub](https://github.com/aseprite/aseprite/)
    - [Steam](https://store.steampowered.com/app/431730/Aseprite/)
- **Python 需要额外添加的软件包**
  - Pygame

## 📄 使用许可

[MIT](LICENSE) © SlenderData
