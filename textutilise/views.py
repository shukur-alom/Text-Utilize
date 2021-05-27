from django.http import HttpResponse, request
from django.shortcuts import render
import pandas as pd


def removepunc_(text):
    func = "'@#$^*&()%+!~`{}[]|/:;"
    plain_text = ''
    for k in text.split('\n'):
        for i in k.split():
            add_text = ""
            for l in i:
                if l not in func:
                    add_text += l
            if add_text != "":
                plain_text += " "
            plain_text += f"{add_text}"
        plain_text += f"\n"
    return plain_text


def capitalizefirst_(text):
    plain_text = ""
    for i in text.split('\n'):
        try:
            for j in i.split('.'):
                add_text = ""
                split = j.split()
                add_text += f"{split[0].capitalize()}"
                for a in split[1:]:
                    add_text += f" {a}"
                plain_text += f"{add_text}. "
        except:
            pass
        plain_text += f"\n"
    return plain_text


def newlineremove_(text):
    plain_text = ""
    for i in text.split("\n"):
        if i != '\r':
            plain_text += f"{str(i)}\n"
    return plain_text


def spaceromove_(text):
    plain_text = ""
    for j in text.split('\n'):
        for i in j.split():
            plain_text += f"{i} "
        plain_text += f"\n"
    return plain_text


def charcount_(text):
    count = 0
    for i in text:
        if i == " " or i == '\n':
            pass
        else:
            count += 1
    return f"Char have {count}"


def index(request):
    return render(request, "index.html")


def analyze(request):
    text = request.GET.get("text_area", 'default')
    type = request.GET.get("analyze_type", 'default')

    if type == "removepunc":
        var = {"input_text": text, "type": type,
               "plain_text": removepunc_(text)}

    elif type == "capitalizefirst":
        var = {"input_text": text, "type": type,
               "plain_text": capitalizefirst_(text)}

    elif type == "spaceromove":
        var = {"input_text": text, "type": type,
               "plain_text": spaceromove_(text)}

    elif type == "newlineremove":
        var = {"input_text": text, "type": type,
               "plain_text": newlineremove_(text)}

    elif type == "charcount":
        var = {"input_text": text, "type": type,
               "plain_text": charcount_(text)}

    return render(request, "show_ans.html", var)


def about(request): return render(request, 'about_us.html')


def cont(request):
    email_ = request.GET.get("email", 'default')
    message_ = request.GET.get("message", 'default')
    if email_ != "default" and message_ != "default":

        c_1 = pd.read_json('/home/shukur/Documents/Django/textutilise/con_us.json')

        email = list(c_1['email'])
        email.append(str(email_))
        message = list(c_1['message'])
        message.append(str(message_))

        c_2 = pd.DataFrame({'email': email,
                            'message': message})
        c_2.to_json("/home/shukur/Documents/Django/textutilise/con_us.json")
        c_1, c_2 = 0, 0
    return render(request, 'cont_us.html')


if __name__ == "__main__":pass
