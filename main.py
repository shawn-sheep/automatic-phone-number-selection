import pyautogui
import pytesseract
from PIL import Image
import time

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

# 初始化OCR
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH


def preprocess_image(image):
    """图像预处理：灰度化 + 增强对比度"""
    image = image.convert("L")  # 转为灰度图
    return image.point(lambda x: 0 if x < 200 else 255)  # 二值化


def extract_phone_number(text):
    """从OCR结果中提取11位电话号码"""
    digits = "".join(filter(str.isdigit, text))
    return digits if len(digits) == 11 else None


def calculate_difference(num1, num2):
    """计算两个号码的差异位数"""
    return sum(n1 != n2 for n1, n2 in zip(num1, num2))


def check_number(number, target) -> bool:
    """检查号码是否符合条件"""
    diff = calculate_difference(number, TARGET_NUMBER)
    print(f"识别到号码: {number} (差异 {diff} 位)")
    if diff <= 4:
        print(f"✅ 找到符合条件的号码: {number}")
        return True
    else:
        return False


def find_phone_numbers():
    """主逻辑：识别号码并检查差异"""
    for region in PHONE_REGIONS:
        # 截图并预处理
        x, y, w, h = region[0], region[1], region[2] - region[0], region[3] - region[1]
        screenshot = pyautogui.screenshot(region=(x, y, w, h))
        # screenshot.show()  # 调试用
        processed_img = preprocess_image(screenshot)
        # processed_img.show() # 调试用
        # OCR识别
        text = pytesseract.image_to_string(processed_img, config="--psm 6")
        number = extract_phone_number(text)

        if number:
            global counter
            counter += 1
            if check_number(number, TARGET_NUMBER):
                return True
        else:
            print("识别异常，识别到的文本:", text)
    return False


if __name__ == "__main__":
    try:
        global counter  # 计数器
        counter = 0
        while True:
            if find_phone_numbers():
                break
            print("未找到匹配号码，点击换一换...")
            print(f"已尝试次数: {counter}")
            pyautogui.click(*REFRESH_BUTTON_POS)
            time.sleep(3)  # 等待新号码加载
    except KeyboardInterrupt:
        print("\n程序已终止")
