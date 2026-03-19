import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import matplotlib.font_manager as fm
from matplotlib import rc
import os

# 엑셀 파일 읽기
file_path = r'C:\Users\user\Desktop\Dscover_study\Main_project\Yealy Sales_amount\Normalization_total_album_sum.xlsx'
data = pd.read_excel(file_path)

# 폰트 설정
font_path = r'C:\Users\user\Desktop\Dscover_study\Main_project\Yealy Sales_amount\BMJUA_ttf.ttf'
if not os.path.exists(font_path):
    raise FileNotFoundError(f"Font file not found at {font_path}")

font_prop = fm.FontProperties(fname=font_path)
rc('font', family=font_prop.get_name())

# 필요한 열 선택
data = data[['artist', 'average_sales_amount']]

# 데이터 정규화
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data[['average_sales_amount']])

# 실루엣 계수를 사용하여 최적의 클러스터 수 찾기
silhouette_scores = []
range_n_clusters = range(2, 11)  # 클러스터 수는 2에서 10까지 시도

for n_clusters in range_n_clusters:
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(data_scaled)
    silhouette_avg = silhouette_score(data_scaled, cluster_labels)
    silhouette_scores.append(silhouette_avg)

# 실루엣 계수 그래프 시각화
plt.figure(figsize=(10, 6))
plt.plot(range_n_clusters, silhouette_scores, marker='o')
plt.xlabel('클러스터의 수')
plt.ylabel('실루엣 계수')
plt.title('최적의 클러스터수를 위한 실루엣 메소드')
plt.xticks(range_n_clusters)
plt.grid(True)
plt.show()
