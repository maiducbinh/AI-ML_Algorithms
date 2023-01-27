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

![image](https://user-images.githubusercontent.com/105925707/215094530-2cb57eeb-66c4-4092-bbfb-14347953accd.png)

![image](https://user-images.githubusercontent.com/105925707/215094551-e91c1bac-845f-4f7d-81e6-b896b1d9027b.png)

Ảnh trên: 900 KB, ảnh dưới (K=16 color): 70KB


Phân loại dữ liệu

![image](https://user-images.githubusercontent.com/105925707/215094486-4b53c0a8-089f-48a0-a256-cd1384ffc9fa.png)


### Linear Regression
#### Sơ lược:
Hồi quy tuyến tính là một thuật toán cung cấp mối quan hệ tuyến tính giữa biến độc lập (independent variable) và biến phụ thuộc (dependent variable) để dự đoán kết quả của các sự kiện trong tương lai.
![output_5_1](https://user-images.githubusercontent.com/105925707/215088605-7dfd26d7-e909-4eba-ba84-dfe418bccd6c.png)
