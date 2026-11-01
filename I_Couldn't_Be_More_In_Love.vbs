Option Explicit

Dim messages, i

messages = Array( _
    "I could have been a great line", _
    "I could have been a sign or overstayed my time", _
    "Say what's on your mind", _
    "Maybe I'll rely on all the things that made it right", _
    "Because I'd give you all the years of my life", _
    "So", _
    "What about these feelings I've got?", _
    "We got it wrong and you said you'd had enough", _
    "But what about these feelings I've got?!", _
    "I couldn't be more in love" _
)

For i = 0 To UBound(messages)
    MsgBox messages(i), vbInformation, "I Couldn't Be More In Love"
Next