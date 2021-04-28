# Tree_data structure and Binary Search Tree #

# <Tree>
# 데이터베이스는 내부적으로 대용량 데이터 처리에 적합한 트리 자료구조를 이용하여 항상 데이터가 정렬되어 있다.
# 따라서 데이터베이스에서의 탐색은 이진탐색과 유사한 방법을 이용하여 탐색을 수행하도록 설계되어있다.
# 트리자료구조 : - 정보를 지니는 노드들이 연결되어 표현되며 부모노드와 자식노드의 관계로 효현된다.
#              - 트리의 최상단 노드를 root node, 최하단 노드를 leaf node라고 한다.
#              - 계층적 (e.g. 파일 시스템), 정렬된 데이터를 다루기에 적합하다.

# < Binary Search Tree>
# Tree 자료구조 중 가장 간단한 형태의 트리
# 이진 탐색이 동작 할 수 있도록 고안된 자료구조
# 이진 탐색 트리 조건 : - 부모노드보다 왼쪽 자식 노드가 작다.
#                    - 부모노드보다 오른쪽 자식 노드가 더 크다.

# 이진탐색 문제는 입력 데이터의 개수가 많거나 탐색 범위가 매우 넓은 편이다.
# 따라서 input() 함수보다 sys 라이브러리의 readline() 함수를 이용한다

import sys
input_data = sys.stdin.readline().rstrip()

# readline() 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력된다. 이때 이 공백 문자를 제거하기위해 rstrip() 함수를 이용한다.