import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import matplotlib.font_manager as fm
from matplotlib import rc
import os


# 엑셀 파일 읽기
file_path = r'C:\Users\user\Desktop\Dscover_study\Main_project\Weekly_rank\rank data.xlsx'
data = pd.read_excel(file_path)

# 모든 열 이름을 문자열로 변환
# data.columns = data.columns.astype(str)

# 데이터 정규화
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# 엘보우 방법을 사용하여 최적의 클러스터 수 찾기
sse = []
range_n_clusters = range(1, 11)
for n_clusters in range_n_clusters:
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(data_scaled)
    sse.append(kmeans.inertia_)

# 엘보우 그래프 시각화
plt.figure(figsize=(10, 6))
plt.plot(range_n_clusters, sse, marker='o')
plt.xlabel('클러스터 수')
plt.ylabel('SSE')
plt.title('엘보우 방법을 사용한 최적의 클러스터 수 찾기')
plt.xticks(range_n_clusters)
plt.grid(True)
plt.show()

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
plt.xlabel('클러스터 수')
plt.ylabel('실루엣 계수')
plt.title('최적의 클러스터 수 찾기를 위한 실루엣 메소드')
plt.xticks(range_n_clusters)
plt.grid(True)
plt.show()

# 최적의 클러스터 수로 KMeans 클러스터링 수행 (예시로 4를 선택)
optimal_n_clusters = 4
kmeans = KMeans(n_clusters=optimal_n_clusters, random_state=42)
data['cluster'] = kmeans.fit_predict(data_scaled)

# 클러스터링 결과 시각화
plt.figure(figsize=(10, 6))
colors = ['gray', 'lightgray', 'darkgray', 'dimgray']
for cluster in range(optimal_n_clusters):
    cluster_data = data[data['cluster'] == cluster]
    plt.scatter(cluster_data.index, cluster_data.iloc[:, :-1].mean(axis=1), c=colors[cluster], label=f'Cluster {cluster}')

plt.xlabel('Index')
plt.ylabel('Average Value')
plt.title('Clustering of Data Points')
plt.legend()
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# 결과 데이터프레임 저장
output_file_path = r'C:\Users\user\Desktop\Dscover_study\Main_project\Weekly_rank\Clustered_Data.xlsx'
data.to_excel(output_file_path, index=False)

print(f'Clustered data saved to {output_file_path}')
