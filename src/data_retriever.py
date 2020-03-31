def parse_html(url, res_type):
    """网页解析函数

    本函数是为了获取 url 的返回结果。君自故乡来，应知故乡事。来日绮窗前，寒梅著花未？

    :param url: 需要访问的网址
    :type url: string
    :param res_type: 请求类型，可以取值为 get 或者 post
    :type res_type: list
    :return: 返回网页的源代码
    :rtype: string
    """
    reponse = requests.res_type(url).content

    return reponse
