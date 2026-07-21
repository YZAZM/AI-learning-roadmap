from utils.validators import validate_score

def calculate_average(scores:list[float]) ->float:
    '''计算平均分'''
    if not scores:
        raise ValueError('成绩列表不能为空')
    
    for score in scores:
        if not validate_score(score):
            raise ValueError(f'非法成绩：{score}')
    

    return sum(scores)/len(scores)

def get_grade(score:float) -> str:
    '''根据分数返回等级'''
    if not validate_score(score):
        raise ValueError(f"非法成绩：{score}")
    
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
#成绩业务模块