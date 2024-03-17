while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    checklist = dict()
    for _ in range(n):
        m_list = list(map(int, input().split()))
        for m2 in m_list:
            if m2 in checklist:
                checklist[m2] += 1
            else:
                checklist[m2] = 1
    
    # 점수(표)에 따라 선수들 정렬
    sorted_checklist = sorted(checklist.items(), key=lambda item: item[1], reverse=True)
    
    # 가장 많은 표를 받은 선수의 표 수를 찾음
    max_votes = sorted_checklist[0][1]
    
    # 2등의 표 수를 찾음 (가장 많은 표를 받은 선수를 제외하고 가장 높은 표)
    second_highest_votes = next(item[1] for item in sorted_checklist if item[1] < max_votes)
    
    # 2등인 선수들의 번호를 찾아 오름차순으로 정렬
    second_place_players = sorted([item[0] for item in sorted_checklist if item[1] == second_highest_votes])
    
    # 2등 선수 번호 출력
    for players in second_place_players:
        print(players, end=' ')
    print()