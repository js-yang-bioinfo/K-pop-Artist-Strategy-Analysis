import pandas as pd

# 엑셀 파일 읽기
df = pd.read_excel(r'C:\Users\user\Desktop\Dscover_study\Main_project\Weekly_rank\Final data.xlsx')

# 빈 딕셔너리 생성
data_dict = {}

for i in range(0, 4408):
    # 해당 행에서 0 값을 제외하고 값을 리스트로 가져오기
    values_list = df.iloc[i, 3:][df.iloc[i, 3:] != 0].dropna().values.tolist()

    # 해당 행의 인덱스(행 이름) 가져오기
    artist_name = df['artist'][i]
    index_name = artist_name

    # 딕셔너리에 데이터 추가
    if index_name in data_dict:
        data_dict[index_name].extend(values_list)
    else:
        data_dict[index_name] = values_list

# 딕셔너리를 데이터프레임으로 변환
df_new = pd.DataFrame.from_dict(data_dict, orient='index')

# 엑셀 파일로 저장
df_new.to_excel(r'C:\Users\user\Desktop\Dscover_study\Main_project\Weekly_rank\rank data.xlsx')

print("완료")
