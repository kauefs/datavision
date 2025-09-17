import streamlit                              as   st
from langchain_google_genai.chat_models     import ChatGoogleGenerativeAI
from google.generativeai.types.safety_types import HarmBlockThreshold, HarmCategory
st.set_page_config(page_title='LLM', page_icon='📱', layout='wide', initial_sidebar_state='auto')
#  Session State:
st.session_state.setdefault('messages',[])
st.session_state.setdefault( 'prompt' ,'')
st.session_state.setdefault('warning' ,'')
# CallBacks:
def clear( ):
    '''Clears chat history & prompt.'''
    st.session_state.messages=[]
    st.session_state.prompt  =''
def send( ):
    '''Appends user message to history & clears prompt.'''
    if  st.session_state.prompt:
        st.session_state.messages.append({'role':'user','content':st.session_state.prompt,'avatar':'👨🏻‍💻'})
        st.session_state.prompt='' # clear prompt
    else:st.session_state.warning=st.warning('Try a prompt first.')
# API-KEY:
api_key=st.secrets['api_key']
model  ='gemini-2.5-flash-lite'
max_output_tokens =16384
safety_settings={HarmCategory.HARM_CATEGORY_HARASSMENT       :HarmBlockThreshold.BLOCK_ONLY_HIGH,
                 HarmCategory.HARM_CATEGORY_HATE_SPEECH      :HarmBlockThreshold.BLOCK_ONLY_HIGH,
                 HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT:HarmBlockThreshold.BLOCK_ONLY_HIGH,
                 HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT:HarmBlockThreshold.BLOCK_ONLY_HIGH}
# BLOCK_ONLY_HIGH | BLOCK_MEDIUM_AND_ABOVE | BLOCK_LOW_AND_ABOVE | BLOCK_NONE
system_instruction='''
                      you are a very helpful and resourceful llm,
                      you have extensive knowledge (phd level) in multiple areas,
                      notabily data science, computer vision, machine learning, deep learning, artificial intelligence, and cybersecurity.
                      assist users with information and advice across a wide range of topics, leveraging your deep expertise,
                      providing detailed and accurate information based on your extensive knowledge in each field,
                      and maintaining helpful and companionable tone throughout our interactions.
                      overall tone:
                        * knowledgeable and authoritative in your areas of expertise.
                        * helpful and proactive in assisting with requests.
                        * friendly and warm in your interactions.
                        * efficient and resourceful in providing information and solutions.
                   '''
LLM=ChatGoogleGenerativeAI(model  =model,
                           api_key=api_key,
                           max_output_tokens =max_output_tokens,
                           safety_settings   =safety_settings,
                           system_instruction=system_instruction)
# SIDE
st.sidebar.image   ('https://upload.wikimedia.org/wikipedia/commons/8/8a/Google_Gemini_logo.svg')
st.sidebar.markdown('[![Gemini](https://img.shields.io/badge/Powered_by_Google_Gemini-34A853?style=flat&logo=google&logoColor=EA4335&labelColor=4285F4&color=FBBC05)](https://gemini.google.com/)')
st.sidebar.title   ('ƊⱭȾɅViƧi🧿Ƞ&trade;')
st.sidebar.divider (       )
st.sidebar.info    ('Lang' )
st.sidebar.success ('Chain')
st.sidebar.warning ('LLM'  )
st.sidebar.divider (       )
with st.sidebar:
    col1,col2=st.columns(2)
    with col1:st.button('Clear', on_click=clear)
    with col2:st.button('SEND' , on_click= send)
if st.session_state.messages and st.session_state.messages[-1]['role']=='user':
    with     st.chat_message('llm', avatar='🐼'):
        with st.spinner('Processing…'):
            input=st.session_state.messages[-1]['content']
            response=LLM.invoke(input)
            st.markdown(response.content)
            st.session_state.messages.append({'role':'llm','content':response.content,'avatar':'🐼'})
st.sidebar.divider (       )
st.sidebar.markdown('''
![2025.09.17   ](https://img.shields.io/badge/2025.09.17-000000)

[![GitHub      ](https://img.shields.io/badge/-000000?logo=github&logoColor=FFFFFF)](https://github.com/kauefs/)
[![Medium      ](https://img.shields.io/badge/-000000?logo=medium&logoColor=FFFFFF)](https://medium.com/@kauefs)
[![LinkedIn    ](https://img.shields.io/badge/in-0077B5?logo=linkedin&logoColor=FFFFFF)](https://www.linkedin.com/in/kauefs/)
[![Python      ](https://img.shields.io/badge/3-646464?logo=python&logoColor=FFDE57&labelColor=4584B6)](https://www.python.org/)

[![License     ](https://img.shields.io/badge/Apache--2.0-D22128?style=flat&logo=apache&logoColor=CB2138&label=License&labelColor=6D6E71&color=D22128)](https://www.apache.org/licenses/LICENSE-2.0)

[![ƊⱭȾɅViƧi🧿Ƞ](https://img.shields.io/badge/ƊⱭȾɅViƧi🧿Ƞ&trade;-0065FF?style=plastic&label=&copy;2025&labelColor=0065FF)](https://datavision.one/)
                    ''')
# MAIN
st.title('LangChainLLM')
for message in st.session_state.messages:
    with       st.chat_message(message['role'], avatar=message['avatar']):st.markdown(message['content'])
prompt     =   st.text_area('**PromptBox**', key='prompt', value=st.session_state.prompt)
