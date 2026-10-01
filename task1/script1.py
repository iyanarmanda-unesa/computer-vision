import cv2
import matplotlib.pyplot as plt

input_path = 'input/image1.jpg' 
output_path = 'output/task1_script1.png'

img_bgr = cv2.imread(input_path)

if img_bgr is None:
    print(f"Error: Image '{image_path}' not found.")
else:
    b, g, r = cv2.split(img_bgr)

    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(r, cmap='gray')
    plt.title('Channel Red (Grayscale)')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(g, cmap='gray')
    plt.title('Channel Green (Grayscale)')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(b, cmap='gray')
    plt.title('Channel Blue (Grayscale)')
    plt.axis('off')

    plt.tight_layout()

    plt.savefig(output_path, bbox_inches='tight', dpi=300)
    print(f"Image successfully saved to: {output_path}")

    plt.show()
