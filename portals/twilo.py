from twilio.rest import Client

sid = "AC404d2994db3cb5d756ddef2998aa0f78"
auth_token = "1cf72c24c419941c0417302bf5077e47"
phone_no = "+18777804236"
client = Client(sid,auth_token)


try:
    message = client.messages.create(
        body="This is for pride motors verification EMail from twillo",
        from_='+12406182528',
        to='+918329813761'
    )
    print(f"Message SID: {message.sid}")
except Exception as e:
    print(f"Error: {str(e)}")


message_status = client.messages(message.sid).fetch()
print(f"Message Status: {message_status.status}")