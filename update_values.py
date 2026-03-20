import os

directory = r'c:\Users\david\io-value'
files = ['index.html', 'summary.html', 'forth.html', 'second.html', 'third.html', 'fifth.html', 'sixth.html', 'seventh.html', 'seo.html']

for filename in files:
    path = os.path.join(directory, filename)
    if not os.path.exists(path):
        continue
        
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the lower bound (15.0k and 15k) with 20.0k and 20k
    # And specifically target ranges if needed to ensure we hit 20k - 25k
    # Case 1: 15.0k — 25.0k
    content = content.replace('15.0k', '20.0k')
    
    # Case 2: 15k — 25k
    content = content.replace('15k', '20k')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Mass replacement of 15k to 20k complete.")
