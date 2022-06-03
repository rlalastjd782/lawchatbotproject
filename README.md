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
  - konlpy
  - pandas
  - keras
  - numpy
  - socket.io
  
# Structure
- 웹 형태의 챗봇으로써, CSS와 NODE JS도 같이 사용되었으며, 주력 디자인은 'Bootstrap'을 응용했습니다.<br/>
<br/>
├── QnA:&nbsp;&nbsp;&nbsp;&nbsp; 질문과 답변을 저장하는 디렉토리입니다.<br/>
├── socket.io:&nbsp;&nbsp;&nbsp;&nbsp;웹 소켓 구현을 위해 기본적인 파일들이 저장된 디렉토리입니다.<br/>
├── views:&nbsp;&nbsp;&nbsp;&nbsp; 웹 페이지 구현을 위해 작성된 ejs 데이터 파일이 저장된 디렉토리, 'Web Browser'에 해당합니다.<br/>
├── chatbot.py:&nbsp;&nbsp;&nbsp;&nbsp; 프로그램 실행의 시작과 끝까지, 모든 소스가 작성되어 있는 메인 파일입니다.<br/>
├── ChatBotData.csv:&nbsp;&nbsp;&nbsp;&nbsp; '송경숙'님의 데이터 소스(소스 경로는 상위 'Learning Data' 파트에 명시했습니다.)<br/>
├── index.js:&nbsp;&nbsp;&nbsp;&nbsp; 'Web Server'에 해당하는 js 파일입니다.<br/>
├── RealEstate.csv:&nbsp;&nbsp;&nbsp;&nbsp; 부동산(경,공매)및 생활 법률 용어들이 총괄해서 담겨있는 파일입니다.

# Design
<img src="https://user-images.githubusercontent.com/79067558/108025412-c988e100-7069-11eb-8fbd-6903ef0ee0ce.png" width="60%">
<img src="https://user-images.githubusercontent.com/79067558/108144214-951a3100-710c-11eb-9289-41c0f421b2a4.png" width="60%"><br/>
- 디자인은 상위에 소개된 사진과 같으며, 반드시 'chatbot.py'와 'index.js' 이 두 파일을 모두 실행해주셔야 구동됩니다.<br/>
- 챗봇의 전반적인 구동 방식은 'chatbot.py'파일에 수록해놓았으니 참조 바랍니다.<br/>
- 또한 웹 구동 방식 및, 디자인 CSS소스를 비롯하여 'views' 디렉토리 내에 있는 'index.ejs'에 입력 및 설명되어 있으니 참고 하시면 되겠습니다.

