# turn a string to camel case text
def to_camel_case(text):
    camel_text = ''
    text_list = text.split(' ')
    for word in text_list:
        camel_text = camel_text + word [0].upper()+word[1:].lower()
    return(camel_text)
