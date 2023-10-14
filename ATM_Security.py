import winsound
import cv2
import tkinter as tk


def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
def auto_type(label, text, current_index=0):
    if current_index < len(text):
        label.config(text=text[:current_index + 1])
        current_index += 1
        label.after(100, auto_type, label, text, current_index)
def Scan_Complete():
    scan_complete = tk.Tk()
    scan_complete.title("Main Screen")
    scan_complete.geometry("1600x865")
    scan_complete.state("zoomed")
    center_window(scan_complete)
    # Set the window icon
    icon = tk.PhotoImage(file="Image/Logo.png")  # Replace "icon.png" with your icon file
    scan_complete.iconphoto(True, icon)

    # Load the background image using PhotoImage
    background_image = tk.PhotoImage(file="Image/Bg_FaceScan.png")  # Replace with your image file path

    # Create a label widget to display the background image
    background_label = tk.Label(scan_complete, image=background_image)
    background_label.place(relwidth=1, relheight=1)  # Cover the entire window
    winsound.PlaySound('WARNING.wav', winsound.SND_ASYNC)
    text_to_type = "SCAN CAMPLETE."  # The text you want to animate

    text_label = tk.Label(scan_complete, text="", font=("Digital-7 Mono", 50), bg="#0A0F0B", fg="#7AFF00")
    text_label.pack(pady=20)
    text_label.place(x=560, y=400)

    # Start the typing animation when the application starts
    auto_type(text_label, text_to_type)


    scan_complete.mainloop()
   # scan_complete.destroy()

def main_Screen():
    main_window = tk.Tk()
    main_window.title("Main Screen")
    main_window.geometry("1600x865")
    main_window.state("zoomed")
    center_window(main_window)
    # Set the window icon
    icon = tk.PhotoImage(file="Image/Logo.png")  # Replace "icon.png" with your icon file
    main_window.iconphoto(True, icon)

    # Load the background image using PhotoImage
    background_image = tk.PhotoImage(file="Image/Bg_FaceScan.png")  # Replace with your image file path

    # Create a label widget to display the background image
    background_label = tk.Label(main_window, image=background_image)
    background_label.place(relwidth=1, relheight=1)  # Cover the entire window
    winsound.PlaySound('WARNING.wav', winsound.SND_ASYNC)
    text_to_type = "WARNING..."  # The text you want to animate

    text_label = tk.Label(main_window, text="", font=("Digital-7 Mono", 50), bg="#000", fg="#FF4B12")
    text_label.pack(pady=20)
    text_label.place(x=650, y=510)

    # Start the typing animation when the application starts
    auto_type(text_label, text_to_type)

    main_window.mainloop()
    main_window.destroy()

def Camera():
    winsound.PlaySound('s1.wav', winsound.SND_ASYNC)
    video = cv2.VideoCapture(0)
    video.set(3, 640)
    video.set(4, 480)
    imgBackground = cv2.imread('Image/Bg_FaceScan.png')
    facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    count = 0

    while True:
        ret, frame = video.read()
        faces = facedetect.detectMultiScale(frame, 1.3, 5)
        for x, y, w, h in faces:
            count = count + 1
            #winsound.PlaySound('Alert.wav', winsound.SND_ASYNC)
            name = 'G:\Final Project\ATM Security Final Project\ATM-Security-Final-Project\Capture_Image/' + str(count) + '.jpg'

            print("Creating Images........." + name)
            cv2.imwrite(name, frame[y:y + h, x:x + w])
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.rectangle(frame, (x, y - 40), (x + w, y), (0, 255, 0), -1)

            cv2.putText(frame, "Clear Face", (x + 15, y - 15), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.75, (255, 255, 255), 1)


        #cv2.imshow("WindowFrame", frame)
        imgBackground[50:50 + 480, 50:50 + 640] = frame
        cv2.imshow("webcam", frame)
        cv2.imshow("Face Attendance", imgBackground)
        cv2.waitKey(50)
        if count > 5:
            Scan_Complete()
            break

    cv2.waitKey(1)
    Camera_Window = tk.Tk()
    Camera_Window.title("Auto Change Application")
    Camera_Window.geometry("1600x865")
    Camera_Window.state("zoomed")
    video.release()
    cv2.destroyAllWindows()


def auto_type(label, text, current_index=0):
    if current_index < len(text):
        label.config(text=text[:current_index + 1])
        current_index += 1
        label.after(100, auto_type, label, text, current_index)
def auto_change_screen():
    current_label_index = 0
    labels = ["USER DETECTED", "PROCESSING....", "CAMERA STARTING...", "PROCESSING....","Loading..."]
    num_labels = len(labels)

    def update_label():
        nonlocal current_label_index
        current_label_index = (current_label_index + 1) % num_labels
        text_label.config(text=labels[current_label_index])
        text_label.after(5000, update_label)

        if current_label_index >= 3:
            root.destroy()
            Camera()


           # messagebox.showerror("Error", "Camera work pending...")



    text_to_type = "CAMERA STARTING..."
    text_label = tk.Label(root, text=labels[current_label_index], font=("Digital-7 Mono", 60),bg="#011F44", fg="#007CFF")
    text_label.pack(pady=20)
    text_label.place(x=450, y=340)
    #auto_type(text_label, labels)

    text_label.after(5000, update_label)

root = tk.Tk()
root.title("Auto Change Application")
root.geometry("1600x865")
root.state("zoomed")
background_image = tk.PhotoImage(file="Image/Bg_FaceScan.png")  # Replace with your image file path

# Create a label widget to display the background image
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)  # Cover the enti

#winsound.PlaySound('s1.wav', winsound.SND_ASYNC)

auto_change_screen()
center_window(root)
root.mainloop()

