import streamlit as st
from twilio.rest import Client
from google_translate import translations

# Twilio API Credentials
TWILIO_ACCOUNT_SID = "SK2465a9a63e4db3acbbd5537dcedab078"
TWILIO_AUTH_TOKEN = "sa8sNCIIF8r4Kgb00TkAs3R8yhQmOqsT"
TWILIO_PHONE_NUMBER = "+1 253 289 3116"
YOUR_PHONE_NUMBER = "+919421293631"

def send_sms(name, email, phone, message) :
    try :
        client = Client ( TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN )

        sms_body = (
            f"🚜 New Message from Farmer:\n"
            f"👤 Name: {name}\n"
            f"📧 Email: {email}\n"
            f"📞 Phone: {phone}\n"
            f"🌾 Message: {message}"
        )

        client.messages.create (
            body=sms_body,
            from_=TWILIO_PHONE_NUMBER,
            to=YOUR_PHONE_NUMBER
        )
        st.success ( "Message sent successfully!" )
    except Exception as e :
        st.error ( f"Error sending SMS: {e}" )

def Contact(lang_code):

    lang = translations[lang_code]

    st.title(lang["contact-page"])
    st.write(lang["contact-description"])

    # Initialize session state for the form fields
    if "form_data" not in st.session_state :
        st.session_state.form_data = {
            "name" : "",
            "email" : "",
            "address" : "",
            "phone" : "",
            "message" : ""
        }

    # Contact Form Inputs
    col1, col2, col3 = st.columns ( 3 )

    with col1 :
        st.session_state.form_data["name"] = st.text_input (
            "**Your Name**",
            placeholder="Enter your name",
            value=st.session_state.form_data["name"]
        )
        st.session_state.form_data["email"] = st.text_input (
            "**Your Email**",
            placeholder="Enter your email",
            value=st.session_state.form_data["email"]
        )

    with col2 :
        st.session_state.form_data["address"] = st.text_input (
            "**Your Address**",
            placeholder="Enter your address",
            value=st.session_state.form_data["address"]
        )
        st.session_state.form_data["phone"] = st.text_input (
            "**Your Phone**",
            placeholder="Enter your phone number",
            value=st.session_state.form_data["phone"]
        )

    with col3 :
        st.session_state.form_data["message"] = st.text_area (
            "**Your Message**",
            placeholder="Type your message here",
            value=st.session_state.form_data["message"]
        )

        # Submit Button
    if st.button ( "SEND MESSAGE" ) :
            # Validation for mandatory fields
        if not st.session_state.form_data["name"] or not st.session_state.form_data["phone"] or not st.session_state.form_data["message"] :
                st.error ( "Please fill out all required fields (Name, Phone, and Message)." )
        else :
            send_sms ( st.session_state.form_data["name"], st.session_state.form_data["email"],st.session_state.form_data["phone"], st.session_state.form_data["message"] )

            st.session_state.form_data = {
                "name" : "",
                "email" : "",
                "address" : "",
                "phone" : "",
                "message" : ""
            }


    # Expertise Team Section
    st.markdown("---")
    st.subheader(lang["experts"])
    st.write(lang["expert_info"])

    experts = [
        {"name": "Dr. Amit Kumar", "image": "image/team-1.jpg", "phone": "+91 98765 43210"},
        {"name": "Dr. Neha Sharma", "image": "image/team-5.jpg", "phone": "+91 98234 56789"},
        {"name": "Dr. Rajesh Verma", "image": "image/team-4.jpg", "phone": "+91 98712 34567"}
    ]

    col1, col2, col3 = st.columns(3)
    for idx, expert in enumerate(experts):
        with [col1, col2, col3][idx]:
            st.image(expert["image"], width=200)
            st.write(f"**{expert['name']}**")
            st.write(f"📞 {expert['phone']}")

    # Additional Information Section
    st.markdown("---")
    st.write(lang["urgent"])
    st.write(f"📞 **{lang['phone_label']}:** +1 (800) 123-4567")
    st.write(f"📧 **{lang['email_label']}:** support@tomatosystem.com")
    st.write(f"🌐 **{lang['website_label']}:** [www.tomatosystem.com](http://www.tomatosystem.com)")
    st.write(f"📱 **{lang['instagram_label']}:** [@tomatosystem](https://www.instagram.com/tomatosystem)")
    st.write(f"🐦 **{lang['twitter_label']}:** [@tomatosystem](https://www.twitter.com/tomatosystem)")
    st.markdown("---")

