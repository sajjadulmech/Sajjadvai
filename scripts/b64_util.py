import sys, base64

cmd = sys.argv[1]
path = sys.argv[2]

if cmd == 'init':
    with open(path + '.chunks', 'w', encoding='utf-8') as f:
        pass
    print('Init:', path)
elif cmd == 'append':
    chunk = sys.argv[3].strip()
    with open(path + '.chunks', 'a', encoding='utf-8') as f:
        f.write(chunk + '\n---CHUNK---\n')
    print('Appended', len(chunk), 'bytes to', path)
elif cmd == 'decode':
    with open(path + '.chunks', 'r', encoding='utf-8') as f:
        raw = f.read()
    chunks = raw.split('---CHUNK---')
    with open(path, 'wb') as f:
        for c in chunks:
            c = c.strip().replace('\n', '').replace('\r', '')
            if c:
                pad = len(c) % 4
                if pad:
                    c += '=' * (4 - pad)
                f.write(base64.b64decode(c))
    print('Decoded all chunks to', path)
