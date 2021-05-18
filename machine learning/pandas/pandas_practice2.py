import pandas as pd
import numpy as np

# 데이터 분석

# 파일 읽기
# sep : 구분자
# data = pd.read_csv("data/lending-club-loan-data/loan.csv", sep=",")

# 데이터의 행, 열 확인
# data.shape

# 데이터의 columns 확인
# data.cloumns

# 필요한 열만 떼어내기
# df = data[["loan_amnt", "loan_status", "grade", "int_rate", "term"]]

# 앞, 뒤 5개 행만 확인
# df.head()
# df.tail()

# 데이터가 범주형인지 아닌지 확인 (중복 제거)
# df["loan_status"].unique()
# df["grade"].unique()
# df["term"].unique()

# NaN을 포함한 행 제거
# df.dropna(how="any")

# 각 기간에 따른 대출총액의 합을 저장할 딕셔너리
# term_to_loan_amnt_dict = {}

# 대출기간(중복x)
# uniq_terms = df["term"].unique()

# 대출 기간별 총액 대출총액 구하기
# for term in uniq_terms:
#     loan_amnt_sum = df.loc[df["term"] == term, "loan_amnt"].sum()
#     key : 대출 기간, value : 대출 총액
#     term_to_loan_amnt_dict[term] = loan_amnt_sum

# 데이터를 편하게 관리하기 위해 Series에 담아주기
# term_to_loan_amnt = pd.Series(term_to_loan_amnt_dict)

# 중복없는 기준열 변수 생성
# total_status_category = df["loan_status"].unique()
