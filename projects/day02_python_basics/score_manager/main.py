from services.score_service import calculate_average, get_grade

def main():
    scores = [85,92,75,88]

    average = calculate_average(scores)
    grade = get_grade(average)

    print(f"成绩列表：{scores}")
    print(f"平均分 :{average:.2f}")
    print(f"等级：{grade}")

if __name__ == "__main__":
    main()

#程序入口