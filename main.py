def getmess(chanid):
    before = None
    headers = {
        'authorization': '<auth token>'
    }
    while True:
        url = f'<https://discord.com/api/v9/channels/{chanid}/messages?limit=100>'
        if before:
            url += '&before='+before

        r = requests.get(url, headers=headers)
        jsonn = json.loads(r.text)

        if not jsonn:
            break

        print(jsonn)

        if 'retry_after' in jsonn:
            time.sleep(jsonn['retry_after'])
            continue

        for val in jsonn:
            print(val['content'])

        before = jsonn[-1]['id']

getmess(<chanid>)
