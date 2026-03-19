import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.font_manager as fm

# 엑셀 파일 읽기
file_path = r'C:\Users\user\Desktop\Dscover_study\Main_project\Yealy Sales_amount\Normalization_total_album_sum.xlsx'
data = pd.read_excel(file_path)

# 폰트 설정
font_path = r'C:\Users\user\Desktop\Dscover_study\Main_project\Yealy Sales_amount\BMJUA_ttf.ttf'  # 사용 가능한 한글 폰트 경로로 변경
font_prop = fm.FontProperties(fname=font_path)
plt.rc('font', family=font_prop.get_name())


# 필요한 열 선택
data = data[['artist', 'average_sales_amount']]

# 데이터 정규화
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data[['average_sales_amount']])

# 엘보우 방법을 사용하여 최적의 클러스터 수 찾기
sse = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(data_scaled)
    sse.append(kmeans.inertia_)

# 엘보우 그래프 시각화
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), sse, marker='o')
plt.xlabel('클러스터의 수')
plt.ylabel('Sum of Squared Errors (SSE)')
plt.title('최적의 클러스터를 위한 앨보우 매소드')
plt.xticks(range(1, 11))
plt.grid(True)
plt.show()
