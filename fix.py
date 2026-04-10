with open('paper/main.tex', 'r', encoding='utf-8') as f:
    t = f.read()

a = t.find(r'\section{Results (Preliminary)}')
b = t.find(r'\section{Discussion}')
assert a > 0 and b > a, f'markers not found: a={a} b={b}'

out = t[:a] + r'\input{section7}' + '\n\n' + t[b:]
out = out.replace(r'\end{document}', r'\input{appendix_v11}' + '\n' + r'\end{document}')

assert r'\input{section7}' in out
assert r'\input{appendix_v11}' in out
assert 'Results (Preliminary)' not in out
assert len(out) > 15000, f'too short: {len(out)}'

with open('paper/main.tex', 'w', encoding='utf-8', newline='\n') as f:
    f.write(out)

print('Done. Length:', len(out))
