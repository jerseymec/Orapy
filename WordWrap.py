import textwrap

def wrap(sentence, max_width):
    wrapped_sent = []
    wrapped_sent += (sentence[i:(i+max_width)  ] for i in range(0,len(sentence),max_width) )

    #return wrapped_sent
    return "\n".join(textwrap.wrap(sentence,max_width ))

Input = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = 4

Wrapped_Input = wrap(Input,num)
print(Wrapped_Input)
#for i in Wrapped_Input:
#    print(i)
