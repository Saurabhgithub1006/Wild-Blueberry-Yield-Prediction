import streamlit as st
from model import get_prediction
import numpy as np

st.set_page_config(page_title="Wild Blueberry Yield Prediction App",
                   page_icon="🍇", layout="wide")

col1, col2 = st.columns([3,5])
# ['clonesize', 'bumbles', 'adrena', 'osmia', 'MaxOfUpperTRange', 'RainingDays', 'fruitset', 'fruitmass','seeds']
features=['fruitset','seeds','fruitmass','AverageRainingDays','RainingDays','clonesize','honeybee','AverageOfLowerTRange','MinOfLowerTRange','MaxOfLowerTRange']
st.markdown("<h1 style='text-align: center;'>Wild Blueberry Yield Prediction App 🍇</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"]
    {
        background-image: url('https://scx2.b-cdn.net/gfx/news/2020/tractorscanc.jpg');
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def main():
    st.markdown("""
    <style>
    .dark-subheader {
        color: black;
        font-size: 20px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
 
    with st.form('prediction form'):
        st.subheader('Enter the input for the following features:')
        fruitset = st.text_input("Blueberry fruitset value")
        seeds = st.text_input("seeds value")
        fruitmass = st.text_input("fruitmass value")
        AverageRainingDays = st.text_input("AverageRainingDays value")
        RainingDays = st.text_input("Raining days value")
        clonesize = st.text_input("clonesize days value")
        honeybee = st.text_input("honeybee days value")
        AverageOfLowerTRange = st.text_input("AverageOfLowerTRange days value")
        MinOfLowerTRange = st.text_input("MinOfLowerTRange days value")
        MaxOfLowerTRange = st.text_input("MaxOfLowerTRange days value")
        

        
         
        submit = st.form_submit_button("Predict")

        if submit:
            # Construct the input array with actual values
            data = np.array([float(fruitset), float(seeds), float(fruitmass),float(AverageRainingDays),
                        float(RainingDays),float(clonesize),
                        float(honeybee), float(AverageOfLowerTRange), float(MinOfLowerTRange),float(MaxOfLowerTRange)]).reshape(1, -1)
            # Get the prediction from your model
            pred = get_prediction(data=data)
            st.balloons()
            st.write(f"The predicted severity is: {pred[0]}")

if __name__ == '__main__':
    main()