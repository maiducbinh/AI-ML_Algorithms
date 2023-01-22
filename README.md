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