# Video(How to work)
- 구동 영상을 촬영해보았습니다 :)<br/>
- I filmed a video(How to work) :)<br/>
- 클릭을 하시면, 동영상이 재생됩니다. (If you click, The video will play.) <br/>
[![Upload](http://img.youtube.com/vi/yqh6l9gdK9A/0.jpg)](https://youtu.be/yqh6l9gdK9A?t=0s) 

# Data(Send & Receive) Flow
<img src="https://user-images.githubusercontent.com/79067558/108029757-61d69400-7071-11eb-8a82-4d0d27512b6c.png" width="60%"><br/>
- 파일을 실행시키기에 앞서, 전반적인 데이터들의 상호작용(흐름)에 대하여 작성해본 사진입니다.<br/>
- 이 그림을 참조하신 후, 앞서 상위 카테고리들로부터 설명한 파일들을 구동시키시면 이해가 훨씬 수월해지실 것 같아 작성했습니다.

# Languages
- Node js, JavaScript, CSS, Python 이렇게 4개의 랭귀지로 개발되었습니다.<br/>
- 추가적으로 슬라이드(Wrapper) Animation Effect가 적용되었으니 어떻게 구현이 되었으며 어떤 방식으로 작동되는지는 작성된 ppt파일과 함께 각 파일들을 실행해본 후,<br/>
- 해당 파일마다 어떻게 적용시켰으며 이유는 무엇인지, 또한 해당 파트는 작동 방식 중, 어떤 부분에 해당하는 지 등<br/>
- 자세히 수록해 놓았으니 참조하신 후 실행하시면 훨씬 수행과 이해에 있어 쉽게 받아들이실 수 있다고 조심스레 개인적인 사견을 이렇게 남겨봅니다.

# Motivation
- 이 분야에 입문한지 벌써 4개월차가 되어갑니다, 기본적인 이론을 공부한 후 실전으로 뛰어든지 얼마 되지 않았으므로 구성에 있어서 미흡할 수 있습니다 
- 하지만 이 프로젝트를 하게 된 이유는, 직접적으로 나만의 프로젝트를 수행하는 것이 우선이라 생각이 되었으며 또한 현대 이 시대는 너무나 빠르게 급변하고 있기에
- 사회에 적응하고, 사회에서 원하는 챗봇의 모델은 어떤것인지를 고심하다가 이렇게 결정을 내리게 되었습니다.
- 원래 초기에는 부동산에 한정된 챗봇을 구현하려 했으나, 스스로의 실력 향상을 도모하기 위해 일상속에서 적용되는 전반적인 법률의 용어를 총괄하기로 생각을 바꾸었고
- 그 중에서도 직접적으로 많이 사용되는 (고빈도의) 용어들을 정리하여 프로젝트를 수행하게 되었습니다.
- 이쪽 딥러닝 분야에 입문한지 4개월이 다되어가는 이때, 성공적으로 프로젝트를 수행하였고 저만의 챗봇을 개발하게 되어서 매우 뿌듯합니다.
- 모두 읽어주셔서 감사합니다, 항상 행복하세요 :)


# Web-ChatBot-Bell (Eng.ver)
- It can Explain about Words of Standard law from South Korea

# Learning Data
|Title|Contents|From|
|:------:|:---:|:------:|
|Data Name|ChatBot 'Bell'|My Brain|
|Basic Sources From|DeFault ChatBot Data Source|https://github.com/songys/Chatbot_data (Ms.Song)|
| 1st Additional Data  |Additional Data Sources for ChatBot system|https://korquad.github.io/ (KorQuAD Set)|
| 2nd Additional Data  |Legal Terms Data |https://www.data.go.kr/data/15069932/fileData.do (Korea PublicData Portal)|

# Author
Ian/@Ian (aoa8538@gmail.com)

# Requirement
- Tools used include:<br/>
  - Python 3.7.9
  - Tensorflow 2.4.1
  - konlpy
  - pandas
  - keras
  - numpy
  - socket.io

# Structure
- It is a Web-shapped ChatBot, 'CSS' and 'NodeJS' used with main design is 'Bootstrap'.<br/>
<br/>
├── QnA:&nbsp;&nbsp;&nbsp;&nbsp; Directory for storing Questions and Answers.<br/>
├── socket.io:&nbsp;&nbsp;&nbsp;&nbsp;For Web Socket implementation, the required basic files are stored in this Directory.<br/>
├── views:&nbsp;&nbsp;&nbsp;&nbsp; The directory where the 'ejs' file created for implementing the Web Browser is stored.<br/>
├── chatbot.py:&nbsp;&nbsp;&nbsp;&nbsp; This is a 'Deep-Learning' Python file.<br/>
├── ChatBotData.csv:&nbsp;&nbsp;&nbsp;&nbsp; This is the Data Source of 'Ms.Song' (The source is specified in the table of the top from the part 'Learning Data').<br/>
├── index.js:&nbsp;&nbsp;&nbsp;&nbsp; The File 'js' corresponding to 'Web Server'..<br/>
├── RealEstate.csv:&nbsp;&nbsp;&nbsp;&nbsp; This is a file that organizes 'Real-Estate' and 'Standard Legal Terms'.

# Design
<img src="https://user-images.githubusercontent.com/79067558/108025412-c988e100-7069-11eb-8fbd-6903ef0ee0ce.png" width="60%">
<img src="https://user-images.githubusercontent.com/79067558/108144214-951a3100-710c-11eb-9289-41c0f421b2a4.png" width="60%"><br/>
- The design is the same as the top introduced picture, and both files('chatbot.py' and 'index.js')must be executed.<br/>
- The overall operation of the 'Chatbot' is described in the Python file('chatbot.py), so Please refer to it.<br/>
- It is also entered and described in the 'views' folder, including the Web operation method with Design sources('index.ejs').

# Data(Send & Receive) Flow
<img src="https://user-images.githubusercontent.com/79067558/108029757-61d69400-7071-11eb-8a82-4d0d27512b6c.png" width="60%"><br/>
- This is a picture of the overall interaction of Data(About flow).<br/>
- After reffering to this picture, I wrote it cause I thought it would be much easier to understand if who run the files.

# Languages
- Node js, JavaScript, CSS, Python, four Languages were used.<br/>
- Additionally, the Slide animation effect has been applied, so it is recommended that you run the created 'pptx' file to see how it is implemented and how it works<br/>
- (I will write an English version and upload it later, Sorry)

# Motivation
- It's been 4 months since I entered this field. After studying the basic theory, the composition may be insufficient cause I haven't been long since it was put into actual. 
- But the reason why I decided to do this project was because my first priority to carry out my own project, and I thought deeply about the model that the times require for society to adapt quickly and easily changing.
- In the beginning, I tried to implement a Chatbot limited to Real-Estate, but I changed my mind to oversee the terms of laws that apply in daily life to improve my skills.
- Among them, the project was carried out by selecting terms that are used directly frequently.
- It is been 4 months since I started 'Deep-Learning' and I'm very proud that I successfully carried out the project without any errors.
- Thanks to read my post, God Bless you everyday. :)
# lawchatbotproject
