# źródło danych [https://www.kaggle.com/c/titanic/](https://www.kaggle.com/c/titanic)

import streamlit as st
import pickle
from datetime import datetime
startTime = datetime.now()
# import znanych nam bibliotek

filename = "model.sv"
model = pickle.load(open(filename,'rb'))
# otwieramy wcześniej wytrenowany model

pclass_d = {0:"Pierwsza",1:"Druga", 2:"Trzecia"}
embarked_d = {0:"Cherbourg", 1:"Queenstown", 2:"Southampton"}
sex_d = {0:"Female", 1:"Male"}
# o ile wcześniej kodowaliśmy nasze zmienne, to teraz wprowadzamy etykiety z ich nazewnictwem

def main():

	st.set_page_config(page_title="???")
	overview = st.container()
	left, right = st.columns(2)
	prediction = st.container()

	st.image("data:image/jpeg;base64,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")

	with overview:
		st.title("PUM Zajecia 5")

	with left:
		sex_radio = st.radio("Płeć", list(sex_d.keys()), format_func=lambda x : sex_d[x] )
		embarked_radio = st.radio("Port zaokrętowania", list(embarked_d.keys()), index=2, format_func=lambda x: embarked_d[x] )
		pclass_radio = st.radio("Class", list(pclass_d.keys()), format_func=lambda x: pclass_d[x])

	with right:
		age_slider = st.slider("Wiek", value=1, min_value=0, max_value=80)
		sibsp_slider = st.slider("Liczba rodzeństwa i/lub partnera", min_value=0, max_value=8)
		parch_slider = st.slider("Liczba rodziców i/lub dzieci", min_value=0, max_value=6)
		fare_slider = st.slider("Cena biletu", min_value=0, max_value=512, step=1)

	data = [[pclass_radio, sex_radio,  age_slider, sibsp_slider, parch_slider, fare_slider, embarked_radio]]
	survival = model.predict(data)
	s_confidence = model.predict_proba(data)

	with prediction:
		st.subheader("Czy taka osoba przeżyłaby katastrofę?")
		st.subheader(("Tak" if survival[0] == 1 else "Nie"))
		st.write("Pewność predykcji {0:.2f} %".format(s_confidence[0][survival][0] * 100))

if __name__ == "__main__":
    main()
