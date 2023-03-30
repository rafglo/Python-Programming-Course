from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt

def watermark(in_path, w_path, out_path):
    """
    Function
    Funkcja nakładająca znak wodny na obraz

    Input:
    in_path(string) - ścieżka do obrazu
    w_path(string) - ścieżka do znaku wodnego
    out_path(string) - ścieżka wyjściowa obrazu z nałożonym znakiem wodnym

    """
    img = Image.open(in_path)
    wm = Image.open(w_path)
    w, h = img.size
    wm.thumbnail((w//10, h//10))
    alpha = wm.convert("L").point(lambda w: min(w, 200))
    wm.putalpha(alpha)
    img_with_wm = Image.new('RGBA', (w, h), (0,0,0,0))
    img_with_wm.paste(img, (0,0))
    img_with_wm.paste(wm, (w//2,h//2), mask=alpha)
    img_with_wm = img_with_wm.convert("RGB")
    img_with_wm.save(out_path)
    img_with_wm.show()
