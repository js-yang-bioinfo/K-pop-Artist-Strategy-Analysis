import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.font_manager as fm

# 한글 폰트 설정
font_path = r'C:\Users\user\Desktop\Dscover_study\Main_project\Yealy Sales_amount\BMJUA_ttf.ttf'  # 사용 가능한 한글 폰트 경로로 변경
font_prop = fm.FontProperties(fname=font_path)
plt.rc('font', family=font_prop.get_name())

# 엑셀 파일 읽기
file_path = r'C:\Users\user\Desktop\Dscover_study\Main_project\Yealy Sales_amount\Normalization_total_album_sum.xlsx'
data = pd.read_excel(file_path)

# 필요한 열 선택
data = data[['artist', 'average_sales_amount']]

# 데이터 정규화
scaler = StandardScaler()
new = pd.DataFrame()


data_scaled = scaler.fit_transform(data[['average_sales_amount']])


new['artist'] = data['artist']
new['scaler'] = data_scaled
# print(new[new['artist'] == 'X1 (엑스원)'])
# print(new[new['artist'] == 'Stray Kids (스트레이 키즈)'])
# print(new[new['artist']=='Stray Kids (스트레이 키즈)'])

# 2.2
# 0.3

# # KMeans 클러스터링 수행
# kmeans = KMeans(n_clusters=3, random_state=42)
# data['cluster'] = kmeans.fit_predict(data_scaled)

# # 클러스터링 결과 시각화
# plt.figure(figsize=(18, 6))
# colors = ['g', 'skyblue']
# for cluster in range(2):
#     cluster_data = data[data['cluster'] == cluster]
#     plt.scatter(cluster_data['artist'], cluster_data['average_sales_amount'], c=colors[cluster], label=f'Cluster {cluster}')

# plt.xlabel('아티스트명')
# plt.ylabel('아티스트별 앨범 평균 판매량')
# plt.title('앨범 평균 판매량 클러스터링')
# plt.legend(['앨범 1단계','앨범 2단계'])

# # 회전각 적용
# plt.xticks(rotation=90)
# plt.tight_layout()
# plt.show()

# 정규화된 결과를 기준으로 1보다 큰 아티스트와 작은 아티스트 구분

# 0부터 0.3까지
one = data[(data_scaled[:, 0] <= 0.3)]['artist'].tolist()

# 0.3이상부터 2.2미만까지
two = data[(data_scaled[:, 0] > 0.3) & (data_scaled[:, 0] < 2.2)]['artist'].tolist()

# 2.2이상
three = data[data_scaled[:, 0] >= 2.2]['artist'].tolist()


# 새로운 데이터프레임 생성
comparison_df = pd.DataFrame({'앨범 1단계': pd.Series(one), '앨범 2단계': pd.Series(two),'앨범 3단계': pd.Series(three)})

# 결과 데이터프레임 저장
# output_file_path = r'C:\Users\user\Desktop\Dscover_study\Main_project\Yealy Sales_amount\comparison_test.xlsx'
# data.to_excel(output_file_path, index=False)

# # 새로운 데이터프레임 저장
comparison_output_file_path = r'C:\Users\user\Desktop\Dscover_study\Main_project\Yealy Sales_amount\Classification.xlsx'
comparison_df.to_excel(comparison_output_file_path, index=False)

# print(f'Clustered data saved to {output_file_path}')
# print(f'Comparison data saved to {comparison_output_file_path}')
