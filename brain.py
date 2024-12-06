# from webscout import PhindSearch as brain


from webscout import PhindSearch

def Main_Brain(text):

    ai = PhindSearch(quiet=True, filepath=r"D:\A.J.A.R.V.I.S\chat_hystory.txt", is_conversation=None)

    res = ai.chat(text) # internel stream is not available for this Privider

    return res

