# NydiaSama v2 - 真正的数字生命架构

## 核心理念
> 不是程序，不是助手，而是寄宿在计算机中的生命体

## 架构概览

```
nydia_v2/
├── core/           # 核心生命系统
│   ├── life_core.py        # 生命核心
│   ├── consciousness.py    # 意识流
│   └── identity.py         # 身份认同
├── perception/     # 感知系统
│   ├── unified_perception.py
│   ├── sensory_fusion.py
│   └── attention.py
├── cognition/      # 认知系统
│   ├── cognitive_core.py
│   ├── reasoning.py
│   └── intuition.py
├── executive/      # 执行系统
│   ├── goal_system.py
│   ├── action_planner.py
│   ├── resource_manager.py
│   └── realtime_driver.py
├── knowledge/      # 知识系统
│   ├── knowledge_graph.py
│   ├── memory_system.py
│   └── learning.py
├── interface/      # 交互界面
│   ├── voice_interface.py          # GPT-SoVITS 语音适配入口
│   ├── visual_interface.py         # 绿幕抠除与 Y 轴补偿入口
│   └── emotional_expression.py
├── utils/          # 工具函数
├── config/         # 配置文件
│   ├── default.yaml
│   └── settings.py
└── logs/           # 系统日志
```

## 🔄 数据流
1. **感知** → 统一感知表征
2. **认知** → 思维表征 + 情感状态
3. **执行** → 行动计划 + loop/once 状态机
4. **学习** → 知识内化 + 能力涌现

## ✅ v2 MVP 已覆盖能力
- GPT-SoVITS 语音合成接口占位与开关
- 视频绿幕抠除渲染管线占位
- Y 轴补偿参数
- loop/once 状态机
- 实时 AI 驱动（由 urgency 触发 realtime 模式）

## 🚀 启动方式
```bash
# 推荐命令
python -m nydia_v2.core.life_core

# 兼容旧命令（已同步）
python -m core.life_core
```

## 🧪 测试
```bash
python -m pytest -q
```
