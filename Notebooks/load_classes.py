import re

def fetch_classdict(mode='all'):
    if mode == 'all':
        with open('class_names.txt','r') as f:
            content = list(f.readlines())
        combined = ' '.join(content)

        # fetching chars
        pattern = r'\(([A-Z]{1})\)'
        finds = re.findall(pattern, combined)

        # packaging
        classes = {}
        for item, token in zip(content, finds):
            item = item.split(' ')[0]
            classes[token] = item

        return classes
    else:
        with open('coi.txt','r') as f:
            content = list(f.readlines())
        combined = ' '.join(content)

        # fetching chars
        pattern = r'\(([A-Z]{1})\)'
        finds = re.findall(pattern, combined)

        # packaging
        classes = {}
        for item, token in zip(content, finds):
            item = item.split(' ')[0]
            classes[token] = item

    return classes
        



