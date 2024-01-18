import tkinter as tk
from PIL import Image, ImageTk

def upload_resim():
    global new_window
    global img2
    new_window = tk.Toplevel()
    new_window.title('pixel')
    new_window.geometry(f"300x340+500+0")
    img2 = Image.open("pikachu.jpg")
    #img2 = Image.open("/home/rd-pi/rd_share/pikachu.jpg")
    img2 = img2.resize((300, 300), Image.LANCZOS)
    photo2 = ImageTk.PhotoImage(img2)
    label2 = tk.Label(new_window, image=photo2)
    label2.image = photo2
    label2.place(x=0,y=40)

    label = tk.Label(new_window, text="Hazırla butonuna basınız",bg="#5C6BC0", fg="black", font=("Arial", 20))
    label.pack()


def pixel_ayirma():
    new_window.destroy()
    import numpy as np
    import cv2
    #img2=cv2.imread("/home/rd-pi/rd_share/wait.jpg")
    cv2.imshow("resim", img2)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
    img = cv2.imread('pikachu.jpg')
    #img = cv2.imread('/home/rd-pi/rd_share/pikachu.jpg')
    resized_img = cv2.resize(img, (650, 650), interpolation=cv2.INTER_CUBIC)
    #cv2.imshow("resim", resized_img)
    #cv2.waitKey(0)
    # cv2.imwrite("C:/Users/PC/Pictures/Screenshots/karedesenler1.jpg",resized_img)
    mavi = np.array([0, 0, 255])
    kirmizi = np.array([255, 0, 0])
    sari = np.array([0, 255, 255])
    yesil = np.array([0, 255, 0])
    siyah = np.array([0, 0, 0])
    beyaz = np.array([255, 255, 255])
    renk_list = [mavi, kirmizi, yesil, siyah, beyaz, sari]

    height, width, channels = resized_img.shape
    # print(resized_img.shape)

    block_size1 = 50
    block_size = 50
    blocks = []
    blocks1 = []
    pixel = []
    rows = []
    rows1 = []
    
    def buyuk_parca():
        for i in range(0, height, block_size1):
            for j in range(0, width, block_size1):
                block1 = resized_img[i:i + block_size1, j:j + block_size1]
                blocks1.append(block1)

    def bolme():
        global width1
        for i in blocks1:
            height1, width1, channels1 = i.shape

            for a in range(0, height1, block_size):
                for b in range(0, width1, block_size):
                    block = i[a:a + block_size, b:b + block_size]
                    histogram = cv2.calcHist([block], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])

                    max_value = np.unravel_index(histogram.argmax(), histogram.shape)
                    dominant_color = np.array([max_value[0], max_value[1], max_value[2]])
                    max1 = max_value[0]
                    max2 = max_value[1]
                    max3 = max_value[2]
                    renk = siyah
                    for k in renk_list:
                        result = abs(k[0] - max1) + abs(k[1] - max2) + abs(k[2] - max3)
                        renk_result = abs(renk[0] - max1) + abs(renk[1] - max2) + abs(renk[2] - max3)
                        if result < renk_result:
                            renk = k
                    new_values = np.zeros_like(block)
                    new_values[:, :, ] = renk[0], renk[1], renk[2]
                    block = new_values
                    blocks.append(block)
                    print(block.shape)
                    # cv2.imshow("resim",block)
                    # cv2.waitKey(0)
                    
    def buyuk_parca_birlestirme():

        for i in range(0, len(pixel), int(width / block_size1)):
            row1 = np.concatenate(pixel[i:i + int(width / block_size1)], axis=1)
            rows1.append(row1)

    buyuk_parca()
    bolme()
    for c in range(0, len(blocks), int(width1 / block_size)):
        print(c)
        row = np.concatenate(blocks[c:c + int(width1 / block_size)], axis=1)
        if row.shape != (5, 50, 3):
            print(row.shape)
        rows.append(row)

    for d in range(0, len(rows), int(width1 / block_size)):
        result = np.concatenate(rows[d:d + int(width1 / block_size)], axis=0)
        if result.shape != (50, 50, 3):
            print(result.shape)
            cv2.imshow("resim", result)
            cv2.waitKey(0)
        pixel.append(result)

    buyuk_parca_birlestirme()

    for j in range(0, len(rows1), int(height / block_size1)):
        result1 = np.concatenate(rows1[j:j + int(width / block_size1)], axis=0)
    cv2.imshow("resim", result1)
    cv2.waitKey(0)
def button():
    upload_button = tk.Button(canvas, text="YÜKLE", bg="#5C6BC0", fg="black", font=("Arial", 20), command=upload_resim)
    upload_button.place(x=750, y=320, anchor="center")

    upload_button = tk.Button(canvas, text="HAZIRLA", bg="#5C6BC0", fg="black", font=("Arial", 20), command=pixel_ayirma)
    upload_button.place(x=750, y=480, anchor="center")

form = tk.Tk()
form.title('pixel')
screen_width = form.winfo_screenwidth()
screen_height = form.winfo_screenheight()
form.geometry(f"{screen_width}x{screen_height}+0+0")

#img1 = Image.open("/home/rd-pi/rd_share/bum.jpg")
#img1 = img1.resize((screen_width, screen_height), Image.LANCZOS)
#photo = ImageTk.PhotoImage(img1)

# Canvas oluştur
canvas = tk.Canvas(form, width=screen_width, height=screen_height)
canvas.pack()

# Resmi canvas'a ekle
#canvas.create_image(0, 0, image=photo, anchor='nw')

button()

form.mainloop()