import streamlit as st
import os
import steno

st. set_page_config(layout="wide")

enc_col, space, dec_col= st.columns([3,1,3])

def file_updated(args):
    print("file updated to. ", args)

def radio_change(args):
    st.write(st.session_state.decrypt)
    st.write(st.session_state.encrypt)
    print(st.session_state)

def format_func(args):
    print("in format function with: ", args)

#encrypt text
with enc_col:
    file = st.file_uploader("upload photo to encode", type= ['png'] , accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
    text = st.text_input("text to encrypt", value="", max_chars=None, key="ecrypted_text", type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None,  placeholder=None, disabled=False)
    encrypt = st.button("encrypt", key="encrypt", help=None, on_click=None, args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False)
    if encrypt:
        if file is not None:
            # st.image(file)
            with open(os.path.join("tmp","pending_enc.png"),"wb") as f: 
                f.write(file.getbuffer())
            out = steno.encode(text,"tmp/pending_enc.png", "tmp/out_enc.png")
            st.image("tmp/out_enc.png")
            st.text(out)






with dec_col:
    file = st.file_uploader("upload photo to decode", type= ['png'] , accept_multiple_files=False, key=None, help=None, on_change=file_updated, args=["test"], kwargs=None, disabled=False, label_visibility="visible")
    # st.text_input("encrypted text", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None,  placeholder=None, disabled=True)
    decypt = st.button("decrypt", key="decrypt", help=None, on_click=None, args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False)
    if decypt:
        if file is not None:
            # st.image(file)
            with open(os.path.join("tmp","pending_dec.png"),"wb") as f: 
                f.write(file.getbuffer())
            out = steno.decode("tmp/pending_dec.png")
            st.write(out)
