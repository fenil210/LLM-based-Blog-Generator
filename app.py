import streamlit as st 
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
# # CTransformers provide binding for GGML models

# # func to get response from LLAma 2
def LLMlamma(input_text,no_words,blog_style):

#     # call llamma2 modal
    llm = CTransformers(model="models/llama-2-7b-chat.ggmlv3.q8_0.bin", 
                        model_type="llama", 
                        config={"max_new_tokens":256,
                                "temperature":0.01})
    
#     # promp template

    template = """
    Write a blog for {blog_style} for a topic {input_text} within {no_words} words. The blog must cover up all the current ongoing trend and information in {blog_style}'s respective field.
    """

    prompt=PromptTemplate(input_variables=["blog_style","input_text",'no_words'],
                          template=template)

    # responce generation
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))

    print(response)

    return response



st.set_page_config(page_title="Generate Blogs",
                    page_icon='page_facing_up',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate Blogs") 

input_text=st.text_input("Enter the Blog Topic")

# # 2 column : additional fields
# # width
col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('No of Words')
# # for whome writing this blog
with col2:
    blog_style=st.selectbox('Writing the blog for',
                            ('Researchers','Data Scientist','Tech Enthusiast','Environmental Activist','Culinary Connoisseur','Movie Critic','Common People'),index=0)

submit=st.button("Generate")

# # final responce

if submit:
    st.write(LLMlamma(input_text,no_words,blog_style))
