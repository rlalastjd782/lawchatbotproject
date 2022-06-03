from flask import Flask, jsonify, request #Flask 실행을 위한 라이브러리 불러오기
import requests
import pandas as pd
import sys
import json 

application = Flask(__name__)

df = pd.read_csv('RealEstate.csv', encoding='utf-8', index_col=0 )
df2 = df.to_dict()
df3 = dict((value,key) for (key,value) in df2['Q'].items())
df4 = dict((key,value) for (key,value) in df2['A'].items())
data = {
    'que' :  df3,
    'ans' : df4
}
with open("df.json", "w") as json_file :
    json.dump(data, json_file)
with open("df.json", "r") as json_file :
    data1 = json.load(json_file)


# 법률용어
@application.route('/api/answer', methods=['POST'])
def ans() :
    body = request.get_json()
    print(body)
    params_df = body['action']['params']
    print(params_df)
    ans = params_df['law_dict'] # 사용자 발화값 받아와야함
    print(ans)
    Q = data1['que'][ans]# 두번째가 입력값
    a = str(Q)
    A = data1['ans'][a]
    responseBody = {
        "version": "2.0",
        "template": { 
            "outputs": [
                {
                    "simpleText": {
                        "text": A 
                    }
                }
            ]
        }
    }

    return responseBody
# 티키타카
dj = pd.read_csv('chatflow1900.csv', encoding='utf-8', index_col=0 )
# 판다스 dict 형으로 변경 
dj2 = dj.to_dict()
# 번호로 매칭되게 변경
dj3 = dict((value,key) for (key,value) in dj2['Q'].items())
dj4 = dict((key,value) for (key,value) in dj2['A'].items())

# data 파일 만들기
dab = {
    'que' :  dj3,
    'ans' : dj4
}
# json 파일로 변경
with open("dj.json", "w") as json_file :
    json.dump(dab, json_file)
# json 파일가져오기
with open("dj.json", "r") as json_file :
    dab1 = json.load(json_file)

@application.route("/api/chatflow", methods=["POST"])
def chatflow() :
    body = request.get_json()
    print(body)
    
    params_df = body['action']['params']
    print(params_df)
    ans = params_df['chatflow_dic'] 
    print(ans)
    # value 값찾아오는 형식 리스트 리스트
    Q = dab1['que'][ans]# 두번째가 입력값
    a = str(Q)
    A = dab1['ans'][a]

    responseBody = {
        "version": "2.0",
        "template": { 
            "outputs": [
                {
                    "simpleText": {
                        "text": A 
                    }
                }
            ]
        }
    }
    return responseBody

@application.route("/api/main", methods=["POST"])
# 메인2 @ 웰컴블록
def main():
    response = {
"version": "2.0",
  "template": {
    "outputs": [
      {
        "simpleText": { 
          "text": "무엇을 도와드릴까요?"
        }
      }
    ],
      
    "quickReplies": [
      {
        "messageText": "노동",
        "action": "message",
        "label": "노동",
       
      },
      {
        "messageText": "주택임대차",
        "action": "message",
        "label": "주택임대차"
      },
      {
        "messageText": "상가임대차",
        "action": "message",
        "label": "상가임대차"
      },
      {
        "messageText": "손해배상",
        "action": "message",
        "label": "손해배상" 
      },
      {
        "messageText": "민사일반",
        "action": "message",
        "label": "민사일반" 
      },
      {
        "messageText": "물권",
        "action": "message",
        "label": "물권" 
      },
      {
        "messageText": "채권",
        "action": "message",
        "label": "채권" 
      },
      {
        "messageText": "계약",
        "action": "message",
        "label": "계약" 
      },
      {                                                                                                     
        "messageText": "상사",
        "action": "message",
        "label": "상사" 
      },
      {
        "messageText": "민사소송",
        "action": "message",
        "label": "민사소송" 
      },
      {
        "messageText": "친족",
        "action": "message",
        "label": "친족" 
      },
      {
        "messageText": "상속",
        "action": "message",
        "label": "상속" 
      },
      {
        "messageText": "가사소송",
        "action": "message",
        "label": "가사소송" 
      },
      {
        "messageText": "가족관계등록",
        "action": "message",
        "label": "가족관계등록" 
      },
      {
        "messageText": "민사집행",
        "action": "message",
        "label": "민사집행" 
      },
      {
        "messageText": "보전처분",
        "action": "message",
        "label": "보전처분" 
      },
      {
        "messageText": "개인회생 파산 및 면책",
        "action": "message",
        "label": "개인회생 파산 및 면책" 
      },
      {
        "messageText": "형법",
        "action": "message",
        "label": "형법" 
      },
      {
        "messageText": "형사소송",
        "action": "message",
        "label": "형사소송" 
      },
      {
        "messageText": "행정",
        "action": "message",
        "label": "행정" 
      },
      {
        "messageText": "헌법",
        "action": "message",
        "label": "헌법" 
      }
    ]
  }
}
    return jsonify(response)

# 노동메뉴
@application.route("/api/workmenu", methods=["POST"])
def workmenu():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "노동관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "임금 및 퇴직금",
        "action": "message",
        "label": "임금 및 퇴직금",
       
      },
      {
        "messageText": "해고",
        "action": "message",
        "label": "해고"
      }
    ]  
  } 
}
    return jsonify(response)




# 주택임대차메뉴
@application.route("/api/house", methods=["POST"])
def house():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "주택임대차 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "대항력",
        "action": "message",
        "label": "대항력",
      },
      {
        "messageText": "소액임차인의 최우선변제권",
        "action": "message",
        "label": "소액임차인의 최우선변제권"
      },
      {
        "messageText": "임차보증금 · 차임 증감",
        "action": "message",
        "label": "임차보증금 · 차임 증감"
      },
      {
        "messageText": "기타 주택임대차",
        "action": "message",
        "label": "기타 주택임대차"
      },
      {
        "messageText": "임차권등기명령",
        "action": "message",
        "label": "임차권등기명령"
      }
    ]  
  } 
}
    return jsonify(response)



# 헌법 메뉴
@application.route("/api/constitutionmenu", methods=["POST"])
def constitutionmenu():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "헌법 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "헌법소원",
        "action": "message",
        "label": "헌법소원",
       
      },
      {
        "messageText": "위헌",
        "action": "message",
        "label": "위헌"
      }
    ]  
  } 
}
    return jsonify(response)




# 형사소송 메뉴
@application.route("/api/brothercowmenu", methods=["POST"])
def brothercowmenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "형사소송 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "고소와 고발",
        "action": "message",
        "label": "고소와 고발",
       
      },
      {
        "messageText": "기타 형사절차",
        "action": "message",
        "label": "기타 형사절차"
      },
      {
        "messageText": "불기소처분 및 불복",
        "action": "message",
        "label": "불기소처분 및 불복"
      },
      {
        "messageText": "상소",
        "action": "message",
        "label": "상소"
      },
      {
        "messageText": "소년 및 가정보호사건",
        "action": "message",
        "label": "소년 및 가정보호사건"
      },
      {
        "messageText": "소송절차 및 증거",
        "action": "message",
        "label": "소송절차 및 증거"
      },
      {
        "messageText": "인신보호사건",
        "action": "message",
        "label": "인신보호사건"
      },
      {
        "messageText": "재심, 약식절차",
        "action": "message",
        "label": "재심, 약식절차"
      },
      {
        "messageText": "재판의 집행",
        "action": "message",
        "label": "재판의 집행"
      },
      {
        "messageText": "체포, 구속 및 석방, 보석",
        "action": "message",
        "label": "체포, 구속 및 석방, 보석"
      }
    ]  
  } 
}
    return jsonify(response)

# 행정메뉴
@application.route("/api/administrationmenu", methods=["POST"])
def administrationmenu():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "행정 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "건축 관련 행정",
        "action": "message",
        "label": "건축 관련 행정",
       
      },
      {
        "messageText": "교통 관련 행정",
        "action": "message",
        "label": "교통 관련 행정"
      },
      {
        "messageText": "기타 행정",
        "action": "message",
        "label": "기타 행정"
      },
      {
        "messageText": "난민 관련 행정",
        "action": "message",
        "label": "난민 관련 행정"
      },
      {
        "messageText": "부동산 관련 행정",
        "action": "message",
        "label": "부동산 관련 행정"
      },
      {
        "messageText": "산재 관련 행정",
        "action": "message",
        "label": "산재 관련 행정"
      },
      {
        "messageText": "영업 관련 행정",
        "action": "message",
        "label": "영업 관련 행정"
      },
      {
        "messageText": "유공자 관련 행정",
        "action": "message",
        "label": "유공자 관련 행정"
      },
      {
        "messageText": "조세 관련 행정",
        "action": "message",
        "label": "조세 관련 행정"
      },
      {
        "messageText": "행정소송일반",
        "action": "message",
        "label": "행정소송일반"
      },
      {
        "messageText": "행정 심판",
        "action": "message",
        "label": "행정 심판"
      }
    ]  
  } 
}
    return jsonify(response)

# 형법메뉴
@application.route("/api/brotherlawmenu", methods=["POST"])
def brotherlawmenu():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "형법 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "강간과 추행의 죄",
        "action": "message",
        "label": "강간과 추행의 죄",
       
      },
      {
        "messageText": "공무방해에 관한 죄",
        "action": "message",
        "label": "공무방해에 관한 죄"
      },
      {
        "messageText": "공무원의 직무에 관한 죄",
        "action": "message",
        "label": "공무원의 직무에 관한 죄"
      },
      {
        "messageText": "과실치사상의 죄",
        "action": "message",
        "label": "과실치사상의 죄"
      },
      {
        "messageText": "교통사고처리특례법 위반죄",
        "action": "message",
        "label": "교통사고처리특례법 위반죄"
      },
      {
        "messageText": "명예에 관한 죄",
        "action": "message",
        "label": "명예에 관한 죄"
      },
      {
        "messageText": "무고의 죄",
        "action": "message",
        "label": "무고의 죄"
      },
      {
        "messageText": "문서에 관한 죄",
        "action": "message",
        "label": "문서에 관한 죄"
      },
      {
        "messageText": "방화와 실화의 죄",
        "action": "message",
        "label": "방화와 실화의 죄"
      },
      {
        "messageText": "사기와 공갈의 죄",
        "action": "message",
        "label": "사기와 공갈의 죄"
      },
      {
        "messageText": "살인의 죄",
        "action": "message",
        "label": "살인의 죄"
      },
      {
        "messageText": "상해와 폭행의 죄",
        "action": "message",
        "label": "상해와 폭행의 죄"
      }
    ]  
  } 
}
    return jsonify(response)

# 개인회생, 파산 및 면책메뉴
@application.route("/api/personmenu", methods=["POST"])
def personmenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "개인회생, 파산 및 면책 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "개인회생",
        "action": "message",
        "label": "개인회생",
       
      }
    ]  
  } 
}      
    return jsonify(response)  



# 보전처분 메뉴 
@application.route("/api/bojeonmenu", methods=["POST"])
def bojeonmenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "보전처분 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "가압류일반",
        "action": "message",
        "label": "가압류일반",
       
      },
      {
        "messageText": "가처분",
        "action": "message",
        "label": "가처분",
       
      },
      {
        "messageText": "기타 보전처분",
        "action": "message",
        "label": "기타 보전처분",
       
      },
      {
        "messageText": "부동산가압류",
        "action": "message",
        "label": "부동산가압류",
       
      },
      {
        "messageText": "채권가압류",
        "action": "message",
        "label": "채권가압류",
       
      }
    ]  
  } 
}      
    return jsonify(response)

# 민사집행 메뉴 
@application.route("/api/minsagomenu", methods=["POST"])
def minsagomenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "민사집행 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "강제집행일반",
        "action": "message",
        "label": "강제집행일반",
       
      },
      {
        "messageText": "금전채권 강제집행",
        "action": "message",
        "label": "금전채권 강제집행",
       
      },
      {
        "messageText": "기타 강제집행",
        "action": "message",
        "label": "기타 강제집행",
       
      },
      {
        "messageText": "부동산강제집행",
        "action": "message",
        "label": "부동산강제집행",
       
      },
      {
        "messageText": "압류금지채권범위변경",
        "action": "message",
        "label": "압류금지채권범위변경",
       
      },
      {
        "messageText": "유체동산 강제집행",
        "action": "message",
        "label": "유체동산 강제집행",
       
      },
      {
        "messageText": "자동차 등 강제집행",
        "action": "message",
        "label": "자동차 등 강제집행",
       
      }
    ]  
  } 
}      
    return jsonify(response)

# 가족관계등록 메뉴 
@application.route("/api/familymenu", methods=["POST"])
def familymenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "가족관계등록 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "가족관계등록부정정",
        "action": "message",
        "label": "가족관계등록부정정",
       
      },
      {
        "messageText": "가족관계등록창설",
        "action": "message",
        "label": "가족관계등록창설",
       
      },
      {
        "messageText": "국적의 취득과 상실",
        "action": "message",
        "label": "국적의 취득과 상실",
       
      },
      {
        "messageText": "신고",
        "action": "message",
        "label": "신고",
       
      }
    ]  
  } 
}      
    return jsonify(response)

