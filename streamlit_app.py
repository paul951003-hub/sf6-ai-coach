import streamlit as st

st.title("SF6 AI Coach")

jumps = st.number_input("Jump 次數", 0, 100, 10)
anti_air = st.number_input("Anti-air 成功率", 0, 100, 50)
combo_drops = st.number_input("Combo 掉落次數", 0, 20, 3)
di_usage = st.number_input("Drive Impact 次數", 0, 20, 5)

def analyze(jumps, anti_air, combo_drops, di_usage):
    result = []

    if jumps > 15:
        result.append("❌ 你跳太多了")

    if anti_air < 50:
        result.append("❌ Anti-air 不合格")

    if combo_drops > 5:
        result.append("❌ Combo 不穩")

    if di_usage > 10:
        result.append("❌ DI 太多")

    if len(result) == 0:
        return "✅ 沒有重大問題"

    return "\n".join(result)

if st.button("分析戰鬥"):
    st.text(analyze(jumps, anti_air, combo_drops, di_usage))
