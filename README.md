# Web-ChatBot-Bell- (Korean ver.)
It can Explain about Words of Standard law from South Korea
- 이것은 대한민국에서 적용되는 법률의 스탠다드 용어들에 대하여 설명하는 챗봇입니다.

# Learning Data
|Title|Contents|From|
|:------:|:---:|:------:|
|Data Name|ChatBot 'Bell'|My Brain (나의 머리)|
|Basic Sources From|DeFault ChatBot Data Source|https://github.com/songys/Chatbot_data (송영숙님)|
| 1st Additional Data  |Additional Data Sources for ChatBot system|https://korquad.github.io/ (KorQuAD)|
| 2nd Additional Data  |Legal Terms Data |https://www.data.go.kr/data/15069932/fileData.do (공공데이터 포털)|

# Author
Ian/@Ian (aoa8538@gmail.com)

# Requirement
- 사용된 툴은 다음과 같습니다.<br/>
  - Python 3.7.9
  - Tensorflow 2.4.1
  - pandas
  - numpy
  - sys
  - flask
  - requests
  
# Structure
- 카카오 오픈빌더를 이용한 챗봇으로써 보다 쉬운 법률 데이터를 제공하는데에 집중하였습니다<br/>
<br/>
- 재미를 감미하기 위하여 대화형 챗봇에 대한 구현을 하였습니다<br/>
<br/>

├── ChatBotData.csv:&nbsp;&nbsp;&nbsp;&nbsp; '송경숙'님의 데이터 소스(소스 경로는 상위 'Learning Data' 파트에 명시했습니다.).<br/>
├── RealEstate.csv:&nbsp;&nbsp;&nbsp;&nbsp; 부동산(경,공매)및 생활 법률 용어들이 총괄해서 담겨있는 파일입니다..<br/>
├── maincode.py:&nbsp;&nbsp;&nbsp;&nbsp; 프로그램 실행의 시작과 끝까지, 모든 소스가 작성되어 있는 메인 파일입니다.<br/>


# Design
<img width="60%" alt="스크린샷 2022-06-03 오전 11 38 32" src="https://user-images.githubusercontent.com/101306770/171775940-cf5d34ca-8db6-4c7f-a078-7804f3326e8a.png">

- 디자인은 상위에 소개된 사진과 같으며,필수 라이브러리를 설치 후에 'maincode.py'를 실행해주시면됩니다.<br/>
- 챗봇의 전반적인 코드 설명은 'maincode.py'파일에 수록해놓았으니 참조 바랍니다.<br/>


# Video(How to work)
- 구동 영상을 촬영해보았습니다 :)<br/>
- I filmed a video(How to work) :)<br/>
- 클릭을 하시면, 동영상이 재생됩니다. (If you click, The video will play.) <br/>
- 추후 추가예정()

# Data(Send & Receive) Flow
<img width="60%" alt="image" src="https://user-images.githubusercontent.com/101306770/171776673-0ead9d52-0b1c-4690-a4f9-7b323bbfe568.png">

- 파일을 실행시키기에 앞서, 전반적인 데이터들의 상호작용(흐름)에 대하여 작성해본 사진입니다.<br/>


# Languages
- JavaScript, Python 이렇게 2개의 랭귀지로 개발되었습니다.<br/>
- 추가적으로 슬라이드(Wrapper) Animation Effect가 적용되었으니 어떻게 구현이 되었으며 어떤 방식으로 작동되는지는 작성된 ppt파일과 함께 각 파일들을 실행해본 후,<br/>
- 해당 파일마다 어떻게 적용시켰으며 이유는 무엇인지, 또한 해당 파트는 작동 방식 중, 어떤 부분에 해당하는 지 등<br/>
- 자세히 수록해 놓았으니 참조하신 후 실행하시면 훨씬 수행과 이해에 있어 쉽게 받아들이실 수 있다고 조심스레 개인적인 사견을 이렇게 남겨봅니다.

# Motivation
- 현재 저희는 데이터 개발에 입문한지 3개월된 프로젝트 팀입니다.
- 아직 부족하고 미흡한 면이 많지만 잘 봐주시면 감사드리겟습니다.
- 좋은하루되시고 감사합니다.!



