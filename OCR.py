from PIL import Image
import pytesseract

# 指定 Tesseract 的路径
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'  # 根据实际路径调整

# 读取图像文件
image_path = '/Users/jinanzai/东北大学/大创/论文/药品识别/medicineFinder/img/test4.jpg'
image = Image.open(image_path)

# 使用 pytesseract 进行 OCR 识别
text = pytesseract.image_to_string(image, lang='chi_sim')

# 打印识别的文本
print(text)
