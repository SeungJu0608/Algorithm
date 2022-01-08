import re


def solution(new_id):
    # 1. 모든 대문자를 대응되는 소문자로 치환
    new_id = new_id.lower()
    # 2. 알파벳 소문자, 숫자, -, _, . 를 제외한 모든 문자 제거
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)
    # 3. 마침표가 2번 이상 연속된 부분을 하나의 마침표로 치환
    new_id = re.sub('[.]{2,}', '', new_id)
    # 4. 마침표가 처음이나 끝에 위치한다면 제거
    if new_id[0] == ".":
        new_id = new_id[1:]
    elif new_id[-1] ==".":
        new_id = new_id[:-1]
    # 5. new_id 가 빈 문자열이라면 new_id = 'a'
    if new_id == '':
        new_id = "a"
    # 6. new_id의 길이가 16자 이상이면 new_id 의 첫 15개 제외 삭제
    if len(new_id) >= 16:
        new_id = new_id[:15]
    # 삭제 후 맨 끝 문자가 마침표면 삭제
    if new_id[-1] ==".":
        new_id = new_id[:-1]
    # 7. new_id 의 길이가 2 이하라면 마지막 문자를 new_id의 길이가 3이 될 때까지 반복
    if len(new_id) <= 2:
        add_str = new_id[-1]
        while len(new_id) < 3:
            new_id += add_str

    return new_id


id = "=.="
new = solution(id)
print(new)

### 문자열 => 정규식 이용하는 걸 무서워하지 말자!
def another_solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st