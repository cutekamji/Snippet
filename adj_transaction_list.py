# 동일 트랜잭션에 대해 인접한 아이템 목록 생성
# result : 생성하고자 하는 인접 아이템 목록/리스트 (Dict Type)
# tran_list : 트랜잭션별 탐색한 아이템 리스트 (Series Type)

result = dict()
for item in range(len(tran_list)-1):
    if tran_list[item]==tran_list[item+1]:
        pass
    elif tran_list[item+1] not in result[tran_list[item]]:
        result[tran_list[item]]=[]
        result[tran_list[item]].append(tran_list[item+1])
# 역순 조회
tran_list = tran_list[::-1]
for item in range(len(tran_list)-1):
    if tran_list[item]==tran_list[item+1]:
        pass
    elif tran_list[item+1] not in result[tran_list[item]]:
        result[tran_list[item]]=[]
        result[tran_list[item]].result(tran_list[item+1])
