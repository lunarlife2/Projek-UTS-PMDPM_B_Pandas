import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import os

model_path = r'D:\atma\Semester 5\ML\UTS 1.1'
model = os.path.join(model_path,'BestModel_CLF_LR_Pandas.pkl')

model2 = 'BestModel_REG_Lasso_Pandas.pkl'

with open(model, 'rb') as f:
    loaded_model = pickle.load(f)

lr_model = loaded_model

with open(model2, 'rb') as f:
    loaded_model2 = pickle.load(f)

lasso_model = loaded_model2

#sidebar
with st.sidebar:
    selected = option_menu('UTS ML 24/25',['Klasifikasi','Regresi'],default_index=0)

#halaman klasifikasi
if selected == 'Klasifikasi':
    st.title('Klasifikasi')

    file = st.file_uploader("Masukan File", type=["csv","txt"])

    squaremeters = st.number_input("Masukan Luas Square Meter",0)

    numberofrooms = st.slider("Jumlah Ruangan",0,100)

    hasyard = st.radio("Punya Yard",["Yes","No"])

    haspool = st.radio("Punya Kolam Renang",["Yes","No"])

    floors = st.slider("Jumlah Lantai",0,100)

    citycode = st.number_input("City Code",0)

    citypartrange = st.slider("City Part Range",0,100)

    numprevowners = st.slider("Jumlah Pemilik Sebelumnya",0,10)

    made = st.number_input("Dibuat Tahun",0)

    isnewbuilt = st.radio("Baru dibangun",["Yes","No"])

    hasstormprotector = st.radio("Punya Storm Protector",["Yes","No"])

    basement = st.number_input("Luas Basement",0)

    attic = st.number_input("Luas Attic",0)

    garage = st.number_input("Luas Garage",0)

    hasstorageroom = st.radio("Punya Storage Room",["Yes","No"])

    hasguestroom = st.slider("Jumlah Guest Room",0,10)

#halaman regresi
if selected == 'Regresi':
    st.title('Regresi')

    file = st.file_uploader("Masukan File", type=["csv","txt"])

    squaremeters = st.number_input("Masukan Luas Square Meter",0)

    numberofrooms = st.slider("Jumlah Ruangan",0,100)

    hasyard = st.radio("Punya Yard",["Yes","No"])

    haspool = st.radio("Punya Kolam Renang",["Yes","No"])

    floors = st.slider("Jumlah Lantai",0,100)

    citycode = st.number_input("City Code",0)

    citypartrange = st.slider("City Part Range",0,100)

    numprevowners = st.slider("Jumlah Pemilik Sebelumnya",0,10)

    made = st.number_input("Dibuat Tahun",0)

    isnewbuilt = st.radio("Baru dibangun",["Yes","No"])

    hasstormprotector = st.radio("Punya Storm Protector",["Yes","No"])

    basement = st.number_input("Luas Basement",0)

    attic = st.number_input("Luas Attic",0)

    garage = st.number_input("Luas Garage",0)

    hasstorageroom = st.radio("Punya Storage Room",["Yes","No"])

    hasguestroom = st.slider("Jumlah Guest Room",0,10)


if hasyard == "Y":
    hasyard = 1
else:
    hasyard = 0

if haspool == "Y":
    haspool = 1
else:
    haspool = 0

if isnewbuilt == "Y":
    isnewbuilt = 1
else:
    isnewbuilt = 0

if hasstormprotector == "Y":
    hasstormprotector = 1
else:
    hasstormprotector = 0

if hasstorageroom == "Y":
    hasstorageroom = 1
else:
    hasstorageroom = 0

input_data = [[squaremeters, numberofrooms, hasyard, haspool, 
               floors, citycode, citypartrange, numprevowners, 
               made, isnewbuilt, hasstormprotector,  basement, 
               attic, garage, hasstorageroom, hasguestroom]]

st.write("Data properti yang akan diinputkan ke model")
st.write(input_data)

if selected == 'Klasifikasi':
    if st.button("Klasifikasi Category"):
        lr_model_prediction = lr_model.predict(input_data)
        outcome = {0:'Basic', 1:'Luxury', 2:'Middle'}
        st.write(f"Properti tersebut kategori **{outcome[lr_model_prediction[0]]}**")

if selected == 'Regresi':
    if st.button("Prediksi Price"):
        lasso_model_prediction = lasso_model.predict(input_data)
        st.markdown(f"Prediksi Harga properti adalah : $ {lasso_model_prediction[0]:.2f}")