import  streamlit           as   st
import  google.generativeai as   genai
st.set_page_config(page_title='ƊⱭȾɅViƧi🧿Ƞ ChatBot', page_icon='🧿', layout='wide', initial_sidebar_state='collapsed')
#  Session State:
st.session_state.setdefault(None)
if      'message' not in st.session_state:st.session_state.messages=[    ]
if      'api_key' not in st.session_state:st.session_state.api_key = True
if      'model'   not in st.session_state:st.session_state.model   = True
if      'chat'    not in st.session_state:st.session_state.chat    = True
# API-KEY
api_key=st.secrets['api_key']
genai.configure(api_key=api_key)
# SIDE
st.sidebar.image   ('https://upload.wikimedia.org/wikipedia/commons/8/8a/Google_Gemini_logo.svg')
st.sidebar.markdown('[![Gemini](https://img.shields.io/badge/Powered_by_Google_Gemini-34A853?style=flat&logo=google&logoColor=EA4335&labelColor=4285F4&color=FBBC05)](https://gemini.google.com/)')
st.sidebar.title   ('ƊⱭȾɅViƧi🧿Ƞ&trade;')
st.sidebar.divider ( )
st.sidebar.info    (     'ViƧi🧿Ƞ'       )
st.sidebar.success ('ƊⱭȾɅ Assistant'    )
st.sidebar.divider ( )
st.sidebar.markdown('''
![2025.05.15  ](https://img.shields.io/badge/2025.05.15-000000)

[![GitHub     ](https://img.shields.io/badge/-000000?logo=github&logoColor=FFFFFF)](https://github.com/kauefs/)
[![Medium     ](https://img.shields.io/badge/-000000?logo=medium&logoColor=FFFFFF)](https://medium.com/@kauefs)
[![LinkedIn   ](https://img.shields.io/badge/in-0077B5?logo=linkedin&logoColor=FFFFFF)](https://www.linkedin.com/in/kauefs/)
[![Python     ](https://img.shields.io/badge/3-646464?logo=python&logoColor=FFDE57&labelColor=4584B6)](https://www.python.org/)

[![License    ](https://img.shields.io/badge/Apache--2.0-D22128?style=flat&logo=apache&logoColor=CB2138&label=License&labelColor=6D6E71&color=D22128)](https://www.apache.org/licenses/LICENSE-2.0)

[![ƊⱭȾɅViƧi🧿Ƞ](https://img.shields.io/badge/ƊⱭȾɅViƧi🧿Ƞ&trade;-0065FF?style=plastic&label=&copy;2025&labelColor=0065FF)](https://datavision.one/)
                    ''')
# MAIN
st.title    ('ƊⱭȾɅViƧi🧿Ƞ&trade;')
st.header   (    'ViƧi🧿Ƞ'        )
st.subheader(    'ƊⱭȾɅ Assistant')
st.divider( )
# Model:
model_name        =  'gemini-2.5-flash-lite'
generation_config = {'candidate_count'  : 1,
                     'temperature'      : 0.75,
                     'top_p'            : 0.95,
                     'top_k'            : 3,
                     'stop_sequences'   : None,
                     'max_output_tokens': 16384}
safety_settings   = {'HATE'             :'BLOCK_ONLY_HIGH',
                     'HARASSMENT'       :'BLOCK_ONLY_HIGH',
                     'SEXUAL'           :'BLOCK_ONLY_HIGH',
                     'DANGEROUS'        :'BLOCK_ONLY_HIGH'}
tools             =   None
system_instruction='''
                      you are ViƧi🧿Ƞ, a ƊⱭȾɅ assistant for ƊⱭȾɅViƧi🧿Ƞ&trade; company, which specializes in data science and computer vision.
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

                      {query}

                   '''
model             =genai.GenerativeModel(model_name        =     model_name,
                                         generation_config =generation_config,
                                         safety_settings   =    safety_settings,
                                         system_instruction=    system_instruction,
                                         tools             =    tools )
# Chat:
chat            =model.start_chat(enable_automatic_function_calling=False)
start           = chat.send_message(system_instruction.format(query='Prompt'))
ai_avatar       ='🧿'
hm_avatar       ='🧐'
if 'message' not in st.session_state:
        with        st.chat_message('ai', avatar='🧿'):
                    st.write(start.text)
for message    in   st.session_state.messages:
        avatar  =   hm_avatar   if  message['role']=='human' else ai_avatar
        with        st.chat_message(message['role']     , avatar =avatar):st.write(message['content'])
if query       :=   st.chat_input(placeholder='Type message here…', max_chars=None, disabled=False, on_submit=None):
        with        st.chat_message('human')     :         st.write(query)
        st .session_state.messages.append({'role':'human','content':query})
        with        st.chat_message('ai'):response=chat.send_message(system_instruction.format(query=query))
        st .session_state.messages.append({'role':'ai','content':response.text})
        st .write(response.text)
st.toast('ƊⱭȾɅViƧi🧿Ƞ&trade;', icon='🧿')
