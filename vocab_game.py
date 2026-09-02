import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# ----------------------------------------------------
# 1. กำหนดค่าเริ่มต้นใน session_state
# ----------------------------------------------------
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""

# ----------------------------------------------------
# ฟังก์ชันเริ่มเกมใหม่
# ----------------------------------------------------
def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""

    st.session_state.start = time.time()
    st.session_state.is_ended = False


# ----------------------------------------------------
# ฟังก์ชันแสดงผลคะแนน
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4):

    st.balloons()
    score = 0

    # แปลงคำตอบให้เป็นตัวพิมพ์เล็กและตัดช่องว่าง
    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()

    # ------------------------------------------------
    # ตรวจข้อ 1
    # ------------------------------------------------
    if u_ans1 == "apple":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{ans1}')")

    # ------------------------------------------------
    # ตรวจข้อ 2
    # ------------------------------------------------
    if u_ans2 == "fish":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{ans2}')")

    # ------------------------------------------------
    # ตรวจข้อ 3
    # ------------------------------------------------
    if u_ans3 == "strawberry":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{ans3}')")

    # ------------------------------------------------
    # ตรวจข้อ 4
    # ------------------------------------------------
    if u_ans4 == "coconut":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{ans4}')")

    # ------------------------------------------------
    # แสดงคะแนน
    # ------------------------------------------------
    st.info(f"🏆 ได้คะแนนรวม: {score} / 4 คะแนน")

    if score == 4:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")


# ----------------------------------------------------
# 2. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button(
    "🎮 เริ่มเล่นเกม",
    on_click=reset_game
)


# ----------------------------------------------------
# 3. แสดงเวลานับถอยหลัง
# ----------------------------------------------------
if "start" in st.session_state and not st.session_state.get("is_ended", False):

    time_left = int(
        30 - (time.time() - st.session_state.start)
    )

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        # หมดเวลา
        st.session_state.is_ended = True
        st.rerun()


st.divider()


# ----------------------------------------------------
# 4. ช่องกรอกคำตอบ
# ----------------------------------------------------
ans1 = st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
    value=st.session_state.ans1_val
)

ans2 = st.text_input(
    "ข้อ 2: Cats love to eat `f _ s h`. 🐟",
    value=st.session_state.ans2_val
)

ans3 = st.text_input(
    "ข้อ 3: Cats love to eat `st _ a w b e r _ y`. 🍓",
    value=st.session_state.ans3_val
)

ans4 = st.text_input(
    "ข้อ 4: Cats love to eat `c _ c o n _ t`. 🥥",
    value=st.session_state.ans4_val
)


# ----------------------------------------------------
# อัปเดตค่าคำตอบล่าสุด
# ----------------------------------------------------
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4


# ----------------------------------------------------
# 5. ปุ่มส่งคำตอบ
# ----------------------------------------------------
if "start" in st.session_state and not st.session_state.get("is_ended", False):

    if st.button("📥 ส่งคำตอบ"):

        st.session_state.is_ended = True
        st.rerun()

    # อัปเดตเวลาทุก 1 วินาที
    time.sleep(1)
    st.rerun()


# ----------------------------------------------------
# 6. แสดง Dialog ผลลัพธ์
# ----------------------------------------------------
if st.session_state.get("is_ended", False):

    show_result_dialog(
        st.session_state.ans1_val,
        st.session_state.ans2_val,
        st.session_state.ans3_val,
        st.session_state.ans4_val
    )


st.divider()

st.write("นางสาวพรสุดา ทมิฬทร เลขที่ 10 ม.4/4")

