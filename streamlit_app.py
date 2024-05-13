import streamlit as st
import pandas as pd
import datetime as dt
import random
import pytz
import time


def set_seed():
    madrid_tz = pytz.timezone('Europe/Madrid')
    tt = dt.datetime.now(madrid_tz).date().timetuple()
    seed = tt.tm_mday * 1000000 + tt.tm_mon*10000 + tt.tm_year
    random.seed(seed)


def llegeix_dataset():
    """Aquesta funció llegeix el dataset, ho he fet de la manera mes lean
    possible guardant el dataset estàtic al repositori
    """
    df = pd.read_csv("refranys.csv")
    return df


def llegeix_parts(index_primera: int, index_segona: int):
    df = pd.read_csv("refranys.csv", quotechar='"', quoting=1)
    return df.iloc[index_primera]["part1"], df.iloc[index_segona]["part2"], \
        df.iloc[index_primera]["refrany"], df.iloc[index_segona]["refrany"]


def frase_del_dia():
    st.title("La frase del dia és:")
    set_seed()
    primer = random.randint(1, 100)
    segon = random.randint(1, 100)
    p1, p2, f1, f2 = llegeix_parts(primer, segon)
    st.markdown(f"<h2 style='text-align: center'>{p1} {p2}</h2>", unsafe_allow_html=True)
    st.text("")
    st.text("Les frases originals són:")
    st.text(f1)
    st.text(f2)


def generador_aleatori():
    st.title("Generador aleatori")
    random.seed(time.time())
    if st.button("Genera una frase"):
        primer = random.randint(1, 100)
        segon = random.randint(1, 100)
        p1, p2, f1, f2 = llegeix_parts(primer, segon)
        st.markdown(f"<h2 style='text-align: center'>{p1} {p2}</h2>", unsafe_allow_html=True)
        st.text("")
        st.text("Les frases originals són:")
        st.text(f1)
        st.text(f2)

def main():
    st.sidebar.title("Navega")
    app_mode = st.sidebar.radio("Ves a:", ["La frase del dia", "Generador aleatori"])

    if app_mode == "La frase del dia":
        frase_del_dia()
    elif app_mode == "Generador aleatori":
        generador_aleatori()


if __name__ == "__main__":
    main()
