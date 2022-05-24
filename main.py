import streamlit as st
import time

st.title('弁護士紹介サイト(こちらは偽のサイトとなっているので実際には行っていません)')
st.write('現時刻の相談可能な先生を検索')
latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'検索開始:{i+1}%')
    bar.progress(i+1)
    time.sleep(0.03)
'検索終了'

left_column,right_colum=st.columns(2)
button=left_column.button('右カラムに先生を紹介')
if button:
    right_colum.write('(偽名)西方　剛弁護士')
    right_colum.write('(偽名)佐々木　未来弁護士')
    expander=st.expander('西方先生へのお問い合わせ、詳細はこちら')
    expander.write('料金説明：30分5000円　初回のみ無料')
    expander.write('相談内容：不倫関係、相続関係')
    expander1=st.expander('佐々木先生へのお問い合わせ、詳細はこちら')
    expander1.write('料金説明：30分5000円（税抜き）初回のみ半額サービス')
    expander1.write('パラリーガルから見た先生の印象：美人でしっかりと話を聞いてくれますので気軽にご相談できると思います。')