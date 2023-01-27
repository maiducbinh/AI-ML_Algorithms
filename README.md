# AI-ML_Algorithms
## Một số thuật toán cơ bản được sử dụng trong Machine Learning
### KMeans Clustering
#### Sơ lược: 
Trong thuật toán K-means clustering, chúng ta không biết nhãn (label) của từng điểm dữ liệu. Mục đích là làm thể nào để phân dữ liệu thành các cụm (cluster) khác nhau sao cho dữ liệu trong cùng một cụm có tính chất giống nhau.
#### Thuật toán:
Đầu vào: Dữ liệu X và số lượng cluster cần tìm K.

Đầu ra: Các center M và label vector cho từng điểm dữ liệu Y.
1. Chọn K
2. Random các điểm đại diện (center point) cho các cluster
3. Gán các điểm dữ liệu vào các cluster có center gần nó nhất
4. Nếu việc gán dữ liệu vào từng cluster ở bước 2 không thay đổi so với vòng lặp trước đó thì ta dừng thuật toán.
5. Cập nhật center cho từng cluster bằng cách lấy trung bình cộng của tất các các điểm dữ liệu đã được gán vào cluster đó sau bước 2.
6. Quay lại bước 3.

#### Ứng dụng:
Nén dữ liệu (VD: xử lí ảnh)

<img align="right" alt="Coding" width="1000" src="[https://camo.githubusercontent.com/cae12fddd9d6982901d82580bdf321d81fb299141098ca1c2d4891870827bf17/68747470733a2f2f6d69726f2e6d656469756d2e636f6d2f6d61782f313336302f302a37513379765349765f7430696f4a2d5a2e676966](https://dunglai.github.io/public/post-assets/Kmeans/compress1.png)">

Phân loại dữ liệu

### Linear Regression
#### Sơ lược:
Hồi quy tuyến tính là một thuật toán cung cấp mối quan hệ tuyến tính giữa biến độc lập (independent variable) và biến phụ thuộc (dependent variable) để dự đoán kết quả của các sự kiện trong tương lai.
![output_5_1](https://user-images.githubusercontent.com/105925707/215088605-7dfd26d7-e909-4eba-ba84-dfe418bccd6c.png)
