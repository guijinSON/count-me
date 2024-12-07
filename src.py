import math
from scipy.stats import norm


def cal_height(sex,minh,maxh):
    # 2015.05 ~ 2015.12, 16 ~ 69세 남녀 6,413명(남성 3,192명, 여성 3,221명)의 데이터에서 추출
    if sex=='boyfriend 👨🏻':
        mean = 172.2437
        var = 35.37629
    else:
        mean = 158.7105
        var = 32.90762
    sd = math.sqrt(var)
 
    prob = norm.cdf(maxh, loc=mean, scale=sd) - norm.cdf(minh, loc=mean, scale=sd)
    return prob

def cal_age(min_age, max_age):
    # Kosis 연령별 데이터 2024년 기준 linear interpolation 진행
    # Age bracket data (most recent distribution)
    # Each entry: (bracket_min, bracket_max, probability)
    # Probabilities are in decimal form, e.g., 12.4% = 0.124
    age_brackets = [
        (0, 9, 0.124),
        (10, 19, 0.137),
        (20, 29, 0.135),
        (30, 39, 0.141),
        (40, 49, 0.140),
        (50, 59, 0.131),
        (60, 69, 0.098),
        (70, 79, 0.061),
        (80, 89, 0.033)  # Assuming 80–89 as a bracket for simplicity
    ]
    
    # Ensure min_age <= max_age
    if min_age > max_age:
        min_age, max_age = max_age, min_age
    
    total_probability = 0.0
    
    for (b_min, b_max, b_prob) in age_brackets:
        # Check if this bracket overlaps with [min_age, max_age]
        if b_max < min_age or b_min > max_age:
            # No overlap
            continue
        
        # Find overlap region
        overlap_start = max(b_min, min_age)
        overlap_end = min(b_max, max_age)
        
        # Calculate the fraction of this bracket covered
        bracket_range = (b_max - b_min + 1)
        overlap_range = (overlap_end - overlap_start + 1)
        
        # Fraction of this bracket that is within the desired range
        fraction = overlap_range / bracket_range
        
        # Add the fraction of the bracket's probability
        total_probability += b_prob * fraction
    
    return total_probability

def cal_education(edu):
# 지표나라 국민교육수준(학력별 인구분포)
# - Total 대입응시자수 (test takers): 444,870 (2024년 기준)
# - 인서울 4년제 이상: 86,331 seats total (~19.4% of 444,870)
# - Individual university admissions (seats):
#   - 서울대: 3,472
#   - 연세대: 3,788
#   - 고려대: 4,273
#   - 서강대: 1,718
#   - 성균관대: 3,678
#   - 한양대: 3,294
#   - 중앙대: 3,841
#   - 경희대: 5,413
#   - 한국외대: 3,643
#   - 시립대: 1,843
    
    edud = {"고졸 이상":0.91, "대학 이상":0.53,"인서울 4년제 이상":0.194,
     "서연고서성한중경외시":0.0786, "서연고서성한":0.0455, "서연고":0.0259, "연대 이상":0.0163}
    return edud[edu]


def cal_mbti(mbtis):
    mbti_distribution = {
    "INFP": 0.1339,
    "ENFP": 0.1260,
    "ESFJ": 0.0835,
    "ISFJ": 0.0766,
    "ISFP": 0.0661,
    "ESFP": 0.0636,
    "INTP": 0.0628,
    "INFJ": 0.0625,
    "ENFJ": 0.0609,
    "ENTP": 0.0504,
    "ESTJ": 0.0456,
    "ISTJ": 0.0428,
    "INTJ": 0.0375,
    "ISTP": 0.0311,
    "ESTP": 0.0294,
    "ENTJ": 0.0273
}
    return sum(mbti_distribution[m] for m in mbtis)