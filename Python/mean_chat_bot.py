while True: x=input('YOU: '); print('ROBOT: ', 'Why do you care?' if any(q in x.lower() for q in ['why','what','where','who','how']) else (quit() if 'bye' in x.lower() else x))