# 가사소송 메뉴 
@application.route("/api/familysomenu", methods=["POST"])
def familysomenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "가사소송 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "가,나,다류 가사소송",
        "action": "message",
        "label": "가,나,다류 가사소송",
       
      },
      {
        "messageText": "가사소송일반",
        "action": "message",
        "label": "가사소송일반",
       
      },
      {
        "messageText": "과태료와 감치",
        "action": "message",
        "label": "과태료와 감치",
       
      },
      {
        "messageText": "기타",
        "action": "message",
        "label": "기타",
       
      }
    ]  
  } 
}      
    return jsonify(response)


# 상속 메뉴 
@application.route("/api/sangsokmenu", methods=["POST"])
def sangsokmenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "상속 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "상속분",
        "action": "message",
        "label": "상속분",
       
      },
      {
        "messageText": "상속일반",
        "action": "message",
        "label": "상속일반",
       
      },
      {
        "messageText": "상속재산분할",
        "action": "message",
        "label": "상속재산분할",
       
      },
      {
        "messageText": "유류분",
        "action": "message",
        "label": "유류분",
       
      },
      {
        "messageText": "유언",
        "action": "message",
        "label": "유언",
       
      }
    ]  
  } 
}      
    return jsonify(response)

# 친족 메뉴 
@application.route("/api/relationmenu", methods=["POST"])
def relationmenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "친족 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "면접교섭권",
        "action": "message",
        "label": "면접교섭권",
       
      },
      {
        "messageText": "부양",
        "action": "message",
        "label": "부양",
       
      },
      {
        "messageText": "약혼",
        "action": "message",
        "label": "약혼",
       
      },
      {
        "messageText": "양육비",
        "action": "message",
        "label": "양육비",
       
      },
      {
        "messageText": "이혼 및 위자료",
        "action": "message",
        "label": "이혼 및 위자료",
       
      },
      {
        "messageText": "이혼 및 재산분할청구권",
        "action": "message",
        "label": "이혼 및 재산분할청구권",
       
      }
    ]  
  } 
}      
    return jsonify(response)

# 민사소송 메뉴 
@application.route("/api/minsasosongmenu", methods=["POST"])
def minsasosongmenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "민사소송 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "간이소송절차",
        "action": "message",
        "label": "간이소송절차",
       
      },
      {
        "messageText": "관할",
        "action": "message",
        "label": "관할",
       
      },
      {
        "messageText": "기타 민사소송",
        "action": "message",
        "label": "기타 민사소송",
       
      },
      {
        "messageText": "당사자",
        "action": "message",
        "label": "당사자",
       
      },
      {
        "messageText": "상소",
        "action": "message",
        "label": "상소",
       
      },
      {
        "messageText": "소송비용",
        "action": "message",
        "label": "소송비용",
       
      },
      {
        "messageText": "소송절차",
        "action": "message",
        "label": "소송절차",
       
      },
      {
        "messageText": "재심",
        "action": "message",
        "label": "재심",
       
      },
      {
        "messageText": "증거",
        "action": "message",
        "label": "증거",
       
      }
    ]  
  } 
}      
    return jsonify(response)

# 상사 메뉴 
@application.route("/api/bossmenu", methods=["POST"])
def bossmenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "상사 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "보험",
        "action": "message",
        "label": "보험",
       
      },
      {
        "messageText": "상사일반",
        "action": "message",
        "label": "상사일반",
       
      },
      {
        "messageText": "어음,수표",
        "action": "message",
        "label": "어음,수표",
       
      },
      {
        "messageText": "회사",
        "action": "message",
        "label": "회사",
       
      }
    ]  
  } 
}      
    return jsonify(response)

# 계약메뉴 
@application.route("/api/trademenu", methods=["POST"])
def trademenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "계약 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "계약금",
        "action": "message",
        "label": "계약금",
       
      },
      {
        "messageText": "계약의 해지 해제",
        "action": "message",
        "label": "계약의 해지 해제",
       
      },
      {
        "messageText": "기타 계약",
        "action": "message",
        "label": "기타 계약",
       
      },
      {
        "messageText": "대여금 등",
        "action": "message",
        "label": "대여금 등",
       
      },
      {
        "messageText": "도급",
        "action": "message",
        "label": "도급",
       
      },
      {
        "messageText": "매매",
        "action": "message",
        "label": "매매",
       
      },
      {
        "messageText": "부동산중개",
        "action": "message",
        "label": "부동산중개",
       
      },
      {
        "messageText": "위임",
        "action": "message",
        "label": "위임",
       
      },
      {
        "messageText": "임대차",
        "action": "message",
        "label": "임대차",
       
      },
      {
        "messageText": "조합과 계",
        "action": "message",
        "label": "조합과 계",
       
      },
      {
        "messageText": "할부거래 및 방문판매,신용카드",
        "action": "message",
        "label": "할부거래 및 방문판매,신용카드",
       
      },
      {
        "messageText": "화해",
        "action": "message",
        "label": "화해",
       
      }
    ]  
  } 
}      
    return jsonify(response)

#  채권메뉴 
@application.route("/api/chaemenu", methods=["POST"])
def chaemenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "채권 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "기타 채권",
        "action": "message",
        "label": "기타 채권",
       
      },
      {
        "messageText": "부당이득",
        "action": "message",
        "label": "부당이득",
       
      },
      {
        "messageText": "연대채무,보증채무",
        "action": "message",
        "label": "연대채무,보증채무",
       
      },
      {
        "messageText": "채권양도",
        "action": "message",
        "label": "채권양도",
       
      },
      {
        "messageText": "채권의 소멸(공탁 등)",
        "action": "message",
        "label": "채권의 소멸(공탁 등)",
       
      },
      {
        "messageText": "채권자취소권",
        "action": "message",
        "label": "채권자취소권",
       
      },
      {
        "messageText": "채무인수",
        "action": "message",
        "label": "채무인수",
       
      }
    ]  
  } 
}      
    return jsonify(response)


# 물권 메뉴 
@application.route("/api/mulmenu", methods=["POST"])
def mulmenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "물권 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "공동소유",
        "action": "message",
        "label": "공동소유",
       
      },
      {
        "messageText": "기타 물권",
        "action": "message",
        "label": "기타 물권",
       
      },
      {
        "messageText": "물권의 변동(부동산등기 등)",
        "action": "message",
        "label": "물권의 변동(부동산등기 등)",
       
      },
      {
        "messageText": "상린관계",
        "action": "message",
        "label": "상린관계",
       
      },
      {
        "messageText": "소유권",
        "action": "message",
        "label": "소유권",
       
      },
      {
        "messageText": "소유권에 기한 물권적 청구권",
        "action": "message",
        "label": "소유권에 기한 물권적 청구권",
       
      },
      {
        "messageText": "저당권",
        "action": "message",
        "label": "저당권",
       
      },
      {
        "messageText": "점유권",
        "action": "message",
        "label": "점유권",
       
      },
      {
        "messageText": "지상권과 전세권",
        "action": "message",
        "label": "지상권과 전세권",
       
      },
      {
        "messageText": "취득시효",
        "action": "message",
        "label": "취득시효",
       
      
      }
    ]  
  } 
}      
    return jsonify(response)


# 민사일반 메뉴 
@application.route("/api/minsa1menu", methods=["POST"])
def minsa1menu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "민사일반 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "대리",
        "action": "message",
        "label": "대리",
       
      },
      {
        "messageText": "법률행위일반",
        "action": "message",
        "label": "법률행위일반",
       
      },
      {
        "messageText": "소멸시효",
        "action": "message",
        "label": "소멸시효",
       
      },
      {
        "messageText": "제한능력자",
        "action": "message",
        "label": "제한능력자",
       
      }
    ]  
  } 
}      
    return jsonify(response)

# 손해배상 메뉴 
@application.route("/api/sonbaemenu", methods=["POST"])
def sonbaemenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "손해배상 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "공해",
        "action": "message",
        "label": "공해",
       
      },
      {
        "messageText": "기타 손해배상",
        "action": "message",
        "label": "기타 손해배상",
       
      },
      {
        "messageText": "범죄피해",
        "action": "message",
        "label": "범죄피해",
       
      },
      {
        "messageText": "불법사금융(보이스피싱)",
        "action": "message",
        "label": "불법사금융(보이스피싱)",
       
      },
      {
        "messageText": "산재사고",
        "action": "message",
        "label": "산재사고",
       
      },
      {
        "messageText": "성폭력피해(일반)",
        "action": "message",
        "label": "성폭력피해(일반)",
       
      },
      {
        "messageText": "의료과오",
        "action": "message",
        "label": "의료과오",
       
      },
      {
        "messageText": "자동차사고",
        "action": "message",
        "label": "자동차사고",
       
      },
      {
        "messageText": "지적소유권",
        "action": "message",
        "label": "지적소유권",
       
      }
    ]  
  } 
}      
    return jsonify(response)

# 상가임대차메뉴 
@application.route("/api/sanggamenu", methods=["POST"])
def sanggamenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "상가임대차 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "계약갱신요구",
        "action": "message",
        "label": "계약갱신요구",
       
      },
      {
        "messageText": "권리금",
        "action": "message",
        "label": "권리금",
       
      },
      {
        "messageText": "임차보증금반환",
        "action": "message",
        "label": "임차보증금반환",
       
      }
    ]  
  } 
}      
    return jsonify(response)


## 주택임대차 6개 ##
# 기타 주택임대차
@application.route("/api/etchouseimdae", methods=["POST"])
def etchouseimdae ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"기타 주택임대차",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTUy/MDAxNjUzMDMwODc5ODcw.EY3quvGq6MHJyHrcwtyHqBsYyO0YMjQgs2xLdTvi-Asg.lPA7dO-1Xc0TCYXICxf6SzkJK2q9em4Ie0rUqDM7Oo4g.JPEG.sjkor1005/KakaoTalk_20220520_143304994.jpg?type=w800",
          "description":"내용증명(주택임대차 계약해지-임대료 연체)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=946a6439c059438682db3aacc3cf8949&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 대항력
@application.route("/api/bighang", methods=["POST"])
def bighang ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"대항력",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTUy/MDAxNjUzMDMwODc5ODcw.EY3quvGq6MHJyHrcwtyHqBsYyO0YMjQgs2xLdTvi-Asg.lPA7dO-1Xc0TCYXICxf6SzkJK2q9em4Ie0rUqDM7Oo4g.JPEG.sjkor1005/KakaoTalk_20220520_143304994.jpg?type=w800",
          "description":"준비서면(건물인도, 피고)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=1f180279d663431488870a308afbce41&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 소액임차인의 최우선변제권
@application.route("/api/littlemoney", methods=["POST"])
def littlemoney ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"소액임차인의 최우선변제권",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTUy/MDAxNjUzMDMwODc5ODcw.EY3quvGq6MHJyHrcwtyHqBsYyO0YMjQgs2xLdTvi-Asg.lPA7dO-1Xc0TCYXICxf6SzkJK2q9em4Ie0rUqDM7Oo4g.JPEG.sjkor1005/KakaoTalk_20220520_143304994.jpg?type=w800",
          "description":"임차보증금반환채권 부존재확인의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=4666a423614148658c65e2139c10529d&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 임차권등기명령
@application.route("/api/ordertoimcha", methods=["POST"])
def ordertoimcha ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"임차권등기명령",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTUy/MDAxNjUzMDMwODc5ODcw.EY3quvGq6MHJyHrcwtyHqBsYyO0YMjQgs2xLdTvi-Asg.lPA7dO-1Xc0TCYXICxf6SzkJK2q9em4Ie0rUqDM7Oo4g.JPEG.sjkor1005/KakaoTalk_20220520_143304994.jpg?type=w800",
          "description":"주택임차권등기명령(설명)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=8ab28448566947258db5b39cfcad2e12&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 임차보증금,차임증감
@application.route("/api/imchamoney", methods=["POST"])
def imchamoney ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"임차보증금, 차임 증감",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTUy/MDAxNjUzMDMwODc5ODcw.EY3quvGq6MHJyHrcwtyHqBsYyO0YMjQgs2xLdTvi-Asg.lPA7dO-1Xc0TCYXICxf6SzkJK2q9em4Ie0rUqDM7Oo4g.JPEG.sjkor1005/KakaoTalk_20220520_143304994.jpg?type=w800",
          "description":"임대료청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=e6d5a419255346eca0b2d5783adc0b7a&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 임차보증금반환
