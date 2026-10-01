import cv2
import matplotlib.pyplot as plt

input_path = 'input/image3.jpg'
output_path = 'output/task1_script2.png'

img_bgr = cv2.imread(input_path)

if img_bgr is None:
    print(f"Error: Image '{image_path}' not found.")
else:
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    plt.figure(figsize=(12, 5))


    plt.subplot(1, 2, 1)
    plt.imshow(img_gray, cmap='gray')
    plt.title('Grayscale Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.hist(img_gray.ravel(), bins=256, range=[0, 256], color='black', alpha=0.75, label='Pixel Frequency')
    plt.title('Pixel Intensity Histogram')
    plt.xlabel('Pixel Intensity (0 = Dark, 255 = Bright)')
    plt.ylabel('Number of Pixels (Frequency)')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.legend(loc='upper right')

    plt.tight_layout()

    plt.savefig(output_path, bbox_inches='tight', dpi=300)
    print(f"Image successfully saved to: {output_path}")

    plt.show()
