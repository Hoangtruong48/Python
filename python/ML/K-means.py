import numpy as np
from sklearn.cluster import KMeans
from PIL import Image
import cv2


def image_segmentation(image_path, num_clusters):
    # Đọc ảnh và chuyển đổi thành mảng numpy
    image = Image.open(image_path)
    image_array = np.array(image)

    # Định hình lại mảng ảnh thành một mảng hai chiều
    height, width, _ = image_array.shape
    image_array = image_array.reshape(height * width, -1)

    # Áp dụng thuật toán K-means
    kmeans = KMeans(n_clusters=num_clusters, random_state=0)
    kmeans.fit(image_array)

    # Dự đoán nhãn cho từng điểm dữ liệu
    labels = kmeans.predict(image_array)

    # Tạo mảng ảnh phân đoạn từ các nhãn
    segmented_image_array = np.zeros_like(image_array)
    for i in range(num_clusters):
        segmented_image_array[labels == i] = kmeans.cluster_centers_[i]

    # Định hình lại mảng ảnh phân đoạn thành kích thước ban đầu
    segmented_image_array = segmented_image_array.reshape(height, width, -1)

    # Tạo ảnh phân đoạn từ mảng numpy
    segmented_image = Image.fromarray(segmented_image_array.astype('uint8'))

    return segmented_image


# Gọi hàm phân đoạn ảnh
image_path = "C:\\Users\\acer\\OneDrive\\Pictures\\4.jpg"
num_clusters = 5
segmented_image = image_segmentation(image_path, num_clusters)

# Chuyển đổi ảnh phân đoạn thành định dạng OpenCV (BGR)
segmented_image_cv = cv2.cvtColor(np.array(segmented_image), cv2.COLOR_RGB2BGR)

# Hiển thị ảnh gốc và ảnh phân đoạn bằng OpenCV
image = cv2.imread(image_path)
cv2.imshow("Original Image", image)
cv2.imshow("Segmented Image", segmented_image_cv)
cv2.waitKey(0)
cv2.destroyAllWindows()