import streamlit as st
from model import Evaluate

evaluator = Evaluate()

st.title("Ask")
#st.markdown('built by [@shreydan](https://github.com/shreydan)')
#st.markdown("### Praise the Lord.")
st.markdown("##### Please type the question you want to ask to Quran")


with st.container():
    text_input:str = st.text_input(label='type verse and submit',key='input')
    text_input = text_input.strip()
    st.caption('Examples: do not be afraid, bless the Lord oh my soul')
    num_responses = st.number_input(
        label='number of responses',
        min_value=10,
        max_value=500,
        step=10,
        value=25
    )
    num_responses = int(num_responses)

    submitted = st.button(
        label='Search',
        type='primary'
    )




if len(text_input) != 0 or submitted:
    response = evaluator.get_verses(text_input,top=num_responses)
    references = response['reference']
    verses = response['verse']
    
    response2 = evaluator.get_verses2(text_input,top=num_responses)
    references2 = response2['reference']
    verses2 = response2['verse']
    st.markdown('#### here are the verses...\n___')
    limit = min(len(verses2),len(verses))
    for i in range(limit):
        with st.container():
            md = f"""
            -----
            
            {verses[i]} ({references[i]})
            
            {verses2[i]} ({references2[i]})
            
            -----
            """
            st.markdown(md)
