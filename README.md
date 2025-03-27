# automatic phone number selection

Python实现的基于OCR的自动选号工具

## 1. 项目简介

本项目是一个自动选号工具，主要是通过OCR识别图片中的手机号码，然后按照规则进行检查，如果没有符合规则的号码，则会点击换一批按钮继续检查，直到找到符合规则的号码为止。

## 2. 项目结构

```bash
.
├── README.md
├── auto_select_phone_number.py
└── requirements.txt
```

## 3. 默认算法说明

默认的算法是寻找和目标手机号码的差距小于4个数字的号码，逻辑实现在check_number函数中，可以根据实际需求进行修改。

## 4. 使用方法

### 4.1 安装依赖

需要手动安装[Tesseract库](https://github.com/tesseract-ocr/tesseract)，默认路径如下：

```python
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Tesseract安装路径
```

安装Python依赖：

```bash
pip install -r requirements.txt
```

### 4.2 修改配置

```python
# ------------------ 配置区域 ------------------
TARGET_NUMBER = "138XXXXXXXX"  # 目标电话号码示例（必须是11位）

PHONE_REGIONS = [  # 每个电话号码的屏幕区域坐标 (左, 上, 右, 下)
    (2960, 570, 3100, 600),  # 第1个号码区域
    (2960, 630, 3100, 670),  # 第2个号码区域
    (2960, 690, 3100, 720),  # 第3个号码区域
    (2960, 755, 3100, 785),  # 第4个号码区域
    (2960, 820, 3100, 850),  # 第5个号码区域
    (3235, 570, 3375, 600),  # 第6个号码区域
    (3235, 630, 3375, 670),  # 第7个号码区域
    (3235, 690, 3375, 720),  # 第8个号码区域
    (3235, 755, 3375, 785),  # 第9个号码区域
    (3235, 820, 3375, 850),  # 第10个号码区域
]
REFRESH_BUTTON_POS = (3200, 950)  # "换一换"按钮坐标
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Tesseract安装路径
# ---------------------------------------------

```

需要配置的参数包括目标电话号码、每个号码的屏幕区域坐标、"换一换"按钮坐标、Tesseract安装路径（如安装在默认路径无需更改）。

### 4.3 运行

在管理员权限下运行：

```bash
python auto_select_phone_number.py
```
