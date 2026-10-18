# 健身刷题助手 — 源码说明（v1.0.3）

单文件 HTML 应用，功能：健身计划/训练计时、跑步（GPS 轨迹）、刷题学习（CSV/JSON 导入，四种模式）、统计记录、日历排班、AI 健身教练、AI 伴侣（DeepSeek）。

## 直接运行
双击 `index.html`，用 Chrome / Edge 打开即可，无需安装任何东西。

## 打包成 Android App
1. 用 HBuilderX 打开本文件夹（不是打开 index.html，是打开文件夹）。
2. 双击 `manifest.json` 核对：AppID `H5E2157D8`，Android 包名 `plus.H5E2157D8`，版本 1.0.3 / 103。
3. 右键工程 → 发行 → 原生App-云打包 → 勾选 Android。
4. 图标与启动图在 `unpackage/res/` 下，可直接被识别。

## 数据存储
浏览器 localStorage：
- `gym_pro_max`：健身/跑步/题库/记录
- `partner_data_v1`：AI 伴侣的会话与设置

支持在「统计 → 数据管理」导出/导入 JSON 备份。

## AI 功能
需要 DeepSeek API Key：进入「AI 健身教练 → 生成计划」，在「🔑 DeepSeek 联网」里填写并保存。
浏览器直连可能受 CORS 限制，打包成 App 后正常。

## 说明
- 这是完整可运行源码，全部逻辑都在 `index.html` 里。
- `unpackage/cache`、`unpackage/release` 是 HBuilderX 的打包缓存，未包含（不影响开发和打包）。