@application.route("/api/housearch", methods=["POST"])
def housearch ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"임차보증금반환",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTUy/MDAxNjUzMDMwODc5ODcw.EY3quvGq6MHJyHrcwtyHqBsYyO0YMjQgs2xLdTvi-Asg.lPA7dO-1Xc0TCYXICxf6SzkJK2q9em4Ie0rUqDM7Oo4g.JPEG.sjkor1005/KakaoTalk_20220520_143304994.jpg?type=w800",
          "description":"아파트, 맨션, 빌라 등 임대차계약서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=bfdad6bf254943f1b0fbbd19429f7c23&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


##헌법 ##

# 헌법소원
@application.route("/api/constitutionappeal", methods=["POST"])
def constitutionappeal ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"헌법소원",
          "imageUrl":"data:image/png;base64,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",
          "description":"국선대리인 선임신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=47382ea69fa943b0b4b1a013adffe84e&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    },
    {
      "type":"card.image",
      "cards":[
        {
          "title":"헌법소원",
          "imageUrl":"data:image/png;base64,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",
          "description":"의견서 제출",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=79bc5247e0c94be0be5e4fdb1ca70c3d&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
        ]
    },
    {
      "type":"card.image",
      "cards":[
        {
          "title":"헌법소원",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MThfMTYy/MDAxNjUyODU0NDY0NzI5.i1LunqRLcMHkfVpV8j1tzGZQR-AjnE6JO-Gw3YC0gC4g.pkcpXr47IHWl0zTEhd4JRohvbSVbDRClCJL_wkZIOQ4g.JPEG.sjkor1005/%EC%9E%AC%ED%8C%90.jpg?type=w800",
          "description":"헌법소원의 종류와 그 성격",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=f517a3b24a9f40c0ad90db9edd111638&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
    return jsonify(response)
    

# 위헌
@application.route("/api/unconstitutional", methods=["POST"])
def unconstitutional ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"위헌",
          "imageUrl":"data:image/png;base64,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",
          "description":"위헌법률심판제청신청",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=412b016af48947ac9576e1ceac96d1bf&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
              {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}
    return jsonify(response)   

## 상사 4개##
# 보험
@application.route("/api/insurance", methods=["POST"])
def insurance ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"보험",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjA2/MDAxNjUzMDMwODgwMTcx.HhfDspigEvB6ky1xD5RxziSXOTSM_TcWYTJ4QyJ6uHsg.ebAd2cZDyG93MCvCjMpKtcAytYC0mzPUAAkczGOiVAUg.JPEG.sjkor1005/KakaoTalk_20220520_151423054.jpg?type=w800",
          "description":"보험금청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{ 
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=320172f7121c46498d5a6de78e6f72dc&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 상사일반
@application.route("/api/boss1ban", methods=["POST"])
def boss1ban ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"상사일반",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjA2/MDAxNjUzMDMwODgwMTcx.HhfDspigEvB6ky1xD5RxziSXOTSM_TcWYTJ4QyJ6uHsg.ebAd2cZDyG93MCvCjMpKtcAytYC0mzPUAAkczGOiVAUg.JPEG.sjkor1005/KakaoTalk_20220520_151423054.jpg?type=w800",
          "description":"대리점계약서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=180834c607484f8088e3f674a8b88b50&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 어음수표
@application.route("/api/umm", methods=["POST"])
def umm ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"어음, 수표",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjA2/MDAxNjUzMDMwODgwMTcx.HhfDspigEvB6ky1xD5RxziSXOTSM_TcWYTJ4QyJ6uHsg.ebAd2cZDyG93MCvCjMpKtcAytYC0mzPUAAkczGOiVAUg.JPEG.sjkor1005/KakaoTalk_20220520_151423054.jpg?type=w800",
          "description":"약속어음금청구의 소(백지어음)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=668e1f64b4d140a8bfd44abd1c60f455&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 회사
@application.route("/api/hell", methods=["POST"])
def hell ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"회사",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjA2/MDAxNjUzMDMwODgwMTcx.HhfDspigEvB6ky1xD5RxziSXOTSM_TcWYTJ4QyJ6uHsg.ebAd2cZDyG93MCvCjMpKtcAytYC0mzPUAAkczGOiVAUg.JPEG.sjkor1005/KakaoTalk_20220520_151423054.jpg?type=w800",
          "description":"주식회사 이사해임의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=59180e69999b4fd684e2c21113051baa&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


## 채권 7개 ##
# 기타 채권
@application.route("/api/etcchaekwon", methods=["POST"])
def etcchaekwon ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"기타 채권",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTYy/MDAxNjUzMDMwODgwMDgw.SpODrctWrmDHis_fyHHsusm4fBwt2TqIpSgdsr9LHQEg.df0zpJdbNfZD7NWnKI2UgTFrpfCuI6G-MQZKQNROKwwg.JPEG.sjkor1005/KakaoTalk_20220520_150734939.jpg?type=w800",
          "description":"영농보상금수령권 확인의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=094b48c7019641c1aa16143bf7fc4051&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)
  

# 부당이득
@application.route("/api/budang2", methods=["POST"])
def budang2 ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"부당이득",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTYy/MDAxNjUzMDMwODgwMDgw.SpODrctWrmDHis_fyHHsusm4fBwt2TqIpSgdsr9LHQEg.df0zpJdbNfZD7NWnKI2UgTFrpfCuI6G-MQZKQNROKwwg.JPEG.sjkor1005/KakaoTalk_20220520_150734939.jpg?type=w800",
          "description":"반소장(부당이득금 반환청구)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=55d11b7a3138451c9d081c7004f72067&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)
  

# 연대채무, 보증채무
@application.route("/api/imchaemu", methods=["POST"])
def imchaemu ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"연대채무, 보증채무",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTYy/MDAxNjUzMDMwODgwMDgw.SpODrctWrmDHis_fyHHsusm4fBwt2TqIpSgdsr9LHQEg.df0zpJdbNfZD7NWnKI2UgTFrpfCuI6G-MQZKQNROKwwg.JPEG.sjkor1005/KakaoTalk_20220520_150734939.jpg?type=w800",
          "description":"구상금청구의 소(물상보증인)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=6e09643aa56d417085e448c7d0417b4d&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 채권양도
@application.route("/api/sheepdo", methods=["POST"])
def sheepdo ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"채권양도",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTYy/MDAxNjUzMDMwODgwMDgw.SpODrctWrmDHis_fyHHsusm4fBwt2TqIpSgdsr9LHQEg.df0zpJdbNfZD7NWnKI2UgTFrpfCuI6G-MQZKQNROKwwg.JPEG.sjkor1005/KakaoTalk_20220520_150734939.jpg?type=w800",
          "description":"양수금청구의 소(공사대금 양수)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=e4a9e3f3d0464b8795b80f5dea7c04c0&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 채권의 소멸(공탁 등)
@application.route("/api/chaekwonbye", methods=["POST"])
def chaekwonbye ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"채권의 소멸(공탁 등)",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTYy/MDAxNjUzMDMwODgwMDgw.SpODrctWrmDHis_fyHHsusm4fBwt2TqIpSgdsr9LHQEg.df0zpJdbNfZD7NWnKI2UgTFrpfCuI6G-MQZKQNROKwwg.JPEG.sjkor1005/KakaoTalk_20220520_150734939.jpg?type=w800",
          "description":"공탁금출급권자확인의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=76792060d058419db63b865fd40885f2&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 채권자취소권
@application.route("/api/cancel", methods=["POST"])
def cancel ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"채권자취소권",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTYy/MDAxNjUzMDMwODgwMDgw.SpODrctWrmDHis_fyHHsusm4fBwt2TqIpSgdsr9LHQEg.df0zpJdbNfZD7NWnKI2UgTFrpfCuI6G-MQZKQNROKwwg.JPEG.sjkor1005/KakaoTalk_20220520_150734939.jpg?type=w800",
          "description":"사해행위취소 및 원상회복청구",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=52a57c01b3e94b57a5cc72a967ef19ec&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

  
# 채무인수
@application.route("/api/getchaemu", methods=["POST"])
def getchaemu ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"채무인수",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTYy/MDAxNjUzMDMwODgwMDgw.SpODrctWrmDHis_fyHHsusm4fBwt2TqIpSgdsr9LHQEg.df0zpJdbNfZD7NWnKI2UgTFrpfCuI6G-MQZKQNROKwwg.JPEG.sjkor1005/KakaoTalk_20220520_150734939.jpg?type=w800",
          "description":"면책적 채무인수계약서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=489d798542254af38e3c4360f44da8fe&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


## 계약 12개 ##
# 계약금
@application.route("/api/cmoney", methods=["POST"])
def cmoney ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"계약금",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjcg/MDAxNjUzMDMwODgwMTU5.1l_mDrtY9go2_fXu2ANXs18-v7xMrX_paFPOy9lRrd8g.2wBf9mPasQgjyeGUxUYhTSEFlwswCN2AysUTC5CVyCcg.JPEG.sjkor1005/KakaoTalk_20220520_150956609.jpg?type=w800",
          "description":"준비서면(계약금 등 반환, 원고)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=cda2343461754185812c50a61b77dba9&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 계약의 해지 해제
@application.route("/api/cbye", methods=["POST"])
def cbye ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"계약의 해지 해제",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjcg/MDAxNjUzMDMwODgwMTU5.1l_mDrtY9go2_fXu2ANXs18-v7xMrX_paFPOy9lRrd8g.2wBf9mPasQgjyeGUxUYhTSEFlwswCN2AysUTC5CVyCcg.JPEG.sjkor1005/KakaoTalk_20220520_150956609.jpg?type=w800",
          "description":"소유권이전등기말소청구의 소(교환계약 해제)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=97cc6192cbd240ecadec17a5b5be39bc&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 기타계약
@application.route("/api/etccontract", methods=["POST"])
def etccontract ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"기타 계약",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjcg/MDAxNjUzMDMwODgwMTU5.1l_mDrtY9go2_fXu2ANXs18-v7xMrX_paFPOy9lRrd8g.2wBf9mPasQgjyeGUxUYhTSEFlwswCN2AysUTC5CVyCcg.JPEG.sjkor1005/KakaoTalk_20220520_150956609.jpg?type=w800",
          "description":"특허권의 통상실시권 설정계약서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=2d5c85ac4cb7454397392b776c9c57e2&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 대여금 등
@application.route("/api/loan", methods=["POST"])
def loan ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"대여금 등",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjcg/MDAxNjUzMDMwODgwMTU5.1l_mDrtY9go2_fXu2ANXs18-v7xMrX_paFPOy9lRrd8g.2wBf9mPasQgjyeGUxUYhTSEFlwswCN2AysUTC5CVyCcg.JPEG.sjkor1005/KakaoTalk_20220520_150956609.jpg?type=w800",
          "description":"대여금청구의 소(연대보증인이 있는 경우)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=e78973e7f8f44b819b9efc5d107e4eac&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 도급
@application.route("/api/subcontract", methods=["POST"])
def subcontract ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"도급",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjcg/MDAxNjUzMDMwODgwMTU5.1l_mDrtY9go2_fXu2ANXs18-v7xMrX_paFPOy9lRrd8g.2wBf9mPasQgjyeGUxUYhTSEFlwswCN2AysUTC5CVyCcg.JPEG.sjkor1005/KakaoTalk_20220520_150956609.jpg?type=w800",
          "description":"임가공료청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=59b4ab97d1ae46e890bc726f9899dc25&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 매매
@application.route("/api/dealing", methods=["POST"])
def dealing ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"매매",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjcg/MDAxNjUzMDMwODgwMTU5.1l_mDrtY9go2_fXu2ANXs18-v7xMrX_paFPOy9lRrd8g.2wBf9mPasQgjyeGUxUYhTSEFlwswCN2AysUTC5CVyCcg.JPEG.sjkor1005/KakaoTalk_20220520_150956609.jpg?type=w800",
          "description":"물품대금청구의 소(식료품)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=e16058eea45e4f0e841d0eab24ed5435&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 부동산중개
@application.route("/api/mediation", methods=["POST"])
def mediation ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"부동산중개",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjcg/MDAxNjUzMDMwODgwMTU5.1l_mDrtY9go2_fXu2ANXs18-v7xMrX_paFPOy9lRrd8g.2wBf9mPasQgjyeGUxUYhTSEFlwswCN2AysUTC5CVyCcg.JPEG.sjkor1005/KakaoTalk_20220520_150956609.jpg?type=w800",
          "description":"중개업자의 손해배상",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=309eb22a6a284066917c1c767de27be4&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 위임
@application.route("/api/mandate", methods=["POST"])
def mandate ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"위임",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjcg/MDAxNjUzMDMwODgwMTU5.1l_mDrtY9go2_fXu2ANXs18-v7xMrX_paFPOy9lRrd8g.2wBf9mPasQgjyeGUxUYhTSEFlwswCN2AysUTC5CVyCcg.JPEG.sjkor1005/KakaoTalk_20220520_150956609.jpg?type=w800",
          "description":"위임계약서(일반)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=a7a79921c3ca41ffa6d128a0126a65f7&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 임대차
@application.route("/api/imdaecar", methods=["POST"])
def imdaecar ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"임대차",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjcg/MDAxNjUzMDMwODgwMTU5.1l_mDrtY9go2_fXu2ANXs18-v7xMrX_paFPOy9lRrd8g.2wBf9mPasQgjyeGUxUYhTSEFlwswCN2AysUTC5CVyCcg.JPEG.sjkor1005/KakaoTalk_20220520_150956609.jpg?type=w800",
          "description":"임대차계약서(자동차)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=c85749d3bd44495191e81b5b0c9bb40e&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 조합과 계
@application.route("/api/johab", methods=["POST"])
def johab ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"조합과 계",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjcg/MDAxNjUzMDMwODgwMTU5.1l_mDrtY9go2_fXu2ANXs18-v7xMrX_paFPOy9lRrd8g.2wBf9mPasQgjyeGUxUYhTSEFlwswCN2AysUTC5CVyCcg.JPEG.sjkor1005/KakaoTalk_20220520_150956609.jpg?type=w800",
          "description":"계금청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=9bbb56520cfe4512902bac54b02075f9&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 할부거래 및 방문판매, 신용카드
@application.route("/api/credit", methods=["POST"])
def credit ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"할부,방문판매,신용카드",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjcg/MDAxNjUzMDMwODgwMTU5.1l_mDrtY9go2_fXu2ANXs18-v7xMrX_paFPOy9lRrd8g.2wBf9mPasQgjyeGUxUYhTSEFlwswCN2AysUTC5CVyCcg.JPEG.sjkor1005/KakaoTalk_20220520_150956609.jpg?type=w800",
          "description":"미성년자가 체결한 계약의 청약 철회 신고서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=38489078f0534b8f8db726d9ecf7750d&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 화해
@application.route("/api/reconcilaition", methods=["POST"])
def reconciliation ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"화해",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjcg/MDAxNjUzMDMwODgwMTU5.1l_mDrtY9go2_fXu2ANXs18-v7xMrX_paFPOy9lRrd8g.2wBf9mPasQgjyeGUxUYhTSEFlwswCN2AysUTC5CVyCcg.JPEG.sjkor1005/KakaoTalk_20220520_150956609.jpg?type=w800",
          "description":"화해계약서(교통사고, 물적손해)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=3fcc9d7cf476477381e6ca81d4bf8a55&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


## 민사소송 9개 ##
# 간이소송절차
@application.route("/api/minsagan2", methods=["POST"])
def minsagan2 ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"간이소송절차",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjIg/MDAxNjUzMDMwODgwMjE2.RqQvY3VzGJHDEqXaCg7jU38YyUfHCCZ4nIUwd1b1m1wg.NfuKVSzVeiLNA5eQ0uQxdMzXmam8rnC_vdjAdmS2_Gog.JPEG.sjkor1005/KakaoTalk_20220520_151958512.jpg?type=w800",
          "description":"이행권고결정에 대한 이의신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=64b993fd7fbe42f2bffd1b61eba2f25d&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 관할
@application.route("/api/gwanhal", methods=["POST"])
def gwanhal ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"관할",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjIg/MDAxNjUzMDMwODgwMjE2.RqQvY3VzGJHDEqXaCg7jU38YyUfHCCZ4nIUwd1b1m1wg.NfuKVSzVeiLNA5eQ0uQxdMzXmam8rnC_vdjAdmS2_Gog.JPEG.sjkor1005/KakaoTalk_20220520_151958512.jpg?type=w800",
          "description":"관할합의서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=6c77884132d7472fa98d0a74fdb97764&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 기타민사소송
@application.route("/api/etcminsa1", methods=["POST"])
def etcminsa1 ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"기타 민사소송",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjIg/MDAxNjUzMDMwODgwMjE2.RqQvY3VzGJHDEqXaCg7jU38YyUfHCCZ4nIUwd1b1m1wg.NfuKVSzVeiLNA5eQ0uQxdMzXmam8rnC_vdjAdmS2_Gog.JPEG.sjkor1005/KakaoTalk_20220520_151958512.jpg?type=w800",
          "description":"법관기피신청 기각결정에 대한 즉시항고장",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=50b41977c7b740e9b714a626a93e4788&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 당사자
@application.route("/api/danglion", methods=["POST"])
def danglion ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"당사자",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjIg/MDAxNjUzMDMwODgwMjE2.RqQvY3VzGJHDEqXaCg7jU38YyUfHCCZ4nIUwd1b1m1wg.NfuKVSzVeiLNA5eQ0uQxdMzXmam8rnC_vdjAdmS2_Gog.JPEG.sjkor1005/KakaoTalk_20220520_151958512.jpg?type=w800",
          "description":"특별대리인 개임신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=2b24cab0e47945b3bca0dea5e9fc11bd&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 상소
@application.route("/api/minsaupcow", methods=["POST"])
def minsaupcow ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"상소",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjIg/MDAxNjUzMDMwODgwMjE2.RqQvY3VzGJHDEqXaCg7jU38YyUfHCCZ4nIUwd1b1m1wg.NfuKVSzVeiLNA5eQ0uQxdMzXmam8rnC_vdjAdmS2_Gog.JPEG.sjkor1005/KakaoTalk_20220520_151958512.jpg?type=w800",
          "description":"항소이유서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=7cc4919c6cd34a8fb2fde694342c06a6&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 소송비용
@application.route("/api/sosongmoney", methods=["POST"])
def sosongmoney ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"소송비용",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjIg/MDAxNjUzMDMwODgwMjE2.RqQvY3VzGJHDEqXaCg7jU38YyUfHCCZ4nIUwd1b1m1wg.NfuKVSzVeiLNA5eQ0uQxdMzXmam8rnC_vdjAdmS2_Gog.JPEG.sjkor1005/KakaoTalk_20220520_151958512.jpg?type=w800",
          "description":"소송비용액확정결정신청서(일부부담)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=3d73c917cc6e468898741e16696794f8&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 소송절차
@application.route("/api/sosongmenual", methods=["POST"])
def sosongmenual ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"소송절차",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjIg/MDAxNjUzMDMwODgwMjE2.RqQvY3VzGJHDEqXaCg7jU38YyUfHCCZ4nIUwd1b1m1wg.NfuKVSzVeiLNA5eQ0uQxdMzXmam8rnC_vdjAdmS2_Gog.JPEG.sjkor1005/KakaoTalk_20220520_151958512.jpg?type=w800",
          "description":"공시송달신청서(소장제출과 함께)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=b090a85601734398924c618cc7497654&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 재심
@application.route("/api/againsim", methods=["POST"])
def againsim ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"재심",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjIg/MDAxNjUzMDMwODgwMjE2.RqQvY3VzGJHDEqXaCg7jU38YyUfHCCZ4nIUwd1b1m1wg.NfuKVSzVeiLNA5eQ0uQxdMzXmam8rnC_vdjAdmS2_Gog.JPEG.sjkor1005/KakaoTalk_20220520_151958512.jpg?type=w800",
          "description":"재심소장",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=7ca7a2156fb14f4fb63e33ab078aa5e7&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 증거
@application.route("/api/evidence", methods=["POST"])
def evidence ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"증거",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjIg/MDAxNjUzMDMwODgwMjE2.RqQvY3VzGJHDEqXaCg7jU38YyUfHCCZ4nIUwd1b1m1wg.NfuKVSzVeiLNA5eQ0uQxdMzXmam8rnC_vdjAdmS2_Gog.JPEG.sjkor1005/KakaoTalk_20220520_151958512.jpg?type=w800",
          "description":"사실조회신청서(노동청)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=78bcd2750aaf430181c51c1a4fbb3184&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


## 물권 10개 ##
# 공동소유
@application.route("/api/togethermul", methods=["POST"])
def togethermul ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"공동소유",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDYg/MDAxNjUzMDMwODgwMDQz.ZEtfPtFJWuk8x2S5CJmzC4bKDq69JDLSCCAzsfCRMo0g.LXLYL_ULYoJK4dlRIMMV22ACLf-I4WDiCOt_8bbV0Rsg.JPEG.sjkor1005/KakaoTalk_20220520_150455625.jpg?type=w800",
          "description":"소유권이전등기(공유자전원 지분전부이전)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=9e97e78f8e2042338cc83d27aa09a614&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 기타물권
@application.route("/api/etcmulkwon", methods=["POST"])
def etcmulkwon ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"기타 물권",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDYg/MDAxNjUzMDMwODgwMDQz.ZEtfPtFJWuk8x2S5CJmzC4bKDq69JDLSCCAzsfCRMo0g.LXLYL_ULYoJK4dlRIMMV22ACLf-I4WDiCOt_8bbV0Rsg.JPEG.sjkor1005/KakaoTalk_20220520_150455625.jpg?type=w800",
          "description":"양도담보계약서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=6a25be879f074e9eb64a8b2319ac4bb5&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 물권의 변동(부동산등기 등)
@application.route("/api/mulchange", methods=["POST"])
def mulchange ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"물권의 변동(부동산등기 등)",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDYg/MDAxNjUzMDMwODgwMDQz.ZEtfPtFJWuk8x2S5CJmzC4bKDq69JDLSCCAzsfCRMo0g.LXLYL_ULYoJK4dlRIMMV22ACLf-I4WDiCOt_8bbV0Rsg.JPEG.sjkor1005/KakaoTalk_20220520_150455625.jpg?type=w800",
          "description":"건물멸시등기신청",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=740835ee9d4c447b9bc13aee9cb31eab&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 상린관계
@application.route("/api/sangrin", methods=["POST"])
def sangrin ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"상린관계",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDYg/MDAxNjUzMDMwODgwMDQz.ZEtfPtFJWuk8x2S5CJmzC4bKDq69JDLSCCAzsfCRMo0g.LXLYL_ULYoJK4dlRIMMV22ACLf-I4WDiCOt_8bbV0Rsg.JPEG.sjkor1005/KakaoTalk_20220520_150455625.jpg?type=w800",
          "description":"대지경계확정의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=4d59d3f8c97a40eba7c6249f565cac66&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 소유권
@application.route("/api/cowyou", methods=["POST"])
def cowyou ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"소유권",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDYg/MDAxNjUzMDMwODgwMDQz.ZEtfPtFJWuk8x2S5CJmzC4bKDq69JDLSCCAzsfCRMo0g.LXLYL_ULYoJK4dlRIMMV22ACLf-I4WDiCOt_8bbV0Rsg.JPEG.sjkor1005/KakaoTalk_20220520_150455625.jpg?type=w800",
          "description":"소유권보존등기(대위)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=cc2b09da7ac64c969552cf125e017056&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 소유권에 기한 물권적 청구권
@application.route("/api/cowyoumul", methods=["POST"])
def cowyoumul ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"소유권에 기한 물권적 청구권",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDYg/MDAxNjUzMDMwODgwMDQz.ZEtfPtFJWuk8x2S5CJmzC4bKDq69JDLSCCAzsfCRMo0g.LXLYL_ULYoJK4dlRIMMV22ACLf-I4WDiCOt_8bbV0Rsg.JPEG.sjkor1005/KakaoTalk_20220520_150455625.jpg?type=w800",
          "description":"준비서면(건물 등 철거, 피고)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=78228593e5ba41beb585885c19baa535&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 저당권
@application.route("/api/jeodang", methods=["POST"])
def jeodang ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"저당권",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDYg/MDAxNjUzMDMwODgwMDQz.ZEtfPtFJWuk8x2S5CJmzC4bKDq69JDLSCCAzsfCRMo0g.LXLYL_ULYoJK4dlRIMMV22ACLf-I4WDiCOt_8bbV0Rsg.JPEG.sjkor1005/KakaoTalk_20220520_150455625.jpg?type=w800",
          "description":"저당권설정 계약서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=7e684d568d54490abd6c940e3fdb317d&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 점유권
@application.route("/api/jeomu", methods=["POST"])
def jeomu ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"점유권",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDYg/MDAxNjUzMDMwODgwMDQz.ZEtfPtFJWuk8x2S5CJmzC4bKDq69JDLSCCAzsfCRMo0g.LXLYL_ULYoJK4dlRIMMV22ACLf-I4WDiCOt_8bbV0Rsg.JPEG.sjkor1005/KakaoTalk_20220520_150455625.jpg?type=w800",
          "description":"점유보유의 소(점유권에 기한 방해배제청구)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=387dd864722c484ea7745bcd1025f0b2&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

  
# 지상권과 전세권
@application.route("/api/onkwon", methods=["POST"])
def onkwon ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"지상권과 전세권",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDYg/MDAxNjUzMDMwODgwMDQz.ZEtfPtFJWuk8x2S5CJmzC4bKDq69JDLSCCAzsfCRMo0g.LXLYL_ULYoJK4dlRIMMV22ACLf-I4WDiCOt_8bbV0Rsg.JPEG.sjkor1005/KakaoTalk_20220520_150455625.jpg?type=w800",
          "description":"전세권설정등기신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=5c9472460a0b4bc4838d9bf023788d15&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

  
# 취득시효
@application.route("/api/sihyo", methods=["POST"])
def sihyo ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"취득시효",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDYg/MDAxNjUzMDMwODgwMDQz.ZEtfPtFJWuk8x2S5CJmzC4bKDq69JDLSCCAzsfCRMo0g.LXLYL_ULYoJK4dlRIMMV22ACLf-I4WDiCOt_8bbV0Rsg.JPEG.sjkor1005/KakaoTalk_20220520_150455625.jpg?type=w800",
          "description":"소유권이전등기청구의 소(국유 일반재산 점유취득)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=743bf657b0484249acc2ad0f9edd3355&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

## 형사소송 10개 ##
# 고소 고발
@application.route("/api/secret", methods=["POST"])
def secret ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"고소 고발",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjgg/MDAxNjUzMDMwODgwNzYy.JqA5JKUj0wdzNYRJmvANWzEIiUP22iXPuPImaV9GOUgg.ke6InpeEZd5hd5fWK-f1hKG7kg8kT4FpqphN6ufWwlQg.JPEG.sjkor1005/KakaoTalk_20220520_160327703.jpg?type=w800",
          "description":"비밀침해죄",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=7ef68a2d6f724150b05b0da8f0fc7873&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 기타 형사절차
@application.route("/api/etcbrothersa", methods=["POST"])
def etcbrothersa ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"기타 형사절차",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjgg/MDAxNjUzMDMwODgwNzYy.JqA5JKUj0wdzNYRJmvANWzEIiUP22iXPuPImaV9GOUgg.ke6InpeEZd5hd5fWK-f1hKG7kg8kT4FpqphN6ufWwlQg.JPEG.sjkor1005/KakaoTalk_20220520_160327703.jpg?type=w800",
          "description":"사건이송신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=a8eeb0a3958c4d23a360d0e0130d27b0&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 불기소처분 및 불복
@application.route("/api/firecow", methods=["POST"])
def firecow ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"불기소처분 및 불복",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjgg/MDAxNjUzMDMwODgwNzYy.JqA5JKUj0wdzNYRJmvANWzEIiUP22iXPuPImaV9GOUgg.ke6InpeEZd5hd5fWK-f1hKG7kg8kT4FpqphN6ufWwlQg.JPEG.sjkor1005/KakaoTalk_20220520_160327703.jpg?type=w800",
          "description":"항고장(검사의 불기소처분)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=de8accb841334e09b10cfd3c9431e4d6&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 상소
@application.route("/api/upso", methods=["POST"])
def upso ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"상소",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjgg/MDAxNjUzMDMwODgwNzYy.JqA5JKUj0wdzNYRJmvANWzEIiUP22iXPuPImaV9GOUgg.ke6InpeEZd5hd5fWK-f1hKG7kg8kT4FpqphN6ufWwlQg.JPEG.sjkor1005/KakaoTalk_20220520_160327703.jpg?type=w800",
          "description":"상고이유서(절도)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=d5bf4df34281471d8ed5ab34acdbc461&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 소년 및 가정보호사건
@application.route("/api/boyand", methods=["POST"])
def boyand ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"소년 및 가정보호사건",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjgg/MDAxNjUzMDMwODgwNzYy.JqA5JKUj0wdzNYRJmvANWzEIiUP22iXPuPImaV9GOUgg.ke6InpeEZd5hd5fWK-f1hKG7kg8kT4FpqphN6ufWwlQg.JPEG.sjkor1005/KakaoTalk_20220520_160327703.jpg?type=w800",
          "description":"위탁변경신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=6ba8de0ec3bb4500ac521652edc806f1&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 소송절차 및 증거
@application.route("/api/sosongevidence", methods=["POST"])
def sosongevidence ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"소송절차 및 증거",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjgg/MDAxNjUzMDMwODgwNzYy.JqA5JKUj0wdzNYRJmvANWzEIiUP22iXPuPImaV9GOUgg.ke6InpeEZd5hd5fWK-f1hKG7kg8kT4FpqphN6ufWwlQg.JPEG.sjkor1005/KakaoTalk_20220520_160327703.jpg?type=w800",
          "description":"증언거부사유서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=e30def2ec2db4aecb04629db0f6733a0&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 인신보호사건
@application.route("/api/insinboho", methods=["POST"])
def insinboho ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"인신보호사건",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjgg/MDAxNjUzMDMwODgwNzYy.JqA5JKUj0wdzNYRJmvANWzEIiUP22iXPuPImaV9GOUgg.ke6InpeEZd5hd5fWK-f1hKG7kg8kT4FpqphN6ufWwlQg.JPEG.sjkor1005/KakaoTalk_20220520_160327703.jpg?type=w800",
          "description":"구제청구서(수용시설)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=5cf960297ed94f0bb561143ea932618b&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 재심, 약식절차
@application.route("/api/jaesimmanual", methods=["POST"])
def jaesimmanual ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"재심, 약식절차",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjgg/MDAxNjUzMDMwODgwNzYy.JqA5JKUj0wdzNYRJmvANWzEIiUP22iXPuPImaV9GOUgg.ke6InpeEZd5hd5fWK-f1hKG7kg8kT4FpqphN6ufWwlQg.JPEG.sjkor1005/KakaoTalk_20220520_160327703.jpg?type=w800",
          "description":"재심청구서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=fa82a255747a4b62b66b3573759fd539&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 재판의 집행
@application.route("/api/jibhang", methods=["POST"])
def jibhang ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"재판의 집행",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjgg/MDAxNjUzMDMwODgwNzYy.JqA5JKUj0wdzNYRJmvANWzEIiUP22iXPuPImaV9GOUgg.ke6InpeEZd5hd5fWK-f1hKG7kg8kT4FpqphN6ufWwlQg.JPEG.sjkor1005/KakaoTalk_20220520_160327703.jpg?type=w800",
          "description":"재판 집행에 관한 이의신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=293d02cb845944a882c6b8e859081d56&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 체포구속및 석방 보석
@application.route("/api/arrest", methods=["POST"])
def arrest ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"체포,구속,석방,보석",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjgg/MDAxNjUzMDMwODgwNzYy.JqA5JKUj0wdzNYRJmvANWzEIiUP22iXPuPImaV9GOUgg.ke6InpeEZd5hd5fWK-f1hKG7kg8kT4FpqphN6ufWwlQg.JPEG.sjkor1005/KakaoTalk_20220520_160327703.jpg?type=w800",
          "description":"보석조건변경신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=a8af82edb8634b2fa14ac3d1567eaffb&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)



## 형법 12개 ##
# 강간과 추행의 죄
@application.route("/api/rape", methods=["POST"])
def rape ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"강간과 추행의 죄",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDkg/MDAxNjUzMDMwODgwNzY3.q2zxowJ7byvF3ZSN0Uj7WguAaP_-g-2brbLJdolaDlwg.-MTnx2yqFMDIjckwXpAqUsdMLBlwv7OiFfcMzDHMqJwg.JPEG.sjkor1005/KakaoTalk_20220520_160557016.jpg?type=w800",
          "description":"강제추행죄(고소장)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=f3acfa39942c4339ba0d39dafa34c125&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 공무방해에 관한 죄
@application.route("/api/banghae", methods=["POST"])
def banghae ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"공무방해에 관한 죄",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDkg/MDAxNjUzMDMwODgwNzY3.q2zxowJ7byvF3ZSN0Uj7WguAaP_-g-2brbLJdolaDlwg.-MTnx2yqFMDIjckwXpAqUsdMLBlwv7OiFfcMzDHMqJwg.JPEG.sjkor1005/KakaoTalk_20220520_160557016.jpg?type=w800",
          "description":"공무상비밀표시무효죄",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=270d6c59391b4c4eabbcc2c866d5991e&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 공무원의 직무에 관한 죄
@application.route("/api/gongmu1", methods=["POST"])
def gongmu1 ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"공무원의 직무에 관한 죄",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDkg/MDAxNjUzMDMwODgwNzY3.q2zxowJ7byvF3ZSN0Uj7WguAaP_-g-2brbLJdolaDlwg.-MTnx2yqFMDIjckwXpAqUsdMLBlwv7OiFfcMzDHMqJwg.JPEG.sjkor1005/KakaoTalk_20220520_160557016.jpg?type=w800",
          "description":"폭행가혹행위죄",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=263528c8c4df4ca6a3d5abd5ced80982&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 과실치사상의 죄
@application.route("/api/fruit", methods=["POST"])
def fruit ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"과실치사상의 죄",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDkg/MDAxNjUzMDMwODgwNzY3.q2zxowJ7byvF3ZSN0Uj7WguAaP_-g-2brbLJdolaDlwg.-MTnx2yqFMDIjckwXpAqUsdMLBlwv7OiFfcMzDHMqJwg.JPEG.sjkor1005/KakaoTalk_20220520_160557016.jpg?type=w800",
          "description":"업무상과실치상죄(의료사고)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=b58d5fe904dc464b904788ad0113ef62&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 교통사고처리특례법 위반죄
@application.route("/api/gyotong", methods=["POST"])
def gyotong ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"교통사고처리특례법 위반죄",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDkg/MDAxNjUzMDMwODgwNzY3.q2zxowJ7byvF3ZSN0Uj7WguAaP_-g-2brbLJdolaDlwg.-MTnx2yqFMDIjckwXpAqUsdMLBlwv7OiFfcMzDHMqJwg.JPEG.sjkor1005/KakaoTalk_20220520_160557016.jpg?type=w800",
          "description":"중앙선침범",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=15fdf655f72a4c4d9da3188c0c90307b&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 명예에 관한 죄
@application.route("/api/myungyeah", methods=["POST"])
def myungyeah ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"명예에 관한 죄",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDkg/MDAxNjUzMDMwODgwNzY3.q2zxowJ7byvF3ZSN0Uj7WguAaP_-g-2brbLJdolaDlwg.-MTnx2yqFMDIjckwXpAqUsdMLBlwv7OiFfcMzDHMqJwg.JPEG.sjkor1005/KakaoTalk_20220520_160557016.jpg?type=w800",
          "description":"명예훼손죄",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=8dce60f87cd54cde8ff21ef2ad972d16&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 무고의 죄
@application.route("/api/mugo", methods=["POST"])
def mugo ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"무고의 죄",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDkg/MDAxNjUzMDMwODgwNzY3.q2zxowJ7byvF3ZSN0Uj7WguAaP_-g-2brbLJdolaDlwg.-MTnx2yqFMDIjckwXpAqUsdMLBlwv7OiFfcMzDHMqJwg.JPEG.sjkor1005/KakaoTalk_20220520_160557016.jpg?type=w800",
          "description":"무고죄",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=24a67d343d244384ba30a836337f6f3b&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 문서에 관한 죄
@application.route("/api/doorup", methods=["POST"])
def doorup ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"문서에 관한 죄",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDkg/MDAxNjUzMDMwODgwNzY3.q2zxowJ7byvF3ZSN0Uj7WguAaP_-g-2brbLJdolaDlwg.-MTnx2yqFMDIjckwXpAqUsdMLBlwv7OiFfcMzDHMqJwg.JPEG.sjkor1005/KakaoTalk_20220520_160557016.jpg?type=w800",
          "description":"사문서위조죄",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=8379327ae49d464baa9f8707248c3e45&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 방화와 실화의 죄
@application.route("/api/fire", methods=["POST"])
def fire ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"방화와 실화의 죄",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDkg/MDAxNjUzMDMwODgwNzY3.q2zxowJ7byvF3ZSN0Uj7WguAaP_-g-2brbLJdolaDlwg.-MTnx2yqFMDIjckwXpAqUsdMLBlwv7OiFfcMzDHMqJwg.JPEG.sjkor1005/KakaoTalk_20220520_160557016.jpg?type=w800",
          "description":"방화죄",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=955036d13e8f42f8992c08cead6a4cb9&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 사기와 공갈의 죄
@application.route("/api/cheater", methods=["POST"])
def cheater ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"사기와 공갈의 죄",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDkg/MDAxNjUzMDMwODgwNzY3.q2zxowJ7byvF3ZSN0Uj7WguAaP_-g-2brbLJdolaDlwg.-MTnx2yqFMDIjckwXpAqUsdMLBlwv7OiFfcMzDHMqJwg.JPEG.sjkor1005/KakaoTalk_20220520_160557016.jpg?type=w800",
          "description":"사기죄",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=40c6241e60ef43a1a0e8d423a694c931&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 살인의 죄
@application.route("/api/murder", methods=["POST"])
def murder ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"살인의 죄",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDkg/MDAxNjUzMDMwODgwNzY3.q2zxowJ7byvF3ZSN0Uj7WguAaP_-g-2brbLJdolaDlwg.-MTnx2yqFMDIjckwXpAqUsdMLBlwv7OiFfcMzDHMqJwg.JPEG.sjkor1005/KakaoTalk_20220520_160557016.jpg?type=w800",
          "description":"위계에 의한 살인미수죄",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=bf85acf3e00145f5914baa5670b8d331&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 상해와 폭행의 죄
@application.route("/api/hit", methods=["POST"])
def hit ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"상해와 폭행의 죄",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDkg/MDAxNjUzMDMwODgwNzY3.q2zxowJ7byvF3ZSN0Uj7WguAaP_-g-2brbLJdolaDlwg.-MTnx2yqFMDIjckwXpAqUsdMLBlwv7OiFfcMzDHMqJwg.JPEG.sjkor1005/KakaoTalk_20220520_160557016.jpg?type=w800",
          "description":"폭행죄",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=0eda475e89b94f91a5d2af5984fcb2a5&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


## 손해배상 9개 ##
# 공해
@application.route("/api/gonghae", methods=["POST"])
def gonghae ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"공해",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjI1/MDAxNjUzMDMwODc5ODk1.MyrLpEd4CufvgwFR1E2c_zl34r8wxUz1bEvXvRvSKw4g.0KsSmolLQZ5DHjO3TrSW92WC2opmmnUGgcx0MhN-CwUg.JPEG.sjkor1005/KakaoTalk_20220520_145354742.jpg?type=w800",
          "description":"손해배상(공)청구의 소(기름유출)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=60be68b8c57b4d31b2c7fce47d366828&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 기타 손해배상
@application.route("/api/etccompensation", methods=["POST"])
def etccompensation ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"기타손해배상",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjI1/MDAxNjUzMDMwODc5ODk1.MyrLpEd4CufvgwFR1E2c_zl34r8wxUz1bEvXvRvSKw4g.0KsSmolLQZ5DHjO3TrSW92WC2opmmnUGgcx0MhN-CwUg.JPEG.sjkor1005/KakaoTalk_20220520_145354742.jpg?type=w800",
          "description":"반론보도청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=702a89c9e33b4f59ac53a049889fbb68&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 범죄피해
@application.route("/api/criminal", methods=["POST"])
def criminal ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"범죄피해",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjI1/MDAxNjUzMDMwODc5ODk1.MyrLpEd4CufvgwFR1E2c_zl34r8wxUz1bEvXvRvSKw4g.0KsSmolLQZ5DHjO3TrSW92WC2opmmnUGgcx0MhN-CwUg.JPEG.sjkor1005/KakaoTalk_20220520_145354742.jpg?type=w800",
          "description":"손해배상(공)청구의 소(협박)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=1cf3d5ed37374519ae2812717bd7e5f9&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 불법사금융(보이스피싱)
@application.route("/api/voice", methods=["POST"])
def voice ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"불법사금융(보이스피싱)",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjI1/MDAxNjUzMDMwODc5ODk1.MyrLpEd4CufvgwFR1E2c_zl34r8wxUz1bEvXvRvSKw4g.0KsSmolLQZ5DHjO3TrSW92WC2opmmnUGgcx0MhN-CwUg.JPEG.sjkor1005/KakaoTalk_20220520_145354742.jpg?type=w800",
          "description":"손해배상(기) 청구의 소(보이스 피싱)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=015787c1051c4e198668a553345588bf&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 산재사고
@application.route("/api/accident", methods=["POST"])
def accident ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"산재사고",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjI1/MDAxNjUzMDMwODc5ODk1.MyrLpEd4CufvgwFR1E2c_zl34r8wxUz1bEvXvRvSKw4g.0KsSmolLQZ5DHjO3TrSW92WC2opmmnUGgcx0MhN-CwUg.JPEG.sjkor1005/KakaoTalk_20220520_145354742.jpg?type=w800",
          "description":"손해배상(산)청구의 소(안전시설 미비, 공동불법행위)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=5d41f5462d1b49a4a5af929f5855a0cc&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 성폭력피해(일반)
@application.route("/api/violence", methods=["POST"])
def violence ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"성폭력피해(일반)",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjI1/MDAxNjUzMDMwODc5ODk1.MyrLpEd4CufvgwFR1E2c_zl34r8wxUz1bEvXvRvSKw4g.0KsSmolLQZ5DHjO3TrSW92WC2opmmnUGgcx0MhN-CwUg.JPEG.sjkor1005/KakaoTalk_20220520_145354742.jpg?type=w800",
          "description":" 손해배상(기)청구의 소(강간)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=75d2c947c0094a76a0b32cefd7dff817&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 의료과오
@application.route("/api/doctor", methods=["POST"])
def doctor ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"의료과오",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjI1/MDAxNjUzMDMwODc5ODk1.MyrLpEd4CufvgwFR1E2c_zl34r8wxUz1bEvXvRvSKw4g.0KsSmolLQZ5DHjO3TrSW92WC2opmmnUGgcx0MhN-CwUg.JPEG.sjkor1005/KakaoTalk_20220520_145354742.jpg?type=w800",
          "description":"손해배상(의)청구의 소(출산 중 사고, 장해발생, 채무불이행책임)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=de912ec8349d40ca90352e3e36a77642&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 자동차사고
@application.route("/api/car", methods=["POST"])
def car ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"자동차사고",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjI1/MDAxNjUzMDMwODc5ODk1.MyrLpEd4CufvgwFR1E2c_zl34r8wxUz1bEvXvRvSKw4g.0KsSmolLQZ5DHjO3TrSW92WC2opmmnUGgcx0MhN-CwUg.JPEG.sjkor1005/KakaoTalk_20220520_145354742.jpg?type=w800",
          "description":"손해배상(자)청구의 소(미성년 남자고등학생, 부상)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=204869758823486eae79210fbb1941ce&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 지적소유권
@application.route("/api/ownership", methods=["POST"])
def ownership ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"지적소유권",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjI1/MDAxNjUzMDMwODc5ODk1.MyrLpEd4CufvgwFR1E2c_zl34r8wxUz1bEvXvRvSKw4g.0KsSmolLQZ5DHjO3TrSW92WC2opmmnUGgcx0MhN-CwUg.JPEG.sjkor1005/KakaoTalk_20220520_145354742.jpg?type=w800",
          "description":"손해배상(의)청구의 소(저작권 침해)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=8e1b34e037e04502b00fcb05caf325e6&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

## 친족 6개 ##
# 입양,파양,친양자 / 재판상이혼 / 친권 / 친생자 / 협의이혼 / 혼인의성립~/후견인 없음
# 면접교섭권
@application.route("/api/meetplz", methods=["POST"])
def meetplz ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"면접교섭권",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjg2/MDAxNjUzMDMwODgwMjIz.evmsQvzTJJHw88iTdE4SDZp9XievJ6k1eZruPGcdhXQg.mZlyYt1WRcFovI8goChh2ilqjPibqlD4CCrlkGtQbMAg.JPEG.sjkor1005/KakaoTalk_20220520_152145221.jpg?type=w800",
          "description":"면접교섭허가 심판청구서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=07b107fe376d4b1bad8f79130d9d1034&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 부양
@application.route("/api/parent", methods=["POST"])
def parent ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"부양",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjg2/MDAxNjUzMDMwODgwMjIz.evmsQvzTJJHw88iTdE4SDZp9XievJ6k1eZruPGcdhXQg.mZlyYt1WRcFovI8goChh2ilqjPibqlD4CCrlkGtQbMAg.JPEG.sjkor1005/KakaoTalk_20220520_152145221.jpg?type=w800",
          "description":"부양료청구 조정신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=3c240f18fe6c41e98c2a3663b444ab86&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 약혼
@application.route("/api/yakkon", methods=["POST"])
def yakkon ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"약혼",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjg2/MDAxNjUzMDMwODgwMjIz.evmsQvzTJJHw88iTdE4SDZp9XievJ6k1eZruPGcdhXQg.mZlyYt1WRcFovI8goChh2ilqjPibqlD4CCrlkGtQbMAg.JPEG.sjkor1005/KakaoTalk_20220520_152145221.jpg?type=w800",
          "description":"약혼예물 반환 조정신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=fc695bc39a1541778c92f155ecc0f73b&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 양육비
@application.route("/api/childmoney", methods=["POST"])
def childmoney ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"양육비",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjg2/MDAxNjUzMDMwODgwMjIz.evmsQvzTJJHw88iTdE4SDZp9XievJ6k1eZruPGcdhXQg.mZlyYt1WRcFovI8goChh2ilqjPibqlD4CCrlkGtQbMAg.JPEG.sjkor1005/KakaoTalk_20220520_152145221.jpg?type=w800",
          "description":"양육비 심판청구서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=577b82e32e844623862da7d09a4438bb&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 이혼및 위자료
@application.route("/api/devomoney", methods=["POST"])
def devomoney ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"이혼 및 위자료",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjg2/MDAxNjUzMDMwODgwMjIz.evmsQvzTJJHw88iTdE4SDZp9XievJ6k1eZruPGcdhXQg.mZlyYt1WRcFovI8goChh2ilqjPibqlD4CCrlkGtQbMAg.JPEG.sjkor1005/KakaoTalk_20220520_152145221.jpg?type=w800",
          "description":"이혼 및 위자료 조정신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=b630bb4dd845490883518f251ef241ae&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 이혼및 재산분할청구권
@application.route("/api/devoshare", methods=["POST"])
def devoshare ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"이혼 및 재산분할청구권",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjg2/MDAxNjUzMDMwODgwMjIz.evmsQvzTJJHw88iTdE4SDZp9XievJ6k1eZruPGcdhXQg.mZlyYt1WRcFovI8goChh2ilqjPibqlD4CCrlkGtQbMAg.JPEG.sjkor1005/KakaoTalk_20220520_152145221.jpg?type=w800",
          "description":"재산분할 심판청구서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=b5672ff47265455a97ba6c862c54341a&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

## 가족관계등록 4개 ##
# 가족관계등록부정정
@application.route("/api/fchange", methods=["POST"])
def fchange ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"가족관계등록부 정정",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjE5/MDAxNjUzMDMwODgwNTE2.tCYAFhpraHU57yBETLnAF2SdM7_J7tGpTDN8Cin5RLMg.Nn_zF964R9YTUY1-_qvJ2h7XJpWIUiD6jQ1aztVXsCQg.JPEG.sjkor1005/KakaoTalk_20220520_153418176.jpg?type=w800",
          "description":"등록부정정허가신청서(성전환자)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=888037d05726488f8eb4d29fab256bfd&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 가족관계등록창설
@application.route("/api/fmake", methods=["POST"])
def fmake ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"가족관계등록창설",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjE5/MDAxNjUzMDMwODgwNTE2.tCYAFhpraHU57yBETLnAF2SdM7_J7tGpTDN8Cin5RLMg.Nn_zF964R9YTUY1-_qvJ2h7XJpWIUiD6jQ1aztVXsCQg.JPEG.sjkor1005/KakaoTalk_20220520_153418176.jpg?type=w800",
          "description":"가족관계등록 창설허가신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=784c1257d8224f1983b530824ba30c4e&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 국적의 취득과 상실
@application.route("/api/nation", methods=["POST"])
def nation ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"국적의 취득과 상실",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjE5/MDAxNjUzMDMwODgwNTE2.tCYAFhpraHU57yBETLnAF2SdM7_J7tGpTDN8Cin5RLMg.Nn_zF964R9YTUY1-_qvJ2h7XJpWIUiD6jQ1aztVXsCQg.JPEG.sjkor1005/KakaoTalk_20220520_153418176.jpg?type=w800",
          "description":"국적취득 신고서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=b8f3942aacda454a938989c50a149da2&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 신고
@application.route("/api/tell", methods=["POST"])
def tell ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"신고",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjE5/MDAxNjUzMDMwODgwNTE2.tCYAFhpraHU57yBETLnAF2SdM7_J7tGpTDN8Cin5RLMg.Nn_zF964R9YTUY1-_qvJ2h7XJpWIUiD6jQ1aztVXsCQg.JPEG.sjkor1005/KakaoTalk_20220520_153418176.jpg?type=w800",
          "description":"혼인신고서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=655c677604f14a17ada3f1762ddfac17&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


## 가사소송 4개 ##
# 가,나,다류 가사소송
@application.route("/api/fsosong", methods=["POST"])
def fsosong ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"가,나,다류 가사소송",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM0/MDAxNjUzMDI5NjMyODcz.4TEg-GKjBWl1vgbI0LPzPNUZYj2or1DOpZI1atSRCz4g.UPU82fFQ2VMXF9QJZ4lOBhNsXUJSmHRMDSqeVt7hJ9Mg.JPEG.sjkor1005/KakaoTalk_20220520_153001826.jpg?type=w800",
          "description":"친자 감정신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=f2733558278a4a038eff25e7675bc02d&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}           
 
    return jsonify(response)


# 가사소송 일반
@application.route("/api/fsosong1ban", methods=["POST"])
def fsosong1ban ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"가사소송 일반",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM0/MDAxNjUzMDI5NjMyODcz.4TEg-GKjBWl1vgbI0LPzPNUZYj2or1DOpZI1atSRCz4g.UPU82fFQ2VMXF9QJZ4lOBhNsXUJSmHRMDSqeVt7hJ9Mg.JPEG.sjkor1005/KakaoTalk_20220520_153001826.jpg?type=w800",
          "description":"불거주확인서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=7a16dd1df94749508ccf5aa2a927a309&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 과태료와 감치
@application.route("/api/gamchi", methods=["POST"])
def gamchi ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"과태료와 감치",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM0/MDAxNjUzMDI5NjMyODcz.4TEg-GKjBWl1vgbI0LPzPNUZYj2or1DOpZI1atSRCz4g.UPU82fFQ2VMXF9QJZ4lOBhNsXUJSmHRMDSqeVt7hJ9Mg.JPEG.sjkor1005/KakaoTalk_20220520_153001826.jpg?type=w800",
          "description":"감치명령신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=33f5da7315ac4503b0e39a57e8bfefec&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 기타
@application.route("/api/etcfsosong", methods=["POST"])
def etcfsosong ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"기타",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM0/MDAxNjUzMDI5NjMyODcz.4TEg-GKjBWl1vgbI0LPzPNUZYj2or1DOpZI1atSRCz4g.UPU82fFQ2VMXF9QJZ4lOBhNsXUJSmHRMDSqeVt7hJ9Mg.JPEG.sjkor1005/KakaoTalk_20220520_153001826.jpg?type=w800",
          "description":"유아인도 조정신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=911d141c3bda454489067173355818f2&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


## 행정 11개 ##
# 건축관련 행정
@application.route("/api/archhaeng", methods=["POST"])
def archhaeng ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"건축 관련 행정",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM5/MDAxNjUzMDMwODgwOTA5.uXUwMxhaiAAZgM-gQswiIucIUn42L7ZMo_J53F0Zvcgg.8tXS2tRV4QPePUQ5ivRb1dC6EdRKlPawUT69Q7JSGtAg.JPEG.sjkor1005/KakaoTalk_20220520_160826196.jpg?type=w800",
          "description":"건축공사 중지명령처분 취소청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=d2d8c2381d6b4eca98161392c1742d1f&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    },
    {
      "type":"card.image",
      "cards":[
        {
          "title":"건축 관련 행정",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM5/MDAxNjUzMDMwODgwOTA5.uXUwMxhaiAAZgM-gQswiIucIUn42L7ZMo_J53F0Zvcgg.8tXS2tRV4QPePUQ5ivRb1dC6EdRKlPawUT69Q7JSGtAg.JPEG.sjkor1005/KakaoTalk_20220520_160826196.jpg?type=w800",
          "description":"건축 불허가처분 취소청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=f252ab0af9f342c6a0a88a4433da0259&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
        ]
    }
    return jsonify(response)


# 교통관련 행정
@application.route("/api/carhaeng", methods=["POST"])
def carhaeng ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"교통 관련 행정",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM5/MDAxNjUzMDMwODgwOTA5.uXUwMxhaiAAZgM-gQswiIucIUn42L7ZMo_J53F0Zvcgg.8tXS2tRV4QPePUQ5ivRb1dC6EdRKlPawUT69Q7JSGtAg.JPEG.sjkor1005/KakaoTalk_20220520_160826196.jpg?type=w800",
          "description":"자동차 운전면허취소처분 취소청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=3915ab8b88914229acb4a9a8422dbadb&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}    
    return jsonify(response)


# 기타행정
@application.route("/api/etchaeng", methods=["POST"])
def etchaeng ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"기타 행정",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM5/MDAxNjUzMDMwODgwOTA5.uXUwMxhaiAAZgM-gQswiIucIUn42L7ZMo_J53F0Zvcgg.8tXS2tRV4QPePUQ5ivRb1dC6EdRKlPawUT69Q7JSGtAg.JPEG.sjkor1005/KakaoTalk_20220520_160826196.jpg?type=w800",
          "description":"해임처분 취소청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=1842373d1c9848f9a76fccd51baee827&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    },
    {
      "type":"card.image",
      "cards":[
        {
          "title":"기타 행정",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM5/MDAxNjUzMDMwODgwOTA5.uXUwMxhaiAAZgM-gQswiIucIUn42L7ZMo_J53F0Zvcgg.8tXS2tRV4QPePUQ5ivRb1dC6EdRKlPawUT69Q7JSGtAg.JPEG.sjkor1005/KakaoTalk_20220520_160826196.jpg?type=w800",
          "description":"부당해고 구제재심판정 취소청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=330034a7a382431da7300061bbf22c07&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}
    return jsonify(response)


# 난민관련 행정
@application.route("/api/nanminhaeng", methods=["POST"])
def nanminhaeng ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"난민관련 행정",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM5/MDAxNjUzMDMwODgwOTA5.uXUwMxhaiAAZgM-gQswiIucIUn42L7ZMo_J53F0Zvcgg.8tXS2tRV4QPePUQ5ivRb1dC6EdRKlPawUT69Q7JSGtAg.JPEG.sjkor1005/KakaoTalk_20220520_160826196.jpg?type=w800",
          "description":"난민불인정처분 취소청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=d28e27b69a3d45098b5ebe41ab7fd02e&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
            
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 부동산 관련 행정
@application.route("/api/budongsanhaeng", methods=["POST"])
def budongsanhaeng ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"부동산관련 행정",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM5/MDAxNjUzMDMwODgwOTA5.uXUwMxhaiAAZgM-gQswiIucIUn42L7ZMo_J53F0Zvcgg.8tXS2tRV4QPePUQ5ivRb1dC6EdRKlPawUT69Q7JSGtAg.JPEG.sjkor1005/KakaoTalk_20220520_160826196.jpg?type=w800",
          "description":"손실보상금 청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=51a9b96541d54f30900aa0e3bbfb3b50&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
            
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 산재 관련 행정
@application.route("/api/sanjaehaeng", methods=["POST"])
def sanjaehaeng ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"산재관련 행정",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM5/MDAxNjUzMDMwODgwOTA5.uXUwMxhaiAAZgM-gQswiIucIUn42L7ZMo_J53F0Zvcgg.8tXS2tRV4QPePUQ5ivRb1dC6EdRKlPawUT69Q7JSGtAg.JPEG.sjkor1005/KakaoTalk_20220520_160826196.jpg?type=w800",
          "description":"장해등급 결정처분 취소청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=a00cf5941e274d638674d191021f9034&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 영업관련 행정
@application.route("/api/up0haeng", methods=["POST"])
def up0haeng ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"영업관련 행정",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM5/MDAxNjUzMDMwODgwOTA5.uXUwMxhaiAAZgM-gQswiIucIUn42L7ZMo_J53F0Zvcgg.8tXS2tRV4QPePUQ5ivRb1dC6EdRKlPawUT69Q7JSGtAg.JPEG.sjkor1005/KakaoTalk_20220520_160826196.jpg?type=w800",
          "description":"영업정지처분 취소청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=5015d95281c6413bb75de83d3220016e&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 유공자관련 행정
@application.route("/api/honorhaeng", methods=["POST"])
def honorhaeng ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"유공자관련 행정",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM5/MDAxNjUzMDMwODgwOTA5.uXUwMxhaiAAZgM-gQswiIucIUn42L7ZMo_J53F0Zvcgg.8tXS2tRV4QPePUQ5ivRb1dC6EdRKlPawUT69Q7JSGtAg.JPEG.sjkor1005/KakaoTalk_20220520_160826196.jpg?type=w800",
          "description":"전공상 불인정처분 취소청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=2e6250be23a447afbe21fb4f59a5bc33&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 조세관련 행정
@application.route("/api/jobirdhaeng", methods=["POST"])
def jobirdhaeng ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"조세관련 행정",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM5/MDAxNjUzMDMwODgwOTA5.uXUwMxhaiAAZgM-gQswiIucIUn42L7ZMo_J53F0Zvcgg.8tXS2tRV4QPePUQ5ivRb1dC6EdRKlPawUT69Q7JSGtAg.JPEG.sjkor1005/KakaoTalk_20220520_160826196.jpg?type=w800",
          "description":"양도소득세 부과처분 취소청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=07ac45a36f574cfb870e4ad8a268953f&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 행정소송일반
@application.route("/api/haeng1ban", methods=["POST"])
def haeng1ban ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"행정소송 일반",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM5/MDAxNjUzMDMwODgwOTA5.uXUwMxhaiAAZgM-gQswiIucIUn42L7ZMo_J53F0Zvcgg.8tXS2tRV4QPePUQ5ivRb1dC6EdRKlPawUT69Q7JSGtAg.JPEG.sjkor1005/KakaoTalk_20220520_160826196.jpg?type=w800",
          "description":"행정소송의 관할",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=136dc06a196e4592b0f3fd96f92146ca&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 행정심판
@application.route("/api/haengsimpan", methods=["POST"])
def haengsimpan ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"행정심판",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM5/MDAxNjUzMDMwODgwOTA5.uXUwMxhaiAAZgM-gQswiIucIUn42L7ZMo_J53F0Zvcgg.8tXS2tRV4QPePUQ5ivRb1dC6EdRKlPawUT69Q7JSGtAg.JPEG.sjkor1005/KakaoTalk_20220520_160826196.jpg?type=w800",
          "description":"행정심판의 대상",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=c2e4d00ee4954a7b9aa5ba4b897477b4&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


## 민사일반 4개 ##
# 대리
@application.route("/api/daeri", methods=["POST"])
def daeri ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"대리",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTU0/MDAxNjUzMDMwODc5OTA3.v9zTR-h9yigO1D0rbGoed9fsEtb5-NWuIU_3KSwCSR4g.bTsEYl7VXy-tHwh74Yz9P4sb2BYvarUndbuVbqlLTPMg.JPEG.sjkor1005/KakaoTalk_20220520_145831643.jpg?type=w800",
          "description":"소유권이전등기말소청구의 소(토지, 사실혼관계 처의 무권대리)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=fbd53b69e3a748d991b9d86b1671135a&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 법률행위일반
@application.route("/api/legalact", methods=["POST"])
def legalact ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"법률행위일반",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTU0/MDAxNjUzMDMwODc5OTA3.v9zTR-h9yigO1D0rbGoed9fsEtb5-NWuIU_3KSwCSR4g.bTsEYl7VXy-tHwh74Yz9P4sb2BYvarUndbuVbqlLTPMg.JPEG.sjkor1005/KakaoTalk_20220520_145831643.jpg?type=w800",
          "description":"소유권이전등기말소청구의 소(토지, 제3자의 문서위조)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=96fc1a44596749bf9607cd571769f25c&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 소멸시효
@application.route("/api/somuel", methods=["POST"])
def somuel ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"소멸시효",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTU0/MDAxNjUzMDMwODc5OTA3.v9zTR-h9yigO1D0rbGoed9fsEtb5-NWuIU_3KSwCSR4g.bTsEYl7VXy-tHwh74Yz9P4sb2BYvarUndbuVbqlLTPMg.JPEG.sjkor1005/KakaoTalk_20220520_145831643.jpg?type=w800",
          "description":"소멸시효 일람표",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=b374fd4445f6422b9e9182b394b6818b&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 제한능력자
@application.route("/api/limitperson", methods=["POST"])
def limitperson ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"제한능력자",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTU0/MDAxNjUzMDMwODc5OTA3.v9zTR-h9yigO1D0rbGoed9fsEtb5-NWuIU_3KSwCSR4g.bTsEYl7VXy-tHwh74Yz9P4sb2BYvarUndbuVbqlLTPMg.JPEG.sjkor1005/KakaoTalk_20220520_145831643.jpg?type=w800",
          "description":"내용증명(계약취소-미성년자 할부구입 책)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=15750fd2ac8a4962badec7b678403f1e&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


## 민사집행 8개 ##
# 강제집행일반
@application.route("/api/must1", methods=["POST"])
def must1 ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"강제집행일반",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjM0/MDAxNjUzMDMwODgwNTY1.TDf0TP5ijzmF-3RJ8RIPuMUnM6H8jJspL7ZaoDUX35Yg.yWKCWZtgEgqpfBfhxqWBqTqeDp7zFM8tjYp0lmQjmVYg.JPEG.sjkor1005/KakaoTalk_20220520_153817905.jpg?type=w800",
          "description":"간접강제신청",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=6cccf70ca841464abe1a3263f17e8751&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 금전채권 강제집행
@application.route("/api/moneymust", methods=["POST"])
def moneymust ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"금전채권 강제집행",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjM0/MDAxNjUzMDMwODgwNTY1.TDf0TP5ijzmF-3RJ8RIPuMUnM6H8jJspL7ZaoDUX35Yg.yWKCWZtgEgqpfBfhxqWBqTqeDp7zFM8tjYp0lmQjmVYg.JPEG.sjkor1005/KakaoTalk_20220520_153817905.jpg?type=w800",
          "description":"채권압류 및 전부명령신청",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=910a22d6c8314719a8be08a4e7df0d07&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 기타강제집행
@application.route("/api/etcmust", methods=["POST"])
def etcmust ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"기타 강제집행",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjM0/MDAxNjUzMDMwODgwNTY1.TDf0TP5ijzmF-3RJ8RIPuMUnM6H8jJspL7ZaoDUX35Yg.yWKCWZtgEgqpfBfhxqWBqTqeDp7zFM8tjYp0lmQjmVYg.JPEG.sjkor1005/KakaoTalk_20220520_153817905.jpg?type=w800",
          "description":"특별현금화 매각명령신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=18c0b8c5e6244a15841573ce185652b4&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"금전채권 강제집행",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjM0/MDAxNjUzMDMwODgwNTY1.TDf0TP5ijzmF-3RJ8RIPuMUnM6H8jJspL7ZaoDUX35Yg.yWKCWZtgEgqpfBfhxqWBqTqeDp7zFM8tjYp0lmQjmVYg.JPEG.sjkor1005/KakaoTalk_20220520_153817905.jpg?type=w800",
          "description":"채권압류 및 전부명령신청",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=fea0855b66244f0aa9fceba966dbb700&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 부동산강제집행
@application.route("/api/budongmust", methods=["POST"])
def budongmust ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"부동산 강제집행",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjM0/MDAxNjUzMDMwODgwNTY1.TDf0TP5ijzmF-3RJ8RIPuMUnM6H8jJspL7ZaoDUX35Yg.yWKCWZtgEgqpfBfhxqWBqTqeDp7zFM8tjYp0lmQjmVYg.JPEG.sjkor1005/KakaoTalk_20220520_153817905.jpg?type=w800",
          "description":"배당요구신청서(임금채권)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=d626a0534d7a4920bbcd820a119a4ca5&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 압류금지채권범위변경
@application.route("/api/takemust", methods=["POST"])
def takemust ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"압류금지채권범위변경",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjM0/MDAxNjUzMDMwODgwNTY1.TDf0TP5ijzmF-3RJ8RIPuMUnM6H8jJspL7ZaoDUX35Yg.yWKCWZtgEgqpfBfhxqWBqTqeDp7zFM8tjYp0lmQjmVYg.JPEG.sjkor1005/KakaoTalk_20220520_153817905.jpg?type=w800",
          "description":"압류금지채권",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=4aac966f95ce4c85a1256d0921d7c89e&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 유체동산 강제집행
@application.route("/api/ucmust", methods=["POST"])
def ucmust ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"유체동산 강제집행",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjM0/MDAxNjUzMDMwODgwNTY1.TDf0TP5ijzmF-3RJ8RIPuMUnM6H8jJspL7ZaoDUX35Yg.yWKCWZtgEgqpfBfhxqWBqTqeDp7zFM8tjYp0lmQjmVYg.JPEG.sjkor1005/KakaoTalk_20220520_153817905.jpg?type=w800",
          "description":"유체동산 강제집행신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=a6a59cfa0b03405a8977be681a42af3b&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 자동차 등 강제집행
@application.route("/api/carmust", methods=["POST"])
def carmust ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"자동차 등 강제집행",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjM0/MDAxNjUzMDMwODgwNTY1.TDf0TP5ijzmF-3RJ8RIPuMUnM6H8jJspL7ZaoDUX35Yg.yWKCWZtgEgqpfBfhxqWBqTqeDp7zFM8tjYp0lmQjmVYg.JPEG.sjkor1005/KakaoTalk_20220520_153817905.jpg?type=w800",
          "description":"자동차강제경매신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=10df7219f12a4d8ea49b130384581d9f&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


## 개인회생, 파산 및 면책 1개 ##
# 개인회생
@application.route("/api/helpme", methods=["POST"])
def helpme ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"개인회생",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjM5/MDAxNjUzMDMwNDkxMzI2.mw9I9Yn8AMXIJC15zroBt8pDN1Te6ScBjvr7KfUdqtUg.G07FlXifiRFTI8cYA-QbrXtq_-dl1zgrhWRoNbvB6MEg.JPEG.sjkor1005/KakaoTalk_20220520_160122483.jpg?type=w800",
          "description":"회생채권확정의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=702df1829423469a921767f0f0af7f3b&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)



## 보전처분 5개 ##
# 가압류 일반
@application.route("/api/ga1", methods=["POST"])
def ga1 ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"가압류일반",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjk0/MDAxNjUzMDI5NzczMTE0.3OdTgt-gnsE1CVodM3Q9Mevo4XEPOc2Uu1-Tu3n2FQQg.x5Dl1E1-r0Cx0Sd6cXYUqU5DUAhBxVoiQOQk3SnWfTMg.JPEG.sjkor1005/KakaoTalk_20220520_155419064.jpg?type=w800",
          "description":"제소신고서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=a7de23b9e1e3408c8640e22a13ed1642&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 가처분
@application.route("/api/gacheo", methods=["POST"])
def gacheo ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"가처분",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjk0/MDAxNjUzMDI5NzczMTE0.3OdTgt-gnsE1CVodM3Q9Mevo4XEPOc2Uu1-Tu3n2FQQg.x5Dl1E1-r0Cx0Sd6cXYUqU5DUAhBxVoiQOQk3SnWfTMg.JPEG.sjkor1005/KakaoTalk_20220520_155419064.jpg?type=w800",
          "description":"가처분취소신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=a0b8f885ad4a4f6cb403e0d3db008ded&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)
  
# 기타 보전처분
@application.route("/api/etcbojeon", methods=["POST"])
def etcbojeon ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"기타 보전처분",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjk0/MDAxNjUzMDI5NzczMTE0.3OdTgt-gnsE1CVodM3Q9Mevo4XEPOc2Uu1-Tu3n2FQQg.x5Dl1E1-r0Cx0Sd6cXYUqU5DUAhBxVoiQOQk3SnWfTMg.JPEG.sjkor1005/KakaoTalk_20220520_155419064.jpg?type=w800",
          "description":"자동차가압류명령신청",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=45472fc7b0f944f3b488f5062f6bf94d&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 부동산가압류
@application.route("/api/budonggab", methods=["POST"])
def budonggab ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"부동산 가압류",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjk0/MDAxNjUzMDI5NzczMTE0.3OdTgt-gnsE1CVodM3Q9Mevo4XEPOc2Uu1-Tu3n2FQQg.x5Dl1E1-r0Cx0Sd6cXYUqU5DUAhBxVoiQOQk3SnWfTMg.JPEG.sjkor1005/KakaoTalk_20220520_155419064.jpg?type=w800",
          "description":"부동산가압류신청(대여금)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=fb74f37d208e429a8eda93783044d11d&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 채권가압류
@application.route("/api/moneyab", methods=["POST"])
def moneyab ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"채권가압류 신청서",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjk0/MDAxNjUzMDI5NzczMTE0.3OdTgt-gnsE1CVodM3Q9Mevo4XEPOc2Uu1-Tu3n2FQQg.x5Dl1E1-r0Cx0Sd6cXYUqU5DUAhBxVoiQOQk3SnWfTMg.JPEG.sjkor1005/KakaoTalk_20220520_155419064.jpg?type=w800",
          "description":"임금채권으로 강제집행정지 담보의 공탁금 회수청구권",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=f979a23cb52347ed9dc306bc22068d05&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


## 상가임대차 4개 
# 계약갱신요구
@application.route("/api/trade", methods=["POST"])
def trade ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"계약갱신요구",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjkx/MDAxNjUzMDMwODc5ODg3.3EVvHKAnyDlmCGm2n_NIXoF7wVdyM5al8r03NOY0Wgcg.0sIceL3Kx94iWUn3P_E60nI7G8TzxWxA4OLhY2_MraMg.JPEG.sjkor1005/KakaoTalk_20220520_143646617.jpg?type=w800",
          "description":"최고서(상가임대차계약 갱신권 요구 주장)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=6f379d90540a41c5a2a4541c33cde65c&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 권리금
@application.route("/api/premium", methods=["POST"])
def premium ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"권리금",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjkx/MDAxNjUzMDMwODc5ODg3.3EVvHKAnyDlmCGm2n_NIXoF7wVdyM5al8r03NOY0Wgcg.0sIceL3Kx94iWUn3P_E60nI7G8TzxWxA4OLhY2_MraMg.JPEG.sjkor1005/KakaoTalk_20220520_143646617.jpg?type=w800",
          "description":"권리금반환청구의 소(계약기간내 계약해지할 때 권리금반환특약)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=335aba3f69794649a1e0df752c030bb3&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 기타 상가임대차
@application.route("/api/etcsanga", methods=["POST"])
def etcsanga ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"상가임대차",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjkx/MDAxNjUzMDMwODc5ODg3.3EVvHKAnyDlmCGm2n_NIXoF7wVdyM5al8r03NOY0Wgcg.0sIceL3Kx94iWUn3P_E60nI7G8TzxWxA4OLhY2_MraMg.JPEG.sjkor1005/KakaoTalk_20220520_143646617.jpg?type=w800",
          "description":"건물인도 등 청구의 소(월임차료 체불, 상가 일부)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=2a7440cd65e0474c94b0b2b05bf6ef40&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 임차보증금반환
@application.route("/api/lentfee", methods=["POST"])
def lentfee ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"임차보증금반환",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjkx/MDAxNjUzMDMwODc5ODg3.3EVvHKAnyDlmCGm2n_NIXoF7wVdyM5al8r03NOY0Wgcg.0sIceL3Kx94iWUn3P_E60nI7G8TzxWxA4OLhY2_MraMg.JPEG.sjkor1005/KakaoTalk_20220520_143646617.jpg?type=w800",
          "description":"일반점포의 임대차계약서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=1b69bc30bb7a4e1b9c241fc7cfa635d3&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


## 상속 5개 ##
# 상속분
@application.route("/api/sangsokbun", methods=["POST"])
def sangsokbun ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"상속분",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfOTUg/MDAxNjUzMDI5NjMyODU3.1Dh9bxVQwl9deoON_ta_JchXrUz76KWAL3G390owC3kg.-iwx2S2SfxlyeiUzN-tgfz5UMybYWKlvXIUV9XCTjQcg.JPEG.sjkor1005/KakaoTalk_20220520_152344382.jpg?type=w800",
          "description":"소유권이전등기신청서(상속)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=716f04ee29fa4cf98d53140bb7af525c&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 상속일반
@application.route("/api/sangsok1", methods=["POST"])
def sangsok1 ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"상속일반",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfOTUg/MDAxNjUzMDI5NjMyODU3.1Dh9bxVQwl9deoON_ta_JchXrUz76KWAL3G390owC3kg.-iwx2S2SfxlyeiUzN-tgfz5UMybYWKlvXIUV9XCTjQcg.JPEG.sjkor1005/KakaoTalk_20220520_152344382.jpg?type=w800",
          "description":"상속인수색의 공고청구서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=6decb7d5423e458a89c74b136fe09310&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 상속재산분할
@application.route("/api/sangsokmoney", methods=["POST"])
def sangsokmoney ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"상속재산분할",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfOTUg/MDAxNjUzMDI5NjMyODU3.1Dh9bxVQwl9deoON_ta_JchXrUz76KWAL3G390owC3kg.-iwx2S2SfxlyeiUzN-tgfz5UMybYWKlvXIUV9XCTjQcg.JPEG.sjkor1005/KakaoTalk_20220520_152344382.jpg?type=w800",
          "description":"상속재산분할협의서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=1a63412472d9473dacc6541a5fe84318&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 유류분
@application.route("/api/uryu", methods=["POST"])
def uryu ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"유류분",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfOTUg/MDAxNjUzMDI5NjMyODU3.1Dh9bxVQwl9deoON_ta_JchXrUz76KWAL3G390owC3kg.-iwx2S2SfxlyeiUzN-tgfz5UMybYWKlvXIUV9XCTjQcg.JPEG.sjkor1005/KakaoTalk_20220520_152344382.jpg?type=w800",
          "description":"유류분반환청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=52860d2397a341539264035d6ce3002b&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 유언
@application.route("/api/dietell", methods=["POST"])
def dietell ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"유언",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfOTUg/MDAxNjUzMDI5NjMyODU3.1Dh9bxVQwl9deoON_ta_JchXrUz76KWAL3G390owC3kg.-iwx2S2SfxlyeiUzN-tgfz5UMybYWKlvXIUV9XCTjQcg.JPEG.sjkor1005/KakaoTalk_20220520_152344382.jpg?type=w800",
          "description":"자필증서에 의한 유언증서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=c1fdaadcee314b419abfb99d71d77064&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

if __name__ == "__main__":
    application.run(host='0.0.0.0', port = int(sys.argv[1]), debug = True)