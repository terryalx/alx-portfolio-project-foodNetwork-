def user_agent_select(request):
    user_agent = request.META.get('HTTP_USER_AGENT')
    
    # Check if User-Agent string exists
    if user_agent:
        user_agent = user_agent.lower()
        specific_mobile_browsers = [
            'chrome', 'firefox', 'safari', 'edge', 'opera', 'brave', 'vivaldi', 'internet explorer', 
            'tor', 'chromium', 'duckduckgo', 'uc browser', 'maxthon', 'netscape', 
            'seamonkey', 'pale moon', 'konqueror', 'lynx', 'yandex'
        ]
    
        for browser in specific_mobile_browsers:
            if browser in user_agent:
                return True
    
    return False



# def user_agent_select(request):
#     user_agent = request.META.get('HTTP_USER_AGENT').lower()

#     specific_mobile_browsers = [
#                                 'chrome', 'firefox', 'safari', 'edge', 'opera', 'brave', 'vivaldi', 'internet explorer', 
#                                 'tor', 'chromium', 'duckduckgo', 'uc browser', 'maxthon', 'netscape', 
#                                 'seaMonkey', 'pale moon', 'konqueror', 'lynx', 'yandex'
#                                 ]

#     for browser in specific_mobile_browsers:
#         if browser in user_agent:
#             return True
    
#     return False